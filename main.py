"""
 # coding: utf-8
 # @Author：xiabo
 # @File : main.py
 # @Date ：2021/6/16 下午5:18
 
"""

'''
自动化测试的主运行脚本
'''

from untils.read_excel import create
from untils.log import LOG, logger
from untils.make_case import make_casefile
from multiprocessing import Pool
from untils.Parame_unittest import Parame
from untils.AppiumServer import AppiumServer
from untils.base_apk import getPhoneInfo, AndroidDebugBridge
from config.config import base_dir
from testcase.login_case_test import Logintest

import os
import unittest
import datetime
import time

l_devices = []


@logger('生成设备配置链接的进程池')
def runner_pool(getDevices):
    """
    根据链接的设备生成不同的dict
    然后放到设备的list里面
    设备list的长度产生进行池大小
    """
    devices_Pool = []
    for device in getDevices:
        _pool = []
        _initApp = {
            "udid": device["devices"],
            "port": device["port"],
            "deviceName": device["devices"],
            "platformVersion": getPhoneInfo(devices=device["devices"])["release"],
            "platformName": "android",
            "appPackage": 'com.pep.riyuxunlianying',
            "appActivity": 'com.pep.riyuxunlianying.activity.StartActivity'
        }
        _pool.append(_initApp)
        devices_Pool.append(_initApp)

    pools = Pool(processes=1)  # 定义CPU核数量为3
    res = pools.map(runner_case_app, devices_Pool)  # 把测试用例放到设置到进程池
    LOG.info(res)
    pools.close()
    pools.join()


@logger('组织测试用例')
def runner_case_app(devices):
    """
    利用unittest的testsuite来组织测试用例
    """
    LOG.info(devices)
    test_suit = unittest.TestSuite()
    test_suit.addTest(Parame.parametrize(Logintest, param=devices))  # 扩展的其他的测试用例都可以这样添加
    unittest.TextTestRunner(verbosity=2).run(test_suit)


if __name__ == '__main__':
    LOG.info("测试开始执行")
    start_time = datetime.datetime.now()
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    devices = AndroidDebugBridge().attahced_devices()
    LOG.info(devices)

    if len(devices) > 0:
        for dev in devices:
            app = {
                "devices": dev,
                "port": "4723"
            }
            l_devices.append(app)
        # appium开始
        # appium_server = AppiumServer(l_devices)
        # appium_server.start_server()  # 启动服务
        runner_pool(l_devices)

        # try:
        #     appium_server.stop_server(l_devices)
        # except Exception as e:
        #     LOG.info("关闭服务失败！失败原因：{}".format(e))

        end_time = datetime.datetime.now()
        hour = end_time - start_time

        # 生成测试报告
        filenm = os.path.join(base_dir, 'testreports/{}result.xls'.format(date))
        create(filename=filenm, devices_list=devices, Test_version='x.x.x', testtime=str(hour))
        LOG.info("测试执行完毕，耗时：{}".format(hour))

    else:
        LOG.info("没有可用的安卓设备")
