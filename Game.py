import pygame
from Board import Board
from Block import Block
class Game:

    def __init__(self):
        self.board = Board()
        self.block = Block()

    def Render(self):
        running = True
        self.board.Grid()
        self.block.Block_piece()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    pass


if __name__ == '__main__':
	app = Game()
	app.Render()