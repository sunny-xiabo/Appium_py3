"""
 # coding: utf-8
 # @Author：xiabo
 # @File : test_fun.py
 # @Date ：2021/6/22 上午10:22
 
"""

import time
from untils.load_yaml import open_da
from untils.log import logger, LOG
from untils.py_app import driver_encap as enc

"""
    解析测试步骤，按照需求进行测试用例
    默认定位的最后一组为断言
"""


@logger('解析测试步骤')
class MakeAppCace(object):

    def __init__(self, driver, path):
        self.driver = driver
        self.path = path

    def open_file(self):
        return open_da(path=self.path)

    def exce_case(self, **kwargs):
        data = self.open_file()['data']
        case_der = enc(driver=self.driver)

        for json_data in data:
            LOG.info(json_data)
            f = case_der.find_elemens(path=json_data['element_info'], method=json_data['find_type'])
            if json_data['operate_type'] == 'click':
                f[int(json_data['index'])].click()
            elif json_data['operate_type'] == 'text':
                f[int(json_data['index'])].text
            elif json_data['operate_type'] == 'send_key':
                f[int(json_data['index'])].clear()
                f[int(json_data['index'])].set_value(kwargs.get(json_data['key']))
            else:
                LOG.info('请您检查步骤')
            time.sleep(5)

        f = case_der.find_elemens(method=json_data['find_type'], path=json_data['element_info'])

        if json_data['operate_type'] == 'text':
            unit = {'code': 0, 'data': f[int(json_data['index'])].text}
        else:
            unit = {'code': 1, 'data': "请检查您的测试步骤最后一步为断言用的"}
            LOG.info('请检查您的测试步骤最后一步为断言用的')

        return unit
