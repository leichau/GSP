# -*- coding: utf-8 -*-

"""
Module implementing AutoConnect.
"""

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QDialog

from Ui_AutoConnect import Ui_Dialog

import serial

class AutoConnect(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, port=None, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(AutoConnect, self).__init__(parent)
        self.setupUi(self)
        #去掉标题栏问号按钮
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        index = None
        port_list=list(serial.tools.list_ports.comports())
        portComList = []
        for port_list_0 in port_list:
            portNum = list(port_list_0)
            if port != None and port==portNum[0]:
                index = port_list.index(port_list_0)
            # self.comboBoxPort.addItem(portNum[0])
            portComList.append(portNum[0])
        if port:
            if port not in portComList:
                portComList.append(port)
        portComList.sort()
        if len(portComList):
            if port in portComList:
                index = portComList.index(port)
            else:
                index = 0
            for port in portComList:
                self.comboBoxPort.addItem(port)
            self.comboBoxPort.setCurrentIndex(index)
        self.port = None
    
    @pyqtSlot(int)
    def on_comboBoxPort_currentIndexChanged(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type int
        """
        #print('current index:', index)
    
    @pyqtSlot()
    def on_pushButtonCancel_clicked(self):
        """
        Slot documentation goes here.
        """
        self.reject()
    
    @pyqtSlot()
    def on_pushButtonOk_clicked(self):
        """
        Slot documentation goes here.
        """
        port = self.comboBoxPort.currentText().strip()
        if port == '':
            self.tip.setStyleSheet("color: red;font: 9pt 'Arial'")
            self.tip.setText('请选择有效端口')
        else:
            self.port = port
            self.accept()

    def getAutoConnectPort(parent=None):
        dialog = AutoConnect(parent)
        result = dialog.exec_()
        return (dialog.port, result == QDialog.Accepted)
