#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Date: 2019/11/28
# @Author: Tigerots

# 系统模块引用
import os
import sys
# sys.path.append('/excel_pandas_matplotlib/main_winform')


import threading
# pyqt5 相关引用
import time

from PyQt5 import QtGui
from PyQt5.QtWidgets import QLabel, QFileDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
# 自定义模块引用
from matplotlib.ticker import FuncFormatter

import MainForm
import signal_emit
import stop_threading

import openpyxl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
# ==========================================================================




# 以下为生成图标函数定义 =====================================================
# 设置图表字体
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'
# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 坐标轴显示格式
def formatnum_x(x, pos):
    return '$%.8f$' % (x)

# X:Y 点线图
def plt_plot_table(x, y, color):
    plt.gca().yaxis.set_major_formatter(FuncFormatter(formatnum_x))
    plt.gca().xaxis.set_major_formatter(FuncFormatter(formatnum_x))

    plt.plot(x, y, '.', label='经纬度', color=color)
    plt.xlabel(u'纬度(度)')
    plt.ylabel(u'经度(度)')
    plt.title(u'基站信号稳定性测试数据')
    plt.legend(loc="best")
    plt.gcf().autofmt_xdate() # 自动旋转X轴标记
    plt.savefig('信号图.png',bbox_inches='tight',dpi=300) # 保存图片
    plt.show() # 如果不显示, 数据会重叠
    plt.close()

# Y:时间 点线图
def plt_plot_table_2(x, y, color):
    x = np.linspace(0, x, len(y))
    plt.plot(x, y, label='卫星数', color=color)
    plt.xlabel(u'时间(时)')
    plt.ylabel(u'卫星数(个)')
    plt.title(u"基站24小时搜星数据图")
    plt.legend(loc="best")
    plt.savefig('搜星图.png', bbox_inches='tight', dpi=300)
    plt.show()
    plt.close()
# ==========================================================================





