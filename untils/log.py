"""
 # coding: utf-8
 # @Author：xiabo
 # @File : log.py
 # @Date ：2021/6/16 下午5:30
 
"""

'''
日志相关
'''

import os
import logbook
from config.config import base_dir
from logbook.more import ColorizedStderrHandler
from functools import wraps


LOG_DIR = os.path.join(base_dir, 'testlog')
file_stream = False


if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)
    file_stream = True


def get_logger(name='appium_test', file_log=file_stream, level=''):
    logbook.set_datetime_format('local')
    ColorizedStderrHandler(bubble=False, level=level).push_thread()
    logbook.TimedRotatingFileHandler(
        os.path.join(LOG_DIR, '%s.log' % name),
        date_format='%Y-%m-%d-%H', bubble=True, encoding='utf-8').push_thread()
    return logbook.Logger(name)


LOG = get_logger(file_log=file_stream, level='INFO')


def logger(param):
    def wrap(function):
        @wraps(function)
        def _wrap(*args, **kwargs):
            LOG.info("当前模块 {}".format(param))
            LOG.info("全部kwargs参数信息， {}".format(str(kwargs)))
            return function(*args, **kwargs)
        return _wrap
    return wrap