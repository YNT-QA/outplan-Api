# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/3/8 17:06
# 文件: scenemanage.py
import requests
import json
from data.userinfo import *
import time
import unittest

class SceneMange(unittest.TestCase):
    def __init__(self,address):
        unittest.TestCase.__init__(self)
        self.address=address
        self.insert='/scene/manage/insert.do'
        self.deleteScene='/scene/manage/deleteScene.do'
        self.addQuestion='/knowledge/addQuestion.do'
        self.compositeSpeech='/audio/compositeSpeech.do'
        self.add='/scene/manage/question/add.do'
        self.conclusion='/scene/manage/add/conclusion.do'
        self.addSubprocess='/scene/process/addSubprocess.do'
        self.addAnswer='/scene/answer/addAnswer.do'
        self.addTag='/tag/global/addTag.do'

    #创建测试场景
    def create_testscene(self,token,scenename,industrytype=20,scenetemp=''):
        headers = {'Content-Type': 'application/json', 'token': token}
        data ={"sceneName":scenename,"industryType":industrytype,"sceneTemplate":scenetemp}
        res = requests.post(self.address + self.insert, headers=headers, data=json.dumps(data))
        self.assertTrue(res.status_code, code_200)
        return json.loads(res.text)

    #删除测试场景
    def delete_scenetemp(self,token,sceneId):
        headers = {'Content-Type': 'application/json', 'token': token}
        data ={"sceneId":sceneId}
        res = requests.post(self.address + self.deleteScene, headers=headers, data=json.dumps(data))
        self.assertTrue(res.status_code, code_200)
        return json.loads(res.text)

    #TTS
    def composite_Speech(self,token,compContent):
        headers = {'Content-Type': 'application/json', 'token': token}
        data={"compContent":compContent}
        res = requests.post(url=self.address +self.compositeSpeech,headers=headers,data=json.dumps(data))
        self.assertTrue(res.status_code, code_200)
        res=json.loads(res.text)
        audiofp = None
        for i in range(time_out):
            try:
                if res['status']==code_1000 and res['msg']==success:
                    audiofp = res['data']['audioFilePath']
                    break
            except:
                time.sleep(1)
        return audiofp

    #主流程添加问答
    def add_process(self,token):
        headers = {'Content-Type': 'application/json','token':token}
        data={
            "question": "贷款意向提问",
            "triggerCondition": 0,
            "sid": 5546,
            "audioId": "",
            "presetAnswers": [
                {
                    "answer": "匹配知识库",
                    "preType": 1
                },
                {
                    "answer": "其他任意回答",
                    "preType": 2
                }
            ],
            "globalPresetAnswers": [
                {
                    "answerId": 27431,
                    "preType": 3
                },
                {
                    "answerId": 27432,
                    "preType": 3
                }
            ],
            "supportInterrupt": 1,
            "status": 0,
            "noResponseIds": [],
            "notIdentifyIds": [],
            "id": None,
            "subProcessId": 0,
            "sceneDynamicAudioReq": [],
            "audioSpeech": {
                "compContent": "喂，您好，我这边呢是专业办理银行贷款的，请问您最近有没有资金上的需求呢？",
                "userId": 21,
                "sceneId": 5546,
                "type": "main",
                "audioFilePath": "/data1/outbound/product/temp_tts/2019/03/12/1552374062788_00689.wav",
                "inputWay": 1
            }
        }
        res = requests.post(self.address + self.add,headers=headers,data=json.dumps(data))
        self.assertTrue(res.status_code, code_200)
        return json.loads(res.text)

    #场景流程-》主流程-》添加结束语
    def add_conclusion(self,token):
        headers = {'Content-Type': 'application/json', 'token': token}
        data={
                "question": "wqwqr",
                "triggerCondition": 0,
                "sceneDynamicAudioReq": [],
                "audioSpeech": {
                    "compContent": "qwrqr",
                    "sceneId": "14442",
                    "type": "main",
                    "audioFilePath": "/data1/outbound/qa/temp_tts/2019/03/27/1553691242455_30027.wav",
                    "inputWay": 1
                },
                "sid": "14442",
                "audioId": "",
                "audioPath": "/data1/outbound/qa/temp_tts/2019/03/27/1553691242455_30027.wav",
                "stdQuestion": "qwrqr",
                "subProcessId": 0
            }
        res = requests.post(self.address + self.conclusion,headers=headers,data=json.dumps(data))
        self.assertTrue(res.status_code, code_200)
        return json.loads(res.text)

    #场景流程-》子流程-》添加子流程
    def add_Subprocess(self,token):
        headers = {'Content-Type': 'application/json', 'token': token}
        data={"processName": "safaf","sceneId":"14442"}
        res = requests.post(self.address + self.addSubprocess, headers=headers, data=json.dumps(data))
        self.assertTrue(res.status_code, code_200)
        return json.loads(res.text)

    #场景问答-》添加单轮回答/1相似回答2相识回答反义词3.全匹配相似回答
    def add_Answer(self,token):
        headers = {'Content-Type': 'application/json', 'token': token}
        data={
                "sceneId": 5549,
                "qType": 0,
                "id": 0,
                "answerName": "肯定",
                "standardAnswer": "是的",
                "sceneClass": [None],
                "context": [
                    {
                        "content": "哎没错",
                        "createTime": "2019-03-12  17:27:00",
                        "type": 1,
                        "id": 0
                    },
                    {
                        "content": "对啊",
                        "createTime": "2019-03-12  17:27:00",
                        "type": 1,
                        "id": 1
                    }
                ],
                "exeAction": "",
                "exeActionId": "",
                "exeActionDesc": ""
            }
        res = requests.post(self.address + self.addAnswer, headers=headers, data=json.dumps(data))
        self.assertTrue(res.status_code, code_200)
        return json.loads(res.text)

    #知识库-》添加知识库question:2,子流程
    def add_Question(self,token,knowledgeid,question,audioPath,similarList,userFocus='1',exeAction='1',compContent='',sceneId=None):
        headers = {'Content-Type':'application/json','token':token}
        data={
                "knowledgeId": knowledgeid,
                "answer": "",
                "question": question,
                "audioId": "",
                "similar": similarList,
                "keywordRules": [],
                "userFocus": userFocus,
                "exeAction": exeAction
            }
        if question=='1':
            data['audioSpeech']={
                    "compContent": compContent,
                    "sceneId": sceneId,
                    "type": "knowledge",
                    "audioFilePath": audioPath,
                    "inputWay": 1}

            data['sceneDynamicAudio']=[]
        elif question=='2':
            data['exeActionId']=2305

        res = requests.post(self.address+self.addQuestion, headers=headers, data=json.dumps(data))
        self.assertTrue(res.status_code,code_200)
        return json.loads(res.text)

    #用户标签-》全局标签
    def add_Tag(self,token,sceneid,tagname,keywordList):
        headers = {'Content-Type': 'application/json','token':token}
        data={
                "sceneId": sceneid,
                "tagName": tagname,
                "tagValue": "",
                "keywordList":keywordList,
                "skipQuestionList": []
            }
        res = requests.post(self.address+self.addTag,headers=headers,data=json.dumps(data))
        self.assertTrue(res.status_code, code_200)
        return json.loads(res.text)
