# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/11/16 9:51
# 文件: mysql.py
import  MySQLdb

class Mysql:
    '''
    uat=Mysql()
    con=uat.connect_mysql()
    res=uat.mysql_select(con[0],'SELECT * FROM ko_sipmanager where privately=21')
    for row in res:
        print(row)

    '''
    def __init__(self,host='192.168.88.63',port=3306,user='root',passwd='kalamodo',db='outbound_uat'):
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.db=db


    # 数据库连接
    def connect_mysql(self):
        db = MySQLdb.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db,charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        con=[cursor,db]
        return con

    #SQL查询
    def mysql_select(self,cursor,sql):
        # 使用execute方法执行SQL语句
        cursor.execute(sql)

        # 获取所有记录列表
        results = cursor.fetchall()
        return results

    # SQL插入
    def mysql_insert(self,con,sql):
        try:
            # 执行sql语句
            con[0].execute(sql)
            # 提交到数据库执行
            con[1].commit()
        except:
            # 如果发生错误则回滚
            con[1].rollback()

    # SQL删除
    def mysql_delete(self,con,sql):
         try:
            # 执行sql语句
            con[0].execute(sql)
            # 提交到数据库执行
            con[1].commit()
         except:
            # 如果发生错误则回滚
            con[1].rollback()

    # SQL修改
    def mysql_update(self,con,sql):
        try:
            # 执行sql语句
            con[0].execute(sql)
            # 提交到数据库执行
            con[1].commit()
        except:
            # 如果发生错误则回滚
            con[1].rollback()
