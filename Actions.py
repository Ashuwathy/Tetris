import pygame
from Block import Block
from Board import Board
import rotate_matrix
from constant import cols, rows, white, yellow

class Actions(Block):

    def __init__(self, board):
        super().__init__()
        self.board = board
        self.rotate_flag = -1

    def collision_detection(self, offset):
        for j, row in enumerate(self.tetris_block):
            for i, cell_val in enumerate(row):
                if cell_val and self.board.board[offset + j][self.block_x + i]:
                    return True
        return False

    def moveBlock(self, con):
        new_block_x = self.block_x + con
        if new_block_x < 0:
            self.block_x = 0
        elif new_block_x > cols - len(self.tetris_block[0]):
            self.block_x = cols - len(self.tetris_block[0])
        elif self.block_y + len(self.tetris_block) >= rows or self.collision_detection(offset=self.block_y+1):
            pass
        else:
            self.drawBlock(white)
            self.block_x = new_block_x
            self.drawBlock(yellow)

    def rotate(self):
        if self.block_y + len(self.tetris_block) >= rows or self.collision_detection(offset=self.block_y+1):
            pass
        elif self.block_x == 0 or self.block_x >= cols - len(self.tetris_block[0]):
            pass
        else:
            self.drawBlock(white)
            if self.rotate_flag == -1:
                self.tetris_block = rotate_matrix.anti_clockwise(self.tetris_block)
                self.rotate_flag = 1
            else:
                self.tetris_block = rotate_matrix.clockwise(self.tetris_block)
                self.rotate_flag = -1
            self.drawBlock(yellow)