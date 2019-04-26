# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/3/6 17:52
# 文件: test_addoutacc_cms.py
import unittest
from src.modules.login_cms import LoginCms
from data.userinfo import *
from src.modules.accmanage_cms import AccManage
from src.common.mysql import Mysql
from time import sleep
import time

class TestOutAcc(unittest.TestCase):
    user = None
    token = None
    newuser=None
    user_id=None

    def setUp(self):
        #登录外呼后台
        global token,user
        user = LoginCms(pro_add_cms)
        res = user.login_cms(acc_cms,pawd_cms)
        self.assertEqual(res['data']['realName'],'顾荣荣',msg=msg1)
        self.assertEqual(res['data']['userId'],32)
        token = res['data']['token']

    def test_addoutacc(self):
        u'''添加外部测试账号'''
        global newuser,user_id
        newuser=AccManage(pro_add_cms)
        res=newuser.add_user(token,new_user,pswd,mob_phone,auto_name,accounttype=3,agentexpiredate=time.strftime('%Y-%m-%d',time.localtime()))
        self.assertEqual(res['status'], code_1000,msg='添加外部测试账号失败')
        self.assertEqual(res['msg'], success)
        #查询数据库获取userid
        product_m = Mysql(myq_ip,myq_port,myq_user,myq_pswd,dbname)
        con = product_m.connect_mysql()
        flag = False
        for i in range(time_out):
            res2 = product_m.mysql_select(con[0], "SELECT id FROM user where username='%s' and account_status=1"%new_user)
            for row in res2:
                user_id = row[0]
                flag = True
            sleep(1)

        self.assertTrue(flag,msg='查询数据库获取userid失败')

    def tearDown(self):
        #删除用户
        res =newuser.delete_account(token, user_id)
        result = res(newuser.cdc_url_cms)
        self.assertEqual(result['status'],code_1000,msg='任务结束失败')
        self.assertEqual(result['data']['msg'],'任务已经全部结束')
        result2 = res(newuser.isak_url_cms)
        self.assertEqual(result2['status'],code_1000,msg='删除用户失败')
        self.assertEqual(result2['data'], 2)
        #退出
        logout = user.logout_cms(token)
        self.assertEqual(logout['status'],code_1000,msg=msg2)
        self.assertEqual(logout['msg'],success)