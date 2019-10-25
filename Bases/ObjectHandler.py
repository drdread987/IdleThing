import pygame.sprite


class ObjectHandler:

    def __init__(self):

        self.friendly_spells = pygame.sprite.Group()
        self.neutral_spells = pygame.sprite.Group()
        self.enemy_spells = pygame.sprite.Group()
        self.scene_spells = pygame.sprite.Group()

        self.friendly_units = pygame.sprite.Group()
        self.neutral_units = pygame.sprite.Group()
        self.enemy_units = pygame.sprite.Group()
        self.scene_units = pygame.sprite.Group()

        self.friendly_doodads = pygame.sprite.Group()
        self.neutral_doodads = pygame.sprite.Group()
        self.enemy_doodads = pygame.sprite.Group()
        self.scene_doodads = pygame.sprite.Group()

    def update_objects(self):

        pass

    def draw_objects(self, surface):
        """
        This function is a gateway function calling every object and passing surface,
        allowing each object to handle its own drawing.
        :param surface: the surface to draw our objects on to.
        :return: none
        """

        pass

    def get_all_object(self):

        pass

    def get_units(self):

        pass

    def get_spells(self):

        pass

    def get_doodads(self):

        pass

    def new_object(self, obj, obj_type, alignment):

        pass

    def collide_objects(self, obj, collide_type, collide_alignment):

        pass
