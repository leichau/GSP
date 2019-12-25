# -*- coding: utf-8 -*-

"""
Module implementing Codec.
"""
import re
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget

from Ui_Codec import Ui_Codec


class Codec(QWidget, Ui_Codec):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Codec, self).__init__(parent)
        self.setupUi(self)
        self.inputType.addItems(['字符串', 'gb2312\\gbk\\gb18030','unicode', 'utf-8', 'utf-16', 'utf-32','十进制', '十六进制','big5'])
        self.outputType.addItems(['字符串','gb2312\\gbk\\gb18030','unicode', 'utf-8', 'utf-16', 'utf-32', '十进制', '十六进制', 'big5'])
    
    def convert(self):
        if self.inputType.currentText()=='字符串':
            inputData=self.inputText.toPlainText()
        elif self.inputType.currentText()=='unicode':
            inputData=''
            charList=self.hexExtract()
            i=0
            while len(charList)-i>=2:#切片成功
                inputData+=chr(charList[i]*256+charList[i+1])
                i += 2
        elif self.inputType.currentText()=='十进制':
            inputData=''
            charList=self.decExtract()
            for x in charList:
                inputData+=chr(x)
        elif self.inputType.currentText()=='十六进制':
            inputData=''
            charList=self.hexExtract()
            for x in charList:
                inputData+=chr(x)
        elif self.inputType.currentText()=='utf-8':
            inputData=self.hexExtract().decode('utf8', errors='ignore')
        elif self.inputType.currentText()=='utf-16':
            inputData=self.hexExtract().decode('utf16', errors='ignore')
        elif self.inputType.currentText()=='utf-16':
            inputData=self.hexExtract().decode('utf16', errors='ignore')
        elif self.inputType.currentText()=='utf-32':
            inputData=self.hexExtract().decode('utf32', errors='ignore')
        elif self.inputType.currentText()=='gb2312\\gbk\\gb18030':
            inputData=self.hexExtract().decode('gb18030', errors='ignore')
        elif self.inputType.currentText()=='big5':
            inputData=self.hexExtract().decode('big5', errors='ignore')
        self.setOutputDevice(inputData)
    
    #十进制输入数据提取，返回字节流
    def decExtract(self): 
        char=self.inputText.toPlainText()
        if self.checkBoxPreInput.checkState()==Qt.Checked:            
            char=char.replace(self.lineEditPreInput.text(), '')
        if self.checkBoxDivInput.checkState()==Qt.Checked:
            char=char.replace(self.lineEditDivInput.text(), '')
        pattern=r"\s*[^0-9]*"
        inputData = []
        for x in re.split(pattern, char):
            if len(x):
                if int(x)//256:
                    inputData.append(int(x)//256)
                inputData.append(int(x)%256)
        return bytes(inputData) #返回字节流
    
    #十六进制输入数据提取，返回字节流
    def hexExtract(self): 
        char=self.inputText.toPlainText()
        if self.checkBoxPreInput.checkState()==Qt.Checked:            
            char=char.replace(self.lineEditPreInput.text(), '')
        if self.checkBoxDivInput.checkState()==Qt.Checked:
            char=char.replace(self.lineEditDivInput.text(), '')
        #前一个'\\\\'：表示正则表达式里的一个斜杠，前两个表示转义斜杠，后两个表示要查找的斜杠
        #后一个'\\\\'放到字符串里后表现为两个字符串
        #pattern=re.sub('\\\\', r'\\', pattern)
        pattern=r"[^0-9a-fA-F]+"
        inputData = []
        for x in re.split(pattern, char):
            i=0
            while x and x[i:i+2]:#切片成功
                inputData.append(int(x[i:i+2], 16))
                i += 2
        return bytes(inputData) #返回字节流
    
    #input为输入字符串
    def setOutputDevice(self, inputData):
        if self.checkBoxDivOutput.checkState()==Qt.Checked:
            div=self.lineEditDivOutput.text()
        else:
            div=''
        if self.checkBoxPreOutput.checkState()==Qt.Checked:
            pre=self.lineEditPreOutput.text()
        else:
            pre=''  
        if self.outputType.currentText()=='字符串':
            outputData=inputData
        elif self.outputType.currentText()=='unicode':
            charList=[]
            for x in inputData:
                value=ord(x)
                charList.append('%02X%02X'%(value//256, value%256))
            outputData=div.join(pre+x for x in charList)
        elif self.outputType.currentText()=='十进制':
            charList=[]
            #中文两个字节转十进制为整体，不考虑对齐
            for x in inputData:
                charList.append('%d'% ord(x))
            outputData=div.join(pre+x for x in charList)
        elif self.outputType.currentText()=='十六进制':
            charList=[]
            for x in inputData:
                #中文为两个字节
                if ord(x) > 0xff:
                    temp = (ord(x)>>8)&0xff
                    charList.append('%02X'% temp)
                temp = ord(x) & 0xff
                charList.append('%02X'% temp)
            outputData=div.join(pre+x for x in charList)
        elif self.outputType.currentText()=='utf-8':
            inputData=inputData.encode('utf8')
            outputData=div.join(pre+"%02X" % x for x in inputData)
        elif self.outputType.currentText()=='utf-16':
            inputData=inputData.encode('utf16')
            outputData=div.join(pre+"%02X" % x for x in inputData)
        elif self.outputType.currentText()=='utf-32':
            inputData=inputData.encode('utf32')
            outputData=div.join(pre+"%02X" % x for x in inputData)
        elif self.outputType.currentText()=='gb2312\\gbk\\gb18030':
            inputData=inputData.encode('gb18030')
            outputData=div.join(pre+"%02X" % x for x in inputData)
        elif self.outputType.currentText()=='big5':
            #有不识别的数据替换为'?'
            inputData=inputData.encode('big5', errors='replace')
            outputData=div.join(pre+"%02X" % x for x in inputData)
        self.outputText.setText(outputData)
    
    @pyqtSlot()
    def on_pushButtonClear_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButtonStart_clicked(self):
        """
        Slot documentation goes here.
        """
        self.convert()
