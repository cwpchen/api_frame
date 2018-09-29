# coding=utf-8
# !/usr/bin/env python
from calculator import *
from TestCases.Start_End import *

@unittest.skip(u"开发自验")
class Test_sub(Setup_tearDown):
    def test_sub(self):
        j= Math(5,1)
        self.assertEqual(j.sub(),4)
    def test_sub1(self):
        j= Math(8,8)
        self.assertEqual(j.sub(),0)
