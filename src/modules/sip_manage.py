# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/12/14 16:50
# 文件: sip_manage.py
import requests
import json
from data.userinfo import *
import unittest

class sipManage(unittest.TestCase):
    def __init__(self,address):
        unittest.TestCase.__init__(self)
        self.address = address
        self.addsip_url='/sipmanager/sips.do'
        self.addsipGroup='/sipmanager/sips/addSipGroup.do'
        self.putsip_url='/sipmanager/sips/put.do'
        self.updateSip='/sipmanager/sips/updateSip.do'
        self.deletesip_url='/sipmanager/sips/deleteSipForUser.do'

    #添加sip线路
    def add_sip(self,token,username,password,ip,port,comment,lineType,groupSize):
        headers = {'Content-Type': 'application/json', 'token': token}
        data = {"username":username,
                "password": password,
                "ip": ip,"port": port,
                "locationArray": ["动态显示"],
                "status": 0,
                "comment": comment,
                "lineType": lineType,
                "groupSize": groupSize,
                "location": "动态显示,undefined",
                "industryType": [22]}
        res = requests.post(self.address + self.addsipGroup, headers=headers, data=json.dumps(data))
        self.assertTrue(res.status_code, code_200)
        return json.loads(res.text)

    #修改SIP
    def update_sip(self,token,group_number,sip_id,username,comment,ip,port,privately,lineType,groupSize):
        headers = {'Content-Type': 'application/json', 'token': token}
        data = {"username": username,
                "ip": ip,"port": port,
                "locationArray": ["动态显示","undefined"],
                "status": 4,
                "lineType": lineType,
                "groupSize": groupSize,
                "comment": comment,
                "industryTypeName": "在线教育",
                "prefix": "",
                "bindUserCompanyName": "QA",
                "registerType": 0,
                "callType": None,
                "bindId": privately,
                "bindName": "648186030@qq.com",
                "industryType": [22],
                "id": sip_id,
                "privately": privately,
                "bindUserName": "QA",
                "bindUserAccountType": 1,
                "linePrice": 0,
                "groupNumber": group_number,
                "userIndustryType": "20,22,35,29,36,30,37,38,25,26,34",
                "bindPlanNum": 0,
                "caller": "",
                "location": "动态显示,undefined"}
        res = requests.post(self.address + self.updateSip, headers=headers, data=json.dumps(data))
        self.assertTrue(res.status_code, code_200)
        return json.loads(res.text)

    #删除sip线路
    def delete_sip(self,token,sip_id,lineType=1):
        headers = {'Content-Type': 'application/json', 'token': token}
        data = {"id":sip_id,"lineType":lineType}
        res = requests.post(self.address + self.deletesip_url, headers=headers, data=json.dumps(data))
        self.assertTrue(res.status_code, code_200)
        return json.loads(res.text)