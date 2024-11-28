import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap #usado para lidar com imagens e prver funcionalidades para carregar, manipular e mostrar imagens, coloca-se a imagem no objeto pixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(683, 384, 500, 500)

        label = QLabel(self)
        label.setGeometry(0, 0, 100, 100)

        pixmap = QPixmap("./68 - PyQt5 images/nagi_image.jpg")
        label.setPixmap(pixmap) #Colocando a imagem no label

        label.setScaledContents(True) # A imagem vai se adequar ao tamanho do label

        label.setGeometry(self.width() - label.width() // 2, #// divisão de inteiros pra resultados inteiros
                           self.height() - label.height() // 2, 
                           label.width(), 
                           label.height())



    
def main():
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ =="__main__":
    main()