import pygame
from constant import cols, rows, blockSize, s_width, s_height, white, grey

class Board:
    def __init__(self):
        self.screen = pygame.display.set_mode((s_width, s_height))
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