import sys
from PyQt5.QtWidgets import QApplication, QWidget

#클래스 oop
class qTemplate(QWidget):
    
    #생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self) -> None:
        self.setGeometry(300,100,640,400)
        self.setWindowTitle('QTemplate!!')
        self.show()



if __name__=='__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()
