# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/12/10 11:25
# 文件: outplan.py
from requests_toolbelt import MultipartEncoder
import requests
import json
from data.userinfo import *
import unittest

class OutPlan(unittest.TestCase):
    def __init__(self,address):
        unittest.TestCase.__init__(self)
        self.address=address
        self.addCallLog_url='/outTask/addCallLog.do'
        self.deleteOutTask_url='/outTask/deleteOutTask.do'
        self.getCallDetail_url='/callRecord/getCallDetail.do'
        self.againOutPlan_url='/outTask/createAgainOutPlan.do'

    #form-data,创建计划
    def creat_outplan(self,token,userId,sceneId,planName,sceneName,sip_id,groupId,callType='2',createType='2'):

        data=MultipartEncoder(fields={'userId':userId,
                                      'sceneId':sceneId,
                                      'callType':callType,
                                      'planName':planName,
                                      'sceneName':sceneName,
                                      'sipIds':str(sip_id),
                                      'createType':createType,'groupIds':str(groupId)})
        headers = {'Content-Type':data.content_type, 'token': token}

        res=requests.post(url=self.address+self.addCallLog_url,headers=headers,data=data)
        self.assertTrue(res.status_code, code_200)
        return json.loads(res.text)

    #删除外呼计划
    def delete_outplan(self,token,planId):
        headers = {'Content-Type': 'application/json', 'token': token}
        data={'planId':planId}
        res = requests.post(self.address + self.deleteOutTask_url, headers=headers, data=json.dumps(data))
        self.assertTrue(res.status_code, code_200)
        return json.loads(res.text)

    #获取呼叫明细列表
    def get_CallDetail(self,token,planId):
        headers = {'Content-Type': 'application/json', 'token': token}
        data = {'isPage': 1,'pageNum': 1,'pageSize': 10,'planId':planId,'callTime': -1,
                'status': [-1],'callDuration': [-1],'intentionName': [-1],'sort': 2}
        res = requests.post(self.address + self.getCallDetail_url, headers=headers, data=json.dumps(data))
        self.assertTrue(res.status_code, code_200)
        return json.loads(res.text)

    #创建二次外呼
    def create_AgainOutPlan(self,token,userId,sceneId,sceneName,sip_id,phoneId,planName2,callType=2,createType=1):
        headers = {'Content-Type': 'application/json', 'token': token}
        data = {'userId': userId,'sceneId': sceneId,'callType': callType,'planName': planName2,
                'sceneName':sceneName,'sipIds':str(sip_id),'createType': createType,'phoneIds': phoneId}
        res = requests.post(self.address + self.againOutPlan_url, headers=headers, data=json.dumps(data))
        self.assertTrue(res.status_code, code_200)
        return json.loads(res.text)

