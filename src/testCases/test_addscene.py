# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/1/4 9:24
# 文件: test_addscene.py
import sys
sys.path.append('..')
import unittest
from common.get_value import GetValue
from modules.login import Login
from modules.scene_manage import SceneManage
import time

class TestAddScene(unittest.TestCase):
    lg = None
    data = None
    token = None
    scene = None
    sceneId=None

    def setUp(self):
        global lg,data,token
        data = GetValue()
        # 登录
        lg = Login(data.getvalue('product_address'))
        res = lg.login(data.getvalue('account'), data.getvalue('product_password'))
        token = res['data']['token']
        self.assertEqual(res['data']['userName'], data.getvalue('account'))
        self.assertEqual(res['data']['accountType'], 1)

    def test_addScene(self):
        global scene,sceneId
        #添加场景库
        scene=SceneManage(data.getvalue('product_address'))
        res=scene.add_scene(token,20,data.getvalue('sceneName'),'',data.getvalue('userid'))
        self.assertEqual(res['status'], 1000)
        self.assertEqual(res['msg'], '操作成功')
        time.sleep(5)

        #获取sceneid
        res2=scene.search_scene(token,data.getvalue('sceneName'),data.getvalue('userid'))
        sceneId=res2['data']['list'][0]['id']
        print(sceneId)

    def tearDown(self):
        #删除场景库
        res=scene.delete_scene(token,sceneId,data.getvalue('userid'))
        self.assertEqual(res['status'], 1000)
        self.assertEqual(res['msg'], '操作成功')
        time.sleep(5)

        # 注销用户
        logout = lg.logout(token)
        self.assertEqual(logout['status'], 1000)
        self.assertEqual(logout['msg'], '操作成功')

