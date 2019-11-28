#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Date: 2019/11/28
# @Author: Tigerots

# 系统模块引用
import os
import shutil
import sys
# pyqt5 相关引用
from PyQt5 import QtGui
from PyQt5.QtWidgets import QLabel, QFileDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
# 自定义模块引用
from excel_pandas_matplotlib.main_winform import MainForm
from excel_pandas_matplotlib.main_winform import signal_emit
from excel_pandas_matplotlib.main_winform import stop_threading

# ==========================================================================







# ==========================================================================






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
        # # 列表框 combobox
        # self.cbx_iot_platform.currentTextChanged.connect(self.cbx_iot_platform_changed)
        # # 菜单栏
        # # self.File_Open.triggered.connect(self.openMsg)
        # # 复选框 checkBox
        # # self.checkBox_iot.toggled.connect(self.checkBox_iot_fun)
        # # 信号槽
        self.signal_write_msg.connect(self.write_msg_func)
        pass

    # 合并所有TXT文件到一个文件中
    def commit_all_txt_func(self):
        pass

    def btn_creat_excel_func(self):
        if len(self.txt_files_name) == 0:
            self.txt_files_path, self.txt_files_name = self.list_current_path_all_files(".txt")

        msg = ("\r=== 启动生成data.txt文件流程 ===")
        self.signal_write_msg.emit(msg)  # 发送日志消息

        # 生成合并文件的目标文件
        target_file = os.getcwd() + "\\" + "data.txt"
        with open(target_file, 'a+') as file_t:
            file_t.seek(0)
            file_t.truncate()# 清空文件
            msg = ("创建并清空data.txt文件...")
            self.signal_write_msg.emit(msg)  # 发送日志消息
            # 遍历拷贝
            for i in self.txt_files_name: # 遍历每一个文件
                source_file = self.txt_files_path + "\\" + i[0]
                msg = ("合并{}文件到data.txt, 请稍后...".format(i[0]))
                self.signal_write_msg.emit(msg)  # 发送日志消息
                with open(source_file, 'r') as file_s:
                    file_t.write(file_s.read() + "\n")
        msg = ("\r=== 启动生成data.xlsx文件流程 ===")
        self.signal_write_msg.emit(msg)  # 发送日志消息

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
        # 列出目录下所有文件
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
