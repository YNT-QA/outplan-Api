# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/3/5 17:16
# 文件: scenemange_cms.py
import requests
import json

class SceneMangeCms():
    def __init__(self,address):
        self.address=address
        self.insert='/scene/v1.1/insert'
        self.delete='/scene/v1.1/delete'

    #创建示例场景
    def create_scenetemple(self,token,scenename,industrytype=20):
        headers = {'Content-Type': 'application/json', 'token': token}
        data ={"sceneName":scenename,"industryType":industrytype}
        res = requests.post(self.address + self.insert, headers=headers, data=json.dumps(data))
        return json.loads(res.text)

    #删除示例场景
    def delete_scenetemp(self,token,id):
        headers = {'Content-Type': 'application/json', 'token': token}
        data ={"id":id}
        res = requests.post(self.address + self.delete, headers=headers, data=json.dumps(data))
        return json.loads(res.text)