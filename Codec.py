# -*- coding: utf-8 -*-

"""
Module implementing Codec.
"""
import hashlib
import sys, re
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from Codec_ui import Ui_Codec
from common import Common

'''
待解决问题
1、中文字符串异或校验是双字节参与
2、中文字符串和校验是双字节参与
3、SHA256 添加前后缀支持
'''

class Codec(QMainWindow, Ui_Codec):
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

        self.InputInfo = QLabel()
        self.InputInfo.setAlignment(Qt.AlignCenter)
        self.InputInfo.setText('输入')
        self.InputInfo.setStyleSheet("font: 12pt '微软雅黑'")
        self.statusBar.addWidget(self.InputInfo, 1)
        self.OutputInfo = QLabel()
        self.OutputInfo.setAlignment(Qt.AlignHCenter)
        self.OutputInfo.setText('输出')
        self.OutputInfo.setStyleSheet("font: 12pt '微软雅黑'")
        self.statusBar.addWidget(self.OutputInfo, 1)
        self.SelectWord = 0
        self.SelectByte = 0
        self.SelectInfo = QLabel()
        self.SelectInfo.setAlignment(Qt.AlignHCenter)
        self.SelectInfo.setStyleSheet("font: 12pt '微软雅黑'")
        self.SelectInfo.setText('{} 词 / {} 字'.format(self.SelectWord, self.SelectByte))
        self.statusBar.addWidget(self.SelectInfo, 1)
        self.setWindowIcon(QIcon(':/icon/resource/icon/codec256.ico'))
        self.inputType.addItems(['字符串', 'gb2312/gbk/gb18030','unicode', 'utf-8', 'utf-16', 'utf-32', '十六进制', '十进制', '二进制', 'big5'])
        self.inputType.setCurrentIndex(6)
        self.outputType.addItems(['字符串','gb2312/gbk/gb18030','unicode', 'utf-8', 'utf-16', 'utf-32', '十六进制', '十进制', '二进制', 'big5', '异或校验', '和校验', 'SHA256'])
    
    # 乱码处理
    def garbled(self):
        self.outputText.setText('')
        rawData=self.inputText.toPlainText()
        # 将unicode字符串转成字节流
        byteData=[]
        for x in rawData:
            value=ord(x)
            byteData.append(value//256)
            byteData.append(value%256)
        # 避开起始的残缺数据，取值范围0~4应该可以应对所有残缺可能
        byteData=bytes(byteData)[0:]
        # 将字节流转成unicode字符串
        rawData=''
        i=0
        while len(byteData)-i>=2:# 切片成功
            rawData+=chr(byteData[i]*256+byteData[i+1])
            i += 2
        # 转换格式：unicode>>utf8
        self.outputText.append('unicode>>utf8')
        outputData=byteData.decode('utf8', errors='ignore')
        self.outputText.append(outputData)
        # 转换格式：unicode>>gb18030
        self.outputText.append('unicode>>gb18030')
        outputData=byteData.decode('gb18030', errors='ignore')
        self.outputText.append(outputData)
        # 转换格式：utf8>>gb18030
        self.outputText.append('utf8>>gb18030')
        inputData=rawData.encode('utf8')
        outputData=inputData.decode('gb18030', errors='ignore')
        self.outputText.append(outputData)
        # 转换格式：gb18030>>utf8
        self.outputText.append('gb18030>>utf8')
        inputData=rawData.encode('gb18030')
        outputData=inputData.decode('utf8', errors='ignore')
        self.outputText.append(outputData)
        # 转换格式：unicode>>gb18030>>utf8>>gb18030
        self.outputText.append('unicode>>gb18030>>utf8>>gb18030')
        inputData=rawData.encode('gb18030')
        inputData=inputData.decode('utf8', errors='ignore')
        byteData=[]
        for x in inputData:
            value=ord(x)
            byteData.append(value//256)
            byteData.append(value%256)
        # 避开起始的残缺数据，取值范围0~4应该可以应对所有残缺可能
        byteData=bytes(byteData)
        outputData=byteData.decode('gb18030', errors='ignore')
        self.outputText.append(outputData)
        # 转换格式：unicode>>utf8>>gb18030>>utf8
        self.outputText.append('unicode>>utf8>>gb18030>>utf8')
        inputData=rawData.encode('utf8')
        inputData=inputData.decode('gb18030', errors='ignore')
        byteData=[]
        for x in inputData:
            value=ord(x)
            byteData.append(value//256)
            byteData.append(value%256)
        # 避开起始的残缺数据，取值范围0~4应该可以应对所有残缺可能
        byteData=bytes(byteData)
        outputData=byteData.decode('utf8', errors='ignore')
        self.outputText.append(outputData)

    def convert(self):
        if self.inputType.currentText()=='字符串':
            inputData=self.inputText.toPlainText()
            inputData = inputData.replace('\n', '\r\n')
            self.InputInfo.setText('输入: %d' % len(inputData))
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
        elif self.inputType.currentText()=='二进制':
            inputData=''
            charList=self.binExtract()
            for x in charList:
                inputData+=chr(x)
        elif self.inputType.currentText()=='unicode':
            # 将 unicode 转义格式的字节流解码为字符串
            inputData = self.unicodeExtract().decode('unicode_escape')
        elif self.inputType.currentText()=='utf-8':
            inputData=self.hexExtract().decode('utf8', errors='ignore')
        elif self.inputType.currentText()=='utf-16':
            inputData=self.hexExtract().decode('utf16', errors='ignore')
        elif self.inputType.currentText()=='utf-32':
            inputData=self.hexExtract().decode('utf32', errors='ignore')
        elif self.inputType.currentText()=='gb2312/gbk/gb18030':
            inputData=self.hexExtract().decode('gb18030', errors='ignore')
        elif self.inputType.currentText()=='big5':
            inputData=self.hexExtract().decode('big5', errors='ignore')
        self.setOutputDevice(inputData)
    
    # 十进制输入数据提取，返回字节流
    def decExtract(self): 
        inputRaw = self.inputText.toPlainText()
        if self.checkBoxPreInput.checkState() == Qt.Checked:            
            inputRaw = inputRaw.replace(self.lineEditPreInput.text(), '')
        if self.checkBoxDivInput.checkState() == Qt.Checked:
            inputRaw = inputRaw.replace(self.lineEditDivInput.text(), '')
        # 最大提取 20 位数
        pattern = re.compile(r'[0-9]{1,20}')
        print(pattern.findall(inputRaw))
        inputData = []
        for x in pattern.findall(inputRaw):
            valueStr = '{:X}'.format(int(x))
            if len(valueStr) % 2 == 1:
                valueStr = '0' + valueStr
            i = 0
            while valueStr and valueStr[i:i+2]:# 切片成功
                inputData.append(int(valueStr[i:i+2], 16))
                i += 2
        self.InputInfo.setText('输入: %d' % len(inputData))
        return bytes(inputData) # 返回字节流
    
    # 十六进制输入数据提取，返回字节流
    def hexExtract(self): 
        inputRaw = self.inputText.toPlainText()
        if self.checkBoxPreInput.checkState() == Qt.Checked:            
            inputRaw = inputRaw.replace(self.lineEditPreInput.text(), '')
        if self.checkBoxDivInput.checkState() == Qt.Checked:
            inputRaw = inputRaw.replace(self.lineEditDivInput.text(), '')
        pattern=r"[^0-9a-fA-F]+"
        inputData = []
        for x in re.split(pattern, inputRaw):
            i=0
            while x and x[i:i+2]:# 切片成功
                inputData.append(int(x[i:i+2], 16))
                i += 2
        self.InputInfo.setText('输入: %d' % len(inputData))
        return bytes(inputData) # 返回字节流
    
    # 二进制输入数据提取，返回字节流
    def binExtract(self): 
        char=self.inputText.toPlainText()
        char = re.sub('[^10]', '', char)
        inputData = []
        i = 0
        while char[i:i+8]:
            inputData.append(int(char[i:i+8], 2))
            i += 8
        self.InputInfo.setText('输入: %d' % len(inputData))
        return bytes(inputData) # 返回字节流

    # Unicode 输入数据提取
    def unicodeExtract(self):
        inputRaw = self.inputText.toPlainText()
        if re.search(r'[\\u|\\U|\s]', inputRaw):
            pattern = re.compile(r'[0-9a-fA-F]{1,6}')
        else:
            pattern = re.compile(r'[0-9a-fA-F]{4}')
        unicodeArray = pattern.findall(inputRaw)
        if len(unicodeArray) == 0:
            print('unicode data invalid!')
            return b''
        unicodeStrList = []
        for item in unicodeArray:
            value = int(item, 16)
            if value > 0x10FFFF:
                unicodeStrList.append('\\u{:0>4X}'.format(value>>8))
                unicodeStrList.append('\\u{:0>4X}'.format(value & 0xFF))
            elif value > 0xFFFF:
                unicodeStrList.append('\\U{:0>8X}'.format(value))
            else:
                unicodeStrList.append('\\u{:0>4X}'.format(value))
        # 将字符串编码为 Unicode 转义格式的字节流，如‘测试’转为 b'\\u6d4b\\u8bd5'
        unicodeEscape = ''.join(unicodeStrList).encode('latin-1')
        # print(unicodeEscape)
        self.InputInfo.setText('输入: %d' % len(unicodeStrList))
        return unicodeEscape

    # input为输入字符串
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
            self.OutputInfo.setText('输出: %d' % len(inputData))
            outputData=inputData
        elif self.outputType.currentText()=='unicode':
            charList=[]
            for x in inputData:
                value=ord(x)
                charList.append('%04X'%(value))
            self.OutputInfo.setText('输出: %d' % (len(charList)))
            outputData=div.join(pre+x for x in charList)
        elif self.outputType.currentText()=='十进制':
            charList=[]
            # 中文两个字节转十进制为整体，不考虑对齐
            for x in inputData:
                charList.append('%d'% ord(x))
            self.OutputInfo.setText('输出: %d' % len(charList))
            outputData=div.join(pre+x for x in charList)
        elif self.outputType.currentText()=='十六进制':
            charList=[]
            for x in inputData:
                # 中文为两个字节
                if ord(x) > 0xff:
                    temp = (ord(x)>>8)&0xff
                    charList.append('%02X'% temp)
                temp = ord(x) & 0xff
                charList.append('%02X'% temp)
            self.OutputInfo.setText('输出: %d' % len(charList))
            outputData=div.join(pre+x for x in charList)
        elif self.outputType.currentText()=='二进制':
            charList=[]
            for x in inputData:
                # unicode 两个字节
                for i in [0,1]:
                    if i==0:
                        if ord(x) > 0xff:
                            temp = (ord(x)>>8)&0xff
                        else:
                            continue
                    else:
                        temp = ord(x) & 0xff
                    value = 0
                    for j in range(8):
                        # 转换成 32 位
                        value = value<<4
                        value |= (temp>>(7-j))&0x01
                    charList.append('%08X'% value)
            self.OutputInfo.setText('输出: %d' % len(charList))
            outputData=' '.join(x for x in charList)
        elif self.outputType.currentText()=='utf-8':
            inputData=inputData.encode('utf8')
            self.OutputInfo.setText('输出: %d' % len(inputData))
            outputData=div.join(pre+"%02X" % x for x in inputData)
        elif self.outputType.currentText()=='utf-16':
            inputData=inputData.encode('utf16')
            self.OutputInfo.setText('输出: %d' % len(inputData))
            outputData=div.join(pre+"%02X" % x for x in inputData)
        elif self.outputType.currentText()=='utf-32':
            inputData=inputData.encode('utf32')
            self.OutputInfo.setText('输出: %d' % len(inputData))
            outputData=div.join(pre+"%02X" % x for x in inputData)
        elif self.outputType.currentText()=='gb2312/gbk/gb18030':
            inputData=inputData.encode('gb18030')
            self.OutputInfo.setText('输出: %d' % len(inputData))
            outputData=div.join(pre+"%02X" % x for x in inputData)
        elif self.outputType.currentText()=='big5':
            # 有不识别的数据替换为'?'
            inputData=inputData.encode('big5', errors='replace')
            self.OutputInfo.setText('输出: %d' % len(inputData))
            outputData=div.join(pre+"%02X" % x for x in inputData)
        elif self.outputType.currentText()=='异或校验':
            xor = 0
            charList=[]
            for x in inputData:
                if ord(x) > 0xff:
                    temp = (ord(x)>>8)&0xff
                    xor = xor ^ temp
                    charList.append('%02X'% temp)
                temp = ord(x) & 0xff
                xor = xor ^ temp
                charList.append('%02X'% temp)
            charList.append('%02X'% xor)
            self.OutputInfo.setText('输出: %d' % len(charList))
            outputData=div.join(pre+x for x in charList)
        elif self.outputType.currentText()=='和校验':
            checksum = 0
            charList=[]
            for x in inputData:
                if ord(x) > 0xff:
                    temp = (ord(x)>>8)&0xff
                    checksum = checksum + temp
                    charList.append('%02X'% temp)
                temp = ord(x) & 0xff
                checksum = checksum + temp
                charList.append('%02X'% temp)
            checksum = checksum&0xFF
            charList.append('%02X'% checksum)
            self.OutputInfo.setText('输出: %d' % len(charList))
            outputData=div.join(pre+x for x in charList)
        elif self.outputType.currentText()=='SHA256':
            outputData = hashlib.sha256(inputData.encode('utf-8')).hexdigest()
            outputData = outputData.upper()
            self.OutputInfo.setText('输出: %d' % len(outputData))
        self.outputText.setText(outputData)
    
    @Slot()
    def on_pushButtonStart_clicked(self):
        """
        Slot documentation goes here.
        """
        if True:
            self.convert()
        else:
            # 乱码处理
            self.garbled()

    @Slot()
    def on_inputText_selectionChanged(self):
        """
        Slot documentation goes here.
        """
        text = self.inputText.textCursor().selectedText()
        self.SelectByte, self.SelectWord = Common.word_count(text)
        self.SelectInfo.setText('{} 词 / {} 字'.format(self.SelectWord, self.SelectByte))

    @Slot()
    def on_outputText_selectionChanged(self):
        """
        Slot documentation goes here.
        """
        text = self.outputText.textCursor().selectedText()
        self.SelectByte, self.SelectWord = Common.word_count(text)
        self.SelectInfo.setText('{} 词 / {} 字'.format(self.SelectWord, self.SelectByte))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("windowsvista")
    app.setWindowIcon(QIcon(':/icon/resource/icon/codec256.ico'))
    codec = Codec()
    codec.show()
    sys.exit(app.exec())
