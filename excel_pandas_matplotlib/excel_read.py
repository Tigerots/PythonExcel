#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Date: 2019/11/26
# @Author: Tigerots



'''
读取csv：pandas.read_csv
读取txt：pandas.read_table
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import string
import math
import platform



# df=pd.read_excel('1.xlsx')#这个会直接默认读取到这个Excel的第一个表单
# data=df.head()#默认读取前5行的数据
# print("获取到所有的值:\n{0}".format(data))#格式化输出


# #方法二：通过指定表单名的方式来读取
# df=pd.read_excel('1.xlsx',sheet_name='gpgga')#可以通过sheet_name来指定读取的表单
# data=df.head()#默认读取前5行的数据
# print("获取到所有的值:\n{0}".format(data))#格式化输出


#方法三：通过表单索引来指定要访问的表单，0表示第一个表单
#也可以采用表单名和索引的双重方式来定位表单
#也可以同时定位多个表单，方式都罗列如下所示
df=pd.read_excel('1.xlsx',sheet_name=['gpgga', 1])#可以通过表单名同时指定多个
data=df.values()#获取所有的数据，注意这里不能用head()方法哦~
# data=df._ixs(1,2).values()#读取指定多行的话，就要在ix[]里面嵌套列表指定行数

print("获取到所有的值:\n{0}".format(data))#格式化输出

data2 = df.get_values()
print("获取到所有的值:\n{0}".format(data2))#格式化输出
































# ==========================End============================
