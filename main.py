import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox


class Game(QWidget): # Tic-Tac-Toe
    def __init__(self):
        super().__init__() # parent's init
        self.board = None
        self.buttons = None
        self.grid = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Кресты и Нули")
        self.setGeometry(500,100,300,300) # pos and size of window
        self.grid = QGridLayout()
        self.buttons = [[QPushButton("") for _ in range(3)] for _ in range(3)]
        self.board = [[None for _ in range(3)] for _ in range(3)]

        for row in self.buttons:
            for button in row:
                button.setFixedSize(100, 100)

                button.clicked.connect(lambda _, x=self.buttons.index(row), y=row.index(button): self.player_move(x, y))
                self.grid.addWidget(button, self.buttons.index(row), row.index(button))

        self.setLayout(self.grid)

    def player_move(self, x: int, y: int):
        if self.board[x][y] is not None:
            pass
        else:
            self.board[x][y] = "X"
            self.buttons[x][y].setText("X")
            self.ai_move()

    def ai_move(self):
        best_score = -float("inf")
        best_move = None

        for row in range(3):
            for button in range(3):
                if self.board[row][button] is None:
                    self.board[row][button] = "O"
                    score = self.minimax(False)
                    self.board[row][button] = None
                    if score > best_score:
                        best_score = score
                        best_move = (row, button)

        if best_move:
            x, y = best_move
            self.board[x][y] = "O"
            self.buttons[x][y].setText("O")



    def minimax(self, move: bool) -> float:
        if self.check_winner("X"):
            return -1
        elif self.check_winner("O"):
            return 1
        elif self.board_is_full():
            return 0

        if move:
            best_score = -float("inf")
            for row in range(3):
                for button in range(3):
                    if self.board[row][button] is None:
                        self.board[row][button] = "O"
                        score = self.minimax(False)
                        self.board[row][button] = None
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for row in range(3):
                for button in range(3):
                    if self.board[row][button] is None:
                        self.board[row][button] = "X"
                        score = self.minimax(True)
                        self.board[row][button] = None
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, sign: str):
        for row in self.board:
            if all(cell == sign for cell in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == sign for row in range(3)):
                return True
        if all(self.board[i][i] == sign for i in range(3)) or all(self.board[i][2-i] == sign for i in range(3)):
            return True

        return False

    def board_is_full(self) -> bool:
        return all(all(cell is not None for cell in row) for row in self.board)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Game()
    game.show()
    sys.exit(app.exec())

