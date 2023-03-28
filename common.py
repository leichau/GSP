# -*- coding: utf-8 -*-

"""
Module implementing common.
"""
import re

class Common:
    """
    Class documentation goes here.
    """
    @staticmethod
    def word_count(pstr):
        # 去除首尾空格
        text = pstr.strip(' ')
        if len(text):
            text = re.sub(r'[ ]+', ' ', text)
            textList =  re.split(r" ", text)
            cnt = len(textList)
        else:
            cnt = 0
        return cnt
