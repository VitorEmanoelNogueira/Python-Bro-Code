import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 250, 500, 300)
        self.button = QPushButton("Click me!", self)
        self.label = QLabel("Hello", self)
        self.initUI()
    
    def initUI(self):
        self.button.setGeometry(150, 100, 200, 100)
        self.button.setStyleSheet("font-size: 30px")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(220, 180, 200, 100)
        self.label.setStyleSheet("font-size: 15px")

    def on_click(self):
        print("Button clicked!")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)
        self.label.setText("Goodbye!")




    
def main():
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ =="__main__":
    main()