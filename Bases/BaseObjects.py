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

        self.max_health_points = 0
        self.health_points = self.max_health_points

        self.max_physical_defense = 0
        self.physical_defense = self.max_physical_defense

        self.max_magic_defense = 0
        self.magic_defense = self.max_magic_defense

        self.buffs = []
        self.debuffs = []


class BaseSpell(BaseObject):

    def __init__(self, x, y):
        BaseObject.__init__(self, x, y)


class BaseDoodad(BaseObject):

    def __init__(self, x, y):
        BaseObject.__init__(self, x, y)

        """
        0 = undefined.
        1 = block
        2 = block you can move on to
        3 = 
        """
        self.doodad_type = 0
        self.vulnerable = 0
