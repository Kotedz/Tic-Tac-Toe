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

                button.clicked.connect(lambda _, x=self.buttons.index(row), y=row.index(button): self.player_move(x, y))
                self.grid.addWidget(button, self.buttons.index(row), row.index(button))

        self.setLayout(self.grid)

    def player_move(self, x: int, y: int):
        if self.field[x][y] is not None:
            pass
        else:
            self.field[x][y] = "X"
            self.buttons[x][y].setText("X")

    def ai_move(self):
        best_score = -float("inf")
        best_move = None

        for row in self.field:
            for button in row:
                if button is None:
                    button = "0"
                    score = self.minimax(False)
                    button = None
                    if score > best_score:
                        best_move = (self.field.index(row), row.index(button))
        if best_move:
            x, y = best_move
            self.field[x][y] = "0"
            self.buttons[x][y].setText("0")



    def minimax(self, Bool: bool) -> float:
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Game()
    game.show()
    sys.exit(app.exec())

