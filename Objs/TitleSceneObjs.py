from Bases.BaseObjects import BaseUnit
from Bases.BaseObjects import BaseDoodad
from Tools.Images import ImageEnum
import pygame


class NormalSquare(BaseUnit):

    def __init__(self, oh, il, x, y):
        BaseUnit.__init__(self, oh, il, x, y)

        self.image = il.load_image(ImageEnum.Bush)
        self.width = 75
        self.height = 75
        self.update_rect()
        self.set_events(oh)

        self.max_health_points = 50
        self.health_points = self.max_health_points

        self.speed = 2
        self.a = False
        self.d = False
        self.w = False
        self.s = False

        self.unit_id = 1

    def set_events(self, oh):

        oh.OEH.add_listener(43, self, self.on_key_press, 0)
        oh.OEH.add_listener(44, self, self.on_key_up, 0)
        oh.OEH.add_listener(40, self, self.on_click, 0)

    def on_key_press(self, key, mod):

        if key == pygame.K_w:
            self.on_w()
        elif key == pygame.K_s:
            self.on_s()
        elif key == pygame.K_a:
            self.on_a()
        elif key == pygame.K_d:
            self.on_d()

    def on_key_up(self, key, mod):

        if key == pygame.K_w:
            self.on_w_up()
        elif key == pygame.K_s:
            self.on_s_up()
        elif key == pygame.K_a:
            self.on_a_up()
        elif key == pygame.K_d:
            self.on_d_up()

    def on_w(self):

        self.w = True

    def on_w_up(self):

        self.w = False

    def on_s(self):

        self.s = True

    def on_s_up(self):

        self.s = False

    def on_a(self):

        self.a = True

    def on_a_up(self):

        self.a = False

    def on_d(self):

        self.d = True

    def on_d_up(self):

        self.d = False

    def on_click(self, button, x, y):

        pass

    def update(self, scene, i_events, inputs):

        super().update(scene, i_events, inputs)

        horizontal = 0
        vertical = 0

        if self.a:
            horizontal = -self.speed
        if self.d:
            horizontal = self.speed
        if self.d and self.a:
            horizontal = 0
        if self.w:
            vertical = -self.speed
        if self.s:
            vertical = self.speed
        if self.w and self.s:
            vertical = 0
        if (abs(horizontal) + abs(vertical)) > self.speed:
            horizontal = horizontal // ((abs(horizontal) + abs(vertical)) / self.speed)
            vertical = vertical // ((abs(horizontal) + abs(vertical)) / self.speed)

        self.x += horizontal
        self.y += vertical

        collides_enemy_doodad = self.oh.collide_objects(self, 2, 2)
        for col in collides_enemy_doodad:
            self.take_damage("NATURE", 1, self, self.oh)


class NormalBlock(BaseDoodad):

    def __init__(self, oh, il, x, y):
        super().__init__(oh, il, x, y)

        self.image = il.load_image(ImageEnum.Bush)
        self.width = 75
        self.height = 75
        self.update_rect()
        self.doodad_type = 1
        self.doodad_id = 1

    def update(self, scene, i_events, inputs):

        super().update(scene, i_events, inputs)
