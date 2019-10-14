import pygame.sprite


class BaseObject(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.interactive = False

    def update(self, scene):

        pass

