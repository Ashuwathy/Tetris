import pygame
import random
from constant import tetris_shapes, blockSize, cols, grey, yellow
from Board import Board
class Block:

    def __init__(self):
        self.board = Board()
        self.block_x = None
        self.block_y = None
        self.tetris_block = None

    def Block_piece(self):
        self.tetris_block = random.choice(tetris_shapes)
        self.block_x = int(cols / 2 - len(self.tetris_block) / 2)
        self.block_y = 0
        self.drawBlock(yellow)


    def drawBlock(self, color):
        for j, row in enumerate(self.tetris_block):
            for i, val in enumerate(row):
                if val:
                    rect = pygame.Rect((self.block_x+i)*blockSize, (self.block_y+j)*blockSize, blockSize, blockSize)
                    pygame.draw.rect(self.board.screen, color, rect, 0)
                    pygame.draw.rect(self.board.screen, grey, rect, 1)
        pygame.display.update()