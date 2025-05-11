import sys, random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox

class Game(QWidget): # Tic-Tac-Toe

    def __init__(self):
        super().__init__() # parent's init
        self.grid = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Кресты и Нули")
        self.setGeometry(100,100,300,300) # pos and size of window
        self.grid = QGridLayout()
        self.setLayout(self.grid)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Game()
    game.show()
    sys.exit(app.exec())

