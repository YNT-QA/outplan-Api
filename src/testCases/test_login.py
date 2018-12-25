# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/18 11:25
# 文件: test_login.py
import sys
sys.path.append('..')
from modules.login import Login
import unittest
from common.get_value import GetValue

class TestLogin(unittest.TestCase):
     lg=None
     data=None
     token=None
     def setUp(self):
         global lg,data,path

         data = GetValue()

         lg = Login(data.getvalue('product_address'))

     def test_login(self):
         global lg,data,token
         res = lg.login(data.getvalue('account'),data.getvalue('product_password'))
         token=res['data']['token']
         self.assertEqual(res['data']['userName'],data.getvalue('account'))
         self.assertEqual(res['data']['accountType'], 1)


     def tearDown(self):
         logout = lg.logout(token)
         self.assertEqual(logout['status'], 1000)
         self.assertEqual(logout['msg'], '操作成功')






