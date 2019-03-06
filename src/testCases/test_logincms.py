# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/2/22 14:50
# 文件: test_logincms.py
from src.modules.login_cms import LoginCms
import unittest
from data.userinfo import *

class TestLoginCms(unittest.TestCase):
     user=None
     token=None
     def setUp(self):
         global user
         user = LoginCms(pro_add_cms)

     def test_login(self):
         '''登录'''
         global token
         res = user.login_cms(acc_cms,pawd_cms)
         self.assertEqual(res['data']['realName'],'顾荣荣')
         self.assertEqual(res['data']['userId'], 32)
         token = res['data']['token']

     def tearDown(self):
         logout = user.logout_cms(token)
         self.assertEqual(logout['status'], code_1000)
         self.assertEqual(logout['msg'],success)