'''
Pyt5 + 有道爬虫制作翻译APP


'''

import sys

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from translate import translated_get



class Ui_mainWindow(object):
    def Ui(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.WindowModal)
        mainWindow.resize(470,600)  # 可拖拽，界面大小
        # mainWindow.setFixedSize(600,500)# 不可拖拽，界面大小
        # mainWindow相当于 QtWidgets.QWidget
        # self.bgUrl = "{0}\\bg.png".format(sys.path[0])
        # mainWindow.setStyleSheet('background-image:url({0})'.format(self.bgUrl.replace('\\', "/")))
        self.centralWidget = QtWidgets.QWidget(mainWindow) # 调用工具
        self.centralWidget.setObjectName("centralWidget")
        # 定义字体
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(10)
        font.setWeight(30)

        self.switchButton = QtWidgets.QPushButton(self.centralWidget)
        self.switchButton.setGeometry(QtCore.QRect(235, 5, 60, 60))
        self.switchButton.setObjectName("button1")
        self.switchButton.setText("Switch")
        # 设置按钮保持点击或释放状态
        self.switchButton.setCheckable(True)
        self.switchButton.setFont(font)
        self.switchButton.setAutoRepeatDelay(200)
        self.switchButton.setToolTip("切换自动翻译/点击翻译")
        self.switchButton.clicked.connect(self.SwitchButtonCheck)

        self.trButton = QtWidgets.QPushButton(self.centralWidget)
        self.trButton.setGeometry(QtCore.QRect(305, 5, 150, 60))
        self.trButton.setObjectName("button2")
        self.trButton.setText("点击翻译")
        self.trButton.setFont(font)
        self.trButton.hide()
        self.trButton.clicked.connect(self.word_get)

        self.lineEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.lineEdit.setGeometry(10, 80, 450, 180)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlainText('''输入翻译内容''')
        self.lineEdit.setStyleSheet('color:black')
        self.lineEdit.textChanged.connect(self.isAutoTr)

        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(12)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        #self.lineEdit.textChanged.connect(self.textAreaChanged)
        # 定义文本框--输出
        self.lineTranslated = QtWidgets.QTextEdit(self.centralWidget)
        self.lineTranslated.setGeometry(10, 280, 450, 280)
        self.lineTranslated.setObjectName("lineTranslated")
        self.lineTranslated.setFont(font)
        self.bgUrl = ".\\bg.png"
        self.lineTranslated.setStyleSheet('background-image:url({0})'.format(self.bgUrl.replace('\\', "/")))
        # 定义标签
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 5, 210, 60))
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(11)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setText("<font color=%s>%s</font>" % ('#7EC7FF', "简单的翻译@_@ by chen"))
        mainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Tranlation@link"))

    def SwitchButtonCheck(self):
        if self.switchButton.isChecked() == True:
            self.trButton.show()
        else:
            self.trButton.hide()

    def isAutoTr(self):
        if self.switchButton.isChecked() == False:
            self.word_get()

    def word_get(self):
        word = self.lineEdit.toPlainText()
        if word:
            try:
                re = translated_get(word)
                self.lineTranslated.setPlainText(re)
            except requests.exceptions.ConnectionError:
                self.lineTranslated.setPlainText('--没有网络,请检查网络--')
        else:
            self.lineTranslated.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.Ui(mainWindow)
    mainWindow.show()
    # print(ui.switchButton.isChecked())
    # 查看switch按钮是否开启
    sys.exit(app.exec_())






