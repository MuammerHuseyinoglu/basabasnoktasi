import sys 
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui,uic
class Proje(QtGui.QMainWindow):
    def __init__(self):
        super(Proje,self).__init__()
        uic.loadUi('Proje.ui',self)
        self.connect(self.pushButton, SIGNAL("pressed()"),self.hesapla)
        self.show()
        
        
    def hesapla(self):
        sm=self.lineEdit.text()
        dg=self.lineEdit_2.text()
        um=self.lineEdit_3.text()
        bdm=self.lineEdit_4.text()
        
        a=int(sm)+int(dg)
        b=int(bdm)*int(um)
        c=int(um)
        d=int(a)+int(b)
        g=int(d)/int(c)
        self.label_6.setText(str(g))
        
        

        
    def build(self):
        self.statusBar()

uyg=QApplication([])
pencere=Proje()
pencere.resize(350,450)
pencere.move(450,100)
pencere.show()
uyg.exec_
