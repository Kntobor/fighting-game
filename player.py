import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, playerOne):
        self.playerOne = playerOne

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((50, 50))
        self.image.fill('white')

        if self.playerOne:
            self.rect = (100, 100)
        else:
            self.rect = (700, 100)

        self.moveTime = 0
        self.direction = 'eekum bokum'

    def input(self):
        keys = pygame.key.get_pressed()

        if self.playerOne:
            if keys[pygame.K_d]:
                self.direction = 'right'
            elif keys[pygame.K_a]:
                self.direction = 'left'
            elif keys[pygame.K_w]:
                self.direction = 'up'
            elif keys[pygame.K_s]:
                self.direction = 'down'
        else:
            if keys[pygame.K_RIGHT]:
                self.direction = 'right'
            elif keys[pygame.K_LEFT]:
                self.direction = 'left'
            elif keys[pygame.K_UP]:
                self.direction = 'up'
            elif keys[pygame.K_DOWN]:
                self.direction = 'down'

    def move(self):
        self.moveTime += 0.1

        if self.moveTime >= 1:
            match self.direction:
                case 'right':
                    pass
                case 'left':
                    pass
                case 'up':
                    pass
                case 'down':
                    pass
            
            self.moveTime = 0

    def update(self):
        self.input()
        self.move()