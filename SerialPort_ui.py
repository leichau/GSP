# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SerialPort.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QFrame, QGroupBox, QHBoxLayout, QLCDNumber,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTextBrowser, QToolBar,
    QVBoxLayout, QWidget)
import imgResource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(922, 618)
        self.run = QAction(MainWindow)
        self.run.setObjectName(u"run")
        icon = QIcon()
        icon.addFile(u":/icon/resource/icon/trist48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.run.setIcon(icon)
        self.stop = QAction(MainWindow)
        self.stop.setObjectName(u"stop")
        icon1 = QIcon()
        icon1.addFile(u":/icon/resource/icon/rect48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stop.setIcon(icon1)
        self.codec = QAction(MainWindow)
        self.codec.setObjectName(u"codec")
        icon2 = QIcon()
        icon2.addFile(u":/icon/resource/icon/codec48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.codec.setIcon(icon2)
        self.about = QAction(MainWindow)
        self.about.setObjectName(u"about")
        icon3 = QIcon()
        icon3.addFile(u":/icon/resource/icon/setting48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.about.setIcon(icon3)
        self.clear = QAction(MainWindow)
        self.clear.setObjectName(u"clear")
        icon4 = QIcon()
        icon4.addFile(u":/icon/resource/icon/clean48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clear.setIcon(icon4)
        self.actionAutoConnect = QAction(MainWindow)
        self.actionAutoConnect.setObjectName(u"actionAutoConnect")
        self.actionAutoConnect.setCheckable(True)
        icon5 = QIcon()
        icon5.addFile(u":/icon/resource/icon/link48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAutoConnect.setIcon(icon5)
        self.sideView = QAction(MainWindow)
        self.sideView.setObjectName(u"sideView")
        self.sideView.setCheckable(True)
        self.sideView.setChecked(False)
        self.sendView = QAction(MainWindow)
        self.sendView.setObjectName(u"sendView")
        self.sendView.setCheckable(True)
        self.sendView.setChecked(True)
        self.option = QAction(MainWindow)
        self.option.setObjectName(u"option")
        self.option.setIcon(icon3)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 2, 3, 3)
        self.sideLayout = QVBoxLayout()
        self.sideLayout.setSpacing(7)
        self.sideLayout.setObjectName(u"sideLayout")
        self.sideLayout.setContentsMargins(3, -1, 3, -1)
        self.groupBoxPort = QGroupBox(self.centralWidget)
        self.groupBoxPort.setObjectName(u"groupBoxPort")
        sizePolicy.setHeightForWidth(self.groupBoxPort.sizePolicy().hasHeightForWidth())
        self.groupBoxPort.setSizePolicy(sizePolicy)
        self.groupBoxPort.setMinimumSize(QSize(210, 191))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(9)
        self.groupBoxPort.setFont(font)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBoxPort)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 5, 7, 5)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelPort = QLabel(self.groupBoxPort)
        self.labelPort.setObjectName(u"labelPort")

        self.verticalLayout_4.addWidget(self.labelPort)

        self.labelBaud = QLabel(self.groupBoxPort)
        self.labelBaud.setObjectName(u"labelBaud")

        self.verticalLayout_4.addWidget(self.labelBaud)

        self.labelDataBit = QLabel(self.groupBoxPort)
        self.labelDataBit.setObjectName(u"labelDataBit")

        self.verticalLayout_4.addWidget(self.labelDataBit)

        self.labelParity = QLabel(self.groupBoxPort)
        self.labelParity.setObjectName(u"labelParity")

        self.verticalLayout_4.addWidget(self.labelParity)

        self.labelStopBit = QLabel(self.groupBoxPort)
        self.labelStopBit.setObjectName(u"labelStopBit")

        self.verticalLayout_4.addWidget(self.labelStopBit)

        self.labelFlow = QLabel(self.groupBoxPort)
        self.labelFlow.setObjectName(u"labelFlow")

        self.verticalLayout_4.addWidget(self.labelFlow)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.comboBoxPort = QComboBox(self.groupBoxPort)
        self.comboBoxPort.setObjectName(u"comboBoxPort")
        sizePolicy.setHeightForWidth(self.comboBoxPort.sizePolicy().hasHeightForWidth())
        self.comboBoxPort.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.comboBoxPort)

        self.comboBoxBaud = QComboBox(self.groupBoxPort)
        self.comboBoxBaud.setObjectName(u"comboBoxBaud")
        sizePolicy.setHeightForWidth(self.comboBoxBaud.sizePolicy().hasHeightForWidth())
        self.comboBoxBaud.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.comboBoxBaud)

        self.comboBoxDataBit = QComboBox(self.groupBoxPort)
        self.comboBoxDataBit.setObjectName(u"comboBoxDataBit")
        sizePolicy.setHeightForWidth(self.comboBoxDataBit.sizePolicy().hasHeightForWidth())
        self.comboBoxDataBit.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.comboBoxDataBit)

        self.comboBoxParity = QComboBox(self.groupBoxPort)
        self.comboBoxParity.setObjectName(u"comboBoxParity")
        sizePolicy.setHeightForWidth(self.comboBoxParity.sizePolicy().hasHeightForWidth())
        self.comboBoxParity.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.comboBoxParity)

        self.comboBoxStopBit = QComboBox(self.groupBoxPort)
        self.comboBoxStopBit.setObjectName(u"comboBoxStopBit")
        sizePolicy.setHeightForWidth(self.comboBoxStopBit.sizePolicy().hasHeightForWidth())
        self.comboBoxStopBit.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.comboBoxStopBit)

        self.comboBoxFlow = QComboBox(self.groupBoxPort)
        self.comboBoxFlow.setObjectName(u"comboBoxFlow")
        sizePolicy.setHeightForWidth(self.comboBoxFlow.sizePolicy().hasHeightForWidth())
        self.comboBoxFlow.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.comboBoxFlow)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 4)

        self.sideLayout.addWidget(self.groupBoxPort)

        self.groupBoxRecv = QGroupBox(self.centralWidget)
        self.groupBoxRecv.setObjectName(u"groupBoxRecv")
        sizePolicy.setHeightForWidth(self.groupBoxRecv.sizePolicy().hasHeightForWidth())
        self.groupBoxRecv.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        self.groupBoxRecv.setFont(font1)
        self.verticalLayout_6 = QVBoxLayout(self.groupBoxRecv)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 5, 7, 5)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radioButtonRecvASCII = QRadioButton(self.groupBoxRecv)
        self.radioButtonRecvASCII.setObjectName(u"radioButtonRecvASCII")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.radioButtonRecvASCII.sizePolicy().hasHeightForWidth())
        self.radioButtonRecvASCII.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.radioButtonRecvASCII)

        self.radioButtonRecvHex = QRadioButton(self.groupBoxRecv)
        self.radioButtonRecvHex.setObjectName(u"radioButtonRecvHex")
        sizePolicy1.setHeightForWidth(self.radioButtonRecvHex.sizePolicy().hasHeightForWidth())
        self.radioButtonRecvHex.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.radioButtonRecvHex)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.checkBoxTime = QCheckBox(self.groupBoxRecv)
        self.checkBoxTime.setObjectName(u"checkBoxTime")
        sizePolicy1.setHeightForWidth(self.checkBoxTime.sizePolicy().hasHeightForWidth())
        self.checkBoxTime.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.checkBoxTime)

        self.checkBoxNewLine = QCheckBox(self.groupBoxRecv)
        self.checkBoxNewLine.setObjectName(u"checkBoxNewLine")
        sizePolicy1.setHeightForWidth(self.checkBoxNewLine.sizePolicy().hasHeightForWidth())
        self.checkBoxNewLine.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.checkBoxNewLine)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)


        self.sideLayout.addWidget(self.groupBoxRecv)

        self.groupBoxSend = QGroupBox(self.centralWidget)
        self.groupBoxSend.setObjectName(u"groupBoxSend")
        sizePolicy.setHeightForWidth(self.groupBoxSend.sizePolicy().hasHeightForWidth())
        self.groupBoxSend.setSizePolicy(sizePolicy)
        self.groupBoxSend.setFont(font1)
        self.verticalLayout = QVBoxLayout(self.groupBoxSend)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 5, 7, 5)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.radioButtonSendASCII = QRadioButton(self.groupBoxSend)
        self.radioButtonSendASCII.setObjectName(u"radioButtonSendASCII")
        sizePolicy1.setHeightForWidth(self.radioButtonSendASCII.sizePolicy().hasHeightForWidth())
        self.radioButtonSendASCII.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.radioButtonSendASCII)

        self.radioButtonSendHex = QRadioButton(self.groupBoxSend)
        self.radioButtonSendHex.setObjectName(u"radioButtonSendHex")
        sizePolicy1.setHeightForWidth(self.radioButtonSendHex.sizePolicy().hasHeightForWidth())
        self.radioButtonSendHex.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.radioButtonSendHex)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.checkBoxEcho = QCheckBox(self.groupBoxSend)
        self.checkBoxEcho.setObjectName(u"checkBoxEcho")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.checkBoxEcho.sizePolicy().hasHeightForWidth())
        self.checkBoxEcho.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.checkBoxEcho)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.sendReturn = QCheckBox(self.groupBoxSend)
        self.sendReturn.setObjectName(u"sendReturn")
        sizePolicy1.setHeightForWidth(self.sendReturn.sizePolicy().hasHeightForWidth())
        self.sendReturn.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.sendReturn)

        self.sendEscape = QCheckBox(self.groupBoxSend)
        self.sendEscape.setObjectName(u"sendEscape")
        sizePolicy1.setHeightForWidth(self.sendEscape.sizePolicy().hasHeightForWidth())
        self.sendEscape.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.sendEscape)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkBoxResend = QCheckBox(self.groupBoxSend)
        self.checkBoxResend.setObjectName(u"checkBoxResend")
        sizePolicy1.setHeightForWidth(self.checkBoxResend.sizePolicy().hasHeightForWidth())
        self.checkBoxResend.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.checkBoxResend)

        self.spinBoxTime = QSpinBox(self.groupBoxSend)
        self.spinBoxTime.setObjectName(u"spinBoxTime")
        sizePolicy1.setHeightForWidth(self.spinBoxTime.sizePolicy().hasHeightForWidth())
        self.spinBoxTime.setSizePolicy(sizePolicy1)
        self.spinBoxTime.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinBoxTime.setMinimum(10)
        self.spinBoxTime.setMaximum(1000000000)
        self.spinBoxTime.setSingleStep(100)
        self.spinBoxTime.setValue(1000)

        self.horizontalLayout_8.addWidget(self.spinBoxTime)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.sideLayout.addWidget(self.groupBoxSend)

        self.groupBox = QGroupBox(self.centralWidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.groupBox.setFont(font1)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBoxBeep = QCheckBox(self.groupBox)
        self.checkBoxBeep.setObjectName(u"checkBoxBeep")
        sizePolicy1.setHeightForWidth(self.checkBoxBeep.sizePolicy().hasHeightForWidth())
        self.checkBoxBeep.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.checkBoxBeep)

        self.checkBoxMonitor = QCheckBox(self.groupBox)
        self.checkBoxMonitor.setObjectName(u"checkBoxMonitor")
        sizePolicy.setHeightForWidth(self.checkBoxMonitor.sizePolicy().hasHeightForWidth())
        self.checkBoxMonitor.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.checkBoxMonitor)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEditMonitor = QLineEdit(self.groupBox)
        self.lineEditMonitor.setObjectName(u"lineEditMonitor")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEditMonitor.sizePolicy().hasHeightForWidth())
        self.lineEditMonitor.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        self.lineEditMonitor.setFont(font2)

        self.horizontalLayout_2.addWidget(self.lineEditMonitor)

        self.colorButton = QPushButton(self.groupBox)
        self.colorButton.setObjectName(u"colorButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.colorButton.sizePolicy().hasHeightForWidth())
        self.colorButton.setSizePolicy(sizePolicy5)
        self.colorButton.setMaximumSize(QSize(28, 16777215))
        self.colorButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.colorButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lcdNumber = QLCDNumber(self.groupBox)
        self.lcdNumber.setObjectName(u"lcdNumber")
        sizePolicy3.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy3)
        self.lcdNumber.setFont(font1)
        self.lcdNumber.setFrameShape(QFrame.Shape.Box)
        self.lcdNumber.setFrameShadow(QFrame.Shadow.Sunken)
        self.lcdNumber.setDigitCount(6)
        self.lcdNumber.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_5.addWidget(self.lcdNumber)

        self.monitorClear = QPushButton(self.groupBox)
        self.monitorClear.setObjectName(u"monitorClear")
        sizePolicy4.setHeightForWidth(self.monitorClear.sizePolicy().hasHeightForWidth())
        self.monitorClear.setSizePolicy(sizePolicy4)
        self.monitorClear.setFont(font2)

        self.horizontalLayout_5.addWidget(self.monitorClear)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.sideLayout.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sideLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.sideLayout)

        self.dataLayout = QVBoxLayout()
        self.dataLayout.setSpacing(1)
        self.dataLayout.setObjectName(u"dataLayout")
        self.textBrowser = QTextBrowser(self.centralWidget)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy6)
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(11)
        self.textBrowser.setFont(font3)

        self.dataLayout.addWidget(self.textBrowser)

        self.sendBox = QHBoxLayout()
        self.sendBox.setSpacing(5)
        self.sendBox.setObjectName(u"sendBox")
        self.plainTextEdit = QPlainTextEdit(self.centralWidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy7)
        self.plainTextEdit.setMaximumSize(QSize(16777215, 80))
        self.plainTextEdit.setFont(font3)

        self.sendBox.addWidget(self.plainTextEdit)

        self.pushButtonSend = QPushButton(self.centralWidget)
        self.pushButtonSend.setObjectName(u"pushButtonSend")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.pushButtonSend.sizePolicy().hasHeightForWidth())
        self.pushButtonSend.setSizePolicy(sizePolicy8)
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.pushButtonSend.setFont(font4)

        self.sendBox.addWidget(self.pushButtonSend)


        self.dataLayout.addLayout(self.sendBox)

        self.comboBoxSend = QComboBox(self.centralWidget)
        self.comboBoxSend.setObjectName(u"comboBoxSend")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.comboBoxSend.sizePolicy().hasHeightForWidth())
        self.comboBoxSend.setSizePolicy(sizePolicy9)
        self.comboBoxSend.setFont(font2)

        self.dataLayout.addWidget(self.comboBoxSend)


        self.horizontalLayout.addLayout(self.dataLayout)

        self.horizontalLayout.setStretch(1, 4)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy1.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy1)
        self.toolBar.setIconSize(QSize(40, 40))
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.run)
        self.toolBar.addAction(self.stop)
        self.toolBar.addAction(self.actionAutoConnect)
        self.toolBar.addAction(self.clear)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.option)
        self.toolBar.addAction(self.codec)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GSP", None))
        self.run.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.codec.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u8f6c\u6362", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u5c4f", None))
