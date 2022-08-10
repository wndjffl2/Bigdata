import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt 
#클래스 oop
class qTemplate(QWidget):
    
    #생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(300,100,640,400)
        self.setWindowTitle('QTemplate!!')
        self.text = 'What a wonderful world~'
        self.show()
    
    def addControls(self)-> None:
        self.setWindowIcon(QIcon('./pyqt01/img/lion.png')) #윈도우 아이콘 지정
        label1 = QLabel('',self)
        label2 = QLabel('',self)
        label1.setStyleSheet(
            'border-width: 3px;' #선 두께
            'border-style: solid;' #선 종류 solid = 실선
            'border-color: blue;' #선 색
            'image: url(./pyqt01/img/image1.png)'
            )

        label2.setStyleSheet(
            'border-width: 3px;' #선 두께
            'border-style: dot-dot-dash;' #선 종류 solid = 실선
            'border-color: red;' #선 색
            'image: url(./pyqt01/img/image2.png)'
            )
        
        box = QHBoxLayout()
        box.addWidget(label1)
        box.addWidget(label2)

        self.setLayout(box)




if __name__=='__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()
