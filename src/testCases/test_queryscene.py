# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/21 11:36
# 文件: test_queryscene.py
import sys
sys.path.append('..')
import unittest
from modules.login import Login
from modules.queryscene import QueryScene
from data.userinfo import *

class TestQueryScene(unittest.TestCase):
    lg = None
    qs=None
    token=None

    def setUp(self):
        global lg,token

        lg = Login(product_address)

        res = lg.login(account,product_password)
        token=res['data']['token']
        self.assertEqual(res['data']['userName'],account)
        self.assertEqual(res['data']['accountType'], 1)

    def test_queryScene(self):
        global qs

        qs=QueryScene(product_address)
        res=qs.get_queryscene(userid,token)

        self.assertEqual(res['success'],True)


    def tearDown(self):
        logout=lg.logout(token)
        self.assertEqual(logout['status'],1000)
        self.assertEqual(logout['msg'],'操作成功')