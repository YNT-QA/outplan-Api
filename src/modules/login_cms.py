# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/2/22 14:46
# 文件: login_cms.py
import requests
import json
import hashlib
import rsa
import base64
from data.userinfo import *
import unittest

class LoginCms(unittest.TestCase):

    def __init__(self,address):
        unittest.TestCase.__init__(self)
        self.address=address
        self.logout_url_cms ='/permission/logout'
        self.login_url_cms='/permission/login'
        self.getPublicKey = '/permission/getPublicKey'

    # 获取公钥
    def get_PublicKey(self):
        res = requests.get(self.address + self.getPublicKey)
        self.assertTrue(res.status_code, code_200)
        return json.loads(res.text)

    #外呼后台登录
    def login_cms(self,acc_cms,pswd_cms):
        #md5加密
        md = hashlib.md5()
        md.update(pswd_cms.encode())
        #获取公钥
        pubkey = self.get_PublicKey()
        b_str = base64.b64decode(pubkey['data'])
        #转换成16进制
        hex_str = b_str.hex()
        #找到模数和指数的开头结束位置
        m_start = 29*2
        e_start = 159*2
        m_len = 128*2
        e_len = 3*2

        modulus = hex_str[m_start:m_start + m_len]
        exponent = hex_str[e_start:e_start + e_len]
        rsa_pubkey = rsa.PublicKey(int(modulus,16),int(exponent,16))
        #rsa加密
        pswd = rsa.encrypt(md.hexdigest().encode('utf-8'),rsa_pubkey)

        headers = {'Content-Type': 'application/json'}
        data={'userName':acc_cms,'password':str(base64.b64encode(pswd),'utf-8'),'publicKey':pubkey['data']}
        res=requests.post(self.address+self.login_url_cms,headers=headers,data=json.dumps(data))
        self.assertTrue(res.status_code, code_200)
        return  json.loads(res.text)

    #外呼后台登出
    def logout_cms(self,token):
        headers = {'Content-Type':'application/json','token':token}
        res=requests.get(self.address+self.logout_url_cms,headers=headers)
        self.assertTrue(res.status_code, code_200)
        return  json.loads(res.text)