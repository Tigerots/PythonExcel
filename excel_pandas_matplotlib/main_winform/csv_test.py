#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Date: 2019/11/30
# @Author: Tigerots




import csv
import pandas as pd

from readtxt_writexls import read_tableMethod


def csv_test():
    with open('data.csv', 'w') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})



def excel_test():
    df = read_tableMethod('data.txt')

    writer = pd.ExcelWriter("data.xlsx")
    workbook = writer.book
    # 标题文本格式
    note_fmt = workbook.add_format({'bold': True,
                                    'font_name': u'微软雅黑',
                                    'font_color': 'blue',
                                    'align': 'center',
                                    'valign': 'vcenter'})
    # 文本格式
    text_fmt = workbook.add_format({'bold': False,
                                    'font_name': u'微软雅黑',
                                    'font_color': 'black',
                                    'align': 'center',
                                    'valign': 'vcenter',
                                    'num_format': '0.00000000'})
    df.to_excel(excel_writer=writer, sheet_name='gpgga_data', columns=[2, 4], index=False, header=False)
    worksheet1 = writer.sheets['gpgga_data']
    # 向excel中写入数据，建立图标时要用到
    headings = ['纬度值', '经度值','卫星数']
    # 写入表头
    worksheet1.write_row('A1', headings)
    # 设置列宽
    worksheet1.set_column('A:B', 30, text_fmt)
    # 将写入的内容进行保存
    writer.save()

if __name__ == '__main__':
    excel_test()



# ==========================End============================
