# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/12/26 16:24
# 文件: scene_manage.py
import requests
import json

class SceneManage():

    def __init__(self,address):
        self.address = address
        self.scene_url='/scene/manage/insert.do'
        self.getScene_url='/scene/manage/search.do'
        self.compositeSpeech_url='/audio/compositeSpeech.do'
        self.addAudio_url='/audio/addAudio.do'
        self.deleteScene_url='/scene/manage/deleteScene.do'

    #新建场景库
    def add_scene(self,token,industryType,sceneName,sceneTemplate,userId):
        headers = {'Content-Type': 'application/json', 'token': token}
        data = {'industryType':industryType,'sceneName':sceneName,'sceneTemplate':sceneTemplate,'userId':userId}
        res = requests.post(self.address + self.scene_url, headers=headers, data=json.dumps(data))
        print(res.text)
        return json.loads(res.text)

    #删除场景库
    def delete_scene(self,token,sceneId,userId):
        headers = {'Content-Type': 'application/json', 'token': token}
        data = {'sceneId':sceneId,'userId':userId}
        res = requests.post(self.address + self.deleteScene_url, headers=headers, data=json.dumps(data))
        return json.loads(res.text)

    #查询场景库
    def search_scene(self,token,sceneName,userId):
        headers = {'Content-Type': 'application/json', 'token': token}
        data = {'pageNum': 20,'pageSize':100,'sceneName': sceneName,'userId': userId}
        res = requests.post(self.address + self.getScene_url, headers=headers, data=json.dumps(data))
        return json.loads(res.text)

    #语音合成
    def speech_composite(self,token,sceneId,compContent):
        headers = {'Content-Type': 'application/json', 'token': token}
        data = {'pId': 21,'sceneId':sceneId,'compAudioInfo':{'compContent':compContent}}
        res = requests.post(self.address + self.compositeSpeech_url, headers=headers, data=json.dumps(data))
        return json.loads(res.text)

    #添加音频
    def add_audio(self,token,audioContext,audioPath,sceneId):
        headers = {'Content-Type': 'application/json', 'token': token}
        data = {'pId': 21, 'audioPath': audioPath, 'audioContext': audioContext,'audioSex':2,'inputWay':1,'sceneId':sceneId}
        res = requests.post(self.address + self.addAudio_url, headers=headers, data=json.dumps(data))
        return json.loads(res.text)
