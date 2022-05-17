from gui2 import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from data import GridElement
from counter import Time
from database.rank import Database

DICTIONARY_ICONES = {
    1: './icones/1.png',
    2: './icones/2.png',
    3: './icones/3.png',
    4: './icones/4.png',
    5: './icones/5.png',
    6: './icones/6.png'
}


class Game(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.gridele = GridElement(self)
        self.gui.btn = [[QtWidgets.QPushButton(self.gui.centralwidget) for _ in range(len(self.gridele.grid))] for _ in
                        range(len(self.gridele.grid))]
        self.setupButton()
        self.gui.flagreset = False
        self.gui.flagstop = 0
        self.listClick = []
        self.gui.pushButton_5.clicked.connect(self.reset)
        self.gui.pushButton_3.clicked.connect(self.connectbuttonstop)
        self.gui.pushButton_2.clicked.connect(self.connectbuttonstart)
        self.data = Database("example.db")
        self.showtable()
    def updatetime(self, value):
        time = value
        if time > 0:
            self.gui.label_3.setText(str(time))
        else:
            self.gui.label_3.setText('Time out')
            text, okPressed = QtWidgets.QInputDialog.getText(self, "Greatt!!", "Your name:",
                                                             QtWidgets.QLineEdit.Normal, "")
            for i in range(len(self.gui.btn)):
                for y in range(len(self.gui.btn)):
                    self.gui.btn[i][y].setEnabled(False)
            self.gui.pushButton_3.setEnabled(False)
            if okPressed == True and len(text) > 0:
                self.data.insert(text, self.gui.label_5.text())
            self.showtable()
    def setupButton(self):
        for i in range(len(self.gridele.grid)):
            for y in range(len(self.gridele.grid)):
                self.gui.btn[i][y].setGeometry(QtCore.QRect(50 * y + 10, 50 * i + 10, 50, 50))
                self.gui.btn[i][y].setStyleSheet("background-color: transparent; border: 0px")
                self.gui.btn[i][y].setText("")
                self.setIconButton(i, y)
                self.gui.btn[i][y].clicked.connect(self.buttonClicked)
                self.gui.btn[i][y].value = [i, y]
                self.gui.btn[i][y].setEnabled(False)
        self.gui.pushButton_3.setEnabled(False)
        self.gui.pushButton_5.setEnabled(False)
    def connectbuttonstart(self):
        # self.threadupdatetable()
        self.gui.pushButton_2.setEnabled(False)
        self.gui.pushButton_3.setEnabled(True)
        self.gui.pushButton_5.setEnabled(True)
        for i in range(len(self.gui.btn)):
            for y in range(len(self.gui.btn)):
                self.gui.btn[i][y].setEnabled(True)
        self.time = Time(self)
        self.time.time_signal.connect(self.updatetime)
        self.time.start()

    def connectbuttonstop(self):
        if self.gui.pushButton_3.text() == 'Stop':
            self.gui.label.setStyleSheet("border-image: url(:/images/background1.jpg);\n"
                                         "background:rgb(255, 255, 255);\n"
                                         "border-top-left-radius:10px;\n"
                                         "border-bottom-left-radius:10px;\n"
                                         "border-top-right-radius:10px;\n"
                                         "border-bottom-right-radius:10px;")
            for i in range(len(self.gridele.grid)):
                for y in range(len(self.gridele.grid)):
                    self.gui.btn[i][y].hide()
            self.gui.flagstop = 1
            self.gui.pushButton_2.setEnabled(False)
            self.gui.pushButton_5.setEnabled(False)
            self.gui.pushButton_3.setText('Continue')
            for i in range(len(self.gui.btn)):
                for y in range(len(self.gui.btn)):
                    self.gui.btn[i][y].setEnabled(False)
        else:
            self.gui.label.setStyleSheet("border-image: url(:/images/background.jpg);\n"
                                         "background:rgb(255, 255, 255);\n"
                                         "border-top-left-radius:10px;\n"
                                         "border-bottom-left-radius:10px;\n"
                                         "border-top-right-radius:10px;\n"
                                         "border-bottom-right-radius:10px;")
            for i in range(len(self.gridele.grid)):
                for y in range(len(self.gridele.grid)):
                    self.gui.btn[i][y].show()
            self.gui.flagstop = 2
            self.gui.pushButton_5.setEnabled(True)
            self.gui.pushButton_3.setText('Stop')
            for i in range(len(self.gui.btn)):
                for y in range(len(self.gui.btn)):
                    self.gui.btn[i][y].setEnabled(True)

    def setIconButton(self, i, y):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(DICTIONARY_ICONES[self.gridele.getitem(i, y)]),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gui.btn[i][y].setIcon(icon)
        self.gui.btn[i][y].setIconSize(QtCore.QSize(30, 30))

    def resetGrid(self):
        for i in range(len(self.gridele.grid)):
            for y in range(len(self.gridele.grid)):
                self.setIconButton(i, y)
                self.gui.btn[i][y].setStyleSheet("background-color: transparent; border: 0px")

    def buttonClicked(self):
        sender = self.sender()
        index = sender.value
        sender.setStyleSheet("border :2px solid ;"
                             "border-color :yellow;")
        self.setClick(index)

    def setClick(self, index):
        if len(self.listClick) == 0:
            self.listClick.append(index)
        elif len(self.listClick) == 1:
            self.listClick.append(index)
            self.gridele.move(self.listClick[0][0], self.listClick[0][1], self.listClick[1][0], self.listClick[1][1])
            self.resetGrid()
        else:
            self.listClick = []
            self.listClick.append(index)

    def reset(self):
        self.showtable()
        self.gridele = GridElement(self)
        self.resetGrid()
        self.gui.flagreset = True
        for i in range(len(self.gui.btn)):
            for y in range(len(self.gui.btn)):
                self.gui.btn[i][y].setEnabled(True)
        self.gui.pushButton_3.setEnabled(True)
        self.gui.label_5.setText("0")
    def showtable(self):
        self.gui.tableWidget.setRowCount(0)
        for value in self.data.select():
            rowPosition = self.gui.tableWidget.rowCount()
            self.gui.tableWidget.insertRow(rowPosition)
            self.gui.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(value[0])))
            self.gui.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(value[1])))

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    game = Game()
    game.show()
    sys.exit(app.exec())
