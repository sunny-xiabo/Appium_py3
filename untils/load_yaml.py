"""
 # coding: utf-8
 # @Author：xiabo
 # @File : load_yaml.py
 # @Date ：2021/6/17 上午10:49
 
"""

'''
读取解析yaml文件
'''

import yaml
from untils.log import LOG,logger


@logger('解析yaml文件')
def open_da(path):
    try:
        with open('{}'.format(path), 'r', encoding='utf-8') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            return {'code':0, 'data': data}
    except Exception as e:
        LOG.info('yaml文档解析失败！原因：{}'.format(e))
        return {'code': 1, 'data':e}