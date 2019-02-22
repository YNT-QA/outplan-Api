# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/2/22 14:46
# 文件: login_cms.py
import requests
import json

class LoginCms():

    def __init__(self,address):
        self.address=address
        self.logout_url_cms ='/permission/logout'
        self.login_url_cms='/permission/login'

    #外呼后台登录
    def login_cms(self,acc_cms,pswd_cms):
        headers = {'Content-Type': 'application/json'}
        data={'userName':acc_cms,'password':pswd_cms}
        res=requests.post(self.address+self.login_url_cms,headers=headers,data=json.dumps(data))
        return  json.loads(res.text)

    #外呼后台登出
    def logout_cms(self,token):
        headers = {'Content-Type':'application/json','token':token}
        res=requests.get(self.address+self.logout_url_cms,headers=headers)
        return  json.loads(res.text)