# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/18 11:25
# 文件: test_login.py
import sys
sys.path.append('..')
from modules.login import Login
import unittest
from data.userinfo import *

class TestLogin(unittest.TestCase):
     lg=None
     data=None
     token=None
     def setUp(self):
         global lg
         lg = Login(product_address)

     def test_login(self):
         '''登录'''
         global lg,token
         res = lg.login(account,product_password)
         self.assertEqual(res['data']['userName'],account)
         self.assertEqual(res['data']['accountType'], 1)
         token = res['data']['token']

     def tearDown(self):
         logout = lg.logout(token)
         self.assertEqual(logout['status'], 1000)
         self.assertEqual(logout['msg'], '操作成功')






