import pygame
import random
from constant import tetris_shapes, blockSize, cols, grey, colors
from Board import Board
class Block:

    def __init__(self, screen):
        self.block_x = None
        self.block_y = None
        self.tetris_block = None
        self.color = None
        self.screen = screen

    def Block_piece(self):
        self.tetris_block = random.choice(tetris_shapes)
        self.block_x = int(cols / 2 - len(self.tetris_block[0]) / 2)
        self.block_y = 0
        self.color = random.choice(colors)
        self.drawBlock(self.color)


    def drawBlock(self, color):
        for j, row in enumerate(self.tetris_block):
            for i, val in enumerate(row):
                if val:
                    rect = pygame.Rect((self.block_x+i)*blockSize, (self.block_y+j)*blockSize, blockSize, blockSize)
                    pygame.draw.rect(self.screen, color, rect, 0)
                    pygame.draw.rect(self.screen, grey, rect, 1)
        pygame.display.update()