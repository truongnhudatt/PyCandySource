# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
import res


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowFlag(Qt.FramelessWindowHint)
        MainWindow.resize(1007, 412)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icones/4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 9, 400, 400))
        self.label.setStyleSheet("border-image: url(:/images/background.jpg);\n"
                                 "background:rgb(255, 255, 255);\n"
                                 "border-top-left-radius:10px;\n"
                                 "border-bottom-left-radius:10px;\n"
                                 "border-top-right-radius:10px;\n"
                                 "border-bottom-right-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(420, 10, 191, 91))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 171, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(620, 0, 381, 411))
        self.groupBox_2.setAccessibleDescription("")
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 362, 381))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(420, 110, 191, 301))
        self.groupBox_3.setStyleSheet("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.widget = QtWidgets.QWidget(self.groupBox_3)
        self.widget.setGeometry(QtCore.QRect(40, 30, 101, 251))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setStyleSheet("background-color: white;\n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-radius: 10px;\n"
                                        "border-color: black;\n"
                                        "padding: 5px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setStyleSheet("background-color: white;\n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-radius: 10px;\n"
                                        "border-color: black;\n"
                                        "padding: 5px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setStyleSheet("background-color: white;\n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-radius: 10px;\n"
                                        "border-color: black;\n"
                                        "padding: 5px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setStyleSheet("background-color: white;\n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-radius: 10px;\n"
                                        "border-color: black;\n"
                                        "padding: 5px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Candy Crush Saga"))
        self.label_2.setText(_translate("MainWindow", "Time"))
        self.label_3.setText(_translate("MainWindow", "30"))
        self.label_4.setText(_translate("MainWindow", "Score"))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Rank"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Score"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Button"))
        self.pushButton_3.setText(_translate("MainWindow", "Stop"))
        self.pushButton_5.setText(_translate("MainWindow", "Reset"))
        self.pushButton_4.setText(_translate("MainWindow", "Exit"))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))
        self.pushButton_4.clicked.connect(lambda _ : MainWindow.close())
# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
