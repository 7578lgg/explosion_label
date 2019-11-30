# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'label_demo_v3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from glob import glob
from PyQt5.QtGui import *

import os
import numpy as np


class Ui_mainWindow(object):
    def __init__(self):
        self.open_first = 0
        self.alreadylabel = 0
        self.alreadysave = 0

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1041, 791)
        mainWindow.setStyleSheet("QGroupBox{border:none;}")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.group_box_all = QtWidgets.QGroupBox(self.centralwidget)
        self.group_box_all.setTitle("")
        self.group_box_all.setObjectName("group_box_all")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.group_box_all)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.group_box_all)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_open = QtWidgets.QPushButton(self.groupBox)
        self.btn_open.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btn_open.setObjectName("btn_open")
        self.horizontalLayout_6.addWidget(self.btn_open)
        spacerItem = QtWidgets.QSpacerItem(685, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.source_imageView = QtWidgets.QLabel(self.groupBox)
        self.source_imageView.setMinimumSize(QtCore.QSize(600, 400))
        self.source_imageView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.source_imageView.setAlignment(QtCore.Qt.AlignCenter)
        self.source_imageView.setObjectName("source_imageView")
        self.horizontalLayout_3.addWidget(self.source_imageView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_explode = QtWidgets.QPushButton(self.groupBox)
        self.btn_explode.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btn_explode.setObjectName("btn_explode")
        self.horizontalLayout.addWidget(self.btn_explode)
        self.btn_safe = QtWidgets.QPushButton(self.groupBox)
        self.btn_safe.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btn_safe.setObjectName("btn_safe")
        self.horizontalLayout.addWidget(self.btn_safe)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_pre = QtWidgets.QPushButton(self.groupBox)
        self.btn_pre.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btn_pre.setObjectName("btn_pre")
        self.horizontalLayout_5.addWidget(self.btn_pre)
        self.btn_relabel = QtWidgets.QPushButton(self.groupBox)
        self.btn_relabel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btn_relabel.setObjectName("btn_relabel")
        self.horizontalLayout_5.addWidget(self.btn_relabel)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_next = QtWidgets.QPushButton(self.groupBox)
        self.btn_next.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btn_next.setObjectName("btn_next")
        self.horizontalLayout_2.addWidget(self.btn_next)
        self.btn_save = QtWidgets.QPushButton(self.groupBox)
        self.btn_save.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_2.addWidget(self.btn_save)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 9)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3.setStretch(0, 11)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 13)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.gridLayout.addWidget(self.group_box_all, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        self.btn_open.clicked.connect(self.on_btn_open_clicked)
        self.btn_safe.clicked.connect(self.on_btn_safe_clicked)
        self.btn_explode.clicked.connect(self.on_btn_explode_clicked)
        self.btn_pre.clicked.connect(self.on_btn_pre_clicked)
        self.btn_relabel.clicked.connect(self.on_btn_relabel_clicked)
        self.btn_next.clicked.connect(self.on_btn_next_clicked)
        self.btn_save.clicked.connect(self.on_btn_save_clicked)



    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.label.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">请不要考虑字幕等文字内容，只需认真观察图像中有无火焰、浓烟、枪击或其他燃烧、爆炸现象发生，并进行标注，谢谢！</span></p></body></html>"))
        self.btn_open.setText(_translate("mainWindow", "浏览并选择文件夹"))
        self.source_imageView.setText(_translate("mainWindow", "显示当前图像"))
        self.btn_safe.setText(_translate("mainWindow", "【默认】标记为0:无爆炸"))
        self.btn_explode.setText(_translate("mainWindow", "标记为1:有爆炸"))
        self.btn_pre.setText(_translate("mainWindow", "返回上一张"))
        self.btn_relabel.setText(_translate("mainWindow", "重新标注当前图像"))
        self.btn_next.setText(_translate("mainWindow", "确认并显示下一张"))
        self.btn_save.setText(_translate("mainWindow", "保存已标注结果到文件"))
        self.textEdit.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">提示信息</p></body></html>"))

    # @pyqtSlot(bool)
    def on_btn_open_clicked(self, checked):
        if self.open_first == 1:
            self.textEdit.setPlainText("将重新选择图像文件夹!")

        # print("进入槽函数")
        current_dir = os.getcwd()
        # print("Current root dir: ", current_dir)
        quary_dir = QFileDialog.getExistingDirectory(self.centralwidget, "浏览并选择图像文件夹", current_dir)
        # print("Current frame dir: ", quary_dir)
        

        if quary_dir:
            self.open_first = 1

            if '\\' in quary_dir:
                self.quary_dir_name = quary_dir.strip().split('\\')[-1]
            elif '/' in quary_dir:
                self.quary_dir_name = quary_dir.strip().split('/')[-1]
            # print("Name of quary_dir: ",self.quary_dir_name)

            #cur_frames_path = os.path.join(current_dir, self.quary_dir_name)
            cur_frames_path = quary_dir

            self.frame_path_list = sorted(glob(os.path.join(cur_frames_path, '*.jpg')))
            # print(self.frame_path_list)
            self.frame_name_list = []
            for frame_path in self.frame_path_list:
                self.frame_name_list.append(os.path.split(frame_path)[1])
            # print(self.frame_name_list)

            self.textEdit.setPlainText("已选择图像帧文件夹: " + self.quary_dir_name)
            self.textEdit.append("图像帧数量: " + str(len(self.frame_name_list)))

            if len(self.frame_path_list) == 0:
                self.textEdit.append("此文件夹下没有图像，请重新选择文件夹！")
                self.open_first = 0

            else:
                self.label_result = np.zeros((len(self.frame_name_list),2), dtype=int)
                self.cur_frame_index = 0
                self.alreadysave = 0

                if os.path.exists(self.quary_dir_name + ".txt"):
                    self.textEdit.append("已存在对此文件夹下图像的部分标注，将加载并继续标注剩余图像！")
                    read_exist_file = open(self.quary_dir_name + ".txt")
                    for line in read_exist_file:
                        if 'vid' in line:
                            self.cur_frame_index += 1
                    self.textEdit.append("将从此图像继续标注：" + str(self.frame_name_list[self.cur_frame_index]))
                else:
                    self.textEdit.append("未标注过此文件夹，将从第一张图像开始标注")
                    
                self.continue_index = self.cur_frame_index
                self.open_file = open(self.quary_dir_name + '.txt', 'a+')

                self.textEdit.append("标注结果将被保存到: " + self.quary_dir_name + ".txt")
                self.textEdit.moveCursor(QTextCursor.End)
                
                cur_frame_path = self.frame_path_list[self.cur_frame_index]
                # print(cur_frame_path)

                image = QImage(cur_frame_path)
                # jpg = QtGui.QPixmap(image).scaled(self.source_imageView.width(), self.source_imageView.height())
                jpg = QtGui.QPixmap(image)
                self.source_imageView.setPixmap(jpg)

                self.textEdit.append("当前图像: " + str(self.frame_name_list[self.cur_frame_index]))
                self.textEdit.moveCursor(QTextCursor.End)


                
                self.textEdit.moveCursor(QTextCursor.End)
                # print("FileName\tLabel", file=self.open_file)
                self.alreadylabel = 0
                self.cur_frame_label = 0

    # @pyqtSlot(bool)
    def on_btn_explode_clicked(self, checked):

        if self.open_first == 1:
            self.cur_frame_label = 1
            self.textEdit.append("即将把当前图像标注为: " + str(self.cur_frame_label))
            self.textEdit.moveCursor(QTextCursor.End)
            self.alreadylabel = 1
        else:
            self.textEdit.setPlainText("请首先选择图像文件夹！")
            self.textEdit.moveCursor(QTextCursor.End)

    # @pyqtSlot(bool)
    def on_btn_safe_clicked(self, checked):

        if self.open_first == 1:
            self.cur_frame_label = 0
            self.textEdit.append("即将把当前图像标注为: " + str(self.cur_frame_label))
            self.textEdit.moveCursor(QTextCursor.End)
            self.alreadylabel = 1
        else:
            self.textEdit.setPlainText("请首先选择图像文件夹！")
            self.textEdit.moveCursor(QTextCursor.End)

    # @pyqtSlot(bool)
    def on_btn_relabel_clicked(self, checked):

        if self.open_first == 1:
            self.cur_frame_label = 0
            self.textEdit.append("已将当前图像标签重置为默认值: " + str(self.cur_frame_label))
            self.textEdit.moveCursor(QTextCursor.End)
            self.alreadylabel = 0
        else:
            self.textEdit.setPlainText("请首先选择图像文件夹！")
            self.textEdit.moveCursor(QTextCursor.End)

    # @pyqtSlot(bool)
    def on_btn_pre_clicked(self, checked):
        if self.open_first == 0:
            self.textEdit.setPlainText("请首先选择图像文件夹！")
            self.textEdit.moveCursor(QTextCursor.End)
        else:
            if self.cur_frame_index < 1:
                self.textEdit.append("当前图像是文件夹中第一张图像，无上一张图像！")
                self.textEdit.moveCursor(QTextCursor.End)
            else:
                self.cur_frame_index -= 1
                cur_frame_path = self.frame_path_list[self.cur_frame_index]
                image = QImage(cur_frame_path)
                jpg = QtGui.QPixmap(image)
                self.source_imageView.setPixmap(jpg)
                self.textEdit.append("已回退至图像: " + str(self.frame_name_list[self.cur_frame_index]))
                self.textEdit.append("请重新对图像进行标注！")
            self.textEdit.moveCursor(QTextCursor.End)

    # @pyqtSlot(bool)
    def on_btn_next_clicked(self, checked):
        if self.open_first == 0:
            self.textEdit.setPlainText("请首先选择图像文件夹！")
            self.textEdit.moveCursor(QTextCursor.End)
        else:
            if self.alreadylabel == 1:
                self.label_result[self.cur_frame_index, 0] = self.cur_frame_index + 1
                self.label_result[self.cur_frame_index, 1] = self.cur_frame_label
                # print("%s\t%d" % (self.frame_name_list[self.cur_frame_index], self.cur_frame_label), file=self.open_file)
                self.textEdit.append("已将当前图像标注结果保存到内存")
            else:
                self.textEdit.append("默认将当前图像标记为0：无爆炸")
                self.label_result[self.cur_frame_index, 0] = self.cur_frame_index + 1
                self.label_result[self.cur_frame_index, 1] = self.cur_frame_label
                # print("%s\t%d" % (self.frame_name_list[self.cur_frame_index], self.cur_frame_label), file=self.open_file)
                self.textEdit.append("已将当前图像标注结果保存到内存")

            self.textEdit.moveCursor(QTextCursor.End)
            self.alreadylabel = 0
            self.cur_frame_index += 1
            self.cur_frame_label = 0

            if self.cur_frame_index < len(self.frame_name_list):
                cur_frame_path = self.frame_path_list[self.cur_frame_index]
                image = QImage(cur_frame_path)
                jpg = QtGui.QPixmap(image)
                self.source_imageView.setPixmap(jpg)
                self.textEdit.append("当前图像: " + str(self.frame_name_list[self.cur_frame_index]))
            else:
                for i in range(self.continue_index, len(self.frame_name_list)):
                    print("%s\t%d" % (self.frame_name_list[i], self.label_result[i,1]), file=self.open_file)
                
                self.open_file.close()
                self.textEdit.setPlainText("已完成当前文件夹内所有图像帧的标注并写入文件，\n请选择下一个未标注的文件夹，谢谢！")
            self.textEdit.moveCursor(QTextCursor.End)
    
    # @pyqtSlot(bool)
    def on_btn_save_clicked(self, clicked):
        if (self.open_first == 1 and self.alreadylabel == 0):
            self.textEdit.setPlainText("即将保存，请为当前显示的图像打好标签后，再点击保存!")
        elif (self.open_first == 1 and self.alreadysave == 1):
            self.textEdit.setPlainText("您已经保存此文件夹标注记录，请不要重复点击保存按钮")        
        elif self.open_first == 0:
            self.textEdit.setPlainText("请首先选择图像文件夹！")
        else:
            self.textEdit.setPlainText("当前已经标注完成：" + str(self.frame_name_list[self.cur_frame_index]))
            self.textEdit.append("当前已经标注完成：" + str(self.frame_name_list[self.cur_frame_index]))
            for i in range(self.continue_index, self.cur_frame_index + 1):
                print("%s\t%d" % (self.frame_name_list[i], self.label_result[i,1]), file=self.open_file)
            self.open_file.close()
            self.open_first = 0
            self.textEdit.append("您已主动将当前内存中已标注结果写入到相应文件！\n 如需继续标注本文件夹，请重新选择打开本文件夹！")
            self.alreadysave = 1
