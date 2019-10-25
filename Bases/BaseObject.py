import pygame.sprite


class BaseObject(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([0, 0])

        self.interactive = False
        self.width = 0
        self.height = 0

        self.rect = self.image.get_rect()

    def update(self, scene, inputs):

        pass

