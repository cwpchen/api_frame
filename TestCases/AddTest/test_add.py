# coding=utf-8
# !/usr/bin/env python
from calculator import *
from Start_End import *

class Test_add(Setup_tearDown):
    @classmethod
    def setUpClass(cls):
        print ("class Test_add methoud start >>>>>>>>>>>>>>>>")
    @classmethod
    def tearDownClass(cls):
        print ("class Test_add methoud end >>>>>>>>>>>>>>>>")

    def test_add(self):
        j= Math(5,5)
        self.assertEqual(j.add(),10)
    def test_add1(self):
        j= Math(5,8)
        self.assertEqual(j.add(),13)
