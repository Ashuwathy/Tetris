import pygame
from Board import Board
from Actions import Actions
class Game:

    def __init__(self):
        self.actions = Actions()

    def Render(self):
        running = True
        # time_delay = 500
        # timer_event = pygame.USEREVENT + 1
        # pygame.time.set_timer(timer_event, time_delay)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # if event.type == timer_event:
                #     self.actions.drop()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.actions.moveBlock(-1)
                    if event.key == pygame.K_RIGHT:
                        self.actions.moveBlock(+1)
                    if event.key == pygame.K_UP:
                        self.actions.rotate()
                    if event.key == pygame.K_DOWN:
                        self.actions.drop()
                else:
                    pass


if __name__ == '__main__':
	app = Game()
	app.Render()