# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\workbench\PyQt\GSP\SerialPort.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 712)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.optionLayout = QtWidgets.QVBoxLayout()
        self.optionLayout.setContentsMargins(3, -1, 3, -1)
        self.optionLayout.setSpacing(7)
        self.optionLayout.setObjectName("optionLayout")
        self.groupBoxPort = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxPort.sizePolicy().hasHeightForWidth())
        self.groupBoxPort.setSizePolicy(sizePolicy)
        self.groupBoxPort.setMinimumSize(QtCore.QSize(210, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.groupBoxPort.setFont(font)
        self.groupBoxPort.setObjectName("groupBoxPort")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBoxPort)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(-1, 5, 7, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelPort = QtWidgets.QLabel(self.groupBoxPort)
        self.labelPort.setObjectName("labelPort")
        self.verticalLayout_4.addWidget(self.labelPort)
        self.labelBaud = QtWidgets.QLabel(self.groupBoxPort)
        self.labelBaud.setObjectName("labelBaud")
        self.verticalLayout_4.addWidget(self.labelBaud)
        self.labelDataBit = QtWidgets.QLabel(self.groupBoxPort)
        self.labelDataBit.setObjectName("labelDataBit")
        self.verticalLayout_4.addWidget(self.labelDataBit)
        self.labelParity = QtWidgets.QLabel(self.groupBoxPort)
        self.labelParity.setObjectName("labelParity")
        self.verticalLayout_4.addWidget(self.labelParity)
        self.labelStopBit = QtWidgets.QLabel(self.groupBoxPort)
        self.labelStopBit.setObjectName("labelStopBit")
        self.verticalLayout_4.addWidget(self.labelStopBit)
        self.labelFlow = QtWidgets.QLabel(self.groupBoxPort)
        self.labelFlow.setObjectName("labelFlow")
        self.verticalLayout_4.addWidget(self.labelFlow)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.comboBoxPort = QtWidgets.QComboBox(self.groupBoxPort)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxPort.sizePolicy().hasHeightForWidth())
        self.comboBoxPort.setSizePolicy(sizePolicy)
        self.comboBoxPort.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBoxPort.setObjectName("comboBoxPort")
        self.verticalLayout_5.addWidget(self.comboBoxPort)
        self.comboBoxBaud = QtWidgets.QComboBox(self.groupBoxPort)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxBaud.sizePolicy().hasHeightForWidth())
        self.comboBoxBaud.setSizePolicy(sizePolicy)
        self.comboBoxBaud.setObjectName("comboBoxBaud")
        self.verticalLayout_5.addWidget(self.comboBoxBaud)
        self.comboBoxDataBit = QtWidgets.QComboBox(self.groupBoxPort)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxDataBit.sizePolicy().hasHeightForWidth())
        self.comboBoxDataBit.setSizePolicy(sizePolicy)
        self.comboBoxDataBit.setObjectName("comboBoxDataBit")
        self.verticalLayout_5.addWidget(self.comboBoxDataBit)
        self.comboBoxParity = QtWidgets.QComboBox(self.groupBoxPort)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxParity.sizePolicy().hasHeightForWidth())
        self.comboBoxParity.setSizePolicy(sizePolicy)
        self.comboBoxParity.setObjectName("comboBoxParity")
        self.verticalLayout_5.addWidget(self.comboBoxParity)
        self.comboBoxStopBit = QtWidgets.QComboBox(self.groupBoxPort)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxStopBit.sizePolicy().hasHeightForWidth())
        self.comboBoxStopBit.setSizePolicy(sizePolicy)
        self.comboBoxStopBit.setObjectName("comboBoxStopBit")
        self.verticalLayout_5.addWidget(self.comboBoxStopBit)
        self.comboBoxFlow = QtWidgets.QComboBox(self.groupBoxPort)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxFlow.sizePolicy().hasHeightForWidth())
        self.comboBoxFlow.setSizePolicy(sizePolicy)
        self.comboBoxFlow.setObjectName("comboBoxFlow")
        self.verticalLayout_5.addWidget(self.comboBoxFlow)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 4)
        self.optionLayout.addWidget(self.groupBoxPort)
        self.groupBoxRecv = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxRecv.sizePolicy().hasHeightForWidth())
        self.groupBoxRecv.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBoxRecv.setFont(font)
        self.groupBoxRecv.setObjectName("groupBoxRecv")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBoxRecv)
        self.verticalLayout_6.setContentsMargins(-1, 5, 7, 5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButtonRecvASCII = QtWidgets.QRadioButton(self.groupBoxRecv)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonRecvASCII.sizePolicy().hasHeightForWidth())
        self.radioButtonRecvASCII.setSizePolicy(sizePolicy)
        self.radioButtonRecvASCII.setObjectName("radioButtonRecvASCII")
        self.horizontalLayout_4.addWidget(self.radioButtonRecvASCII)
        self.radioButtonRecvHex = QtWidgets.QRadioButton(self.groupBoxRecv)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonRecvHex.sizePolicy().hasHeightForWidth())
        self.radioButtonRecvHex.setSizePolicy(sizePolicy)
        self.radioButtonRecvHex.setObjectName("radioButtonRecvHex")
        self.horizontalLayout_4.addWidget(self.radioButtonRecvHex)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.checkBoxTime = QtWidgets.QCheckBox(self.groupBoxRecv)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxTime.sizePolicy().hasHeightForWidth())
        self.checkBoxTime.setSizePolicy(sizePolicy)
        self.checkBoxTime.setObjectName("checkBoxTime")
        self.horizontalLayout_9.addWidget(self.checkBoxTime)
        self.checkBoxNewLine = QtWidgets.QCheckBox(self.groupBoxRecv)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxNewLine.sizePolicy().hasHeightForWidth())
        self.checkBoxNewLine.setSizePolicy(sizePolicy)
        self.checkBoxNewLine.setObjectName("checkBoxNewLine")
        self.horizontalLayout_9.addWidget(self.checkBoxNewLine)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.optionLayout.addWidget(self.groupBoxRecv)
        self.groupBoxSend = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxSend.sizePolicy().hasHeightForWidth())
        self.groupBoxSend.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBoxSend.setFont(font)
        self.groupBoxSend.setObjectName("groupBoxSend")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxSend)
        self.verticalLayout.setContentsMargins(-1, 5, 7, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.radioButtonSendASCII = QtWidgets.QRadioButton(self.groupBoxSend)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonSendASCII.sizePolicy().hasHeightForWidth())
        self.radioButtonSendASCII.setSizePolicy(sizePolicy)
        self.radioButtonSendASCII.setObjectName("radioButtonSendASCII")
        self.horizontalLayout_7.addWidget(self.radioButtonSendASCII)
        self.radioButtonSendHex = QtWidgets.QRadioButton(self.groupBoxSend)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonSendHex.sizePolicy().hasHeightForWidth())
        self.radioButtonSendHex.setSizePolicy(sizePolicy)
        self.radioButtonSendHex.setObjectName("radioButtonSendHex")
        self.horizontalLayout_7.addWidget(self.radioButtonSendHex)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.checkBoxEcho = QtWidgets.QCheckBox(self.groupBoxSend)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxEcho.sizePolicy().hasHeightForWidth())
        self.checkBoxEcho.setSizePolicy(sizePolicy)
        self.checkBoxEcho.setObjectName("checkBoxEcho")
        self.verticalLayout.addWidget(self.checkBoxEcho)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.sendReturn = QtWidgets.QCheckBox(self.groupBoxSend)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendReturn.sizePolicy().hasHeightForWidth())
        self.sendReturn.setSizePolicy(sizePolicy)
        self.sendReturn.setObjectName("sendReturn")
        self.horizontalLayout_10.addWidget(self.sendReturn)
        self.sendEscape = QtWidgets.QCheckBox(self.groupBoxSend)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendEscape.sizePolicy().hasHeightForWidth())
        self.sendEscape.setSizePolicy(sizePolicy)
        self.sendEscape.setObjectName("sendEscape")
        self.horizontalLayout_10.addWidget(self.sendEscape)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBoxResend = QtWidgets.QCheckBox(self.groupBoxSend)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxResend.sizePolicy().hasHeightForWidth())
        self.checkBoxResend.setSizePolicy(sizePolicy)
        self.checkBoxResend.setObjectName("checkBoxResend")
        self.horizontalLayout_8.addWidget(self.checkBoxResend)
        self.spinBoxTime = QtWidgets.QSpinBox(self.groupBoxSend)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxTime.sizePolicy().hasHeightForWidth())
        self.spinBoxTime.setSizePolicy(sizePolicy)
        self.spinBoxTime.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBoxTime.setMinimum(10)
        self.spinBoxTime.setMaximum(1000000000)
        self.spinBoxTime.setSingleStep(100)
        self.spinBoxTime.setProperty("value", 1000)
        self.spinBoxTime.setObjectName("spinBoxTime")
        self.horizontalLayout_8.addWidget(self.spinBoxTime)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.optionLayout.addWidget(self.groupBoxSend)
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBoxBeep = QtWidgets.QCheckBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxBeep.sizePolicy().hasHeightForWidth())
        self.checkBoxBeep.setSizePolicy(sizePolicy)
        self.checkBoxBeep.setObjectName("checkBoxBeep")
        self.horizontalLayout_6.addWidget(self.checkBoxBeep)
        self.checkBoxMonitor = QtWidgets.QCheckBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxMonitor.sizePolicy().hasHeightForWidth())
        self.checkBoxMonitor.setSizePolicy(sizePolicy)
        self.checkBoxMonitor.setObjectName("checkBoxMonitor")
        self.horizontalLayout_6.addWidget(self.checkBoxMonitor)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditMonitor = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditMonitor.sizePolicy().hasHeightForWidth())
        self.lineEditMonitor.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEditMonitor.setFont(font)
        self.lineEditMonitor.setObjectName("lineEditMonitor")
        self.horizontalLayout_2.addWidget(self.lineEditMonitor)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lcdNumber.setFont(font)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber.setDigitCount(6)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_5.addWidget(self.lcdNumber)
        self.monitorClear = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.monitorClear.sizePolicy().hasHeightForWidth())
        self.monitorClear.setSizePolicy(sizePolicy)
        self.monitorClear.setObjectName("monitorClear")
        self.horizontalLayout_5.addWidget(self.monitorClear)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.optionLayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.optionLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.optionLayout)
        self.dataLayout = QtWidgets.QVBoxLayout()
        self.dataLayout.setSpacing(3)
        self.dataLayout.setObjectName("dataLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.dataLayout.addWidget(self.textBrowser)
        self.sendBox = QtWidgets.QHBoxLayout()
        self.sendBox.setSpacing(5)
        self.sendBox.setObjectName("sendBox")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.sendBox.addWidget(self.plainTextEdit)
        self.pushButtonSend = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.sendBox.addWidget(self.pushButtonSend)
        self.dataLayout.addLayout(self.sendBox)
        self.comboBoxSend = QtWidgets.QComboBox(self.centralWidget)
        self.comboBoxSend.setObjectName("comboBoxSend")
        self.dataLayout.addWidget(self.comboBoxSend)
        self.horizontalLayout.addLayout(self.dataLayout)
        self.horizontalLayout.setStretch(1, 4)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(40, 40))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1023, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuTool = QtWidgets.QMenu(self.menuBar)
        self.menuTool.setObjectName("menuTool")
        self.menuSet = QtWidgets.QMenu(self.menuBar)
        self.menuSet.setObjectName("menuSet")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.run = QtWidgets.QAction(MainWindow)
        self.run.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/resource/icon/trist48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.run.setIcon(icon)
        self.run.setObjectName("run")
        self.stop = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/resource/icon/rect48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop.setIcon(icon1)
        self.stop.setObjectName("stop")
        self.codec = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/resource/icon/codec48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.codec.setIcon(icon2)
        self.codec.setObjectName("codec")
        self.about = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/resource/icon/info48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about.setIcon(icon3)
        self.about.setObjectName("about")
        self.clear = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/resource/icon/clean48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear.setIcon(icon4)
        self.clear.setObjectName("clear")
        self.actionAutoConnect = QtWidgets.QAction(MainWindow)
        self.actionAutoConnect.setCheckable(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/resource/icon/link48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAutoConnect.setIcon(icon5)
        self.actionAutoConnect.setObjectName("actionAutoConnect")
        self.optionView = QtWidgets.QAction(MainWindow)
        self.optionView.setCheckable(True)
        self.optionView.setChecked(False)
        self.optionView.setObjectName("optionView")
        self.sendView = QtWidgets.QAction(MainWindow)
        self.sendView.setCheckable(True)
        self.sendView.setChecked(True)
        self.sendView.setObjectName("sendView")
        self.actionFont = QtWidgets.QAction(MainWindow)
        self.actionFont.setObjectName("actionFont")
        self.toolBar.addAction(self.run)
        self.toolBar.addAction(self.stop)
        self.toolBar.addAction(self.actionAutoConnect)
        self.toolBar.addAction(self.clear)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.codec)
        self.toolBar.addAction(self.about)
        self.menuSet.addAction(self.optionView)
        self.menuSet.addAction(self.sendView)
        self.menuSet.addAction(self.actionFont)
        self.menuBar.addAction(self.menuSet.menuAction())
        self.menuBar.addAction(self.menuTool.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GSP"))
        self.groupBoxPort.setTitle(_translate("MainWindow", "串口设置"))
        self.labelPort.setText(_translate("MainWindow", "端    口"))
        self.labelBaud.setText(_translate("MainWindow", "波特率"))
        self.labelDataBit.setText(_translate("MainWindow", "数据位"))
        self.labelParity.setText(_translate("MainWindow", "校验位"))
        self.labelStopBit.setText(_translate("MainWindow", "停止位"))
        self.labelFlow.setText(_translate("MainWindow", "流    控"))
        self.groupBoxRecv.setTitle(_translate("MainWindow", "显示设置"))
        self.radioButtonRecvASCII.setText(_translate("MainWindow", "ASCII"))
        self.radioButtonRecvHex.setText(_translate("MainWindow", "HEX"))
        self.checkBoxTime.setText(_translate("MainWindow", "显示时间"))
        self.checkBoxNewLine.setText(_translate("MainWindow", "自动换行"))
        self.groupBoxSend.setTitle(_translate("MainWindow", "发送设置"))
        self.radioButtonSendASCII.setText(_translate("MainWindow", "ASCII"))
        self.radioButtonSendHex.setText(_translate("MainWindow", "HEX"))
        self.checkBoxEcho.setText(_translate("MainWindow", "显示发送"))
        self.sendReturn.setText(_translate("MainWindow", "添加回车"))
        self.sendEscape.setText(_translate("MainWindow", "转义 \\r \\n"))
        self.checkBoxResend.setText(_translate("MainWindow", "自动重发"))
        self.spinBoxTime.setSuffix(_translate("MainWindow", " ms"))
        self.groupBox.setTitle(_translate("MainWindow", "接收监测"))
        self.checkBoxBeep.setText(_translate("MainWindow", "提示音"))
        self.checkBoxMonitor.setText(_translate("MainWindow", "启用"))
        self.monitorClear.setText(_translate("MainWindow", "清零"))
        self.pushButtonSend.setText(_translate("MainWindow", "发送"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuTool.setTitle(_translate("MainWindow", "工具"))
        self.menuSet.setTitle(_translate("MainWindow", "设置"))
        self.menuHelp.setTitle(_translate("MainWindow", "帮助"))
        self.run.setText(_translate("MainWindow", "运行"))
        self.stop.setText(_translate("MainWindow", "停止"))
        self.codec.setText(_translate("MainWindow", "编码转换"))
        self.about.setText(_translate("MainWindow", "关于"))
        self.clear.setText(_translate("MainWindow", "清屏"))
        self.clear.setToolTip(_translate("MainWindow", "清屏"))
        self.actionAutoConnect.setText(_translate("MainWindow", "自动连接"))
        self.actionAutoConnect.setToolTip(_translate("MainWindow", "自动连接"))
        self.optionView.setText(_translate("MainWindow", "侧边栏"))
        self.sendView.setText(_translate("MainWindow", "发送项"))
        self.actionFont.setText(_translate("MainWindow", "字体"))
        self.actionFont.setToolTip(_translate("MainWindow", "字体"))
import imgResource_rc
