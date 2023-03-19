import pygame
import random
from constant import cols, rows, blockSize, width, height, white, grey, colors

class Board:
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill(white)
        self.board = None

    def Grid(self):
        self.board = [[0 for _ in range(cols)]
                      for _ in range(rows)]
        self.drawGrid()

    def drawGrid(self):
        for y, row in enumerate(self.board):
            for x, val in enumerate(row):
                rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
                if val:
                    pygame.draw.rect(self.screen, random.choice(colors), rect, 0)
                else:
                    pygame.draw.rect(self.screen, white, rect, 0)
                pygame.draw.rect(self.screen, grey, rect, 1)
        pygame.display.update()

    def remove_row(self):
        for j, row in enumerate(self.board[::-1]):
            if 0 not in row:
                self.board.remove(row)
                self.board = [[0 for _ in range(cols)]] + self.board
                self.drawGrid()
            else:
                break