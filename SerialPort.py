# -*- coding: utf-8 -*-

"""
Module implementing SerialPort.
"""
import serial, serial.tools.list_ports, threading, re
import sys, time
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication

from Ui_SerialPort import Ui_MainWindow

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
        self.comboBoxDataBit.addItems(["5", "6", "7", "8"])
        self.comboBoxParity.addItems(["None", "Even", "Odd", "Mark", "Space"])
        self.comboBoxStopBit.addItems(["1", "1.5", "2"])
        self.comboBoxFlow.addItems(["None", "RTS/CTS", "XON/XOFF"])
        self.RecvFormate = 1    #1:ASCII  0:HEX
        self.radioButtonRecvASCII.setChecked(True)
        self.SendFormate = 1    #1:ASCII  0:HEX
        self.radioButtonSendASCII.setChecked(True)
        self.serial = serial.Serial()
        self.autoScroll = True  #接收自动滚动
    
    def serial_thread(self):
        print(threading.current_thread().name, "start")
        self.serialThreadState = True
        while self.serialThreadState:
            data = self.serial.read_all() 
            #data = b''
            #while self.serial.inWaiting() > 0:   
            #   data += self.serial.read(512)
            if data:
                if self.RecvFormate == 1:                    
                    self.textBrowser.append(data.decode("gbk", "ignore"))
                    #self.textBrowser.append(data.decode("gbk", "replace"))
                else:
                    self.textBrowser.append(' '.join("%02X" % x for x in data))
                if self.autoScroll:
                    self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
                continue 
            if self.serialThreadState == False:
                break   #结束线程         
            time.sleep(0.02)
            if self.textBrowser.verticalScrollBar().value()==self.textBrowser.verticalScrollBar().maximum():
                self.autoScroll=True
            else:
                #print("%d,%d" % (self.textBrowser.verticalScrollBar().value(), self.textBrowser.verticalScrollBar().maximum()))
                self.autoScroll=False
        print(threading.current_thread().name, "end")
    
    def serial_open(self):
        self.serial_close()     
        self.serial = serial.Serial(port=self.port, baudrate=self.baudrate, bytesize=self.bytesize, parity=self.parity, stopbits=self.stopbits, timeout=2, 
                                         xonxoff=self.xonxoff, rtscts=self.rtscts)
        self.serialThread = threading.Thread(target=self.serial_thread, name='serialThread')
        self.serialThread.start()
        #self.serialThread.join()
        print(self.serial)
    
    def serial_close(self):
        if self.serial.isOpen():
            self.serialThreadState = False
            while self.serialThread.is_alive():
                continue
            self.serial.close()
        print(self.serial)
    
    @pyqtSlot(bool)
    def on_checkBoxEcho_toggled(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(bool)
    def on_checkBoxTime_toggled(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(bool)
    def on_checkBoxNewLine_toggled(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(bool)
    def on_checkBoxRetry_toggled(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButtonSend_clicked(self):
        """
        Slot documentation goes here.
        """        
        if self.serial.isOpen():
            if self.SendFormate==1:
                self.serial.write(self.plainTextEdit.toPlainText().encode("gbk"))
                #self.serial.write(self.plainTextEdit.toPlainText().encode("utf-8"))
            else:  
                intText = []
                for x in re.split(r"\s*[^0-9a-fA-F]*", self.plainTextEdit.toPlainText()):
                    i=0
                    while x[i:i+2]:
                        intText.append(int(x[i:i+2], 16)) 
                        i += 2
                self.serial.write(bytes(intText))  
                print(len(bytes(intText)))
    
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
        self.baudrate=int(self.comboBoxBaud.currentText())
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
        # TODO: not implemented yet
        #raise NotImplementedError
    
    @pyqtSlot()
    def on_radioButtonRecvASCII_pressed(self):
        """
        Slot documentation goes here.
        """
        self.RecvFormate = 1
        print(self.RecvFormate)
    
    @pyqtSlot()
    def on_radioButtonRecvHex_pressed(self):
        """
        Slot documentation goes here.
        """
        self.RecvFormate = 0
        print(self.RecvFormate)
    
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = SerialPort()
    dlg.show()
    sys.exit(app.exec_())   
    
    
