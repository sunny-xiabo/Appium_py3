"""
 # coding: utf-8
 # @Author：xiabo
 # @File : save_result.py
 # @Date ：2021/6/18 下午5:45
 
"""

'''
记录测试结果
'''

import os
import time
from untils.log import logger, LOG
from config.config import base_dir


date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
recording = os.path.join(base_dir, 'testreports/{}.txt'.format("tmp"))


@logger("保存测试结果")
def save_result(data):

    if os.path.exists(recording):
        with open(recording, 'w+', encoding='utf-8')as f:
            f.write(data + '\n')

    else:
        with open(recording, 'w+')as f:
            f.write(data + '\n')

    LOG.info("记录测试结果完毕")


@logger('解析测试结果')
def parse_result(devices):
    with open(recording, 'r+', encoding='utf-8')as f:
        result = f.readlines()

    list_result = []
    for j in result:
        if devices in j:
            list_result.append(
                {
                    "devcies": devices,
                    "result": j.split('&')[1],
                    "params": j.split('&')[2]
                }
            )

    passnum = 0
    failnum = 0
    for i in list_result:
        if i['result'] == 'pass':
            passnum += 1
        else:
            failnum += 1
    LOG.info('解析设备测试结果完毕')
    return passnum, failnum, list_result
