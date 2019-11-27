#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Date: 2019/11/26
# @Author: Tigerots

import glob
import os



path1 = "..\\excel_pandas_matplotlib\\data"


def list_path_allfile(path, filetype):
    # 列出目录下所有文件
    dirs = os.listdir(path)
    print(dirs)
    # 筛选txt文件
    for i in dirs:
        if os.path.splitext(i)[1] == filetype:
            print(i)




def read_writeFile(path, f):
    cate = [path + '/' + x for x in os.listdir(path)]
    f2 = open(f, 'a+')
    for idx, folder in enumerate(cate):
        for im in glob.glob(folder + '/*.jpg.txt'):
            f1 = open(im, 'r')
            for eachLine in f1:
                f2.write(eachLine)
                f2.write(' ' + str(idx + 1) + '\n')
            f1.close()

if __name__ == '__main__':
    list_path_allfile(path1, ".txt")
    # read_writeFile(path, f)
    pass

# ==========================End============================
