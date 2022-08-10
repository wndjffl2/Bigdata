from PyQt5 import QtWidgets as qw



def run():
    app = qw.QApplication([])
    wnd = qw.QMainWindow()
    label = qw.QLabel('Hello Qt!')
    wnd.setCentralWidget(label)
    wnd.show()
    app.exec_()

if __name__ =='__main__':
    run()
    

