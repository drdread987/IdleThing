import Bases.ObjectHandler
import pygame


class SceneBase:
    def __init__(self, il):
        self.next = self
        self.IL = il
        self.OH = Bases.ObjectHandler.ObjectHandler()
        self.interactive_events = None
        self.pressed_keys = []
        self.environment_type = "DEFAULT"

    def process_input(self, events, pressed_keys_n):
        self.interactive_events = events
        for event in self.interactive_events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.OH.OEH.event(40, event.button, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            elif event.type == pygame.MOUSEBUTTONUP:
                self.OH.OEH.event(41, event.button, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            elif event.type == pygame.MOUSEMOTION:
                self.OH.OEH.event(42, event.buttons, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        modifiers = []
        if pygame.K_LALT in pressed_keys_n or pygame.K_RALT in pressed_keys_n:
            modifiers.append('ALT')
        if pygame.K_LSHIFT in pressed_keys_n or pygame.K_RSHIFT in pressed_keys_n:
            modifiers.append('SHIFT')
        if pygame.K_LCTRL in pressed_keys_n or pygame.K_RCTRL in pressed_keys_n:
            modifiers.append('CONTROL')

        for key in pressed_keys_n:
            self.OH.OEH.event(43, key, modifiers)
        for key in self.pressed_keys:
            if key not in pressed_keys_n:
                self.OH.OEH.event(44, key, modifiers)

        self.pressed_keys = list(pressed_keys_n)

    def update(self, screen):
        self.OH.update_objects(screen, self.interactive_events, self.pressed_keys)

    def render(self, screen):
        self.OH.draw_objects(screen)

    def switch_to_scene(self, next_scene):
        self.next = next_scene

    def terminate(self):
        self.switch_to_scene(None)
