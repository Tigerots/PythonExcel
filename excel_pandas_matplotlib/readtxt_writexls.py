#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Date: 2019/11/26
# @Author: Tigerots


import xlsxwriter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def read_tableMethod(filename):
    '''用read_table方法读取TXT文件'''
    data = pd.read_table(filename, header=None, delimiter=",")
    return  data


def creat_excel_book(bookname, sheetname, datas):
    # 创建一个excel
    workbook = xlsxwriter.Workbook(bookname)
    # 创建一个sheet
    worksheet = workbook.add_worksheet(sheetname)
    # 自定义样式，加粗
    bold = workbook.add_format({'bold': 1})
    # --------1、准备数据并写入excel---------------
    # 向excel中写入数据，建立图标时要用到
    headings = ['N', 'E']
    # 写入表头
    worksheet.write_row('A1', headings, bold)
    # 写入数据
    # worksheet.write_column('A2', datas[0])
    workbook.close()




if __name__ == '__main__':
    df = read_tableMethod('t1.txt')

    print("输出行号列表", df.index.values) # 行号
    print("输出列名标题", df.columns.values) # 列名


    df1 = read_tableMethod('t2.txt')
    # 追加数据到df
    df = df.append(df1, ignore_index=True)
    # 创建Excel的ExcelWriter对象
    writer = pd.ExcelWriter("t1.xlsx")
    workbook = writer.book

    '''
    'bold': True,  # 字体加粗
    'text_wrap': True,  # 是否自动换行
    'valign': 'top',  # 垂直对齐方式
    'align': 'right',  # 水平对齐方式
    'fg_color': '#D7E4BC',  # 单元格背景颜色
    'border': 2  # 单元格边框宽度
    'num_format': '0.00000000' # 小数点位数
    '''
    '''
    fmt = workbook.add_format({"font_name": u"微软雅黑"})
    percent_fmt = workbook.add_format({'num_format': '0.00%'})
    amt_fmt = workbook.add_format({'num_format': '#,##0.00'})
    border_format = workbook.add_format({'border': 1})
    # 日期格式
    date_fmt = workbook.add_format({'bold': False, 'font_name': u'微软雅黑', 'num_format': 'yyyy-mm-dd'})
    date_fmt1 = workbook.add_format(
        {'bold': True, 'font_size': 10, 'font_name': u'微软雅黑', 'num_format': 'yyyy-mm-dd', 'bg_color': '#9FC3D1',
         'valign': 'vcenter', 'align': 'center'})
    # 高亮
    highlight_fmt = workbook.add_format({'bg_color': '#FFD7E2', 'num_format': '0.00%'})
    '''
    # 标题文本格式
    note_fmt = workbook.add_format({ 'bold': True,
                                     'font_name': u'微软雅黑',
                                     'font_color': 'blue',
                                     'align': 'center',
                                     'valign': 'vcenter'})
    # 标题文本格式
    text_fmt = workbook.add_format({ 'bold': False,
                                     'font_name': u'微软雅黑',
                                     'font_color': 'black',
                                     'align': 'center',
                                     'valign': 'vcenter',
                                     'num_format': '0.00000000'})






    # 将df_content的内容写入通过Writer写入excel 中sheet名称为sheet_name的sheet页
    df.to_excel(excel_writer=writer, sheet_name='gpgga_data', columns=[2,4], index=False, header=False)
    # df1.to_excel(excel_writer=writer, sheet_name='gpgga_data', columns=[2,4], index=False, header=False)

    worksheet1 = writer.sheets['gpgga_data']
    # 向excel中写入数据，建立图标时要用到
    headings = ['N', 'E']
    # 写入表头
    worksheet1.write_row('A1', headings)


    # 生效单元格格式
    # 增加个表格说明
    # worksheet1.merge_range('A1:B1', u'场地基站测试数据', note_fmt)
    # 设置列宽
    worksheet1.set_column('A:B', 30, text_fmt)
    # # 有条件设定表格格式：金额列
    # worksheet1.conditional_format('B3:E%d' % l_end, {'type': 'cell', 'criteria': '>=', 'value': 1, 'format': amt_fmt})
    # # 有条件设定表格格式：百分比
    # worksheet1.conditional_format('E3:E%d' % l_end,
    #                               {'type': 'cell', 'criteria': '<=', 'value': 0.1, 'format': percent_fmt})
    # # 有条件设定表格格式：高亮百分比
    # worksheet1.conditional_format('E3:E%d' % l_end,
    #                               {'type': 'cell', 'criteria': '>', 'value': 0.1, 'format': highlight_fmt})
    # # 加边框
    # worksheet1.conditional_format('A1:E%d' % l_end, {'type': 'no_blanks', 'format': border_format})
    # # 设置日期格式
    # worksheet1.conditional_format('A3:A62', {'type': 'no_blanks', 'format': date_fmt})

    # 将写入的内容进行保存
    writer.save()


    # 此时df是字典呢
    df_sheet = pd.read_excel('t1.xlsx')  # 可以通过表单名同时指定多个
    print(type(df_sheet))
    # print(df)
    print(df_sheet)
    # print("===", df_sheet["N"]) # 行号


    # data1 = df.get_value(1,2)
    # print(data1)
    # data = df.values()  # 获取所有的数据，注意这里不能用head()方法哦~
    # print(type(data))




    # 需要将字典转换为DataFrame
    # d = pd.DataFrame()# 待完成
    # print(d.dtypes)






    x = np.arange(0., 5., 0.2)
    # 红色破折号, 蓝色方块 ，绿色三角块
    plt.plot(x, x, 'r--')
    # plt.show()





















# ==========================End============================
