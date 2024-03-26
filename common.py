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
        # 字数不统计行分隔符 '\u2028'，段分隔符 '\u2029'
        text = re.sub(r'[\u2028\u2029]+', '', pstr)
        byte_len = len(text)
        # 去除首尾空格
        text = pstr.strip(' ')
        if len(text):
            text = re.sub(r'[ \u2028\u2029]+', ' ', text)
            textList =  re.split(r" ", text)
            word_len = len(textList)
        else:
            word_len = 0
        return byte_len, word_len
