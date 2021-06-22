"""
 # coding: utf-8
 # @Author：xiabo
 # @File : make_case.py
 # @Date ：2021/6/21 下午4:18
 
"""

'''
生成测试用例文件
'''

import os
from untils.log import logger, LOG
from config.config import base_dir


def read_header():
    path_new = os.path.join(base_dir, '/testsuite/case.txt')
    return open(path_new, encoding='utf-8').read()


def read_conet():
    path_new = os.path.join(base_dir, '/testsuite/content.txt')
    conet = open(path_new, encoding='utf-8').read()
    return conet


def make_casefile(casename, desc, funtion_name):
    LOG.info("开始生成测试用例文件")
    filepath = os.path.join(base_dir, '/testcase/{}casetest.py').format(casename)
    if not os.path.exists(filepath):
        with open(filepath, 'W', encoding='utf-8')as file:
            file.write(read_header().format(casename, casename))
            file.write(read_conet().format(funtion_name, desc))
    else:
        pass
