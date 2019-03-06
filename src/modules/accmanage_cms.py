# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/2/28 15:08
# 文件: accmanage_cms.py
import requests
import json

class AccManage():
    def __init__(self,address):
        self.address=address
        self.adduser_url_cms='/custManager/formal'
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
    def add_user(self,token,email,password,phone,companyname,accountstatus=1,accounttype=1,plantype='1'):
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
        res = requests.post(self.address +self.adduser_url_cms,headers=headers,data=json.dumps(data))
        return json.loads(res.text)

    #删除账号
    def delete_account(self,token,uids):
        headers = {'Content-Type': 'application/json', 'token': token}
        data ={"uids":[uids]}
        res1 = requests.post(self.address+self.cdc_url_cms,headers=headers,data=json.dumps(data))
        r1=json.loads(res1.text)
        res2 = requests.post(self.address+self.isak_url_cms,headers=headers,data=json.dumps(data))
        r2=json.loads(res2.text)
        return [r1,r2]

    #修改账号
    def modify_account(self,token,userid,industrytypes,scenecount=10):
        headers = {'Content-Type': 'application/json', 'token': token}
        data = {
            "userId": userid,
            "industryTypes": industrytypes,
            "companyName": "杰诺斯",
            "sceneTemplates": [1574,2775],
            "sceneCount": scenecount
        }
        res = requests.post(self.address +self.updateFormalInfo, headers=headers,data=json.dumps(data))
        return json.loads(res.text)