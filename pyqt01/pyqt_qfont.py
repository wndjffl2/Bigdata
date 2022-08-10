import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor,QFont
from PyQt5.QtCore import Qt 
#클래스 oop
class qTemplate(QWidget):
    
    #생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self) -> None:
        self.setGeometry(300,100,640,400)
        self.setWindowTitle('QTemplate!!')
        self.text = 'What a wonderful world~'
        self.show()

    def paintEvent(self,event)-> None:
        paint = QPainter()
        paint.begin(self)
        #그리는 함수 추가
        self.drawText(event, paint)
        paint.end()

    #텍스트 그리기 위한 사용자함수
    def drawText(self, event, paint):
        paint.setPen(QColor(50,50,50))
        paint.drawText(105,100,'Hell world~')
        paint.setPen(QColor(0,250,10))
        paint.setFont(QFont('NanumGothic',10))
        paint.drawText(event.rect(),Qt.AlignCenter, self.text)


if __name__=='__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()
