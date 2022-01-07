# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\workbench\PyQt\GSP\Codec.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Codec(object):
   def setupUi(self, Codec):
      Codec.setObjectName("Codec")
      Codec.resize(900, 600)
      self.verticalLayout = QtWidgets.QVBoxLayout(Codec)
      self.verticalLayout.setContentsMargins(5, 5, 5, 5)
      self.verticalLayout.setSpacing(3)
      self.verticalLayout.setObjectName("verticalLayout")
      self.groupBox = QtWidgets.QGroupBox(Codec)
      font = QtGui.QFont()
      font.setFamily("微软雅黑")
      font.setPointSize(11)
      self.groupBox.setFont(font)
      self.groupBox.setObjectName("groupBox")
      self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
      self.verticalLayout_2.setContentsMargins(5, 2, 5, 5)
      self.verticalLayout_2.setSpacing(5)
      self.verticalLayout_2.setObjectName("verticalLayout_2")
      self.horizontalLayout = QtWidgets.QHBoxLayout()
      self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
      self.horizontalLayout.setObjectName("horizontalLayout")
      self.inputType = QtWidgets.QComboBox(self.groupBox)
      self.inputType.setObjectName("inputType")
      self.horizontalLayout.addWidget(self.inputType)
      self.checkBoxPreInput = QtWidgets.QCheckBox(self.groupBox)
      self.checkBoxPreInput.setObjectName("checkBoxPreInput")
      self.horizontalLayout.addWidget(self.checkBoxPreInput)
      self.lineEditPreInput = QtWidgets.QLineEdit(self.groupBox)
      self.lineEditPreInput.setObjectName("lineEditPreInput")
      self.horizontalLayout.addWidget(self.lineEditPreInput)
      self.checkBoxDivInput = QtWidgets.QCheckBox(self.groupBox)
      self.checkBoxDivInput.setObjectName("checkBoxDivInput")
      self.horizontalLayout.addWidget(self.checkBoxDivInput)
      self.lineEditDivInput = QtWidgets.QLineEdit(self.groupBox)
      self.lineEditDivInput.setObjectName("lineEditDivInput")
      self.horizontalLayout.addWidget(self.lineEditDivInput)
      self.pushButtonStart = QtWidgets.QPushButton(self.groupBox)
      sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
      sizePolicy.setHorizontalStretch(0)
      sizePolicy.setVerticalStretch(0)
      sizePolicy.setHeightForWidth(self.pushButtonStart.sizePolicy().hasHeightForWidth())
      self.pushButtonStart.setSizePolicy(sizePolicy)
      font = QtGui.QFont()
      font.setFamily("Arial")
      font.setPointSize(12)
      font.setBold(True)
      font.setWeight(75)
      self.pushButtonStart.setFont(font)
      self.pushButtonStart.setObjectName("pushButtonStart")
      self.horizontalLayout.addWidget(self.pushButtonStart)
      self.verticalLayout_2.addLayout(self.horizontalLayout)
      self.inputText = QtWidgets.QTextEdit(self.groupBox)
      font = QtGui.QFont()
      font.setFamily("Consolas")
      font.setPointSize(12)
      self.inputText.setFont(font)
      self.inputText.setAcceptRichText(False)
      self.inputText.setObjectName("inputText")
      self.verticalLayout_2.addWidget(self.inputText)
      self.verticalLayout.addWidget(self.groupBox)
      self.groupBox_2 = QtWidgets.QGroupBox(Codec)
      font = QtGui.QFont()
      font.setFamily("微软雅黑")
      font.setPointSize(11)
      font.setBold(False)
      font.setWeight(50)
      font.setKerning(True)
      self.groupBox_2.setFont(font)
      self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
      self.groupBox_2.setObjectName("groupBox_2")
      self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
      self.verticalLayout_3.setContentsMargins(5, 2, 5, 5)
      self.verticalLayout_3.setSpacing(5)
      self.verticalLayout_3.setObjectName("verticalLayout_3")
      self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
      self.horizontalLayout_2.setObjectName("horizontalLayout_2")
      self.outputType = QtWidgets.QComboBox(self.groupBox_2)
      sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
      sizePolicy.setHorizontalStretch(0)
      sizePolicy.setVerticalStretch(0)
      sizePolicy.setHeightForWidth(self.outputType.sizePolicy().hasHeightForWidth())
      self.outputType.setSizePolicy(sizePolicy)
      self.outputType.setSizeIncrement(QtCore.QSize(0, 0))
      font = QtGui.QFont()
      font.setFamily("Arial")
      font.setPointSize(12)
      font.setBold(False)
      font.setWeight(50)
      font.setKerning(True)
      self.outputType.setFont(font)
      self.outputType.setObjectName("outputType")
      self.horizontalLayout_2.addWidget(self.outputType)
      self.checkBoxPreOutput = QtWidgets.QCheckBox(self.groupBox_2)
      font = QtGui.QFont()
      font.setFamily("微软雅黑")
      font.setPointSize(11)
      font.setBold(False)
      font.setWeight(50)
      font.setKerning(True)
      self.checkBoxPreOutput.setFont(font)
      self.checkBoxPreOutput.setObjectName("checkBoxPreOutput")
      self.horizontalLayout_2.addWidget(self.checkBoxPreOutput)
      self.lineEditPreOutput = QtWidgets.QLineEdit(self.groupBox_2)
      sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
      sizePolicy.setHorizontalStretch(0)
      sizePolicy.setVerticalStretch(0)
      sizePolicy.setHeightForWidth(self.lineEditPreOutput.sizePolicy().hasHeightForWidth())
      self.lineEditPreOutput.setSizePolicy(sizePolicy)
      font = QtGui.QFont()
      font.setFamily("Consolas")
      font.setPointSize(12)
      font.setBold(False)
      font.setWeight(50)
      font.setKerning(True)
      self.lineEditPreOutput.setFont(font)
      self.lineEditPreOutput.setObjectName("lineEditPreOutput")
      self.horizontalLayout_2.addWidget(self.lineEditPreOutput)
      self.checkBoxDivOutput = QtWidgets.QCheckBox(self.groupBox_2)
      font = QtGui.QFont()
      font.setFamily("微软雅黑")
      font.setPointSize(11)
      font.setBold(False)
      font.setWeight(50)
      font.setKerning(True)
      self.checkBoxDivOutput.setFont(font)
      self.checkBoxDivOutput.setObjectName("checkBoxDivOutput")
      self.horizontalLayout_2.addWidget(self.checkBoxDivOutput)
      self.lineEditDivOutput = QtWidgets.QLineEdit(self.groupBox_2)
      self.lineEditDivOutput.setObjectName("lineEditDivOutput")
      self.horizontalLayout_2.addWidget(self.lineEditDivOutput)
      self.verticalLayout_3.addLayout(self.horizontalLayout_2)
      self.outputText = QtWidgets.QTextEdit(self.groupBox_2)
      font = QtGui.QFont()
      font.setFamily("Consolas")
      font.setPointSize(12)
      font.setBold(False)
      font.setWeight(50)
      font.setKerning(True)
      self.outputText.setFont(font)
      self.outputText.setAcceptRichText(False)
      self.outputText.setObjectName("outputText")
      self.verticalLayout_3.addWidget(self.outputText)
      self.verticalLayout.addWidget(self.groupBox_2)

      self.retranslateUi(Codec)
      QtCore.QMetaObject.connectSlotsByName(Codec)

   def retranslateUi(self, Codec):
      _translate = QtCore.QCoreApplication.translate
      Codec.setWindowTitle(_translate("Codec", "编码转换"))
      self.groupBox.setTitle(_translate("Codec", "输入"))
      self.checkBoxPreInput.setText(_translate("Codec", "前缀符"))
      self.checkBoxDivInput.setText(_translate("Codec", "分隔符"))
      self.pushButtonStart.setText(_translate("Codec", "转换"))
      self.groupBox_2.setTitle(_translate("Codec", "输出"))
      self.checkBoxPreOutput.setText(_translate("Codec", "前缀符"))
      self.checkBoxDivOutput.setText(_translate("Codec", "分隔符"))


if __name__ == "__main__":
   import sys
   app = QtWidgets.QApplication(sys.argv)
   Codec = QtWidgets.QWidget()
   ui = Ui_Codec()
   ui.setupUi(Codec)
   Codec.show()
   sys.exit(app.exec_())
