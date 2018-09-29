# coding=utf-8
# !/usr/bin/env python
import xml.sax
from xml.sax import parse
from GetXmlInfo import *


class GetElementTool(object):
    def getSearchInfo(self,xmlDir=None):
        '''
        从xml 文件获取搜索信息
        :return:
        '''
        if xmlDir==None:
            xmlDir= r'F:\CWP\project\api_test\Data\WebSeach_config.xml'
        self.test_Info = {}
        parser = xml.sax.make_parser()
        xmlInfo = GetXmlInfo(self.test_Info)
        parser.setContentHandler(xmlInfo)
        parse(xmlDir, GetXmlInfo(self.test_Info))
        return self.test_Info