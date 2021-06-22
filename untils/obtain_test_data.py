"""
 # coding: utf-8
 # @Author：xiabo
 # @File : obtain_test_data.py
 # @Date ：2021/6/21 下午4:08
 
"""

'''从Excel获取测试用例相关数据'''

import xlrd
from untils.log import logger, LOG


@logger('获取测试用例所需要的参数')
def obtain_test_data(file_path, index=1):
    try:
        file = xlrd.open_workbook(file_path)
        me = file.sheets()[index]
        nrows = me.nrows
        listdata = []
        for i in range(1, nrows):
            dict_param = {
                'id': me.cell(i, 0).value,
                'model': me.cell(i, 0).value,
                'logout': (me.cell(i, 2).value)
            }
            dict_param.update(eval(me.cell(i, 3).value))
            dict_param.update(eval(me.cell(i, 4).value))
            listdata.append(dict_param)
        return listdata
    except Exception as e:
        LOG.info('获取测试用例参数失败！失败原因：%s' % e)
        return e
