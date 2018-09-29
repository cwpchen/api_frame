# coding=utf-8
# !/usr/bin/env python
import xml.sax
from xml.sax import parse
from GetXmlInfo import *
import smtplib  #发送邮件模块
from email.mime.text import MIMEText #定义邮件内容
from email.header import Header #定义邮件标题
import string

class SendMailTool():
    '''

    '''
    def __init__(self,subject,content,xmlDir=None):#smtpserver,username,password,sender,receive,port,subject,content
        '''
        从xml 文件获取搜索信息
        :param dict:
        :param subject:
        :param content:
        '''
        self.mailInfoDict = {}
        if xmlDir ==None:
            xmlDir = r'F:\CWP\project\api_test\Data\WebSeach_config.xml'
        parser = xml.sax.make_parser() #创建1个xml Reader
        mailInfo = GetRunCaseInfo(self.mailInfoDict) #实例化GetRunCaseInfo 类
        parser.setContentHandler(mailInfo) #重写content handel setContentHandler
        parse(xmlDir,GetRunCaseInfo(self.mailInfoDict)) #解析xml文件
        self.smtpserver = self.mailInfoDict['smtpserver']
        self.username = self.mailInfoDict['username']
        self.password = self.mailInfoDict['password']
        self.sender = self.mailInfoDict['sender']
        if type(self.mailInfoDict['receive'])==list:
            self.reseive = ','.join(self.mailInfoDict['receive'])
        else:
            self.reseive =self.mailInfoDict['receive']
        self.port = int(self.mailInfoDict['port'])
        self.subject = subject #邮件主题
        self.content = content #邮件内容


    def sendMail(self):
        '''
        发送邮件
        :return:
        '''
        #HTML正文
        msg = MIMEText(self.content,'html','utf-8')
        msg['subject']=Header(self.subject,'utf-8')
        msg['From']=self.sender
        msg['To']=self.reseive

        smtp = smtplib.SMTP_SSL(self.smtpserver ,self.port) #SSL协议使用端口号
        smtp.helo(self.smtpserver)#向服务器标识身份
        smtp.ehlo(self.smtpserver)#服务器返回结果确认
        smtp.login(self.username,self.password)#登录服务器
        print(u'开始发送邮件。。。。。')
        smtp.sendmail(self.sender,self.reseive,msg.as_string())
        smtp.quit()
        print (u'邮件发送完成！')
