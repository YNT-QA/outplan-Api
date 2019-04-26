# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/21 11:48
# 文件: queryscene.py
import requests
import json
from data.userinfo import *
import unittest

class QueryScene(unittest.TestCase):

    def __init__(self,address):
        unittest.TestCase.__init__(self)
        self.address=address
        self.get_queryscene_url = '/scene/queryScene.do'

    def get_queryscene(self,userId,token):
        headers = {'Content-Type': 'application/json','token':token}
        data={'userid':userId}

        res=requests.post(url=self.address+self.get_queryscene_url,headers=headers,data=json.dumps(data))
        self.assertTrue(res.status_code, code_200)
        return  json.loads(res.text)
