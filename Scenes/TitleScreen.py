from Bases.SceneBase import SceneBase
import pygame
from Tools.Images import ImageEnum


class TitleScene(SceneBase):
    def __init__(self, il):
        SceneBase.__init__(self, il)

        self.scene_background = self.IL.load_image(ImageEnum.TitleBackground)
        self.environment_type = "MENU"

    def process_input(self, events, pressed_keys):
        SceneBase.process_input(self, events, pressed_keys)

    def render(self, screen):
        screen.blit(self.scene_background, (0, 0))
        SceneBase.render(self, screen)

