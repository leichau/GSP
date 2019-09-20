# -*- coding: utf-8 -*-

"""
Module implementing SerialPort.
"""
import serial, serial.tools.list_ports, threading, re
import sys, time
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication

from Ui_SerialPort import Ui_MainWindow
from Codec import Codec
from About import About

class SerialPort(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(SerialPort, self).__init__(parent)
        self.setupUi(self)        
        #获取端口
        port_list=list(serial.tools.list_ports.comports())
        for port_list_0 in port_list:
            port = list(port_list_0)
            self.comboBoxPort.addItem(port[1])
        self.comboBoxBaud.addItems(["9600", "19200", "38400", "57600", "115200", "Custom"])
        #self.comboBoxBaud.setEditable(True)
        self.comboBoxDataBit.addItems(["5", "6", "7", "8"])
        self.comboBoxParity.addItems(["None", "Even", "Odd", "Mark", "Space"])
        self.comboBoxStopBit.addItems(["1", "1.5", "2"])
        self.comboBoxFlow.addItems(["None", "RTS/CTS", "XON/XOFF"])
        self.RecvFormate = 1    #1:ASCII  0:HEX
        self.radioButtonRecvASCII.setChecked(True)
        self.SendFormate = 1    #1:ASCII  0:HEX
        self.radioButtonSendASCII.setChecked(True)
        self.checkBoxNewLine.setChecked(True)   #自动换行
        self.serial = serial.Serial()
        self.autoScroll = True  #接收自动滚动
    
    def serial_recvThread(self):
        '''待解决问题
        1、textBrowser.append添加文本会自动换行
        '''
        print(threading.current_thread().name, "start")
        self.recvThreadState = True
        while self.recvThreadState:
            data = self.serial.read_all() 
            #data = b''
            #while self.serial.inWaiting() > 0:   
            #   data += self.serial.read(512)
            if data:
                #自动换行
                if self.checkBoxNewLine.checkState==Qt.Checked:
                    self.textBrowser.append('\n')
                #显示时间
                if self.checkBoxTime.checkState==Qt.Checked:
                    self.textBrowser.append(time.strftime("%H:%M:%S:", time.localtime()))
                if self.RecvFormate == 1:                    
                    self.textBrowser.append(data.decode("gbk", "ignore"))
                    #self.textBrowser.append(data.decode("gbk", "replace"))
                else:
                    self.textBrowser.append(' '.join("%02X" % x for x in data))
                if self.autoScroll:
                    self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
                continue
#            if self.recvThreadState == False:
#                break   #结束线程         
            time.sleep(0.02)
            if self.textBrowser.verticalScrollBar().value()==self.textBrowser.verticalScrollBar().maximum():
                self.autoScroll=True
            else:
                #print("%d,%d" % (self.textBrowser.verticalScrollBar().value(), self.textBrowser.verticalScrollBar().maximum()))
                self.autoScroll=False
        print(threading.current_thread().name, "end")
    
    def serial_resendThread(self):
        resendThreadState=True
        while resendThreadState:
            if self.spinBoxTime.value():
                self.seriel_send()
                time.sleep(self.spinBoxTime.value()/1000)
    
    def serial_send(self):
        if self.serial.isOpen():
            text=''
            if self.SendFormate==1:
                text+=self.plainTextEdit.toPlainText()
                data=text.encode("gbk")
                #self.serial.write(self.plainTextEdit.toPlainText().encode("utf-8"))
            else:  
                intText = []
                for x in re.split(r"\s*[^0-9a-fA-F]*", self.plainTextEdit.toPlainText()):
                    i=0
                    while x[i:i+2]:
                        intText.append(int(x[i:i+2], 16))
                        text+=' %02X'%int(x[i:i+2], 16)
                        i += 2
                        data=bytes(intText)            
            if len(data):
                self.serial.write(data)
            #发送回显
            if self.checkBoxEcho.checkState==Qt.Checked:
                #显示时间
                if self.checkBoxTime.checkState==Qt.Checked:
                    text=time.strftime("%H:%M:%S:", time.localtime())+text                
                self.textBrowser.append(text)
    
    def serial_open(self):
        self.serial_close()     
        self.serial = serial.Serial(port=self.port, baudrate=self.baudrate, bytesize=self.bytesize, parity=self.parity, stopbits=self.stopbits, timeout=2, 
                                         xonxoff=self.xonxoff, rtscts=self.rtscts)
        self.recvThread = threading.Thread(target=self.serial_recvThread, name='recvThread')
        self.recvThread.start()
        #join和setDaemon作用相反，前者等待子线程结束，后者不等子线程结束，有可能把子线程强制结束。
        #如果都不设置，主线程和子线程各自运行，互不影响
        #self.recvThread.join()
        self.recvThread.setDaemon()
        print(self.serial)
    
    def serial_close(self):
        if self.serial.isOpen():
            self.recvThreadState = False
            while self.recvThread.is_alive():
                continue
            self.serial.close()
        print(self.serial)
    
    @pyqtSlot(bool)
    def on_checkBoxResend_toggled(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        if self.checkBoxResend.checkState==Qt.Unchecked:
            self.resendThreadState=False
    
    @pyqtSlot()
    def on_pushButtonSend_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.checkBoxResend.checkState==Qt.Checked:
            if not self.resendState:
                self.resendThread = threading.Thread(target=self.serial_resendThread, name='resendThread')
                self.resendThread.start()
                #join和setDaemon作用相反，前者等待子线程结束，后者不等子线程结束，有可能把子线程强制结束。
                #如果都不设置，主线程和子线程各自运行，互不影响
                #self.resendThread.join()
                self.resendThread.setDaemon()
        else:
            self.serial_send()
    
    @pyqtSlot(bool)
    def on_run_triggered(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        if checked:
            self.serial_open()  
    
    @pyqtSlot(bool)
    def on_stop_triggered(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        self.serial_close()
    
    @pyqtSlot(int)
    def on_comboBoxPort_currentIndexChanged(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type int
        """
        self.port = list(list(serial.tools.list_ports.comports()))[index][0]
        if self.run.isChecked():
            self.serial_open()
    
    @pyqtSlot(int)
    def on_comboBoxBaud_currentIndexChanged(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type int
        """
        if self.comboBoxBaud.currentIndex()>=5:
            self.comboBoxBaud.setEditable(True)
        else:
            self.comboBoxBaud.setEditable(False)
        
        if self.comboBoxBaud.currentText().isdigit():
            self.baudrate=int(self.comboBoxBaud.currentText())
            print(self.baudrate)
            if self.run.isChecked():
                self.serial_open()
    
    @pyqtSlot(str)
    def on_comboBoxBaud_editTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        if self.comboBoxBaud.currentText().isdigit() and self.comboBoxBaud.currentIndex()>=5:
            self.baudrate=int(self.comboBoxBaud.currentText())
            print("change %d" % self.baudrate)
            if self.run.isChecked():
                self.serial_open()
    
    @pyqtSlot(int)
    def on_comboBoxDataBit_currentIndexChanged(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type int
        """
        self.bytesize=int(self.comboBoxDataBit.currentText())
        if self.run.isChecked():
            self.serial_open()
    
    @pyqtSlot(int)
    def on_comboBoxFlow_currentIndexChanged(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type int
        """
        if index == 0:
            self.xonxoff=False
            self.rtscts=False
        elif index == 1:
            self.xonxoff=False
            self.rtscts=True
        elif index == 2:
            self.xonxoff=True
            self.rtscts=False
        if self.run.isChecked():
            self.serial_open()
    
    @pyqtSlot(int)
    def on_comboBoxStopBit_currentIndexChanged(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type int
        """
        self.stopbits=float(self.comboBoxStopBit.currentText())
        if self.run.isChecked():
            self.serial_open()
    
    @pyqtSlot(int)
    def on_comboBoxParity_currentIndexChanged(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type int
        """
        parity=["N", "E", "O", "M", "S"]
        self.parity=parity[index]
        if self.run.isChecked():
            self.serial_open()
    
    @pyqtSlot(int)
    def on_comboBoxSend_currentIndexChanged(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type int
        """
        #TODO 添加最近十条发送数据，最好可以永久保存，考虑数据库支持
        if len(self.comboBoxSend.text()):
            self.plainTextEdit.setPlainText(self.comboBoxSend.text())
    
    @pyqtSlot()
    def on_radioButtonRecvASCII_pressed(self):
        """
        Slot documentation goes here.
        """
        self.RecvFormate = 1
    
    @pyqtSlot()
    def on_radioButtonRecvHex_pressed(self):
        """
        Slot documentation goes here.
        """
        self.RecvFormate = 0
    
    @pyqtSlot()
    def on_radioButtonSendASCII_pressed(self):
        """
        Slot documentation goes here.
        """
        self.SendFormate = 1
        print(self.SendFormate)
    
    @pyqtSlot()
    def on_radioButtonSendHex_pressed(self):
        """
        Slot documentation goes here.
        """
        self.SendFormate = 0
        #print(self.SendFormate)
    
    @pyqtSlot(bool)
    def on_codec_triggered(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        codec.show()
        
    @pyqtSlot()
    def on_about_triggered(self):
        """
        Slot documentation goes here.
        """        
        aboutSoft.show()
        aboutSoft.softInfo.verticalScrollBar().setValue(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = SerialPort()
    dlg.show()
    codec = Codec()
    aboutSoft=About()
    sys.exit(app.exec_())     
