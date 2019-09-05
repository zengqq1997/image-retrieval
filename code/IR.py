# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ZQQ\Desktop\advanced\study\computervision\classtest\image-retrieval\ui\IR.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtWidgets import  QWidget
from PyQt5.QtGui import QPalette,QPixmap,QBrush
import query_online
from PyQt5.QtWidgets import QFileDialog
import matplotlib.image as mpimg
import argparse
import numpy as np
import pachong
from PIL import Image
import index
import sys

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1328, 966)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 1291, 161))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.searchButton = QtWidgets.QToolButton(self.groupBox)
        self.searchButton.setGeometry(QtCore.QRect(960, 60, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.search_text = QtWidgets.QLabel(self.groupBox)
        self.search_text.setGeometry(QtCore.QRect(140, 70, 251, 51))
        self.search_text.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("华文彩云")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.search_text.setFont(font)
        self.search_text.setMouseTracking(True)
        self.search_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.search_text.setObjectName("search_text")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(440, 60, 471, 61))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 170, 1301, 631))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(15)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setMouseTracking(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea.setGeometry(QtCore.QRect(10, 30, 1281, 581))
        self.scrollArea.setMouseTracking(True)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1258, 579))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(0, -1, 1280, 10001))
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setObjectName("listWidget")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 810, 1301, 111))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(15)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.labelnum = QtWidgets.QLabel(self.groupBox_3)
        self.labelnum.setGeometry(QtCore.QRect(140, 40, 131, 51))
        font = QtGui.QFont()
        font.setFamily("华文彩云")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelnum.setFont(font)
        self.labelnum.setObjectName("labelnum")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(270, 40, 131, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(510, 40, 121, 51))
        font = QtGui.QFont()
        font.setFamily("华文彩云")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(670, 30, 131, 61))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(1150, 70, 151, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(970, 30, 151, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1328, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 爬虫数量框
        self.lineEdit.setFocus()
        self.lineEdit.returnPressed.connect(self.pachong)  # 信号绑定到槽
        # 绑定事件
        self.searchButton.clicked.connect(self.suoluetu)
        self.pushButton.clicked.connect(self.created)
        self.pushButton_2.clicked.connect(self.exited)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "以图搜图系统"))
        self.groupBox.setTitle(_translate("MainWindow", "图图搜索"))
        self.searchButton.setText(_translate("MainWindow", "搜索"))
        self.search_text.setText(_translate("MainWindow", "选择你想知道的图片："))
        self.groupBox_2.setTitle(_translate("MainWindow", "显示结果"))
        self.groupBox_3.setTitle(_translate("MainWindow", "图图搜索幕后"))
        self.labelnum.setText(_translate("MainWindow", "图片数量："))
        self.label_2.setText(_translate("MainWindow", "生成图库："))
        self.pushButton.setText(_translate("MainWindow", "创   建"))
        self.label_3.setText(_translate("MainWindow", "Designe by ZQQ"))
        self.pushButton_2.setText(_translate("MainWindow", "退出"))


    def pachong(self):
        num=self.lineEdit.text()
        print (int(num))
        QtWidgets.QMessageBox.information(self, '提示', '正在前往百度下载原图\n期间出现软件未响应属于正常现象')
        pachong.pachong(int(num))
        QtWidgets.QMessageBox.information(self, '提示', '下载完毕，可以开始建立图库')
    def created(self):
        QtWidgets.QMessageBox.information(self, '提示', '你即将开始创建一个本地图库\n这可能会使用你大量的内存空间和时间请耐心等待')
        index.index()
        QtWidgets.QMessageBox.information(self, '提示', '恭喜你，图库建立完成\n请您开始使用图图搜索模块')
    def exited(self):
        reply = QtWidgets.QMessageBox.question(self, '信息', '确认退出吗？',
                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            sys.exit(0)
        else:
            self.close()



    def suoluetu(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self, "选取文件",
                                                          "C:/Users/ZQQ/Desktop/advanced/study/computervision/classtest/image-retrieval/test",
                                                          "All Files (*)")  # 设置文件扩展名过滤,注意用双分号间隔
        print(fileName1, filetype)
        self.label.setText(fileName1)
        names, args, rank_score = query_online.query_online(fileName1)
        na1 = []
        for i in range(len(names)):
            na1.append(names[i].decode())
        # 已经将数据传送过来，现在需要将文件名提取出来
        img_names = []
        positions = [(i, j) for i in range(4) for j in range(30)]
        for i in range(len(na1)):
            img_names.append(
                "C:/Users/ZQQ/Desktop/advanced/study/computervision/classtest/image-retrieval/img" + "/" +
                na1[i])
        self.listWidget = QWidget()
        self.listWidget.setMinimumSize(1280, 9500)
        self.label.setText('你找那张图片的名字应该是叫做'+str(na1[0]).split('_')[0])
        for position, name, nam, score in zip(positions, img_names, na1, rank_score):
            lab = QtWidgets.QLabel(self.listWidget)
            lab.setFixedSize(1080, 600)
            # out=im.resize((500,500),Image.ANTIALIAS)
            # out.save(os.path.join(name,os.path.basename(name)))
            nam1 = str(nam).split('_')[0]
            pix = QtGui.QPixmap(name)
            lab.setPixmap(pix)
            lab.setToolTip('这是' + nam1 + '，他和搜索的图片相似度' + str((np.round(score * 100))) + '%')
            # lab.setText("<a href='www.baidu.com'></a>")
            # lab.setOpenExternalLinks(True)
            lab.setScaledContents(True)
            print (position)
            lab.move(1080 * position[0] + 100, 630 * position[1] + 10)  
        self.scrollArea.setWidget(self.listWidget)
