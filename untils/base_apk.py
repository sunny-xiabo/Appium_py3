"""
 # coding: utf-8
 # @Author：xiabo
 # @File : base_apk.py
 # @Date ：2021/6/18 下午6:19
 
"""

'''
apk文件的读取信息
'''

import re
import subprocess
import os
from untils.log import LOG, logger
from untils.subprocess_popen import subprocess_popen


class ApkInfo(object):

    def __init__(self, apkPth):
        self.apkPath = apkPth

    def getApkBaseInfo(self):

        p = subprocess.Popen(
            "aapt dump badging {}".format(self.apkPath),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            shell=True
        )

        (output, err) = p.communicate()
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName'(\S+)'").match(output.decode())
        if not match:
            raise Exception("can't get packageinfo")

        packagename = match.group(1)
        appKey = match.group(2)
        appVersion = match.group(3)

        LOG.info("=======getApkInfo=======")
        LOG.info('packageName:', packagename)
        LOG.info('appKey:', appKey)
        LOG.info('appVersion:', appVersion)

        return packagename, appKey, appVersion

    # 得到启动类
    def getApkActivity(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, stdin=subprocess.PIPE,
                             shell=True)
        (output, err) = p.communicate()
        match = re.compile("launchable-activity: name=(\S+)").search(output.decode())
        if match is not None:
            return match.group(1)

    # 得到应用名字
    def getApkName(self):
        cmd = "aapt dump badging " + self.apkPath + " | grep application-label: "
        result = ""
        p = subprocess.Popen(
            cmd, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[0].decode()[19:-1]
        return result


def getPhoneInfo(devices):
    '''

    获取设备的一些基本信息
    :param devices:
    :return:
    '''
    cmd = "adb -s " + devices + " shell getprop {}"
    release = subprocess_popen(cmd.format("ro.build.version.release"))[0].decode(encoding='utf-8').strip() # 版本
    model = subprocess_popen(cmd.format("ro.product.model"))[0].decode(encoding='utf-8').strip()   # 型号
    device = subprocess_popen(cmd.format("ro.product.device"))[0].decode(encoding='utf-8').strip()   # 设备名
    brand = subprocess_popen(cmd.format("ro.product.brand"))[0].decode(encoding='utf-8').strip()   # 品牌
    result = {"release": release, "model": model, "device": device, "brand": brand}
    LOG.info(result)



class AndroidDebugBridge(object):

    def call_adb(self, command):
        command_result = ''
        command_text = 'adb %s' % command
        results = os.popen(command_text, 'r')
        while 1:
            line = results.readline()
            if not line: break
            command_result += line
        results.close()
        return command_result

    # 拉数据到本地
    def pull(self, remote, local):
        result = self.call_adb("pull %s %s") % (remote, local)
        return result

    # 获取连接的设备
    def attahced_devices(self):
        devices = []
        result = subprocess_popen("adb devices")
        for item in result:
            t = item.decode().split("\tdevice")
            if len(t) >= 2:
                devices.append(t[0])
        return devices




print(getPhoneInfo('emulator-5554'))