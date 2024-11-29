import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon 
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt # Classe usada para alinhamentos no label

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(500, 250, 500, 300)
        self.setWindowIcon(QIcon("./deadpool.ico"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: purple;" 
                            "background-color: green;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
                            #Outros valores como rgb, hsl, etc. também são aceitos nas cores

        # label.setAlignment(Qt.AlignTop) #Vertically TOP
        # label.setAlignment(Qt.AlignBottom) # Vertically Bottom
        # label.setAlignment(Qt.AlignVCenter) # Vertically Center

        # label.setAlignment(Qt.AlignRight) #Horizontally right
        # label.setAlignment(Qt.AlignHCenter) #Horizontally center
        # label.setAlignment(Qt.AlignLeft) #Horizontally left

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # Usar o | permite combinar flags - Center & Top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # Center & Bottom
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # Absolute center (center & center)
        label.setAlignment(Qt.AlignCenter) #shorthand para centralizar absolutamente 




    
def main():
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ =="__main__":
    main()