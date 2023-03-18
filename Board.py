import pygame
from constant import cols, rows, blockSize, s_width, s_height, white, grey

class Board:
    def __init__(self):
        self.width = cols*blockSize
        self.height = cols*blockSize
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(white)
        self.board = None

    def Grid(self):
        self.board = [[0 for _ in range(cols)]
                      for _ in range(rows)]
        self.drawGrid()

    def drawGrid(self):
        for y, row in enumerate(self.board):
            for x, val in enumerate(self.board):
                rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
                pygame.draw.rect(self.screen, grey, rect, 1)
        pygame.display.update()

    def remove_row(self):
        for j, row in enumerate(self.board[:-1]):
            if 0 not in row:
                del self.board[row]
                self.board = [[0 for _ in range(cols)]] + self.board
            else:
                break
        pygame.display.update()