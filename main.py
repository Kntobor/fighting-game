import pygame
import player
from sys import *

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption('Fighting Game')
        self.clock = pygame.time.Clock()

        self.players = pygame.sprite.Group()
        self.players.add(player.Player(True,))
        self.players.add(player.Player(False))

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                break
        
        pygame.draw.rect(self.screen, 'white', (0, 300, 800, 100))
        
        self.players.update()
        self.players.draw(self.screen)

        pygame.display.update()
        self.clock.tick(60) # Caps framerate at 60

if __name__ == '__main__':
    game = Game()

    while True:
        game.run()