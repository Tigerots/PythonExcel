# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 781, 301))
        self.groupBox.setObjectName("groupBox")
        self.textEdit_msg = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_msg.setGeometry(QtCore.QRect(10, 20, 501, 271))
        self.textEdit_msg.setObjectName("textEdit_msg")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(520, 10, 261, 281))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setGeometry(QtCore.QRect(20, 20, 221, 241))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 310, 781, 241))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 741, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_dir = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_dir.setObjectName("lineEdit_dir")
        self.horizontalLayout.addWidget(self.lineEdit_dir)
        self.btn_open_dir = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_open_dir.setObjectName("btn_open_dir")
        self.horizontalLayout.addWidget(self.btn_open_dir)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(290, 60, 481, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 74, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setEnabled(False)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setEnabled(False)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setEnabled(False)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_5.setEnabled(False)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(90, 20, 181, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.cbx_colour = QtWidgets.QComboBox(self.formLayoutWidget)
        self.cbx_colour.setObjectName("cbx_colour")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cbx_colour)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_plt_x = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_plt_x.setObjectName("lineEdit_plt_x")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_plt_x)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_plt_y = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_plt_y.setObjectName("lineEdit_plt_y")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_plt_y)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_plt_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_plt_name.setObjectName("lineEdit_plt_name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_plt_name)
        self.cbx_sharp = QtWidgets.QComboBox(self.formLayoutWidget)
        self.cbx_sharp.setObjectName("cbx_sharp")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cbx_sharp)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_3)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(280, 20, 191, 88))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_img_name = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_img_name.setObjectName("lineEdit_img_name")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_img_name)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_10.setEnabled(False)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.btn_creat_plt = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_creat_plt.setGeometry(QtCore.QRect(280, 120, 191, 41))
        self.btn_creat_plt.setObjectName("btn_creat_plt")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 60, 271, 171))
        self.groupBox_4.setObjectName("groupBox_4")
        self.btn_creat_excel = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_creat_excel.setGeometry(QtCore.QRect(10, 120, 251, 41))
        self.btn_creat_excel.setObjectName("btn_creat_excel")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_4)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 251, 88))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_excel_name = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_excel_name.setObjectName("lineEdit_excel_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_excel_name)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_sheet_name = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_sheet_name.setObjectName("lineEdit_sheet_name")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_sheet_name)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menug = QtWidgets.QMenu(self.menubar)
        self.menug.setObjectName("menug")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menug.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基站稳定性测试"))
        self.groupBox.setTitle(_translate("MainWindow", "消息"))
        self.groupBox_5.setTitle(_translate("MainWindow", "操作说明"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>1. 用串口助手采集GPS模块返回的GPGGA数据,默认以文本格式保存,可以分包保存</p><p>2. 选择数据文件所在文件夹,软件会自动对文件进行合并</p><p>3. 生成的data.txt文件,该文件为原始数据,未经过处理</p><p>4. 生成的data.csv和data.xlsx文件为处理过的文件,将度分格式转为度格式</p><p>5. 生成图表,默认使用散点图,由于数据量大,执行过程较慢,请耐心等待</p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "工具栏"))
        self.btn_open_dir.setText(_translate("MainWindow", "打开文数据目录"))
        self.groupBox_3.setTitle(_translate("MainWindow", "步骤二: 生成图表"))
        self.checkBox_2.setText(_translate("MainWindow", "点线图"))
        self.checkBox.setText(_translate("MainWindow", "散点图"))
        self.checkBox_3.setText(_translate("MainWindow", "柱状图"))
        self.checkBox_4.setText(_translate("MainWindow", "饼形图"))
        self.checkBox_5.setText(_translate("MainWindow", "三维图"))
        self.label_2.setText(_translate("MainWindow", "图形颜色"))
        self.label_3.setText(_translate("MainWindow", "横坐标名称"))
        self.lineEdit_plt_x.setText(_translate("MainWindow", "纬度值"))
        self.label_4.setText(_translate("MainWindow", "纵坐标名称"))
        self.lineEdit_plt_y.setText(_translate("MainWindow", "经度值"))
        self.label_5.setText(_translate("MainWindow", "图表名称"))
        self.lineEdit_plt_name.setText(_translate("MainWindow", "经纬度数据表"))
        self.label_6.setText(_translate("MainWindow", "数据点形状"))
        self.label_10.setText(_translate("MainWindow", "图片名称"))
        self.lineEdit_img_name.setText(_translate("MainWindow", "经纬度数据表"))
        self.label_11.setText(_translate("MainWindow", "图片格式"))
        self.lineEdit_9.setText(_translate("MainWindow", "*.png"))
        self.label_12.setText(_translate("MainWindow", "保存路径"))
        self.lineEdit_10.setText(_translate("MainWindow", "默认当前文件夹"))
        self.btn_creat_plt.setText(_translate("MainWindow", "生成数据图表"))
        self.groupBox_4.setTitle(_translate("MainWindow", "步骤一: 生成Excel文件"))
        self.btn_creat_excel.setText(_translate("MainWindow", "生成Excel文件"))
        self.label_9.setText(_translate("MainWindow", "保存Excel文件名"))
        self.lineEdit_excel_name.setText(_translate("MainWindow", "经纬度数据表"))
        self.label_7.setText(_translate("MainWindow", "数据Sheet表名"))
        self.lineEdit_sheet_name.setText(_translate("MainWindow", "gpgga_data"))
        self.label_8.setText(_translate("MainWindow", "保存路径"))
        self.lineEdit_6.setText(_translate("MainWindow", "默认当前文件夹"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.menug.setTitle(_translate("MainWindow", "关于"))
