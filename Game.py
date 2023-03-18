import pygame
from Board import Board
from Block import Block
from Actions import Actions
class Game:

    def __init__(self):
        self.board = Board()
        self.actions = Actions(self.board)

    def Render(self):
        running = True
        self.board.Grid()
        self.actions.Block_piece()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.actions.moveBlock(-1)
                    if event.key == pygame.K_RIGHT:
                        self.actions.moveBlock(+1)
                    if event.key == pygame.K_UP:
                        self.actions.rotate()
                else:
                    pass


if __name__ == '__main__':
	app = Game()
	app.Render()