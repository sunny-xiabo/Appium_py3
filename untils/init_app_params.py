"""
 # coding: utf-8
 # @Author：xiabo
 # @File : init_app_params.py
 # @Date ：2021/6/16 下午5:29
 
"""

'''
从配置文件获取相关的APP测试配置信息
'''


from config.config import *
from untils.log import logger


@logger("开始从配置文件中获取测试相关的配置")

def make_dis(params):
    return {
        'platformName': params['platformName'],
        'platformVersion': params['platformVersion'],
        'deviceName': params['deviceName'],
        'appPackage': params['appPackage'],
        'appActivity': params['appActivity'],
        'app': app_path,
        'noReset': True,

        'TestandroidDeviceReadyTimeout': TestandroidDeviceReadyTimeout,
        'TestunicodeKeyboard': TestunicodeKeyboard,
        'TestresetKeyboard': TestresetKeyboard,
    }