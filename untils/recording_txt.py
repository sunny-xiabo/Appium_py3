"""
 # coding: utf-8
 # @Author：xiabo
 # @File : recording_txt.py
 # @Date ：2021/6/21 下午3:36
 
"""

'''采集的性能测试数据存放在TXT文件中'''

import os
import time
from untils.log import LOG, logger
from config.config import base_dir

now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
recording = os.path.join(base_dir, '/testreports/{}-PerFormance.txt'.format(now))


@logger('记录当前的CPU占有率，内存')
def write_record(cpu, memory, devices):
    try:
        with open(recording, 'a', encoding='utf-8')as f:
            m = '%s: cpu:%s, Memory:%s' % (devices, cpu, memory)
            f.write(m + '\n')
            f.close()
    except Exception as e:
        LOG.info('写入性能数据失败！失败原因：%s' % e)
