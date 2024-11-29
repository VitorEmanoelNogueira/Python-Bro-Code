import sys # provê acesso a algumas variáveis usadas ou mantidas pelo interpretador para e a funções que interagem fortemente com ele
from PyQt5.QtWidgets import QApplication, QMainWindow # Imports para a janela
from PyQt5.QtGui import QIcon # Import para icons

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        # self.setGeometry(x, y, width height)
        self.setGeometry(500, 250, 300, 300)
        self.setWindowIcon(QIcon("./deadpool.ico"))

    
def main():
    app = QApplication(sys.argv) # Passar esse argumento permite que o interpretador de python para processar comandos de linha (terminal, linha de comando, etc.)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) #o exec_ espera input do usuário e lida com ele (assim a janela não fecha automaticamente até interagirmos com ela)

if __name__ =="__main__":
    main()