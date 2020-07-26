# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'c:\Users\cultivator\Desktop\audio_linger\mainw.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox
import PyQt5.QtWidgets as qw
import sou
class Ui_audiolinger(object):
    def setupUi(self, audiolinger):
        audiolinger.setObjectName("audiolinger")
        audiolinger.resize(863, 453)
        audiolinger.setStyleSheet("#audiolinger{\n"
"background-image:url(C:/Users/cultivator/Desktop/audio_linger/main_image.jpg)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(audiolinger)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(768, 780, 150, 46))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(590, 200, 512, 512))
        self.textEdit.setStyleSheet("#textEdit{\n"
"background-image:url(C:/Users/cultivator/Desktop/audio_linger/1.jpg)\n"
"}")
        self.textEdit.setObjectName("textEdit")
        audiolinger.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(audiolinger)
        self.statusbar.setObjectName("statusbar")
        audiolinger.setStatusBar(self.statusbar)
        self.retranslateUi(audiolinger)
        QtCore.QMetaObject.connectSlotsByName(audiolinger)

    def retranslateUi(self, audiolinger):
        _translate = QtCore.QCoreApplication.translate
        audiolinger.setWindowTitle(_translate("audiolinger", "MainWindow"))
        self.pushButton.setText(_translate("audiolinger", "开始转换"))
    def solve(self):
        source_path=self.textEdit.toPlainText()   #搜先获取文件的原始路径
        #解析路径
        path=sou.exppath(source_path)
        if(path!=None and path.endswith(".mp4")):
            sou.explict(path)
        else:
            qw.QMessageBox.Critical(self,"错误","请检查文件格式是否为MP4！！")
            sys.exit(app.exec_())

if __name__ == "__main__":    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_audiolinger()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("audio linger")
    MainWindow.setFixedSize(2*MainWindow.width(),2*MainWindow.height())
    MainWindow.show()
    ui.pushButton.clicked.connect(ui.solve)
    sys.exit(app.exec_())