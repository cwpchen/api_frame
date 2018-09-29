# coding=utf-8
# !/usr/bin/env python
import unittest

class RunTools:
    def ChooseDirCases(self,casedir,pattern):
        """
        # 获取根据指定目录获取匹配的测试用例
        :param casedir: 测试用例路径
        :param pattern: 匹配模式
        :return: 测试用例集
        """
        dis = unittest.TestLoader()
        discover_cases = dis.discover(casedir,pattern=pattern)
        return discover_cases

    def ChooseAllCases(self,pattern,testcase_path=None):
        '''
        获取多级目录下所有的测试用例
        :param pattern: 匹配模式
        :param testcase_path : 多级目录中指定的目录下所有用例
        :return: 测试用例集
        '''
        if testcase_path ==None:
            testcase_path = ''#testcase_path是测试用例的根目录
        dis= unittest.TestLoader()
        discover_all_cases = dis.discover(testcase_path,pattern=pattern,top_level_dir=None)
        return discover_all_cases

    def ChooseDifFileCases(self,casedirList,pattern):
        '''
        一次执行不同目录下的测试用例
        :param casedir:
        :param dirList:
        :param pattern:
        :return:
        '''
        discover_dif_cases=[]
        for case in casedirList :
            dis = unittest.TestLoader()
            discover = dis.discover(case,pattern=pattern)
            discover_dif_cases.append(discover)
        return discover_dif_cases
