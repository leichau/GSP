# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'option.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Option(object):
    def setupUi(self, Option):
        if not Option.objectName():
            Option.setObjectName(u"Option")
        Option.resize(639, 489)
        self.verticalLayout = QVBoxLayout(Option)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 5, -1, -1)
        self.tabWidget = QTabWidget(Option)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fontLine = QLineEdit(self.tab)
        self.fontLine.setObjectName(u"fontLine")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(11)
        self.fontLine.setFont(font1)
        self.fontLine.setReadOnly(True)

        self.horizontalLayout.addWidget(self.fontLine)

        self.fontButton = QPushButton(self.tab)
        self.fontButton.setObjectName(u"fontButton")
        self.fontButton.setFont(font)
        self.fontButton.setFocusPolicy(Qt.WheelFocus)

        self.horizontalLayout.addWidget(self.fontButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.softInfo = QTextBrowser(self.tab_2)
        self.softInfo.setObjectName(u"softInfo")
        self.softInfo.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_2.addWidget(self.softInfo)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Option)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Option)
    # setupUi

    def retranslateUi(self, Option):
        Option.setWindowTitle(QCoreApplication.translate("Option", u"\u9009\u9879", None))
        self.fontButton.setText(QCoreApplication.translate("Option", u"\u5b57\u4f53", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Option", u"\u663e\u793a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Option", u"\u5173\u4e8e", None))
    # retranslateUi

