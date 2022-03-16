from Bases.BaseObjects import BaseUnit
from Tools.Images import ImageEnum
import pygame


class NormalSquare(BaseUnit):

    def __init__(self, oh, il, x, y):
        BaseUnit.__init__(self, oh, il, x, y)

        self.image = il.load_image(ImageEnum.Bush)
        self.set_events(oh)

    def set_events(self, oh):

        oh.OEH.add_listener(43, self, self.on_key_press, 0)

    def on_key_press(self, key, mod):

        print("GOT EVENT!!!", key, mod)
        if key == pygame.K_w:
            self.on_w()
        elif key == pygame.K_s:
            self.on_s()

    def on_w(self):

        self.y -= 1

    def on_s(self):

        self.y += 1
