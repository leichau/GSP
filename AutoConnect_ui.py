# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AutoConnect.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(412, 240)
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.tip = QLabel(Dialog)
        self.tip.setObjectName(u"tip")
        font = QFont()
        font.setFamilies([u"Arial"])
        self.tip.setFont(font)

        self.verticalLayout.addWidget(self.tip)

        self.comboBoxPort = QComboBox(Dialog)
        self.comboBoxPort.setObjectName(u"comboBoxPort")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxPort.sizePolicy().hasHeightForWidth())
        self.comboBoxPort.setSizePolicy(sizePolicy)
        self.comboBoxPort.setFont(font)
        self.comboBoxPort.setEditable(True)
        self.comboBoxPort.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)

        self.verticalLayout.addWidget(self.comboBoxPort)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButtonCancel = QPushButton(Dialog)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        self.pushButtonCancel.setFont(font)

        self.horizontalLayout.addWidget(self.pushButtonCancel)

        self.pushButtonOk = QPushButton(Dialog)
        self.pushButtonOk.setObjectName(u"pushButtonOk")
        self.pushButtonOk.setFont(font)

        self.horizontalLayout.addWidget(self.pushButtonOk)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u81ea\u52a8\u8fde\u63a5", None))
        self.tip.setText(QCoreApplication.translate("Dialog", u"\u8bf7\u9009\u62e9\u8fde\u63a5\u7aef\u53e3", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
        self.pushButtonOk.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
    # retranslateUi

