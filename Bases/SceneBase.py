
class SceneBase:
    def __init__(self, il):
        self.next = self
        self.IL = il

    def process_input(self, events, pressed_keys):
        pass

    def update(self):
        pass

    def render(self, screen):
        pass

    def switch_to_scene(self, next_scene):
        self.next = next_scene

    def terminate(self):
        self.switch_to_scene(None)