# 以下为窗口应用 ============================================================
# 主窗口类
class MainLogic(QMainWindow, MainForm.Ui_MainWindow , signal_emit.SignalEmit):
    def __init__(self):
        QMainWindow.__init__(self)
        MainForm.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.txt_files_path = [] # 数据文件路径
        self.txt_files_name = [] # 数据文件名称列表

        # 禁止最大化, 禁止拉伸
        # self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.width(), self.height())

        # 图表 图例颜色
        L_List = ["黑色", "红色", "黄色", "蓝色", "绿色",]
        self.cbx_colour.addItems(L_List)
        # 图表 图例形状
        L_List = ["圆点", "三角", "短横线", ]
        self.cbx_sharp.addItems(L_List)

        # 状态栏
        self.status = self.statusBar()
        self.S_Sta = QLabel("  状态信息: 欢迎使用弗斯特调测软件")
        self.S_IP = QLabel("版本号:V1.0")
        self.S_Port = QLabel("内部使用")
        self.status.addPermanentWidget(self.S_Sta, stretch=7)
        self.status.addPermanentWidget(self.S_IP, stretch=2)
        self.status.addPermanentWidget(self.S_Port, stretch=1)

        # 初始化信号-槽
        self.connect()

    # 绑定信号与槽Signals & slots
    def connect(self):
        # 按键 btn
        self.btn_open_dir.clicked.connect(self.btn_open_dir_func)
        self.btn_creat_excel.clicked.connect(self.btn_creat_excel_func)
        self.btn_creat_plt.clicked.connect(self.btn_creat_plt_func)
        # # 列表框 combobox
        # self.cbx_iot_platform.currentTextChanged.connect(self.cbx_iot_platform_changed)
        # # 菜单栏
        # # self.File_Open.triggered.connect(self.openMsg)
        # # 复选框 checkBox
        # # self.checkBox_iot.toggled.connect(self.checkBox_iot_fun)
        # # 信号槽
        self.signal_write_msg.connect(self.write_msg_func)
        pass

    # 画图线程
    def thread_plt_func(self):
        msg = ("\r=== 启动生成图表流程 ===")
        self.signal_write_msg.emit(msg)  # 发送日志消息
        msg = ("正在读取data.txt数据, 请稍后...")
        self.signal_write_msg.emit(msg)  # 发送日志消息

        start = time.perf_counter()
        target_file = os.getcwd() + "\\" + "data.txt"
        df = pd.read_table(target_file, delimiter=",", header=None)
        elapsed = time.perf_counter() - start
        msg = ("操作完成, 用时: {}秒".format(elapsed))
        self.signal_write_msg.emit(msg)

        # 清除没用的列
        df.drop(df.columns[8:15], axis=1, inplace=True)
        df.drop(df.columns[[0, 1, 3, 5, 6]], axis=1, inplace=True)
        # 处理经纬度数据,(将度分转换为度)
        df[2] = (df[2]//100) + (df[2]%100)/60
        df[4] = (df[4]//100) + (df[4]%100)/60

        msg = ("将数据写入到data.csv文件, 该过程时间较长, 请耐心等待...")
        self.signal_write_msg.emit(msg)  # 发送日志消息
        start = time.perf_counter()
        df.to_csv("data.csv", float_format='%.10f')
        elapsed = time.perf_counter() - start
        msg = ("操作完成, 用时: {}秒".format(elapsed))
        self.signal_write_msg.emit(msg)

        msg = ("将数据写入到data.xlsx文件, 该过程时间较长, 请耐心等待...")
        self.signal_write_msg.emit(msg)  # 发送日志消息
        start = time.perf_counter()
        # 使用writer写Excel
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
                                        'num_format': '0.0000000000'})
        C_fmt = workbook.add_format({'bold': False,
                                     'font_name': u'微软雅黑',
                                     'align': 'center',
                                     'valign': 'vcenter'})

        df.to_excel(excel_writer=writer, sheet_name='gpgga_data', columns=[2, 4, 7], index=False, header=True)
        worksheet1 = writer.sheets['gpgga_data']
        # 向excel中写入数据，建立图标时要用到
        headings = ['纬度值', '经度值', '卫星数']
        # 写入表头
        worksheet1.write_row('A1', headings, note_fmt)
        # 设置列宽
        worksheet1.set_column('A:B', 30, text_fmt)
        worksheet1.set_column('C:C', 10, C_fmt)
        # 将写入的内容进行保存
        writer.save()

        elapsed = time.perf_counter() - start
        msg = ("操作完成, 用时: {}秒".format(elapsed))
        self.signal_write_msg.emit(msg)


        x = df[2]
        y = df[4]
        z = df[7]
        # 生成折线图并保存
        plt_plot_table(x, y, "blue")
        msg = ("正在绘制经纬度点线图, 请稍后...")
        self.signal_write_msg.emit(msg)  # 发送日志消息
        plt_plot_table_2(24, z, "red")
        msg = ("正在绘制搜星数点线图, 请稍后...")
        self.signal_write_msg.emit(msg)  # 发送日志消息
        msg = ("已生成图表并保存,请到文件目录查看!")
        self.signal_write_msg.emit(msg)  # 发送日志消息


    # 生成图标按键指令
    def btn_creat_plt_func(self):
        t = threading.Thread(target=self.thread_plt_func)
        t.setDaemon(True)# 守护, 主线程结束, 子线程就结束, 不等待
        t.start()# 启动
        pass

    # 读取TXT信息, 转存到Excel中
    def translate_to_excel_func(self):

        pass

    # 合并所有TXT文件到一个文件中
    def commit_all_txt_func(self):
        msg = ("\r=== 启动生成data.txt文件流程 ===")
        self.signal_write_msg.emit(msg)  # 发送日志消息
        # 生成合并文件的目标文件
        target_file = os.getcwd() + "\\" + "data.txt"
        with open(target_file, 'a+') as file_t:
            file_t.seek(0)
            file_t.truncate()  # 清空文件
            msg = ("创建并清空data.txt文件...")
            self.signal_write_msg.emit(msg)  # 发送日志消息
            # 遍历拷贝
            for i in self.txt_files_name:  # 遍历每一个文件
                source_file = self.txt_files_path + "\\" + i[0]
                msg = ("合并{}文件到data.txt, 请稍后...".format(i[0]))
                self.signal_write_msg.emit(msg)  # 发送日志消息
                with open(source_file, 'r') as file_s:
                    file_t.write(file_s.read())
        msg = ("\r=== 启动生成data.xlsx文件流程 ===")
        self.signal_write_msg.emit(msg)  # 发送日志消息
        pass

    # 创建Excel文件 按钮操作事件
    def btn_creat_excel_func(self):
        if len(self.txt_files_name) == 0: # 如果没有选择文件路径
            self.txt_files_path, self.txt_files_name = self.list_current_path_all_files(".txt")
        self.commit_all_txt_func() # 合并txt文件
        self.translate_to_excel_func() # 转换为Excel
        pass

    # 打开数据所在文件夹
    def btn_open_dir_func(self):
        directory1 = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")  # 起始路径
        self.lineEdit_dir.setText(directory1) # 填写路径
        msg = ("\r=== 选择数据目录为: ===\r"+ directory1)
        self.signal_write_msg.emit(msg)# 发送日志消息
        self.txt_files_path, self.txt_files_name = self.list_path_all_files(directory1, ".txt")
        pass

    # 列出当前目录data文件夹下的txt文件名称
    def list_current_path_all_files(self, filetype):
        # 列出目录下所有文件,
        # TODO 如果当前目录没有data文件夹或data目录下没有数据文件, 待处理
        filedir = os.getcwd() + '\\data'  # 如果未选择文件,从当前目录查找
        dirs = os.listdir(filedir)
        all_txt_flies = []
        # 筛选txt文件s
        msg = ("\r=== 该目录包含如下数据文件: ===")
        self.signal_write_msg.emit(msg)  # 发送日志消息
        for file_name in dirs:
            if os.path.splitext(file_name)[1] == filetype:
                msg = file_name
                self.signal_write_msg.emit(msg)  # 发送日志消息
                all_txt_flies.append(list([file_name]))
        if len(all_txt_flies) == 0:
            msg = ("没有找到数据文件(.txt格式), 请确认...")
            self.signal_write_msg.emit(msg)  # 发送日志消息
        return filedir, all_txt_flies  # 返回文件名

    # 列出指定文件夹内所有指定类型文件
    def list_path_all_files(self, path, filetype):
        # 列出目录下所有文件
        dirs = os.listdir(path)
        all_txt_flies = []
        # 筛选txt文件s
        msg = ("\r=== 该目录包含如下数据文件: ===")
        self.signal_write_msg.emit(msg)# 发送日志消息

        for file_name in dirs:
            if os.path.splitext(file_name)[1] == filetype:
                msg = file_name
                self.signal_write_msg.emit(msg)# 发送日志消息
                all_txt_flies.append(list([file_name]))
        if len(all_txt_flies) == 0:
            msg = ("没有找到数据文件(.txt格式), 请确认...")
            self.signal_write_msg.emit(msg)  # 发送日志消息
        return path, all_txt_flies# 返回路径+文件名


    # 写消息日志
    def write_msg_func(self, msg):
        self.textEdit_msg.append(msg)
        # 滚动条移动到结尾
        self.textEdit_msg.moveCursor(QtGui.QTextCursor.End)










if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWin = MainLogic()
    MainWin.show()
    sys.exit(app.exec_())







# ==========================End============================
