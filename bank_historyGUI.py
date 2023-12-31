from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TransactionWindow(object):
    def setupUi(self, TransactionWindow):
        TransactionWindow.setObjectName("TransactionWindow")
        TransactionWindow.resize(480, 682)
        TransactionWindow.setMinimumSize(QtCore.QSize(480, 682))
        TransactionWindow.setMaximumSize(QtCore.QSize(480, 682))
        TransactionWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=TransactionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(106, 189, 155);\n"
                                 "")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.transaction_history_text = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.transaction_history_text.setGeometry(QtCore.QRect(50, 110, 381, 501))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.transaction_history_text.setFont(font)
        self.transaction_history_text.setStyleSheet("color: rgb(106, 189, 155);\n"
                                                    "border-color: rgb(106, 189, 155);\n"
                                                    "gridline-color: rgb(106, 189, 155);")
        self.transaction_history_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.transaction_history_text.setReadOnly(True)
        self.transaction_history_text.setObjectName("transaction_history_text")
        TransactionWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=TransactionWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 26))
        self.menubar.setObjectName("menubar")
        TransactionWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=TransactionWindow)
        self.statusbar.setObjectName("statusbar")
        TransactionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TransactionWindow)
        QtCore.QMetaObject.connectSlotsByName(TransactionWindow)

    def retranslateUi(self, TransactionWindow):
        _translate = QtCore.QCoreApplication.translate
        TransactionWindow.setWindowTitle(_translate("TransactionWindow", "Online Banking"))
        self.label.setText(_translate("TransactionWindow", "TRANSACTION HISTORY"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    TransactionWindow = QtWidgets.QMainWindow()
    ui = Ui_TransactionWindow()
    ui.setupUi(TransactionWindow)
    TransactionWindow.show()
    sys.exit(app.exec())
