"""
 # coding: utf-8
 # @Author：xiabo
 # @File : read_excel.py
 # @Date ：2021/6/21 下午1:49
 
"""

'''生成xlsx的测试报告'''

import xlwt
from xlwt import *
from datetime import datetime
from config.config import *
from untils.save_result import parse_result
from untils.log import LOG, logger
from untils.base_apk import getPhoneInfo


def style_one():
    style1 = XFStyle()
    fnt = Font()
    fnt.name = u'微软雅黑'
    fnt.bold = True
    style1.font = fnt
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style1.alignment = alignment  # 给样式添加文字居中属性
    style1.font.height = 430  # 设置字体大小
    return style1


def style_two():
    style2 = XFStyle()
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style2.alignment = alignment
    style2.font.height = 330
    return style2


def style_three():
    style3 = XFStyle()
    style3.font.height = 330
    return style3


def style_que(me):
    if me == 'pass':
        style = style_one()
        Pattern = xlwt.Pattern()
        Pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        Pattern.pattern_fore_colour = xlwt.Style.charset_map['green']
        style.pattern = Pattern
    else:
        style = style_two()
        Pattern = xlwt.Pattern()
        Pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        Pattern.pattern_fore_colour = xlwt.Style.charset_map['red']
        style.pattern = Pattern
        return style


@logger('生成测试报告')
def create(filename, testtime, Test_version, devices_list):

        file = Workbook(filename)
        table = file.add_sheet('测试结果', cell_overwrite_ok=True)
        style = style_one()
        for i in range(0, 7):
            table.col(i).width = 380 * 20
        style1 = style_two()
        table.write_merge(0, 0, 0, 6, '测试报告', style=style)
        table.write_merge(2, 3, 0, 6, '测试详情', style=style1)
        table.write(4, 0, '项目名称', style=style1)
        table.write(5, 0, '测试版本', style=style1)
        table.write(6, 0, '提测时间', style=style1)
        table.write(7, 0, '提测人', style=style1)
        table.write(4, 2, '测试人', style=style1)
        table.write(5, 2, '测试时间', style=style1)
        table.write(6, 2, '审核人', style=style1)
        table.write(8, 0, '链接号', style=style1)
        table.write(8, 1, '品牌', style=style1)
        table.write(8, 2, '设备名', style=style1)
        table.write(8, 3, '型号', style=style1)
        table.write(8, 4, '版本', style=style1)
        table.write(8, 5, '通过', style=style1)
        table.write(8, 6, '失败', style=style1)
        table.write(4, 1, Test_Project_name, style=style1)
        table.write(5, 1, Test_version, style=style1)
        table.write(6, 1, testtime, style=style1)
        table.write(7, 1, TiTestuser, style=style1)
        table.write(4, 3, Test_user, style=style1)
        table.write(5, 3, datetime.now().strftime("%Y-%m-%d %HH:%MM"), style=style1)
        table.write(6, 3, "admin", style=style1)
        all_result = []
        for devices in devices_list:
            fail, pass_a, result = parse_result(devices=str(devices))
            all_result.append(result)
            de_result = getPhoneInfo(devices=str(devices))
            table.write(9, 0, devices, style=style1)
            table.write(9, 1, de_result['brand'], style=style1)
            table.write(9, 2, de_result['device'], style=style1)
            table.write(9, 3, de_result['model'], style=style1)
            table.write(9, 4, de_result['release'], style=style1)
            table.write(9, 5, fail, style=style1)
            table.write(9, 6, pass_a, style=style1)
        table1 = file.add_sheet('测试详情', cell_overwrite_ok=True)
        table1.write_merge(0, 0, 0, 8, '测试详情', style=style)
        for i in range(0, 6):
            table1.col(i).width = 400 * 20
        table1.write(1, 0, '测试用例编号', style=style_three())
        table1.write(1, 1, '测试模块', style=style_three())
        table1.write(1, 2, '所需要参数', style=style_three())
        table1.write(1, 3, '预期', style=style_three())
        table1.write(1, 4, '结果', style=style_three())
        table1.write(1, 5, '测试设备', style=style_three())
        for i in range(len(all_result)):
            for item in all_result[i]:
                table1.write(i + 2, 0, str(eval(item['param'])['id']), style=style_three())
                table1.write(i + 2, 0, str(eval(item['param'])['model']), style=style_three())
                table1.write(i + 2, 0, str(eval(item['param'])), style=style_three())
                table1.write(i + 2, 0, str(eval(item['param'])['assert']), style=style_three())
                table1.write(i + 2, 0, str(item['result']), style=style_three())
                table1.write(i + 2, 0, str['devices'], style=style_three())
        file.save(filename)
        LOG.info("测试报告保存成功")

