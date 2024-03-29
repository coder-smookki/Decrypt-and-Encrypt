# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesignProgramm\UI\design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 200)
        MainWindow.setMinimumSize(QtCore.QSize(580, 200))
        MainWindow.setMaximumSize(QtCore.QSize(580, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("DesignProgramm\\UI\\../Files/icons8_lock_file.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 20, 401, 131))
        self.tabWidget_2.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setMovable(True)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.encoder_2 = QtWidgets.QWidget()
        self.encoder_2.setObjectName("encoder_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.encoder_2)
        self.pushButton_7.setGeometry(QtCore.QRect(280, 20, 91, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.encoder_2)
        self.pushButton_8.setGeometry(QtCore.QRect(280, 60, 91, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.encoder_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 20, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setClearButtonEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("DesignProgramm\\UI\\../Files/Icons/Encode.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.encoder_2, icon1, "")
        self.decoder_2 = QtWidgets.QWidget()
        self.decoder_2.setObjectName("decoder_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.decoder_2)
        self.pushButton_9.setGeometry(QtCore.QRect(280, 20, 91, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.decoder_2)
        self.pushButton_10.setGeometry(QtCore.QRect(270, 60, 101, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.decoder_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 20, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("DesignProgramm\\UI\\../Files/Icons/Decode.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.decoder_2, icon2, "")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(440, 30, 121, 120))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(4, 40, 121, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(4, 80, 121, 30))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 100, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout_us = QtWidgets.QMenu(self.menubar)
        self.menuAbout_us.setObjectName("menuAbout_us")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menuAbout_us.addSeparator()
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuAbout_us.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File Encoder"))
        self.pushButton_7.setText(_translate("MainWindow", "Открыть файл"))
        self.pushButton_8.setText(_translate("MainWindow", "Зашифровать"))
        self.lineEdit_3.setText(_translate("MainWindow", "Путь файла"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "file path"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.encoder_2), _translate("MainWindow", "Encoder"))
        self.tabWidget_2.setTabToolTip(self.tabWidget_2.indexOf(self.encoder_2), _translate("MainWindow", "<html><head/><body><p>You can encode your file here</p></body></html>"))
        self.pushButton_9.setText(_translate("MainWindow", "Открыть Файл"))
        self.pushButton_10.setText(_translate("MainWindow", "Расшифровывать"))
        self.lineEdit_4.setText(_translate("MainWindow", "Путь файла"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "file path"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.decoder_2), _translate("MainWindow", "Decoder"))
        self.tabWidget_2.setTabToolTip(self.tabWidget_2.indexOf(self.decoder_2), _translate("MainWindow", "<html><head/><body><p>You can decode your file here</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Загрузить Ключ"))
        self.pushButton.setText(_translate("MainWindow", "Генерировать Ключ"))
        self.label.setText(_translate("MainWindow", "Key: "))
        self.menuFile.setTitle(_translate("MainWindow", "Help"))
        self.menuAbout_us.setTitle(_translate("MainWindow", "About us"))
        self.menu.setTitle(_translate("MainWindow", "Авторизация"))
        self.action.setText(_translate("MainWindow", "Войти"))
        self.action_2.setText(_translate("MainWindow", "Регистрация"))
        self.action_3.setText(_translate("MainWindow", "Выйти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
