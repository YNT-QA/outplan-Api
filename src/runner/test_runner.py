# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/21 9:56
# 文件: test_runner.py
import sys
sys.path.append('..')
import HTMLTestRunner
import unittest
import datetime
from common.get_path import GetPath
from common.get_value import GetValue
from common.smtp import Smtp

class Runner(unittest.TestCase):
    runner=None
    path=None
    data=None

    def report(self):
        global path,data

        data=GetValue()
        now_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        path=GetPath(data.getvalue('report_path')+'%s.html'%now_time)
        report_path=path.get_filePath()

        with open(report_path,'wb') as fp:
            global runner
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=data.getvalue('title'),description=data.getvalue('description'))

            suiteTest = unittest.TestSuite()

            path=GetPath(data.getvalue('cases_path'))

            all_cases=unittest.defaultTestLoader.discover(path.get_filePath(),'test_*.py')

            for case in all_cases:

                suiteTest.addTest(case)

            runner.run(suiteTest)

        email=Smtp()
        email.sendEmail(report_path)

if __name__ == '__main__':

    testrunner=Runner()
    testrunner.report()

