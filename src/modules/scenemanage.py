# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/3/8 17:06
# 文件: scenemanage.py
import requests
import json

class SceneMange():
    def __init__(self,address):
        self.address=address
        self.insert='/scene/manage/insert.do'
        self.deleteScene='/scene/manage/deleteScene.do'

    #创建测试场景
    def create_testscene(self,token,scenename,userId,industrytype=20,scenetemp=''):
        headers = {'Content-Type': 'application/json', 'token': token}
        data ={"sceneName":scenename,"industryType":industrytype,"userId":userId,"sceneTemplate":scenetemp}
        res = requests.post(self.address + self.insert, headers=headers, data=json.dumps(data))
        return json.loads(res.text)

    #删除测试场景
    def delete_scenetemp(self,token,sceneId,userId):
        headers = {'Content-Type': 'application/json', 'token': token}
        data ={"sceneId":sceneId,"userId":userId}
        res = requests.post(self.address + self.deleteScene, headers=headers, data=json.dumps(data))
        return json.loads(res.text)