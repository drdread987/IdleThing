import pygame.sprite
import Bases.ObjectEventHandler


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

        self.OEH = Bases.ObjectEventHandler.ObjectEventHandler(self)

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

    def does_obj_exist(self, obj):

        all_groups = [self.friendly_spells,
                      self.neutral_spells,
                      self.enemy_spells,
                      self.scene_spells,
                      self.friendly_units,
                      self.neutral_units,
                      self.enemy_units,
                      self.scene_units,
                      self.friendly_doodads,
                      self.neutral_doodads,
                      self.enemy_doodads,
                      self.scene_doodads]

        for group in all_groups:
            if group.has(obj):
                return True
        return False

    def get_all_objects(self):

        returnable = list()

        returnable.append(self.friendly_units.sprites())
        returnable.append(self.neutral_units.sprites())
        returnable.append(self.enemy_units.sprites())
        returnable.append(self.scene_units.sprites())

        returnable.append(self.friendly_spells.sprites())
        returnable.append(self.neutral_spells.sprites())
        returnable.append(self.enemy_spells.sprites())
        returnable.append(self.scene_spells.sprites())

        returnable.append(self.friendly_doodads.sprites())
        returnable.append(self.neutral_doodads.sprites())
        returnable.append(self.enemy_doodads.sprites())
        returnable.append(self.scene_doodads.sprites())

        return returnable

    def get_all_friendly_objects(self):

        returnable = list()

        returnable.append(self.friendly_units.sprites())
        returnable.append(self.friendly_spells.sprites())
        returnable.append(self.friendly_doodads.sprites())

        return returnable

    def get_all_neutral_objects(self):

        returnable = list()

        returnable.append(self.neutral_units.sprites())
        returnable.append(self.neutral_spells.sprites())
        returnable.append(self.neutral_doodads.sprites())

        return returnable

    def get_all_enemy_objects(self):

        returnable = list()

        returnable.append(self.enemy_units.sprites())
        returnable.append(self.enemy_spells.sprites())
        returnable.append(self.enemy_doodads.sprites())

        return returnable

    def get_all_scene_objects(self):

        returnable = list()

        returnable.append(self.scene_units.sprites())
        returnable.append(self.scene_spells.sprites())
        returnable.append(self.scene_doodads.sprites())

        return returnable

    def get_units(self):
        returnable = list()

        returnable.append(self.friendly_units.sprites())
        returnable.append(self.neutral_units.sprites())
        returnable.append(self.enemy_units.sprites())
        returnable.append(self.scene_units.sprites())

        return returnable

    def get_friendly_units(self):
        returnable = list()

        returnable.append(self.friendly_units.sprites())

        return returnable

    def get_neutral_units(self):
        returnable = list()

        returnable.append(self.neutral_units.sprites())

        return returnable

    def get_enemy_units(self):
        returnable = list()

        returnable.append(self.enemy_units.sprites())

        return returnable

    def get_scene_units(self):
        returnable = list()

        returnable.append(self.scene_units.sprites())

        return returnable

    def get_spells(self):

        returnable = list()

        returnable.append(self.friendly_spells.sprites())
        returnable.append(self.neutral_spells.sprites())
        returnable.append(self.enemy_spells.sprites())
        returnable.append(self.scene_spells.sprites())

        return returnable

    def get_friendly_spells(self):
        returnable = list()

        returnable.append(self.friendly_spells.sprites())

        return returnable

    def get_neutral_spells(self):
        returnable = list()

        returnable.append(self.neutral_spells.sprites())

        return returnable

    def get_enemy_spells(self):
        returnable = list()

        returnable.append(self.enemy_spells.sprites())

        return returnable

    def get_scene_spells(self):
        returnable = list()

        returnable.append(self.scene_spells.sprites())

        return returnable

    def get_doodads(self):

        returnable = list()

        returnable.append(self.friendly_doodads.sprites())
        returnable.append(self.neutral_doodads.sprites())
        returnable.append(self.enemy_doodads.sprites())
        returnable.append(self.scene_doodads.sprites())

        return returnable

    def get_friendly_doodads(self):
        returnable = list()

        returnable.append(self.friendly_doodads.sprites())

        return returnable

    def get_neutral_doodads(self):
        returnable = list()

        returnable.append(self.neutral_doodads.sprites())

        return returnable

    def get_enemy_doodads(self):
        returnable = list()

        returnable.append(self.enemy_doodads.sprites())

        return returnable

    def get_scene_doodads(self):
        returnable = list()

        returnable.append(self.scene_doodads.sprites())

        return returnable

    def new_object(self, obj, obj_type, alignment):
        """
        :param obj: Object to be added in to a sprite group.
        :param obj_type: the type of obj, 0 for unit, 1 for spell, 2 for doodad
        :param alignment: the alignment of obj, 0 for friendly, 1 for neutral, 2 for enemy, 3 for scene
        :return: None
        """

        if obj_type == 0:
            if alignment == 0:
                self.friendly_units.add(obj)
            elif alignment == 1:
                self.neutral_units.add(obj)
            elif alignment == 2:
                self.enemy_units.add(obj)
            elif alignment == 3:
                self.scene_units.add(obj)

        elif obj_type == 1:
            if alignment == 0:
                self.friendly_spells.add(obj)
            elif alignment == 1:
                self.neutral_spells.add(obj)
            elif alignment == 2:
                self.enemy_spells.add(obj)
            elif alignment == 3:
                self.scene_spells.add(obj)

        elif obj_type == 2:
            if alignment == 0:
                self.friendly_doodads.add(obj)
            elif alignment == 1:
                self.neutral_doodads.add(obj)
            elif alignment == 2:
                self.enemy_doodads.add(obj)
            elif alignment == 3:
                self.scene_doodads.add(obj)

    def kill_object(self, obj, type=None, alignment=None):

        if type is None and alignment is None:
            obj.kill()

        elif type == 0 and alignment is None:
            self.friendly_units.remove(obj)
            self.enemy_units.remove(obj)
            self.neutral_units.remove(obj)
            self.scene_units.remove(obj)

        elif type == 1 and alignment is None:
            self.friendly_spells.remove(obj)
            self.enemy_spells.remove(obj)
            self.neutral_spells.remove(obj)
            self.scene_spells.remove(obj)

        elif type == 2 and alignment is None:
            self.friendly_doodads.remove(obj)
            self.enemy_doodads.remove(obj)
            self.neutral_doodads.remove(obj)
            self.scene_doodads.remove(obj)

        elif type is None and alignment == 0:
            self.friendly_units.remove(obj)
            self.friendly_spells.remove(obj)
            self.friendly_doodads.remove(obj)

        elif type is None and alignment == 1:
            self.neutral_units.remove(obj)
            self.neutral_spells.remove(obj)
            self.neutral_doodads.remove(obj)

        elif type is None and alignment == 2:
            self.enemy_units.remove(obj)
            self.enemy_spells.remove(obj)
            self.enemy_doodads.remove(obj)

        elif type is None and alignment == 3:
            self.scene_units.remove(obj)
            self.scene_spells.remove(obj)
            self.scene_doodads.remove(obj)

        elif type == 0 and alignment == 0:
            self.friendly_units.remove(obj)

        elif type == 0 and alignment == 1:
            self.neutral_units.remove(obj)

        elif type == 0 and alignment == 2:
            self.enemy_units.remove(obj)

        elif type == 0 and alignment == 3:
            self.scene_units.remove(obj)

        elif type == 1 and alignment == 0:
            self.friendly_spells.remove(obj)

        elif type == 1 and alignment == 1:
            self.neutral_spells.remove(obj)

        elif type == 1 and alignment == 2:
            self.enemy_spells.remove(obj)

        elif type == 1 and alignment == 3:
            self.scene_spells.remove(obj)

        elif type == 2 and alignment == 0:
            self.friendly_doodads.remove(obj)

        elif type == 2 and alignment == 1:
            self.neutral_doodads.remove(obj)

        elif type == 2 and alignment == 2:
            self.enemy_doodads.remove(obj)

        elif type == 2 and alignment == 3:
            self.scene_doodads.remove(obj)

    def collide_objects(self, obj, collide_type, collide_alignment):
        """
        :param obj: The object you are testing if things are colliding with.
        :param collide_type: The type of object you want to know if obj collided with. 0 for unit, 1 for spell,
        2 for doodad.
        :param collide_alignment: The alignment of the object you want to know if obj collided with.
        0 for friendly, 1 for neutral, 2 for enemy, 3 for scene.
        :return: List of objects, empty if no collision.
        """

        pass

    def load_objects(self, instructions):

        pass
