"""
 # coding: utf-8
 # @Author：xiabo
 # @File : Parame_unittest.py
 # @Date ：2021/6/21 下午3:59
 
"""

'''unittest的再次封装'''

import unittest


class Parame(unittest.TestCase):

    def __init__(self, methodName='runTest', param=None):
        super(Parame, self).__init__(methodName)
        self.parme = param

    def parametrize(testcase_klass, param=None):
        test_loader = unittest.TestLoader()
        test_names = test_loader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in test_names:
            suite.addTest(testcase_klass(methodName=name, parm=param))
        return suite
