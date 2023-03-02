# -*- coding: utf-8 -*-

"""
Module implementing SerialPort.
"""
import serial, serial.tools.list_ports, threading, re
import sys, time
from datetime import datetime
from PyQt5.QtCore import pyqtSlot, QAbstractNativeEventFilter, QSettings, pyqtSignal, QSize, QEvent, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QLabel, QFontDialog, QMenu, QToolButton
from PyQt5.QtGui import QTextCursor, QFont, QIcon
from io import StringIO
import json
import ctypes.wintypes

from Ui_SerialPort import Ui_MainWindow
from Codec import Codec
from About import About
from AutoConnect import AutoConnect
from option import Option

'''
待解决问题
1、添加当前端口号列表
2、选择自动连接后禁止端口选择
3、自动换行检测行头换行                     完成
4、添加序号标记                            终止
5、添加时间标记                            完成
6、添加字符串监控                          完成
7、字体设置                                完成
8、保存设置参数                            完成
10、自动连接时漏接起始接收数据              未完成
       在IDE里不会漏接。
       在IDE外直接运行程序有漏接现象。去掉多余调试打印信息后漏接现象减少，推测在IDE外print打印会占用更多时间。
11、textBrowser.append 添加文本会自动换行                      已解决
12、显示时间时会自动换行，导致换行前已在行头时，会多出一个空行   已解决
13、数据量达到限值清除时，异常退出                  已解决
    - 初步分析清除调用 textBrowser.clear 导致
    - 子线程调用 GUI 更新所致
14、添加收发标记
15、按照 html/css 语法实现全局颜色控制
'''

SERIAL_STOP = 0
SERIAL_RUN  = 1
SERIAL_PAUSE = 2

