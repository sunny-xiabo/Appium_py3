"""
 # coding: utf-8
 # @Author：xiabo
 # @File : login_case_test.py
 # @Date ：2021/6/22 上午9:59
 
"""

from appium import webdriver
import ddt
import os
import time
import unittest
from untils.Parame_unittest import Parame
from untils.log import LOG, logger
from untils.init_app_params import make_dis
from untils.obtain_test_data import obtain_test_data
from untils.obtain_performance import obtain_cpu, obtain_physical_memory
from funtions.Loginpub import LoginFun
from untils.recording_txt import write_record
from config.config import AppPackage, base_dir, app_path
from untils.save_result import save_result

data_test = obtain_test_data(os.path.join(base_dir, 'data/testcase_data.xlsx'), index=1)


@ddt.ddt
class Logintest(Parame):

    def __init__(self, parm, methodName='runTest'):
        super(Logintest, self).__init__(methodName)
        self.port = parm['port']  # appium连接端口
        self.udid = parm['udid']  # appium连接设备
        self.parm = parm

    # 这是login测试用例
    def setUp(self):
        """
        setup
        :return:
        """
        LOG.info("setup.......")
        self.dis_app = make_dis(self.parm)
        LOG.info('http://127.0.0.1:{}/wd/hub'.format(self.port))
        self.driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(self.port), self.dis_app)
        if not self.driver.is_app_installed(AppPackage):
            self.driver.install_app(app_path)

        LOG.info(self.driver)
        LOG.info('login测试用例开始执行')

    def tearDown(self):
        """
        teardown
        :return:
        """
        LOG.info('测试用例执行完毕，测试环境正在还原！')
        time.sleep(5)
        self.driver.quit()

    def test_swipe(self):
        # 打印屏幕高和宽
        window_size = self.driver.get_window_size()
        x = window_size['width']
        y = window_size['height']
        LOG.info('打印屏幕大小 window={}'.format(window_size))

        self.driver.swipe(6 / 7 * x, 1 / 2 * y, 1 / 7 * x, 1 / 2 * y, 100)

    @unittest.skip('先跳过登录实例')
    @ddt.data(*data_test)
    def test_login(self, data_test):
        """
        login测试
        :param date_test:
        :return:
        """
        loginfun = LoginFun(driver=self.driver)
        self.assertuen = loginfun.login(**data_test)

        cpu = obtain_cpu(
            packagename=AppPackage,
            devices=self.parm['deviceName']
        )
        memory = obtain_physical_memory(
            packagename=AppPackage,
            devices=self.parm['deviceName']
        )
        write_record(
            cpu=cpu,
            memory=memory,
            devices=str(self.parm['deviceName'])
        )
        if data_test['assert'] == self.assertuen:
            device = self.parm['udid']
            data = "&".join([device, "pass", str(data_test)])  # 设备+ "&"+"pass"+"&"+str(data_test)
            save_result(data)
        else:
            data = "&".join([self.parm['udid'], "pass", str(data_test)])
            save_result(data)
