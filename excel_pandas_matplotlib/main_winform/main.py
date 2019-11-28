#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Date: 2019/11/28
# @Author: Tigerots

# 系统模块引用
import sys
# pyqt5 相关引用
from PyQt5 import QtGui
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
# 自定义模块引用
from excel_pandas_matplotlib.main_winform import MainForm
from excel_pandas_matplotlib.main_winform import signal_emit
from excel_pandas_matplotlib.main_winform import stop_threading


# MQTT 测试工具 主窗口类
class MainLogic(QMainWindow, MainForm.Ui_MainWindow , signal_emit.SignalEmit):
    def __init__(self):
        QMainWindow.__init__(self)
        MainForm.Ui_MainWindow.__init__(self)
        self.setupUi(self)

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

    # 绑定pushButton和comboBox信号与槽Signals & slots
    def connect(self):
        # # 按键 btn
        # self.btn_connect_cloud.clicked.connect(self.btn_connect_cloud_func)
        # self.btn_disconnect_cloud.clicked.connect(self.btn_disconnect_cloud_func)
        # self.btn_creat_3info.clicked.connect(self.btn_creat_3info_func)
        # # 列表框 combobox
        # self.cbx_iot_platform.currentTextChanged.connect(self.cbx_iot_platform_changed)
        # # 菜单栏
        # # self.File_Open.triggered.connect(self.openMsg)
        # # 复选框 checkBox
        # # self.checkBox_iot.toggled.connect(self.checkBox_iot_fun)
        # # 清空按键
        # # self.cbtn_clr.clicked.connect(self.cbtn_clr_recv_func)
        # # 信号槽
        # self.signal_write_msg.connect(self.write_msg)
        # self.signal_list_ip.connect(self.change_list)
        pass













if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWin = MainLogic()
    MainWin.show()
    sys.exit(app.exec_())







# ==========================End============================
