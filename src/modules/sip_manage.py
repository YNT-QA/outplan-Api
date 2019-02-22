# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/12/14 16:50
# 文件: sip_manage.py
import requests
import json

class sipManage():
    def __init__(self,address):
        self.address = address
        self.addsip_url='/sipmanager/sips.do'
        self.putsip_url='/sipmanager/sips/put.do'
        self.deletesip_url='/sipmanager/sips/deleteSipForUser.do'

    #添加sip线路
    def add_sip(self,token,username,password,ip,port,privately,lineType,groupSize):
        headers = {'Content-Type': 'application/json', 'token': token}
        data = {"username":username,
                "password": password,
                "ip": ip,"port": port,
                "locationArray": ["动态显示"],
                "status": 0,
                "privately": privately,
                "lineType": lineType,
                "groupSize": groupSize,
                "location": "动态显示,undefined",
                "industryType": [22]}
        res = requests.post(self.address + self.addsip_url, headers=headers, data=json.dumps(data))
        return json.loads(res.text)

    #修改SIP
    def update_sip(self,token,group_number,sip_id,username,password,ip,port,privately,lineType,groupSize):
        headers = {'Content-Type': 'application/json', 'token': token}
        data = {"username": username,
                "password": password,
                "ip": ip,"port": port,
                "locationArray": ["动态显示","undefined"],
                "status": 4,
                "privately": privately,
                "lineType": lineType,
	            "groupSize": groupSize,
                "industryTypeName": "在线教育",
                "bindId": privately,
                "bindName": "648186030@qq.com",
                "industryType": [22],
                "id": sip_id,
                "bindUserName": "推车狂魔渣渣辉",
                "bindUserAccountType": 1,
	            "linePrice": 0,
                "groupNumber": group_number,
                "userIndustryType": "20,22,35,29,36,30,37,38,25,26,34",
                "bindPlanNum": 0,
                "location": "动态显示,undefined"}
        res = requests.post(self.address + self.putsip_url, headers=headers, data=json.dumps(data))
        return json.loads(res.text)

    #删除sip线路
    def delete_sip(self,token,sip_id,lineType=1):
        headers = {'Content-Type': 'application/json', 'token': token}
        data = {"id":sip_id,"lineType":lineType}
        res = requests.post(self.address + self.deletesip_url, headers=headers, data=json.dumps(data))
        return json.loads(res.text)