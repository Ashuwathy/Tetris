import pygame
from Board import Board
class Game:

    def __init__(self):
        self.board = Board()
    def Render(self):
        running = True
        self.board.Grid()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    pass


if __name__ == '__main__':
	app = Game()
	app.Render()