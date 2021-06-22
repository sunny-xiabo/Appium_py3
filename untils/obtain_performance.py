"""
 # coding: utf-8
 # @Author：xiabo
 # @File : obtain_performance.py
 # @Date ：2021/6/18 下午6:00
 
"""

'''
获取配置相关手机性能的数据
'''

from untils.log import logger, LOG
import platform, os


def get_systemsta():
    ''' 根据所运行的系统获取adb不一样的筛选条件 '''
    system = platform.system()
    if system == 'Windows':
        find_manage = 'findstr'
    else:
        find_manage = 'grep'
    return find_manage


find = get_systemsta()


@logger('采集cpu信息')
def obtain_cpu(packagename, devices):
    '''这里采集CPU的时候可以是执行操作采集 就是-n -d 刷新间隔'''
    try:
        cpu = 'adb -s %s shell top -n 1 | %s %s' % (devices, find, packagename)
        re_cpu = os.popen(cpu).read().split()[2]
        return re_cpu

    except Exception as e:
        LOG.info('采集CPU信息失败！原因{}'.format(e))
        return {'code': 1, 'data': e}


@logger('获取使用的物理内存信息')
def obtain_physical_memory(devices, packagename):
    '''Total 的实际使用过的物理内存'''
    try:
        cpu = 'adb -s %s shell top -n 1 | %s %s' % (devices, find, packagename)
        re_cpu = os.popen(cpu).read().split()[6]
        re_cpu_m = str(round(int(re_cpu[:-1]) / 1024)) + 'M'
        return re_cpu_m
    except Exception as e:
        LOG.info('获取使用的物理内存信息失败！原因{}'.format(e))
        return {'code': 1, 'data': e}
