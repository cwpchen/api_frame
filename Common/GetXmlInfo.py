# coding=utf-8
# !/usr/bin/env python
import xml
import re
import xml.sax

# import xml.etree.ElementTree as ET
class GetXmlInfo(xml.sax.ContentHandler):
    def __init__(self,dict):
        self.test_Info=dict
        self.explorer = None
        self.url = None
        self.key = None
         #"explorer":"",'url':"","key":""

    def startElement(self,name,attrs):
        self.currentData = name
        if name == "search_element":
            self.test_Info['test_type']=attrs["name"]

    def endElement(self,name):
        self.test_Info['explorer'] = self.explorer
        self.test_Info['url'] = self.url
        self.test_Info['key'] = self.key
        return self.test_Info

    def characters(self,content):
        if self.currentData =='explorer':
            pattern = re.compile('".*"')
            element = pattern.findall(content)
            if element:
                self.explorer = element[0]

        elif self.currentData =='url':
            if r'//'in content:
                self.url = content

        elif self.currentData =='key':
            if '"'in content:
                self.key = content

class GetRunCaseInfo(xml.sax.ContentHandler):
    def __init__(self,dict):
        self.run_Info=dict
        self.smtpserver = None
        self.username = None
        self.password = None
        self.sender = None
        self.receive = None
        self.port = None
        self.subject = None  # 邮件主题
        self.content = None  # 邮件内容
         #"explorer":"",'url':"","key":""

    def startElement(self,name,attrs):
        self.currentData = name
        if name == "sendmail_element":
            self.run_Info['run_type']=attrs["name"]

    def endElement(self,name):
        self.run_Info['smtpserver'] = self.smtpserver
        self.run_Info['username'] = self.username
        self.run_Info['password'] = self.password
        self.run_Info['sender'] = self.sender
        self.run_Info['receive'] = self.receive
        self.run_Info['port'] = self.port
        return self.run_Info

    def characters(self,content):

        if self.currentData =='smtpserver':
            if "com" in content:
                self.smtpserver = content

        elif self.currentData =='username':
            if "com" in content:
                self.username = content

        elif self.currentData =='password':
            if  not content.isspace():
                self.password = content

        elif self.currentData =='sender':
            if "com" in content:
                self.sender = content

        elif self.currentData =='receive':
            if "com" in content:
                self.receive = content

        elif self.currentData =='port':
            if content.isdigit():
                self.port = content

