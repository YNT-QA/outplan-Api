# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/12/14 11:59
# 文件: test_againoutplan.py
import sys
sys.path.append('..')
import unittest
from modules.login import Login
from modules.outplan import OutPlan
from modules.customer_manage import CustomerManage
from common.mongodb import Mongodb
import time
from modules.sip_manage import sipManage
from common.mysql import Mysql
from data.userinfo import *

class TestCreateOutPlan(unittest.TestCase):
    lg = None
    token= None
    groupId= None
    csm= None
    planId = None
    auto_test = None
    phoneId=None
    planId2=None
    sip=None
    sip_id=None
    group_number=None

    def setUp(self):
        global lg,token,groupId,csm,planId,phoneId,auto_test,sip,sip_id,group_number

        #登录
        lg = Login(product_address)
        res = lg.login(account,product_password)
        token=res['data']['token']
        self.assertEqual(res['data']['userName'],account)
        self.assertEqual(res['data']['accountType'],1)

        #创建客户组手动上传号码
        csm=CustomerManage(product_address)
        res2=csm.addPhoneNumber(token,userid,phonum_list,1,auto_name)
        self.assertEqual(res2['status'], code_1000)
        self.assertEqual(res2['msg'],import_suc)

        #查询mongodb获取groupId
        product=Mongodb(dbname,table_phonum,db_ip,db_port)
        table=product.connect_mongodb()
        res3=product.mongodb_find(table,{'userId':privately,'groupName':auto_name})
        for item in res3:
            groupId=item['groupId']

        #添加SIP
        sip=sipManage(product_address)
        res=sip.add_sip(token,username,password,ip,port,privately,lineType,groupSize)
        self.assertEqual(res['status'], code_1000)
        self.assertEqual(res['msg'],success)

        #查询mysql获取线路id、group_number
        product_m = Mysql(myq_ip,myq_port,myq_user,myq_pswd,dbname)
        con = product_m.connect_mysql()
        res = product_m.mysql_select(con[0], 'SELECT id,group_number FROM ko_sipmanager where privately=21')
        for row in res:
            sip_id=row[0]
            group_number=row[1]

        #创建外呼计划
        auto_test = OutPlan(product_address)
        res = auto_test.creat_outplan(token,userid,'3706',auto_name,'尚德销售纵线白名单',sip_id,groupId)
        planId = res['data']['planId']
        self.assertEqual(res['status'], code_1000)
        self.assertEqual(res['msg'],success)

        #获取phoneid
        res=auto_test.get_CallDetail(token,planId)
        phoneId=res['data']['list'][0]['id']


    def test_createAgainplan(self):
        '''创建二次外呼'''
        global planId2
        # 查询mongodb外呼计划状态
        product = Mongodb(dbname,tab_calllog,db_ip,db_port)
        table = product.connect_mongodb()

        flag = True
        while flag:
            res2 = product.mongodb_find(table, {'userId':privately, 'planName':auto_name, 'planId': planId})
            for item in res2:
                if item['status'] == status_finish:
                    #二次外呼
                    res=auto_test.create_AgainOutPlan(token,userid,'3706','尚德销售纵线白名单',sip_id,phoneId,planName2)
                    self.assertEqual(res['status'], code_1000)
                    self.assertEqual(res['msg'],success)
                    planId2=res['data']['planId']
                    flag = False
            time.sleep(1)


    def tearDown(self):
        #删除客户组与号码
        res=csm.deleteGroupAndCustomerPhone(token,groupId)
        self.assertEqual(res['status'], code_1000)
        self.assertEqual(res['msg'],del_suc)
        #删除第一个计划
        res2 = auto_test.delete_outplan(token, planId)
        self.assertEqual(res2['status'], code_1000)
        self.assertEqual(res2['msg'],success)

        #查询mongodb外呼计划状态
        product = Mongodb(dbname,tab_calllog,db_ip,db_port)
        table = product.connect_mongodb()

        flag=True
        while flag:
            res3 = product.mongodb_find(table, {'userId':privately, 'planName': planName2, 'planId': planId2})
            for item in res3:
                if item['status']==status_finish:
                    # 删除外呼计划2
                    res4 = auto_test.delete_outplan(token, planId2)
                    self.assertEqual(res4['status'], code_1000)
                    self.assertEqual(res4['msg'],success)
                    flag=False
            time.sleep(1)

        #修改SIP禁用
        res5=sip.update_sip(token,group_number,sip_id,username,password,ip,port,privately,lineType,groupSize)
        self.assertEqual(res5['status'], code_1000)
        self.assertEqual(res5['msg'],success)
        #删除sip
        res6=sip.delete_sip(token,sip_id)
        self.assertEqual(res6['status'], code_1000)
        self.assertEqual(res6['msg'],success)
        #注销用户
        logout=lg.logout(token)
        self.assertEqual(logout['status'],code_1000)
        self.assertEqual(logout['msg'],success)