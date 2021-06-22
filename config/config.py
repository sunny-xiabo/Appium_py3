"""
 # coding: utf-8
 # @Author：xiabo
 # @File : config.py
 # @Date ：2021/6/16 下午5:19
 
"""

'''

配置APP以及测试设备的相关信息
'''

import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #项目首路径

AppPackage = '' #被测应用名称
TestandroidDeviceReadyTimeout = 30  #超时时间
TestunicodeKeyboard = True
TestresetKeyboard = True

Test_Project_name = ''
TiTestuser = ''
Test_user = "自动化"
app_path = os.path.join(base_dir, "data/packages/ryxly.apk")