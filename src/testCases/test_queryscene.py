# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/21 11:36
# 文件: test_queryscene.py
import sys
sys.path.append('..')
import unittest
from common.get_value import GetValue
from modules.login import Login
from modules.queryscene import QueryScene

class TestQueryScene(unittest.TestCase):
    lg = None
    data = None
    qs=None
    token=None
    def setUp(self):
        global lg,data,token

        data = GetValue()

        lg = Login(data.getvalue('uat_address'))

        res = lg.login(data.getvalue('account'), data.getvalue('uat_password'))
        token=res['data']['token']
        self.assertEqual(res['data']['userName'], data.getvalue('account'))
        self.assertEqual(res['data']['accountType'], 1)

    def test_queryScene(self):
        global qs,data

        qs=QueryScene(data.getvalue('uat_address'))
        res=qs.get_queryscene(data.getvalue('userid'),token)

        self.assertEqual(res['success'],True)


    def tearDown(self):
        logout=lg.logout(token)
        self.assertEqual(logout['status'],1000)
        self.assertEqual(logout['msg'],'操作成功')