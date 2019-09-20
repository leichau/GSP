# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\tech\PyQt5\GSP\About.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(400, 304)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        About.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(About)
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.softInfo = QtWidgets.QTextBrowser(About)
        self.softInfo.setObjectName("softInfo")
        self.verticalLayout.addWidget(self.softInfo)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "关于"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QDialog()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())

