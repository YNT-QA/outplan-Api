# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/29 17:29
# 文件: get_path.py
import os

class GetPath():
    def __init__(self,path):
        self.path = path


    def get_filePath(self):
        filePath = os.path.dirname(os.path.abspath('../..')) + '\\' + 'outPlan' + '\\' + self.path    #win/linux路径不同，需要修改
        return filePath