from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QVBoxLayout,QDialog,QComboBox,QHBoxLayout,QLabel
import mysql.connector

class Sql():
    def obterDados():
        cadastrodb = mysql.connector.connect(host="192.168.1.145",user="test",passwd="cerejinha123",database="cadastro")
        mycursor = cadastrodb.cursor()
        mycursor.execute("select date_format(datas, '%i') from controle")
        myresult = mycursor.fetchall()
        return myresult

class Gui(QDialog):
    def __init__(self, parent=None):
        super(Gui, self).__init__(parent)
        
        self.datasComboBox=QComboBox()
        self.datasComboBox.addItems([str(Sql.obterDados())])
        self.datasComboBox.currentIndexChanged.connect(self.selectionchange)
        
        datasLabel = QLabel("&Datas:")
        datasLabel.setBuddy(self.datasComboBox)
        
        layout = QHBoxLayout()
        layout.addWidget(self.datasComboBox)
        layout.addWidget(datasLabel)
        self.setLayout(layout)
        
    def selectionchange(self):
        print("mudou para",self.datasComboBox.currentText())
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    print(Sql.obterDados())
    tudo=Gui()
    tudo.show()
    sys.exit(app.exec_())