class SerialPort(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    sigDispaly = pyqtSignal()
    sigRxCnt = pyqtSignal(int)
    sigLcdNum = pyqtSignal(int)

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(SerialPort, self).__init__(parent)
        self.setupUi(self)

        # 去掉标题栏
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setWindowIcon(QIcon(':/icon/resource/icon/serial256.ico'))
        self.toolBar.setIconSize(QSize(40,40))
        self.settings = QSettings("./user.ini", QSettings.IniFormat)
        #接收栏字体
        textBrowserFont = self.settings.value('Font')
        if textBrowserFont:
            textBrowserFont = textBrowserFont.split(',')
            if len(textBrowserFont) == 3:
                family = textBrowserFont[0]
                pointSize = int(textBrowserFont[1])
                weight = int(textBrowserFont[2])
                font = QFont(family, pointSize,  weight)
                if font:
                    self.textBrowser.setFont(font)
        #显示时间
        DisplayTime = self.settings.value('Time')
        if DisplayTime and DisplayTime == '1':
            self.checkBoxTime.setChecked(True)
        else:
            self.checkBoxTime.setChecked(False)
        #自动换行
        AutoWrap = self.settings.value('AutoWrap')
        if AutoWrap and AutoWrap == '1':
            self.checkBoxNewLine.setChecked(True)
        else:
            self.checkBoxNewLine.setChecked(False)
        #接收格式 1:ASCII  0:HEX
        RecvFormat = self.settings.value('RecvFormat')
        if RecvFormat and RecvFormat == "0":
            self.radioButtonRecvHex.setChecked(True)
        else:
            self.radioButtonRecvASCII.setChecked(True)
        #发送格式 1:ASCII  0:HEX
        SendFormat = self.settings.value('SendFormat')
        if SendFormat and SendFormat == "0":
            self.radioButtonSendHex.setChecked(True)
        else:
            self.radioButtonSendASCII.setChecked(True)
        # 运行状态
        self.runStates = SERIAL_STOP
        #自动连接端口
        AutoConnectPort = self.settings.value('Auto')
        if AutoConnectPort:
            self.AutoConnectPort = AutoConnectPort
        else:
            self.AutoConnectPort = None
        #获取端口
        self.port = None
        port_list=list(serial.tools.list_ports.comports())
        port_list.sort()
        for port_list_0 in port_list:
            port = list(port_list_0)
            self.comboBoxPort.addItem(port[1])
        self.comboBoxBaud.addItems(["9600", "19200", "38400", "57600", "115200", "Custom"])
        self.comboBoxBaud.setCurrentIndex(4)
        self.comboBoxDataBit.addItems(["5", "6", "7", "8"])
        self.comboBoxDataBit.setCurrentIndex(3)
        self.comboBoxParity.addItems(["None", "Even", "Odd", "Mark", "Space"])
        self.comboBoxStopBit.addItems(["1", "1.5", "2"])
        self.comboBoxFlow.addItems(["None", "RTS/CTS", "XON/XOFF"])
        self.serial = serial.Serial(timeout = 2)
        self.autoScroll = True  #接收自动滚动
        #接收监测
        self.monitorCnt = 0
        self.lcdNumber.display(self.monitorCnt)
        MonitorEnable = self.settings.value('Monitor')
        if MonitorEnable and MonitorEnable == '1':
            self.checkBoxMonitor.setChecked(True)
        else:
            self.checkBoxMonitor.setChecked(False)
        #提示音
        BeepEnable = self.settings.value('Beep')
        if BeepEnable and BeepEnable == '1':
            self.checkBoxBeep.setChecked(True)
        else:
            self.checkBoxBeep.setChecked(False)
        #设置栏
        sideView = self.settings.value('sideView')
        if sideView and sideView == '0':
            self.sideView.setChecked(False)
        else:
            self.sideView.setChecked(True)
        #发送栏
        sendView = self.settings.value('SendView')
        if sendView and sendView == '0':
            self.sendView.setChecked(False)
        else:
            self.sendView.setChecked(True)
        # 发送历史
        self.sendHistory = []
        #显示发送
        EchoEnable = self.settings.value('Echo')
        if EchoEnable and EchoEnable == '1':
            self.checkBoxEcho.setChecked(True)
        else:
            self.checkBoxEcho.setChecked(False)
        #添加回车
        SendReturnEnable = self.settings.value('Return')
        if SendReturnEnable and SendReturnEnable == '1':
            self.sendReturn.setChecked(True)
        else:
            self.sendReturn.setChecked(False)
        #转义序列
        EscapeEnable = self.settings.value('Escape')
        if EscapeEnable and EscapeEnable == '1':
            self.sendEscape.setChecked(True)
        else:
            self.sendEscape.setChecked(False)
        #发送列表
        SendList = self.settings.value('SendList')
        if SendList:
            self.comboBoxSend.addItems(SendList)
        #收发统计
        self.rxCount = 0
        self.txCount = 0
        #状态条信息
        self.InfoPort = QLabel()
        self.InfoPort.setText('CLOSED')
        self.InfoPort.setStyleSheet("color: red;font: 9pt 'Arial'")
        self.statusBar.addWidget(self.InfoPort, 2)
        self.InfoRx = QLabel()
        self.InfoRx.setText('RX: {} Bytes'.format(self.rxCount))
        self.statusBar.addWidget(self.InfoRx, 1)
        self.InfoTx = QLabel()
        self.InfoTx.setText('TX: {} Bytes'.format(self.txCount))
        self.statusBar.addWidget(self.InfoTx, 1)
        # 缓存流
        self.memStream = StringIO()
        self.streamCursor = 0
        self.sigDispaly.connect(self.stream_displayRender)
        self.sigRxCnt.connect(self.rxCntUpdate)
        self.sigLcdNum.connect(self.lcdNumUpdate)
        self.resendThreadState = False
        self.resendThread = threading.Thread(target=self.serial_resendThread, name='resendThread')
        # 视图工具
        viewMenu = QMenu("view")
        viewMenu.addAction(self.sideView)
        viewMenu.addAction(self.sendView)
        self.viewLayout = QToolButton()
        self.viewLayout.setMenu(viewMenu)
        self.viewLayout.setToolTip("视图")
        self.viewLayout.setPopupMode(QToolButton.MenuButtonPopup)
        self.viewLayout.setIcon(QIcon(':/icon/resource/icon/view48.png'))
        self.toolBar.insertWidget(self.option, self.viewLayout)
        self.viewLayout.clicked.connect(self.on_viewLayout_clicked)

    #窗口改变事件
    def changeEvent(self, event):
        if event.type() != QEvent.WindowStateChange:
            return
        if self.windowState() == Qt.WindowNoState:
            self.serial_recvAutoScroll()
        print('changeEvent: %d %08X'%(event.type(), self.windowState()))

    def closeEvent(self, event):
        if event.type() == 19:
            print('Close type: close event')
        else:
            print('Close type:', event.type())
        self.serial_close()
        sendList = []
        count = self.comboBoxSend.count()
        for i in range(0, count):
            sendList.append(self.comboBoxSend.itemText(i))
        self.settings.setValue('SendList', sendList)
        # self.stream_displayThreadState = False
        # while self.displayThread.is_alive():
        #     pass

    def lcdNumUpdate(self, num):
        self.lcdNumber.display(num)

    def rxCntUpdate(self, cnt):
        self.InfoRx.setText('RX: {} Bytes'.format(cnt))

    # html 特殊字符处理
    def htmlCharProcess(self, data):
        data = re.sub('(&)', '&amp;', data)
        data = re.sub('(<)', '&lt;', data)
        data = re.sub('(>)', '&gt;', data)
        return data

    #行首检测
    def stream_isHome(self):
        if self.streamCursor > 0:
            self.memStream.seek(self.streamCursor-1, 0)
            endchar = self.memStream.read(1)
            if endchar != '\n':
                return False
        return True

    def stream_write(self, data):
        self.memStream.seek(0, 2)
        self.memStream.write(data)

    def stream_displayRender(self):
        if self.runStates != SERIAL_RUN:
            return
        if not self.memStream.closed:
            self.memStream.seek(0, 2)
            offset = self.memStream.tell()
        else:
            return
        #自动下拉滚动条
        if self.textBrowser.verticalScrollBar().value()==self.textBrowser.verticalScrollBar().maximum():
            self.autoScroll = True
        else:
            self.autoScroll = False
        while self.streamCursor < offset:
            streamRead = self.streamCursor
            self.memStream.seek(streamRead, 0)
            dataHead = self.memStream.readline()
            jsonHead = json.loads(dataHead)
            # print(jsonHead)
            dataLength = jsonHead['Length']
            data = self.memStream.read(dataLength)
            # temp = data.encode("gbk")
            # print(temp)
            streamRead = self.memStream.tell()
            textCursor = self.textBrowser.textCursor()
            textCursor.movePosition(QTextCursor.End)
            lineHomeAdd = 0
            # html 特殊字符处理
            data = self.htmlCharProcess(data)
            received = jsonHead['Received']
            timeEnable = jsonHead['TimeEnable']
            if timeEnable:
                timestamp = jsonHead['Timestamp']
                timestamp = '<font color=#800040>' + timestamp + '</font>'
                if not re.match('(\r\n|\n)', data):
                    data = timestamp + data
                else:
                    data = re.sub('^(\r\n|\n)', '', data)
                    if len(data):
                        data = timestamp + '<br />' + timestamp + data
                    else:
                        data = timestamp + '<br />'
                data = re.sub('(\r\n|\n)$', '<br />', data)
                data = re.sub('(\r\n|\n)', '<br />'+timestamp, data)
                if not self.stream_isHome():
                    lineHomeAdd = 1
            else:
                data = re.sub('(\r\n|\n)', '<br />', data)
            # temp = data.encode("gbk")
            # print(temp)
            if received:    #接收显示
                monitorEnable = jsonHead['MonitorEnable']
                monitor = self.htmlCharProcess(jsonHead['Monitor'])
                if monitorEnable and len(monitor):
                    monitorFont = '<span style="background-color: #ffff00">' + monitor + '</span>'
                    data = data.replace(monitor, monitorFont)
                data = '<font color=#000000>' + data + '</font>'
                lineEnable = jsonHead['LineEnable']
                if lineEnable:
                    if not self.stream_isHome():
                        lineHomeAdd = 1
            else:   #发送显示
                data = '<font color=#008000>' + data + '</font>'
                if not self.stream_isHome():
                    lineHomeAdd = 1
            if lineHomeAdd:
                data = '<br />' + data
                print('Insert line home')
            textCursor.insertHtml(data)
            self.streamCursor = streamRead
            self.memStream.seek(0, 2)
            offset = self.memStream.tell()

    def serial_recvAutoScroll(self):
        if self.autoScroll:
            #self.textBrowser.moveCursor(QTextCursor.End)
            max = self.textBrowser.verticalScrollBar().maximum()
            self.textBrowser.verticalScrollBar().setSliderPosition(max)

    def serial_recvFont(self, font):
        """
        Slot documentation goes here.
        """
        print('serial_receive_font', font.family(), font.pointSize(), font.weight())
        self.textBrowser.setFont(font)
        font = '{},{},{}'.format(font.family(), font.pointSize(), font.weight())
        self.settings.setValue('Font', font)

    def serial_recvThread(self):
        #print(threading.current_thread().name, "start")
        while self.recvThreadState:
            try:
                data = self.serial.read_all()
            except Exception as e:
                self.recvThreadState = False
                print('serial_recvThread error:', str(e))
                break
            if data and not self.memStream.closed:
                if self.rxCount > 500*10000:
                    # print(__file__, sys._getframe().f_lineno)
                    self.clear.trigger()
                    time.sleep(0.05)
                self.rxCount += len(data)
                # self.InfoRx.setText('RX: {} Bytes'.format(self.rxCount))
                self.sigRxCnt.emit(self.rxCount)
                if self.radioButtonRecvASCII.isChecked():
                    data = data.decode("gbk", "ignore")
                else:
                    data = ' '.join("%02X" % x for x in data)
                    data = data + ' '
                #接收监测
                if self.checkBoxMonitor.isChecked():
                    jsonMonitorEnable = 1
                    jsonMonitorString = self.lineEditMonitor.text()
                    if len(self.lineEditMonitor.text()):
                        cnt = data.count(self.lineEditMonitor.text())
                        if cnt > 0:
                            self.monitorCnt += cnt
                            # self.lcdNumber.display(self.monitorCnt)
                            self.sigLcdNum.emit(self.monitorCnt)
                            if self.checkBoxBeep.isChecked():
                                QApplication.beep()
                else:
                    jsonMonitorEnable = 0
                    jsonMonitorString = ''
                #显示时间
                if self.checkBoxTime.isChecked():
                    jsonTimeEnable = 1
                    jsonTimestamp = '['+datetime.now().strftime('%H:%M:%S.%f') [:-3]+']'
                else:
                    jsonTimeEnable = 0
                    jsonTimestamp = ''
                #自动换行
                if self.checkBoxNewLine.isChecked():
                    jsonLineEnable = 1
                else:
                    jsonLineEnable = 0
                jsonRecv = 1
                jsonDataLength = len(data)
                jsonHead = '{"Received":%d, "Length":%d, "TimeEnable":%d, "Timestamp":"%s", "LineEnable":%d, '\
                    '"MonitorEnable":%d, "Monitor":"%s"}\n'%(jsonRecv, jsonDataLength, jsonTimeEnable, \
                                  jsonTimestamp, jsonLineEnable, jsonMonitorEnable, jsonMonitorString)
                self.stream_write(jsonHead)
                self.stream_write(data)
                self.sigDispaly.emit()
                continue
            time.sleep(0.05)

    def serial_recvThreadStart(self):
        self.recvThreadState = True
        self.recvThread = threading.Thread(target=self.serial_recvThread, name='recvThread')
        #join和setDaemon作用相反，前者等待子线程结束，后者不等子线程结束，有可能把子线程强制结束。
        #如果都不设置，主线程和子线程各自运行，互不影响
        #setDaemon必须在start() 方法调用之前设置，否则程序会被无限挂起。参数True表示主调线程为为守护线程，
        self.recvThread.setDaemon(True)
        self.recvThread.start()
        #join在start()之后调用，参数为超时时间
        #self.recvThread.join()

    def serial_recvThreadEnd(self):
        self.recvThreadState = False
        while self.recvThread.is_alive():
            continue

    def serial_resendThread(self):
        self.resendThreadState=True
        while self.resendThreadState:
            if self.spinBoxTime.value():
                self.serial_send()
                time.sleep(self.spinBoxTime.value()/1000)

    def serial_send_history_add(self, item):
        self.comboBoxSend.blockSignals(True)
        currentText = self.comboBoxSend.currentText()
        count = self.comboBoxSend.count()
        for i in range(0, count):
            if self.comboBoxSend.itemText(i) == item:
                self.comboBoxSend.removeItem(i)
                break
        self.comboBoxSend.insertItem(0, item)
        print('serial_send_history_add:', item)
        count = self.comboBoxSend.count()
        if count > 15:
            self.comboBoxSend.removeItem(count-1)
        index = self.comboBoxSend.findText(currentText)
        if index == -1:
            index = 0
        self.comboBoxSend.setCurrentIndex(index)
        self.comboBoxSend.blockSignals(False)

    def serial_send(self):
        if self.serial.isOpen():
            inputString = self.plainTextEdit.toPlainText()
            if len(inputString) == 0:
                return
            self.serial_send_history_add(inputString)
            data=''
            if self.radioButtonSendASCII.isChecked():
                if len(inputString):
                    # 转义替换
                    if self.sendEscape.isChecked():
                        inputString = inputString.replace('\\r', '\r')
                        inputString = inputString.replace('\\n', '\n')
                    if self.sendReturn.isChecked():
                        inputString = inputString + '\r\n'
                data += inputString
                hexData=inputString.encode("gbk")
            else:
                hexDataList = []
                datasplit = re.split(r"[^0-9a-fA-F]+", inputString)
                for x in datasplit:
                    i=0
                    while x[i:i+2]:
                        hexDataList.append(int(x[i:i+2], 16))
                        data+=' %02X'%int(x[i:i+2], 16)
                        i += 2
                        hexData=bytes(hexDataList)
            if len(hexData):
                self.serial.write(hexData)
                self.txCount += len(hexData)
                self.InfoTx.setText('TX: {} Bytes'.format(self.txCount))
            else:
                return
            #发送回显
            if self.checkBoxEcho.isChecked():
                if self.radioButtonRecvASCII.isChecked():
                    data = hexData.decode('gbk', errors='ignore')
                else:
                    data = ''
                    for x in hexData:
                        data = data + '%02X '%x
                    data = data.lstrip()
                #发送结束换行
                if data[-1] != '\n':
                    data = data + '\n'
                #显示时间
                if self.checkBoxTime.isChecked():
                    jsonTimeEnable = 1
                    jsonTimestamp = '['+datetime.now().strftime('%H:%M:%S.%f') [:-3]+']'
                else:
                    jsonTimeEnable = 0
                    jsonTimestamp = ''
                jsonRecv = 0
                jsonDataLength = len(data)
                jsonHead = '{"Received":%d, "Length":%d, "TimeEnable":%d, "Timestamp":"%s"}\n'%(jsonRecv, jsonDataLength, jsonTimeEnable, jsonTimestamp)
                self.stream_write(jsonHead)
                self.stream_write(data)
                self.sigDispaly.emit()

    def serial_open(self):
        if self.serial.isOpen():
            if  self.serial.port == self.port and \
                self.serial.baudrate == self.baudrate and \
                self.serial.bytesize == self.bytesize and \
                self.serial.parity == self.parity and \
                self.serial.stopbits == self.stopbits and \
                self.serial.xonxoff == self.xonxoff and \
                self.serial.rtscts == self.rtscts:
                print('serial_open: opend')
                return True
            else:
                self.serial_close()
        try:
            print('serial_open:', self.port)
            self.serial = serial.Serial(port=self.port, baudrate=self.baudrate, bytesize=self.bytesize, parity=self.parity, stopbits=self.stopbits, timeout=2,
                                             xonxoff=self.xonxoff, rtscts=self.rtscts)
        except serial.SerialException as e:
            print('%s[%d]:%s'%(sys._getframe().f_code.co_name, sys._getframe().f_lineno, str(e)))
            if str(e).find('PermissionError') != -1:
                print('serial_open: PermissionError')
            elif str(e).find('FileNotFoundError') != -1:
                print('serial_open: FileNotFoundError')
            elif str(e).find('OSError(22,') != -1:
                print('serial_open: 请求的资源在使用中')
                QMessageBox.question(self, '{}'.format(self.port), '无法打开 {}\n请确认是否占用'.format(self.port),
                                     QMessageBox.Ok, QMessageBox.Ok)
            else:
                print('serial_open: Undefined exception!')
            return False
        self.InfoPort.setStyleSheet("color: green;font: 9pt 'Arial'")
        self.InfoPort.setText('{} OPENED {} {} {}'.format(self.port, self.baudrate, self.bytesize, self.parity))
        self.serial_recvThreadStart()
        if self.runStates == SERIAL_STOP:
            self.runStates = SERIAL_RUN
            self.run.setIcon(QIcon(':/icon/resource/icon/pause_bk48.png'))
        return True

    def serial_close(self):
        if self.serial.isOpen():
            port = self.serial.port
            self.serial_recvThreadEnd()
            self.serial.close()
            self.InfoPort.setStyleSheet("color: red;font: 9pt 'Arial'")
            self.InfoPort.setText('{} CLOSED'.format(port))
            print('serial_close:', port)
        else:
            print('serial_close: closed')
        if self.runStates != SERIAL_STOP:
            self.runStates = SERIAL_STOP
            self.run.setIcon(QIcon(':/icon/resource/icon/trist48.png'))

    #端口刷新
    def serial_port_refresh(self):
        self.comboBoxPort.blockSignals(True)
        self.comboBoxPort.clear()
        portNameList = []
        port_list=list(serial.tools.list_ports.comports())
        port_list.sort()
        for port_list_0 in port_list:
            port = list(port_list_0)
            self.comboBoxPort.addItem(port[1])
            portNameList.append(port[0])
        if self.port is None:
            if self.comboBoxPort.count():
                self.port = portNameList[self.comboBoxPort.currentIndex()]
        if self.port not in portNameList:#端口移除
            print('serial_port_refresh: remove', self.port)
            self.serial_close()
        else:
            print('serial_port_refresh: insert', self.port)
            # print(portNameList)
            self.comboBoxPort.setCurrentIndex(portNameList.index(self.port))
            if self.actionAutoConnect.isChecked():
                self.serial_open()
        self.comboBoxPort.blockSignals(False)

    def serial_port_set(self, port):
        portComList = []
        port_list=list(serial.tools.list_ports.comports())
        port_list.sort()
        for port_list_0 in port_list:
            com = list(port_list_0)
            portComList.append(com[0])
        if port in portComList:
            self.comboBoxPort.setCurrentIndex(portComList.index(port))
            return True
        else:
            return False

    def view_send_visible(self, visible):
        if visible:
            self.dataLayout.insertLayout(1, self.sendBox)
            self.sendBox.insertWidget(0, self.plainTextEdit)
            self.plainTextEdit.show()
            self.sendBox.insertWidget(1, self.pushButtonSend)
            self.pushButtonSend.show()
            self.dataLayout.insertWidget(2, self.comboBoxSend)
            self.comboBoxSend.show()
            self.serial_recvAutoScroll()
        else:
            self.plainTextEdit.setParent(None)
            self.pushButtonSend.setParent(None)
            self.comboBoxSend.setParent(None)
            self.dataLayout.removeItem(self.sendBox)

    @pyqtSlot()
    def on_textBrowser_textChanged(self):
        """
        Slot documentation goes here.
        """
        self.serial_recvAutoScroll()

    @pyqtSlot(bool)
    def on_checkBoxResend_toggled(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        if not checked:
            self.resendThreadState=False

    @pyqtSlot()
    def on_pushButtonSend_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.checkBoxResend.isChecked():
            if not self.resendThread.is_alive():
                self.resendThread = threading.Thread(target=self.serial_resendThread, name='resendThread')
                #join和setDaemon作用相反，前者等待子线程结束，后者不等子线程结束，有可能把子线程强制结束。
                #如果都不设置，主线程和子线程各自运行，互不影响
                #setDaemon必须在start() 方法调用之前设置，否则程序会被无限挂起。参数True表示主调线程为为守护线程，
                self.resendThread.setDaemon(True)
                self.resendThread.start()
                #join在start()之后调用，参数为超时时间
                #self.resendThread.join()
            else:
                self.resendThreadState=False
        else:
            self.serial_send()

    @pyqtSlot(bool)
    def on_run_triggered(self):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        if self.runStates == SERIAL_STOP:
            portNameList = []
            port_list=list(serial.tools.list_ports.comports())
            port_list.sort()
            for port_list_0 in port_list:
                port = list(port_list_0)
                portNameList.append(port[0])
            if self.port and self.port in portNameList:
                self.serial_open()
        elif self.runStates == SERIAL_RUN:
            self.runStates = SERIAL_PAUSE
            self.run.setIcon(QIcon(':/icon/resource/icon/trist_bk48.png'))
        elif self.runStates == SERIAL_PAUSE:
            self.runStates = SERIAL_RUN
            self.run.setIcon(QIcon(':/icon/resource/icon/pause_bk48.png'))
        else:
            print('on_run_triggered: run state error!')

    @pyqtSlot()
    def on_stop_triggered(self):
        """
        Slot documentation goes here.
        """
        self.actionAutoConnect.setChecked(False)
        self.serial_close()

    @pyqtSlot()
    def on_clear_triggered(self):
        """
        Slot documentation goes here.
        """
        self.rxCount = 0
        self.txCount = 0
        self.streamCursor = 0
        self.memStream.close()
        self.textBrowser.clear()
        self.InfoRx.setText('RX: {} Bytes'.format(self.rxCount))
        self.InfoTx.setText('TX: {} Bytes'.format(self.txCount))
        self.monitorCnt = 0
        self.lcdNumber.display(self.monitorCnt)
        self.memStream = StringIO()

    @pyqtSlot(int)
    def on_comboBoxPort_currentIndexChanged(self, index):
        """
        Slot documentation goes here.

        @param index DESCRIPTION
        @type int
        """
        if index == -1:
            return
        port_list=list(serial.tools.list_ports.comports())
        port_list.sort()
        self.port = list(port_list)[index][0]
        print('comboBoxPort', self.port)
        if self.actionAutoConnect.isChecked():
            self.AutoConnectPort = self.port
            self.settings.setValue('Auto', self.AutoConnectPort)
        if self.runStates != SERIAL_STOP:
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
            if self.runStates != SERIAL_STOP:
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
            print("Baud change %d" % self.baudrate)
            if self.runStates != SERIAL_STOP:
                self.serial_open()

    @pyqtSlot(int)
    def on_comboBoxDataBit_currentIndexChanged(self, index):
        """
        Slot documentation goes here.

        @param index DESCRIPTION
        @type int
        """
        self.bytesize=int(self.comboBoxDataBit.currentText())
        if self.runStates != SERIAL_STOP:
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
        if self.runStates != SERIAL_STOP:
            self.serial_open()

    @pyqtSlot(int)
    def on_comboBoxStopBit_currentIndexChanged(self, index):
        """
        Slot documentation goes here.

        @param index DESCRIPTION
        @type int
        """
        self.stopbits=float(self.comboBoxStopBit.currentText())
        if self.runStates != SERIAL_STOP:
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
        if self.runStates != SERIAL_STOP:
            self.serial_open()

    @pyqtSlot(str)
    def on_comboBoxSend_textActivated(self, text):
        """
        Slot documentation goes here.

        @param index DESCRIPTION
        @type int
        """
        print('on_comboBoxSend_textActivated:', text)
        if len(text):
            self.plainTextEdit.setPlainText(text)

    @pyqtSlot()
    def on_radioButtonRecvASCII_pressed(self):
        """
        Slot documentation goes here.
        """
        self.settings.setValue('RecvFormat', 1)

    @pyqtSlot()
    def on_radioButtonRecvHex_pressed(self):
        """
        Slot documentation goes here.
        """
        self.settings.setValue('RecvFormat', 0)

    @pyqtSlot()
    def on_radioButtonSendASCII_pressed(self):
        """
        Slot documentation goes here.
        """
        self.settings.setValue('SendFormat', 1)

    @pyqtSlot()
    def on_radioButtonSendHex_pressed(self):
        """
        Slot documentation goes here.
        """
        self.settings.setValue('SendFormat', 0)

    @pyqtSlot(bool)
    def on_actionAutoConnect_toggled(self, p0):
        """
        Slot documentation goes here.

        @param p0 DESCRIPTION
        @type bool
        """
        if p0:
            result = False
            port = None
            if self.AutoConnectPort:
                port, result = AutoConnect.getAutoConnectPort(self.AutoConnectPort)
            else:
                port, result = AutoConnect.getAutoConnectPort(self.port)
            if result:
                self.port = port
                self.AutoConnectPort = self.port
                self.settings.setValue('Auto', self.port)
                if self.serial_port_set(self.port):
                    self.serial_open()
            else:
                self.actionAutoConnect.setChecked(False)

    @pyqtSlot(bool)
    def on_codec_triggered(self):
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

    @pyqtSlot()
    def on_option_triggered(self):
        """
        Slot documentation goes here.
        """
        self.option = Option(self)
        self.option.show()

    @pyqtSlot(bool)
    def on_sideView_toggled(self, p0):
        """
        Slot documentation goes here.

        @param p0 DESCRIPTION
        @type bool
        """
        if p0:
            self.horizontalLayout.insertLayout(0, self.sideLayout)
        else:
            #horizontalLayout为应用于centralWidget的布局，从horizontalLayout删除即为从centralWidget删除
            self.horizontalLayout.removeItem(self.sideLayout)
        print('side view:', p0)

    @pyqtSlot(bool)
    def on_sendView_toggled(self, p0):
        """
        Slot documentation goes here.

        @param p0 DESCRIPTION
        @type bool
        """
        self.view_send_visible(p0)
        if p0:
            self.settings.setValue('SendView', 1)
        else:
            self.settings.setValue('SendView', 0)

    @pyqtSlot()
    def on_viewLayout_clicked(self):
        """
        Slot documentation goes here.
        """
        #设置栏
        sideView = self.sideView.isChecked()
        #发送栏
        sendView = self.sendView.isChecked()
        if sideView == False and sendView:
            if self.horizontalLayout.indexOf(self.sideLayout) == -1:
                self.horizontalLayout.insertLayout(0, self.sideLayout)
            else:
                self.horizontalLayout.removeItem(self.sideLayout)
        elif sideView and sendView == False:
            if self.dataLayout.indexOf(self.sendBox) == -1:
                self.view_send_visible(True)
            else:
                self.view_send_visible(False)
        else:
            if self.horizontalLayout.indexOf(self.sideLayout) == -1:
                self.horizontalLayout.insertLayout(0, self.sideLayout)
                self.view_send_visible(True)
            else:
                self.horizontalLayout.removeItem(self.sideLayout)
                self.view_send_visible(False)

    @pyqtSlot(bool)
    def on_checkBoxNewLine_toggled(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        if self.checkBoxNewLine.isChecked():
            self.settings.setValue('AutoWrap', 1)
        else:
            self.settings.setValue('AutoWrap', 0)

    @pyqtSlot(bool)
    def on_checkBoxEcho_toggled(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        if self.checkBoxEcho.isChecked():
            self.settings.setValue('Echo', 1)
        else:
            self.settings.setValue('Echo', 0)

    @pyqtSlot(bool)
    def on_checkBoxTime_toggled(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        if self.checkBoxTime.isChecked():
            self.settings.setValue('Time', 1)
        else:
            self.settings.setValue('Time', 0)

    @pyqtSlot()
    def on_monitorClear_clicked(self):
        """
        Slot documentation goes here.
        """
        self.monitorCnt = 0
        self.lcdNumber.display(self.monitorCnt)
        
    @pyqtSlot(bool)
    def on_checkBoxBeep_toggled(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        if self.checkBoxBeep.isChecked():
            self.settings.setValue('Beep', 1)
        else:
            self.settings.setValue('Beep', 0)
    
    @pyqtSlot(bool)
    def on_checkBoxMonitor_toggled(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        if self.checkBoxMonitor.isChecked():
            self.settings.setValue('Monitor', 1)
        else:
            self.settings.setValue('Monitor', 0)

    @pyqtSlot(bool)
    def on_sendReturn_toggled(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        if self.sendReturn.isChecked():
            self.settings.setValue('Return', 1)
        else:
            self.settings.setValue('Return', 0)
    
    @pyqtSlot(bool)
    def on_sendEscape_toggled(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        if self.sendEscape.isChecked():
            self.settings.setValue('Escape', 1)
        else:
            self.settings.setValue('Escape', 0)

class SysEventFilter(QAbstractNativeEventFilter):
    def __init__(self, dlg):
        #如果直接在主类中写nativeEventFilter，调用此初始化会出问题
        #推测和super()调用有关系
        QAbstractNativeEventFilter.__init__(self)
        self.dlg = dlg

    def nativeEventFilter(self, eventType, message):
        try:
            if eventType == "windows_generic_MSG" or  eventType == "windows_dispatcher_MSG":
                msg = ctypes.wintypes.MSG.from_address(message.__int__())
                if msg.message == 0x0219: # WM_DEVICECHANGE 消息
                    if msg.wParam == 0x8000: # DBT_DEVICEARRIVAL 已插入设备或介质
                        print("A device or piece of media has been inserted and is now available.")
                        self.dlg.serial_port_refresh()
                    elif msg.wParam == 0x8004: # DBT_DEVICEREMOVECOMPLETE 已删除设备或介质
                        print("A device or piece of media has been removed.")
                        self.dlg.serial_port_refresh()
                    elif msg.wParam == 0x0007: # DBT_DEVNODES 已在系统中添加或删除设备
                        pass
                    else:
                        print('nativeEventFilter: %04X %04X'%(msg.message, msg.wParam))
            else:
                print('nativeEventFilter: %s %04X'%(eventType, message))
        except Exception as e:
            print('nativeEventFilter:', e)
        return False, 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(':/icon/resource/icon/serial256.ico'))
    dlg = SerialPort()
    dlg.show()
    sysMsg = SysEventFilter(dlg)
    app.installNativeEventFilter(sysMsg)
    codec = Codec()
    aboutSoft=About()
    ret = app.exec_()
    print('Exit', ret)
    sys.exit(ret)
