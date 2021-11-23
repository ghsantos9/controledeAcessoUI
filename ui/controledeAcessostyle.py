# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controledeAcessostyle.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Imagens/ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(60, 60, 60);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 1021, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_labmaker = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(40)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_labmaker.setFont(font)
        self.label_labmaker.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_labmaker.setAutoFillBackground(False)
        self.label_labmaker.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_labmaker.setAlignment(QtCore.Qt.AlignCenter)
        self.label_labmaker.setWordWrap(False)
        self.label_labmaker.setObjectName("label_labmaker")
        self.verticalLayout.addWidget(self.label_labmaker)
        self.stream = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.stream.setMaximumSize(QtCore.QSize(1024, 600))
        self.stream.setText("")
        self.stream.setPixmap(QtGui.QPixmap("924x450.png"))
        self.stream.setAlignment(QtCore.Qt.AlignCenter)
        self.stream.setObjectName("stream")
        self.verticalLayout.addWidget(self.stream)
        self.aguardando = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.aguardando.setMaximumSize(QtCore.QSize(16777215, 1024))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        self.aguardando.setFont(font)
        self.aguardando.setAlignment(QtCore.Qt.AlignCenter)
        self.aguardando.setObjectName("aguardando")
        self.verticalLayout.addWidget(self.aguardando)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LabMaker"))
        self.label_labmaker.setText(_translate("MainWindow", "Laboratório Maker"))
        self.aguardando.setText(_translate("MainWindow", "Aguardando código QR"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

