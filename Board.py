import pygame
from constant import cols, rows, blockSize, s_width, s_height, white, grey

class Board:
    def __init__(self):
        self.screen = pygame.display.set_mode((s_width, s_height))
        self.screen.fill(white)

    def Grid(self):
        board = [[0 for _ in range(cols)]
                 for _ in range(rows)]
        self.drawGrid(board)

    def drawGrid(self, board):
        for y, row in enumerate(board):
            for x, val in enumerate(board):
                rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
                pygame.draw.rect(self.screen, grey, rect, 1)
        pygame.display.update()