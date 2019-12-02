#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Date: 2019/11/26
# @Author: Tigerots



import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def read_tableMethod(filename):
    '''用read_table方法读取TXT文件'''
    data = pd.read_table(filename, header=None, delimiter=",")
    return  data


if __name__ == '__main__':
    data = read_tableMethod('t1.txt')
    print(data)






















# ==========================End============================
