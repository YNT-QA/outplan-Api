# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/21 9:56
# 文件: test_runner.py
import sys
sys.path.append('..')
import HTMLTestRunner
import unittest
import datetime
from common.smtp import Smtp
from data.userinfo import *
import os

class Runner(unittest.TestCase):
    runner=None
    path=None

    def report(self):
        global path
        now_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        report_path=os.path.dirname(os.path.abspath('../.'))+'\\'+Report_path + '%s.html'%now_time

        with open(report_path,'wb') as fp:
            global runner
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=title,description=description)

            suiteTest = unittest.TestSuite()

            casespath=os.path.dirname(os.path.abspath('../.'))+'\\'+cases_path

            all_cases=unittest.defaultTestLoader.discover(casespath,'test_*.py')

            for case in all_cases:

                suiteTest.addTest(case)

            runner.run(suiteTest)

        email=Smtp()
        email.sendEmail(report_path)

if __name__ == '__main__':

    testrunner=Runner()
    testrunner.report()

