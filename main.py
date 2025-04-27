import sys, random
from types import new_class

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox

class TTT(QWidget): # Tic-Tac-Toe

    def __init__(self):
        super().__init__() # init of parent
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Кресты и Нули")
        self.setGeometry(100,100,300,300) # pos and size of window
        self.grid = QGridLayout()
        self.setLayout(self.grid)




if __name__ == '__main__':
    pass
