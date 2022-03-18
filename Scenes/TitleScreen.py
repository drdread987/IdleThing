from Bases.SceneBase import SceneBase
import pygame
from Tools.Images import ImageEnum
from Objs import TitleSceneObjs


class TitleScene(SceneBase):
    def __init__(self, il):
        SceneBase.__init__(self, il)

        self.scene_background = self.IL.load_image(ImageEnum.TitleBackground)
        self.environment_type = "MENU"

        self.OH.new_object(TitleSceneObjs.NormalSquare(self.OH, self.IL, 0, 0), 0, 0)
        for x in range(500):
            self.OH.new_object(TitleSceneObjs.NormalBlock(self.OH, self.IL, 250, 250), 2, 1)

    def process_input(self, events, pressed_keys):
        SceneBase.process_input(self, events, pressed_keys)

    def render(self, screen):
        screen.blit(self.scene_background, (0, 0))
        SceneBase.render(self, screen)

