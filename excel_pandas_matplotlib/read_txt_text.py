#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Date: 2019/11/28
# @Author: Tigerots


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import time


# 设置图表字体
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'
# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# 点线图
def plt_plot_table(x, y, color):
    plt.plot(x, y, '*', label='Data', color=color)
    plt.xlabel(u'经度')
    plt.ylabel(u'纬度')
    plt.title(u'基站信号稳定性测试数据')
    plt.legend(loc="best")
    # plt.savefig('pic.png',bbox_inches='tight',dpi=300) # 保存图片
    plt.show()

# 散点图
def plt_scatter_table(x, y, color):
    # plt.figure(figsize=(8, 5))
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('data')
    # plt.axis('auto')
    # plt.axis([3816.411, 3816.412, 11652.233, 11652.234])  # 设置横纵坐标轴范围，这个在子图中被分解为下面两个函数
    # ax1.set_xlim(-5, 5)  # 设置横轴范围，会覆盖上面的横坐标,plt.xlim
    # ax1.set_ylim(-10, 10)  # 设置纵轴范围，会覆盖上面的纵坐标,plt.ylim

    plt.scatter(x, y, c=color, marker='o',alpha=0.5,edgecolors= 'white')
    # plt.savefig('pic.png',bbox_inches='tight',dpi=300) # 保存图片
    plt.show()



# ============================================================
# 使用Excel方式读取数据, 读取速度太慢, 大数据量不建议选择
start = time.perf_counter()
df = pd.read_excel('data.xlsx')
x = df["N"]
y = df["E"]

# 散点图, 效果不好, 暂时不使用
# plt_scatter_table(x,y,'y')
plt_plot_table(x,y,"green")

elapsed = time.perf_counter() - start
print("excel Time used:",elapsed)



# ============================================================
# 使用numpy, 读取txt文件, 速度远快于Excel, 可以选择
start = time.perf_counter()
x, y, z = np.loadtxt('data.txt', delimiter=' ', unpack=True)
# print(x)
# print(y)
# print(z)
# 生成图表
plt_plot_table(x,y,"red")
elapsed = (time.perf_counter() - start)
print("plt Time used:",elapsed)



# ============================================================
# 使用pandas, 读取txt文件, 速度最快, 推荐选择
start = time.perf_counter()
data = pd.read_table('data.txt', delimiter=" ", header=None)
x = data[0]
y = data[1]
z = data[2]
# print(x)
# print(y)
# print(z)
# 生成图表
plt_plot_table(x,y,"blue")
elapsed = (time.perf_counter() - start)
print("plt Time used:",elapsed)


# ==========================End============================
