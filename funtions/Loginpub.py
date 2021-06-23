"""
 # coding: utf-8
 # @Author：xiabo
 # @File : Loginpub.py
 # @Date ：2021/6/22 上午11:02
 
"""

'''
登录测试
'''

from untils.log import LOG, logger
from exctfuntion.test_fun import MakeAppCace
import os
from config.config import base_dir

path_case = os.path.join(base_dir, 'data/location/login.yaml')


@logger('登录测试')
class LoginFun():
    def __init__(self, driver):
        self.driver = driver
        self.path = path_case
        self.open = MakeAppCace(self.driver, path=self.path)

    def login(self, **kwargs):
        f = self.open.exce_case(**kwargs)
        if f['code'] == 1:
            LOG.info('无法获取断言')
            return
        else:
            backgroud = f['data']
            return backgroud
