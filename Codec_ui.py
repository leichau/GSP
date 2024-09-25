# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Codec.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)
import imgResource_rc

class Ui_Codec(object):
    def setupUi(self, Codec):
        if not Codec.objectName():
            Codec.setObjectName(u"Codec")
        Codec.resize(900, 600)
        self.centralWidget = QWidget(Codec)
        self.centralWidget.setObjectName(u"centralWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.groupBox = QGroupBox(self.centralWidget)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 2, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.inputType = QComboBox(self.groupBox)
        self.inputType.setObjectName(u"inputType")

        self.horizontalLayout.addWidget(self.inputType)

        self.checkBoxPreInput = QCheckBox(self.groupBox)
        self.checkBoxPreInput.setObjectName(u"checkBoxPreInput")

        self.horizontalLayout.addWidget(self.checkBoxPreInput)

        self.lineEditPreInput = QLineEdit(self.groupBox)
        self.lineEditPreInput.setObjectName(u"lineEditPreInput")

        self.horizontalLayout.addWidget(self.lineEditPreInput)

        self.checkBoxDivInput = QCheckBox(self.groupBox)
        self.checkBoxDivInput.setObjectName(u"checkBoxDivInput")

        self.horizontalLayout.addWidget(self.checkBoxDivInput)

        self.lineEditDivInput = QLineEdit(self.groupBox)
        self.lineEditDivInput.setObjectName(u"lineEditDivInput")

        self.horizontalLayout.addWidget(self.lineEditDivInput)

        self.pushButtonStart = QPushButton(self.groupBox)
        self.pushButtonStart.setObjectName(u"pushButtonStart")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButtonStart.sizePolicy().hasHeightForWidth())
        self.pushButtonStart.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButtonStart.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButtonStart)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.inputText = QTextEdit(self.groupBox)
        self.inputText.setObjectName(u"inputText")
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(12)
        self.inputText.setFont(font2)
        self.inputText.setAcceptRichText(False)

        self.verticalLayout_2.addWidget(self.inputText)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setKerning(True)
        self.groupBox_2.setFont(font3)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 2, 5, 5)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.outputType = QComboBox(self.groupBox_2)
        self.outputType.setObjectName(u"outputType")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.outputType.sizePolicy().hasHeightForWidth())
        self.outputType.setSizePolicy(sizePolicy2)
        self.outputType.setSizeIncrement(QSize(0, 0))
        self.outputType.setFont(font3)

        self.horizontalLayout_2.addWidget(self.outputType)

        self.checkBoxPreOutput = QCheckBox(self.groupBox_2)
        self.checkBoxPreOutput.setObjectName(u"checkBoxPreOutput")
        self.checkBoxPreOutput.setFont(font3)

        self.horizontalLayout_2.addWidget(self.checkBoxPreOutput)

        self.lineEditPreOutput = QLineEdit(self.groupBox_2)
        self.lineEditPreOutput.setObjectName(u"lineEditPreOutput")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEditPreOutput.sizePolicy().hasHeightForWidth())
        self.lineEditPreOutput.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamilies([u"Consolas"])
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setKerning(True)
        self.lineEditPreOutput.setFont(font4)

        self.horizontalLayout_2.addWidget(self.lineEditPreOutput)

        self.checkBoxDivOutput = QCheckBox(self.groupBox_2)
        self.checkBoxDivOutput.setObjectName(u"checkBoxDivOutput")
        self.checkBoxDivOutput.setFont(font3)

        self.horizontalLayout_2.addWidget(self.checkBoxDivOutput)

        self.lineEditDivOutput = QLineEdit(self.groupBox_2)
        self.lineEditDivOutput.setObjectName(u"lineEditDivOutput")

        self.horizontalLayout_2.addWidget(self.lineEditDivOutput)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.outputText = QTextEdit(self.groupBox_2)
        self.outputText.setObjectName(u"outputText")
        self.outputText.setFont(font4)
        self.outputText.setAcceptRichText(False)

        self.verticalLayout_3.addWidget(self.outputText)


        self.verticalLayout.addWidget(self.groupBox_2)

        Codec.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar(Codec)
        self.statusBar.setObjectName(u"statusBar")
        Codec.setStatusBar(self.statusBar)

        self.retranslateUi(Codec)

        QMetaObject.connectSlotsByName(Codec)
    # setupUi

    def retranslateUi(self, Codec):
        Codec.setWindowTitle(QCoreApplication.translate("Codec", u"\u7f16\u7801\u8f6c\u6362", None))
        self.groupBox.setTitle("")
        self.checkBoxPreInput.setText(QCoreApplication.translate("Codec", u"\u524d\u7f00\u7b26", None))
        self.checkBoxDivInput.setText(QCoreApplication.translate("Codec", u"\u5206\u9694\u7b26", None))
        self.pushButtonStart.setText(QCoreApplication.translate("Codec", u"\u8f6c\u6362", None))
        self.groupBox_2.setTitle("")
        self.checkBoxPreOutput.setText(QCoreApplication.translate("Codec", u"\u524d\u7f00\u7b26", None))
        self.checkBoxDivOutput.setText(QCoreApplication.translate("Codec", u"\u5206\u9694\u7b26", None))
    # retranslateUi