#if QT_CONFIG(tooltip)
        self.clear.setToolTip(QCoreApplication.translate("MainWindow", u"\u6e05\u5c4f\uff08Ctrl+Delete\uff09", None))
#endif // QT_CONFIG(tooltip)
        self.actionAutoConnect.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u8fde\u63a5", None))
#if QT_CONFIG(tooltip)
        self.actionAutoConnect.setToolTip(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u8fde\u63a5", None))
#endif // QT_CONFIG(tooltip)
        self.sideView.setText(QCoreApplication.translate("MainWindow", u"\u4fa7\u8fb9\u680f", None))
        self.sendView.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u680f", None))
        self.option.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.option.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.groupBoxPort.setTitle(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u8bbe\u7f6e", None))
        self.labelPort.setText(QCoreApplication.translate("MainWindow", u"\u7aef    \u53e3", None))
        self.labelBaud.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387", None))
        self.labelDataBit.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4f4d", None))
        self.labelParity.setText(QCoreApplication.translate("MainWindow", u"\u6821\u9a8c\u4f4d", None))
        self.labelStopBit.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u4f4d", None))
        self.labelFlow.setText(QCoreApplication.translate("MainWindow", u"\u6d41    \u63a7", None))
        self.groupBoxRecv.setTitle(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u8bbe\u7f6e", None))
        self.radioButtonRecvASCII.setText(QCoreApplication.translate("MainWindow", u"ASCII", None))
        self.radioButtonRecvHex.setText(QCoreApplication.translate("MainWindow", u"HEX", None))
        self.checkBoxTime.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u65f6\u95f4", None))
        self.checkBoxNewLine.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u6362\u884c", None))
        self.groupBoxSend.setTitle(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u8bbe\u7f6e", None))
        self.radioButtonSendASCII.setText(QCoreApplication.translate("MainWindow", u"ASCII", None))
        self.radioButtonSendHex.setText(QCoreApplication.translate("MainWindow", u"HEX", None))
        self.checkBoxEcho.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u53d1\u9001", None))
        self.sendReturn.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6362\u884c", None))
        self.sendEscape.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u4e49 \\r \\n", None))
        self.checkBoxResend.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u91cd\u53d1", None))
        self.spinBoxTime.setSuffix(QCoreApplication.translate("MainWindow", u" ms", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u63a5\u6536\u76d1\u6d4b", None))
        self.checkBoxBeep.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u793a\u97f3", None))
        self.checkBoxMonitor.setText(QCoreApplication.translate("MainWindow", u"\u542f\u7528", None))
        self.colorButton.setText("")
        self.monitorClear.setText(QCoreApplication.translate("MainWindow", u"\u6e05 \u96f6", None))
#if QT_CONFIG(tooltip)
        self.pushButtonSend.setToolTip(QCoreApplication.translate("MainWindow", u"Ctrl+Enter", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonSend.setText(QCoreApplication.translate("MainWindow", u"\u53d1 \u9001", None))
#if QT_CONFIG(tooltip)
        self.comboBoxSend.setToolTip(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u6761\uff08Ctrl+Up\uff09\n"
"\u4e0b\u4e00\u6761\uff08Ctrl+Down\uff09", None))
#endif // QT_CONFIG(tooltip)
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

