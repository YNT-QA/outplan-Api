# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/3/5 15:02
# 文件: test_modifyacc.py
import unittest
from src.modules.accmanage_cms import AccManage
from data.userinfo import *
from src.modules.login_cms import LoginCms
from src.common.mysql import Mysql
from time import sleep

class TestModifyAcc(unittest.TestCase):
    user = None
    token = None
    newuser = None
    userid = None

    def setUp(self):
        # 登录外呼后台
        global token, user,userid,newuser
        user = LoginCms(pro_add_cms)
        res = user.login_cms(acc_cms, pawd_cms)
        self.assertEqual(res['data']['realName'], '顾荣荣')
        self.assertEqual(res['data']['userId'], 32)
        token = res['data']['token']
        #添加正式账号
        newuser = AccManage(pro_add_cms)
        res = newuser.add_user(token, new_user, pswd, mob_phone, auto_name)
        #查询数据库获取userid
        product_m = Mysql(myq_ip, myq_port, myq_user, myq_pswd, dbname)
        con = product_m.connect_mysql()
        flag = True
        while flag:
            res2 = product_m.mysql_select(con[0],"SELECT id FROM user where username='%s' and account_status=1" % new_user)
            for row in res2:
                userid = row[0]
                flag = False
            sleep(1)

        self.assertEqual(res['status'],code_1000)
        self.assertEqual(res['msg'],success)

    def test_modifyaccount(self):
        '''修改正式账号'''
        res=newuser.modify_account(token,userid,indtypes)
        flag=False
        for i in range(time_out):
            try:
                self.assertEqual(res['status'], code_1000)
                self.assertEqual(res['msg'],success)
                flag =True
                break
            except:
                sleep(1)

        self.assertTrue(flag)

    def tearDown(self):
        # 删除用户
        res = newuser.delete_account(token, userid)
        result = res(newuser.cdc_url_cms)
        self.assertEqual(result['status'], code_1000)
        self.assertEqual(result['data']['msg'], '任务已经全部结束')
        result2 = res(newuser.isak_url_cms)
        self.assertEqual(result2['status'], code_1000)
        self.assertEqual(result2['data'], 2)

        logout = user.logout_cms(token)
        self.assertEqual(logout['status'],code_1000)
        self.assertEqual(logout['msg'],success)
