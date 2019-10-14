from enum import Enum
import os.path
from pygame import image


class ImageLoader:

    def __init__(self):
        self.images = {}

    def load_image(self, load_image):
        if load_image.name in self.images:
            return self.images[load_image.name]
        else:
            self._retrieve_image(load_image)
            return self.images[load_image.name]

    def _retrieve_image(self, load_image):
        if os.path.isfile(load_image.value):
            self.images[load_image.name] = image.load(load_image.value)
        else:
            self.images[load_image.name] = image.load(ImageEnum.DNE.value)

    def _delete_image(self, load_image):
        del self.images[load_image]


class ImageEnum(Enum):

    TitleBackground = "resources/backgrounds/Title_screen_background.png"
    DNE = "resources/DNE.png"
