#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Date: 2019/11/26
# @Author: Tigerots


import xlsxwriter
import pandas as pd

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
    # df = df.append(df1, ignore_index=True)
    # 创建Excel的ExcelWriter对象
    writer = pd.ExcelWriter("t1.xlsx")
    # 将df_content的内容写入通过Writer写入excel 中sheet名称为sheet_name的sheet页
    df.to_excel(excel_writer=writer, sheet_name='gpgga_data', columns=[2,4], index=False, header=False)
    df1.to_excel(excel_writer=writer, sheet_name='gpgga_data', columns=[2,4], index=False, header=False)
    # 将写入的内容进行保存
    writer.save()























# ==========================End============================
