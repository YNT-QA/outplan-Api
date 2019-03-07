# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/3/6 14:22
# 文件: test_addscenetemp_cms.py

import unittest
from data.userinfo import *
from src.modules.scenemange_cms import SceneMangeCms
from src.modules.login_cms import LoginCms
from time import sleep
from src.common.mysql import Mysql

class TestAddSceneTemp(unittest.TestCase):
    user = None
    token = None
    scenetemp=None
    s_id=None

    def setUp(self):
        #登录外呼后台
        global token,user
        user = LoginCms(pro_add_cms)
        res = user.login_cms(acc_cms,pawd_cms)
        self.assertEqual(res['data']['realName'],'顾荣荣')
        self.assertEqual(res['data']['userId'],32)
        token = res['data']['token']

    def test_addsceneTemple(self):
        u'''创建示例场景库'''
        global scenetemp,s_id
        scenetemp=SceneMangeCms(pro_add_cms)
        res=scenetemp.create_scenetemple(token,auto_name)
        #查询数据库获取id
        product_m = Mysql(myq_ip, myq_port, myq_user, myq_pswd, dbname)
        con = product_m.connect_mysql()
        flag = False
        for i in range(time_out):
            try:
                self.assertEqual(res['status'],code_1000)
                self.assertEqual(res['msg'],success)
                res2 = product_m.mysql_select(con[0],"SELECT id FROM ko_scene_main where scenename='%s' and state=0"%auto_name)
                for row in res2:
                    s_id = row[0]
                flag = True
                break
            except:
                sleep(1)

        self.assertTrue(flag)

    def tearDown(self):
        #删除示例场景库
        res=scenetemp.delete_scenetemp(token,s_id)
        flag = False
        for i in range(time_out):
            try:
                self.assertEqual(res['status'],code_1000)
                self.assertEqual(res['msg'],success)
                flag = True
                break
            except:
                sleep(1)
        self.assertTrue(flag)
        #退出
        logout = user.logout_cms(token)
        self.assertEqual(logout['status'], code_1000)
        self.assertEqual(logout['msg'], success)