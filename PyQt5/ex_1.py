#pyQt5 inttoduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Cool GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("E:/paambu/PyQt5/pongal.jpg"))

        label = QLabel("Hello",self)
        label.setFont(QFont("Arial", 25))
        label.setGeometry(0, 0, 500, 100) 
        label.setStyleSheet("color: #292929;" 
                            "background-color: #6fdcf7;"
                            "font-weight: bold;" 
                            "font-style: italic;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        #label.setAlignment(Qt.AlignTop) #vertically top
       # label.setAlignment(Qt.AlignBottom)
        #label.setAlignment(Qt.AlignVCenter)
       # label.setAlignment(Qt.AlignRight)
        label.setAlignment(Qt.AlignHCenter |Qt.AlignVCenter)
        label.setGeometry(0,0,250,250)
        pixmap = QPixmap("E:/paambu/PyQt5/pongal.jpg")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setGeometry((self.width() -label.width()) //2, 
                          (self.height() - label.height()) //2,
                          label.width() ,
                          label.height())

        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()