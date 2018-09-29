# coding=utf-8
# !/usr/bin/env python
from RunTools import *
from HTMLTestRunner import HTMLTestRunner
from BSTestRunner import BSTestRunner
from SendMailTool import SendMailTool
import time

mailInfoDict={}
casesdir=['browse_test','SubTest','AddTest'] #'SubTest','AddTest',
runtool = RunTools()
casetest = runtool.ChooseDifFileCases(casedirList=casesdir, pattern="test*.py")
subject = 'web selenium 测试报告'
content = u'<html><h1 style="color:read">selenium 邮件发送测试 from cwp</h1></html>'

if __name__ == '__main__':
    report_dir = r'F:/CWP/project/api_test/Report'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = report_dir +'\\'+now+'result.html'
    fp = open(report_name,'w')
    runner = BSTestRunner(stream=fp,title='test report',description='Test case result')
    for case in casetest:
        runner.run(case)
    fp.close()
    sendmailHandle = SendMailTool(
        subject=subject,
        content=content
    )
    sendmailHandle.sendMail()




