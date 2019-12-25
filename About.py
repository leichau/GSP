
"""
Module implementing Codec.
"""

from PyQt5.QtWidgets import QDialog, QTextEdit

from Ui_About import Ui_About


class About(QDialog, Ui_About):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(About, self).__init__(parent)
        self.setupUi(self)
        #去掉标题栏问号按钮
        #self.setWindowFlags(Qt.WindowCloseButtonHint);
        #行文本不随窗口大小换行
        self.softInfo.setLineWrapMode(QTextEdit.NoWrap)
        self.softInfo.append('Copyright (c) 2017-2019 llc. All Rights Reserved.')
        self.softInfo.append('\n当前版本：0.0.004')
        self.softInfo.append('版本状态：试用版')
        self.softInfo.append('更新内容：')
        self.softInfo.append('编码器：修复十六进制只能提取单个数字的问题')
        self.softInfo.append('\n版本历史')
        self.softInfo.append('---------------------------------------------------')
        self.softInfo.append('0.0.003\t2019-12-23')
        self.softInfo.append('1、补充自动换行、显式发送、显示时间、自动重发功能\n'+
                                      '2、添加软件信息窗口')
        self.softInfo.append('\n0.0.002\t2019-09-20')
        self.softInfo.append('完成编码转换功能')
        self.softInfo.append('\n0.0.001\t2017')
        self.softInfo.append('完成串口基本收发功能')
