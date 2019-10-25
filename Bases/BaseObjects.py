import pygame.sprite


class BaseObject(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([0, 0])

        self.interactive = False
        self.width = 0
        self.height = 0
        self.x = x
        self.y = y

    def update(self, scene, inputs):

        if self.interactive:
            self.interaction(scene, inputs)

    def render(self, canvas):

        pass

    def interaction(self, scene, inputs):

        pass

    def get_dimensions(self):
        """
        :return: Returns the x position, y position, width, height.
        """

        return self.x, self.y, self.width, self.height


class BaseUnit(BaseObject):

    def __init__(self, x, y):
        BaseObject.__init__(self, x, y)


class BaseSpell(BaseObject):

    def __init__(self, x, y):
        BaseObject.__init__(self, x, y)


class BaseDoodad(BaseObject):

    def __init__(self, x, y):
        BaseObject.__init__(self, x, y)
