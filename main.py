import pygame
from sys import *

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption('Pygame Game')
        self.clock = pygame.time.Clock()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                break
        
        pygame.display.update()
        self.clock.tick(60) # Caps framerate at 60

if __name__ == '__main__':
    game = Game()

    while True:
        game.run()