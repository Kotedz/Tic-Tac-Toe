import sys, random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox

# field = board
class Game(QWidget): # Tic-Tac-Toe

    def __init__(self):
        super().__init__() # parent's init
        self.field = None
        self.buttons = None
        self.grid = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Кресты и Нули")
        self.setGeometry(100,100,300,300) # pos and size of window
        self.grid = QGridLayout()
        self.buttons = [[QPushButton("") for _ in range(3)] for _ in range(3)]
        self.field = [[None for _ in range(3)] for _ in range(3)]

        for row in self.buttons:
            for button in row:
                button.setFixedSize(100, 100)
                self.grid.addWidget(button, self.buttons.index(row), row.index(button))

        self.setLayout(self.grid)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Game()
    game.show()
    sys.exit(app.exec())

