# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/2/28 15:08
# 文件: accmanage_cms.py
import requests
import json
from data.userinfo import *
import unittest

class AccManage(unittest.TestCase):
    def __init__(self,address):
        unittest.TestCase.__init__(self)
        self.address=address
        self.adduser_url_cms='/custManager/formal'
        self.informal='/custManager/informal'
        self.cdc_url_cms='/custManager/checkDeleteCondition'
        self.isak_url_cms='/custManager/isStopAndKill'
        self.updateFormalInfo='/custManager/updateFormalInfo'

    '''
    金融类：20,21,39
    教育类：22,23
    旅游类：24,25
    运营商类：26,27,28
    房地产类：29,30
    产品营销类：31,32,33
    其他类：34,35,36,37,38
    '''
    #添加账号
    def add_user(self,token,email,password,phone,companyname,agentnum=1,agentexpiredate=None,accountstatus=1,accounttype=1,plantype='1',isOpen=1):
        headers = {'Content-Type': 'application/json','token':token}
        data ={
                "user": {
                    "accountType": accounttype,
                    "email": email,
                    "password": password,
                    "phone": phone,
                    "companyName": companyname,
                    "accountStatus": accountstatus
                },
                "info": {
                    "planType": plantype,
                    "industryType": "20,21,39,34,35,36,37,38",
                    "sceneTemplate": "1638",
                    "sipType": "0,1"
                }
             }

        if accounttype==2:      #内部测试
            data['user']['effectual']='-1'
            data['user']['agentNum'] = agentnum
            data['user']['agentExpireDate'] = agentexpiredate
            addu_url = self.informal
        elif accounttype==4:    #试用账号
            data['user']['effectual'] = '3day'
            data['user']['followUp'] = 'autotest'
            addu_url = self.informal
        elif accounttype==3:    #外部测试
            data['user']['agentNum']=agentnum
            data['user']['agentExpireDate']=agentexpiredate
            data['user']['isOpen'] = isOpen
            addu_url=self.informal
        else:                   #正式
            data['user']['isOpen'] = isOpen
            addu_url=self.adduser_url_cms

        res = requests.post(self.address + addu_url,headers=headers,data=json.dumps(data))
        self.assertTrue(res.status_code, code_200)
        return json.loads(res.text)

    #删除账号
    def delete_account(self,token,uids):
        headers = {'Content-Type': 'application/json','token':token}
        data ={"uids":[uids]}

        def get_request(url):
            res = requests.post(self.address + url,headers=headers,data=json.dumps(data))
            self.assertTrue(res.status_code, code_200)
            return json.loads(res.text)

        return get_request

    #修改账号
    def modify_account(self,token,userid,industrytypes,scenecount=10,isOpen=1):
        headers = {'Content-Type': 'application/json', 'token': token}
        data = {
            "userId": userid,
            "industryTypes": industrytypes,
            "companyName": "杰诺斯",
            "sceneTemplates": [1574,2775],
            "sceneCount": scenecount,
            "isOpen": isOpen
        }
        res = requests.post(self.address +self.updateFormalInfo, headers=headers,data=json.dumps(data))
        self.assertTrue(res.status_code, code_200)
        return json.loads(res.text)