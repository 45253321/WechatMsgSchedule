# Form implementation generated from reading ui file 'daydayup.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1018, 741)
        MainWindow.setStyleSheet("* {\n"
                                 "font: 700 12pt \"Microsoft YaHei UI\";\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 30, 321, 291))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.edit_topic = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.edit_topic.setObjectName("edit_topic")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.edit_topic)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.person1 = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.person1.setObjectName("person1")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.person1)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.person2 = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.person2.setText("")
        self.person2.setObjectName("person2")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.person2)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.edit_content = QtWidgets.QTextEdit(parent=self.formLayoutWidget)
        self.edit_content.setEnabled(True)
        self.edit_content.setObjectName("edit_content")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.edit_content)
        self.label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.edit_time = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.edit_time.setObjectName("edit_time")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.edit_time)
        self.label_6 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.edit_day = QtWidgets.QSpinBox(parent=self.formLayoutWidget)
        self.edit_day.setMinimum(1)
        self.edit_day.setMaximum(7)
        self.edit_day.setObjectName("edit_day")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.edit_day)
        self.tableView = QtWidgets.QTableView(parent=self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(400, 30, 571, 381))
        self.tableView.setStyleSheet("")
        self.tableView.setObjectName("tableView")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 330, 321, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.bt_save = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.bt_save.setObjectName("bt_save")
        self.gridLayout.addWidget(self.bt_save, 0, 0, 1, 1)
        self.bt_wx = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.bt_wx.setObjectName("bt_wx")
        self.gridLayout.addWidget(self.bt_wx, 2, 1, 1, 1)
        self.bt_exec = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.bt_exec.setObjectName("bt_exec")
        self.gridLayout.addWidget(self.bt_exec, 0, 1, 1, 1)
        self.bt_clear = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.bt_clear.setObjectName("bt_clear")
        self.gridLayout.addWidget(self.bt_clear, 2, 0, 1, 1)
        self.bt_del = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.bt_del.setObjectName("bt_del")
        self.gridLayout.addWidget(self.bt_del, 1, 0, 1, 1)
        self.bt_modify = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.bt_modify.setObjectName("bt_modify")
        self.gridLayout.addWidget(self.bt_modify, 1, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 450, 921, 231))
        self.groupBox.setObjectName("groupBox")
        self.tb_left = QtWidgets.QTextBrowser(parent=self.groupBox)
        self.tb_left.setGeometry(QtCore.QRect(10, 20, 411, 201))
        self.tb_left.setStyleSheet(" border-radius: 10px;\n"
                                   "font: 9pt \"宋体\";")
        self.tb_left.setObjectName("tb_left")
        self.tb_right = QtWidgets.QTextBrowser(parent=self.groupBox)
        self.tb_right.setGeometry(QtCore.QRect(430, 20, 481, 201))
        self.tb_right.setStyleSheet(" border-radius: 10px;\n"
                                    "font: 9pt \"宋体\";")
        self.tb_right.setObjectName("tb_right")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(50, 430, 921, 21))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1018, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMonday = QtGui.QAction(parent=MainWindow)
        self.actionMonday.setObjectName("actionMonday")
        self.actionTues = QtGui.QAction(parent=MainWindow)
        self.actionTues.setObjectName("actionTues")
        self.actionWed = QtGui.QAction(parent=MainWindow)
        self.actionWed.setObjectName("actionWed")
        self.actionThur = QtGui.QAction(parent=MainWindow)
        self.actionThur.setObjectName("actionThur")
        self.actionFri = QtGui.QAction(parent=MainWindow)
        self.actionFri.setObjectName("actionFri")
        self.actionSat = QtGui.QAction(parent=MainWindow)
        self.actionSat.setObjectName("actionSat")
        self.actionSun = QtGui.QAction(parent=MainWindow)
        self.actionSun.setObjectName("actionSun")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "主题"))
        self.label_2.setText(_translate("MainWindow", "通知对象1"))
        self.label_3.setText(_translate("MainWindow", "通知对象2"))
        self.label_4.setText(_translate("MainWindow", "内容"))
        self.label_5.setText(_translate("MainWindow", "时间"))
        self.edit_time.setPlaceholderText(
            _translate("MainWindow", "例如: 12:12"))
        self.label_6.setText(_translate("MainWindow", "星期"))
        self.bt_save.setText(_translate("MainWindow", "保存"))
        self.bt_wx.setText(_translate("MainWindow", "微信检测"))
        self.bt_exec.setText(_translate("MainWindow", "立即执行"))
        self.bt_clear.setText(_translate("MainWindow", "清空"))
        self.bt_del.setText(_translate("MainWindow", "删除"))
        self.bt_modify.setText(_translate("MainWindow", "修改"))
        self.groupBox.setTitle(_translate("MainWindow", "系统日志"))
        self.tb_right.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "hr { height: 1px; border-width: 0; }\n"
                                         "li.unchecked::marker { content: \"\\2610\"; }\n"
                                         "li.checked::marker { content: \"\\2612\"; }\n"
                                         "</style></head><body style=\" font-family:\'宋体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft YaHei UI\'; font-size:12pt; font-weight:700;\"><br /></p></body></html>"))
        self.actionMonday.setText(_translate("MainWindow", "星期一"))
        self.actionMonday.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.actionTues.setText(_translate("MainWindow", "星期二"))
        self.actionTues.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionWed.setText(_translate("MainWindow", "星期三"))
        self.actionWed.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.actionThur.setText(_translate("MainWindow", "星期四"))
        self.actionThur.setShortcut(_translate("MainWindow", "Ctrl+4"))
        self.actionFri.setText(_translate("MainWindow", "星期五"))
        self.actionFri.setShortcut(_translate("MainWindow", "Ctrl+5"))
        self.actionSat.setText(_translate("MainWindow", "星期六"))
        self.actionSat.setShortcut(_translate("MainWindow", "Ctrl+6"))
        self.actionSun.setText(_translate("MainWindow", "星期日"))
        self.actionSun.setShortcut(_translate("MainWindow", "Ctrl+7"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())