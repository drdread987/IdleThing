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

        self.alignment = "neutral"

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

        self.easy_remove = True
        self.unit_id = 0

    def take_damage(self, damage_type, value, actor, scene):

        raw_damage = value

        for buff in self.buffs:
            value = self.buffs[buff].damage_taken(damage_type, value)

        for debuff in self.debuffs:
            value = self.debuffs[debuff].damage_taken(damage_type, value)

        self.health_points -= value
        event_key = 24
        if self.alignment == "friendly":
            event_key = 24
        elif self.alignment == "neutral":
            event_key = 25
        elif self.alignment == "enemy":
            event_key = 26

        scene.OEH.event(event_key, actor, self, raw_damage, value, self.unit_id)

        if self.health_points < 0:
            self.death(actor, scene)

    def death(self, actor, scene):
        death = True
        for buff in self.buffs:
            death = self.buffs[buff].damage_taken(death, actor)

        for debuff in self.debuffs:
            death = self.debuffs[debuff].damage_taken(death, actor)

        event_key = 9
        if self.alignment == "friendly":
            event_key = 9
        elif self.alignment == "neutral":
            event_key = 10
        elif self.alignment == "enemy":
            event_key = 11

        if self.easy_remove and death:
            scene.OEH.event(event_key, self, self.unit_id)
            self.kill()


class BaseSpell(BaseObject):

    def __init__(self, x, y):
        BaseObject.__init__(self, x, y)

        self.spell_id = 0


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
        self.doodad_id = 0
        self.vulnerable = 0
