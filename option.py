# -*- coding: utf-8 -*-

"""
Module implementing Option.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QTextEdit, QFontDialog
from PyQt5.QtGui import QIcon

from Ui_option import Ui_Option
import os.path, time

class Option(QWidget, Ui_Option):
    """
    Class documentation goes here.
    """
    def __init__(self, master=None, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(Option, self).__init__(parent)
        self.setupUi(self)

        self.setWindowIcon(QIcon(':/icon/resource/icon/setting48.png'))
        #行文本不随窗口大小换行
        self.softInfo.setLineWrapMode(QTextEdit.NoWrap)
        self.softInfo.append('Copyright (c) 2017-2022 llc. All Rights Reserved.')
        self.softInfo.append('\n当前版本：0.1.5')
        self.softInfo.append('创建时间: {}'.format(time.strftime('%Y-%m-%dT%H:%M:%S+0800', \
                                                  time.localtime(os.path.getmtime("GSP.exe")))))
        self.softInfo.append('版本状态：试用版')
        self.softInfo.append('更新内容：')
        self.softInfo.append('通用：添加静态版本信息')
        self.softInfo.append('串口：添加清屏')
        self.softInfo.append('串口：添加连接监测')
        self.softInfo.append('串口：解决接收上限清除时的崩溃问题')
        self.softInfo.append('编码器：添加异或校验')
        self.softInfo.append('编码器：添加和校验')
        self.softInfo.append('\n版本历史')
        self.softInfo.append('---------------------------------------------------')
        self.softInfo.append('0.1.4\t2020-03-20')
        self.softInfo.append('编码器：修复十六进制只能提取单个数字的问题')
        self.softInfo.append('\n0.1.3\t2019-12-23')
        self.softInfo.append('串口：补充自动换行、显式发送、显示时间、自动重发功能')
        self.softInfo.append('串口：添加软件信息窗口')
        self.softInfo.append('\n0.1.2\t2019-09-20')
        self.softInfo.append('编码器：完成编码转换功能')
        self.softInfo.append('\n0.1.1\t2017')
        self.softInfo.append('串口：完成串口基本收发功能')
        self.master = master
        font = self.master.textBrowser.font()
        self.fontLine.setText("%s, %d, %d"%(font.family(), font.pointSize(), font.weight()))


    @pyqtSlot()
    def on_fontButton_clicked(self):
        """
        Slot documentation goes here.
        """
        font, ok=QFontDialog.getFont(self.master.textBrowser.font())
        if ok:
            self.fontLine.setText("%s, %d, %d"%(font.family(), font.pointSize(), font.weight()))
            self.master.serial_recvFont(font)
