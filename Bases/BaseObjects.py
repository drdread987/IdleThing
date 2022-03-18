import pygame.sprite


class BaseObject(pygame.sprite.Sprite):

    def __init__(self, oh, il, x, y):
        super().__init__()

        self.image = pygame.Surface([0, 0])

        self.interactive = False
        self.width = 0
        self.height = 0
        self.x = x
        self.y = y
        self.update_rect()
        self.alignment = "neutral"
        self.dead = False

        self.oh = oh

    def update(self, scene, i_events, inputs):

        if self.interactive:
            self.interaction(scene, i_events, inputs)

        self.update_rect()

    def render(self, canvas):

        canvas.blit(self.image, (self.x, self.y))

    def interaction(self, scene, i_events, inputs):

        pass

    def get_dimensions(self):
        """
        :return: Returns the x position, y position, width, height.
        """

        return self.x, self.y, self.width, self.height

    def update_rect(self):

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


class BaseUnit(BaseObject):

    def __init__(self, oh, il, x, y):
        super().__init__(oh, il, x, y)

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

        if self.health_points <= 0:
            self.death(actor, scene)

    def gain_health(self, value, actor, scene):

        raw_damage = value

        for buff in self.buffs:
            value = self.buffs[buff].gain_health(value, actor)

        for debuff in self.debuffs:
            value = self.debuffs[debuff].damage_taken(value, actor)

        if self.health_points + value > self.max_health_points:
            value = self.max_health_points - self.health_points
        event_key = 18
        if self.alignment == "friendly":
            event_key = 18
        elif self.alignment == "neutral":
            event_key = 19
        elif self.alignment == "enemy":
            event_key = 20

        scene.OEH.event(event_key, actor, self, raw_damage, value, self.unit_id)

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
            self.dead = True
            scene.OEH.remove_listener(self)


class BaseSpell(BaseObject):

    def __init__(self, oh, il, x, y):
        BaseObject.__init__(self, oh, il, x, y)

        self.spell_id = 0


class BaseDoodad(BaseObject):

    def __init__(self, oh, il, x, y):
        BaseObject.__init__(self, oh, il, x, y)

        """
        0 = undefined.
        1 = block
        2 = block you can move on to
        3 = 
        """
        self.doodad_type = 0
        self.doodad_id = 0
        self.vulnerable = 0

        self.max_health_points = 0
        self.health_points = self.max_health_points

        self.max_physical_defense = 0
        self.physical_defense = self.max_physical_defense

        self.max_magic_defense = 0
        self.magic_defense = self.max_magic_defense

    def gain_health(self, value, actor, scene):

        raw_damage = value

        if self.health_points + value > self.max_health_points:
            value = self.max_health_points - self.health_points
        event_key = 18
        if self.alignment == "friendly":
            event_key = 18
        elif self.alignment == "neutral":
            event_key = 19
        elif self.alignment == "enemy":
            event_key = 20

        scene.OEH.event(event_key, actor, self, raw_damage, value, self.doodad_id)


