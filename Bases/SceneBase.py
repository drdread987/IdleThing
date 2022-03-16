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

    def process_input(self, events, pressed_keys):
        self.interactive_events = events
        for event in self.interactive_events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.OH.OEH.event(40, event.button, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            elif event.type == pygame.MOUSEBUTTONUP:
                self.OH.OEH.event(41, event.button, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            elif event.type == pygame.MOUSEMOTION:
                self.OH.OEH.event(42, event.buttons, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        modifiers = []
        for key in pressed_keys:
            if key == pygame.K_LALT or key == pygame.K_RALT:
                modifiers.append('ALT')
            elif key == pygame.K_LSHIFT or key == pygame.K_RSHIFT:
                modifiers.append('SHIFT')
            elif key == pygame.K_LCTRL or key == pygame.K_RCTRL:
                modifiers.append('CONTROL')
        for key in self.pressed_keys:
            if key == pygame.K_LALT or key == pygame.K_RALT:
                modifiers.append('ALT')
            elif key == pygame.K_LSHIFT or key == pygame.K_RSHIFT:
                modifiers.append('SHIFT')
            elif key == pygame.K_LCTRL or key == pygame.K_RCTRL:
                modifiers.append('CONTROL')
        for key in pressed_keys:
            if key not in self.pressed_keys:
                self.OH.OEH.event(43, key, modifiers)
        for key in self.pressed_keys:
            if key not in pressed_keys:
                self.OH.OEH.event(44, key, modifiers)

        self.pressed_keys = pressed_keys

    def update(self, screen):
        self.OH.update_objects(screen, self.interactive_events, self.pressed_keys)

    def render(self, screen):
        self.OH.draw_objects(screen)

    def switch_to_scene(self, next_scene):
        self.next = next_scene

    def terminate(self):
        self.switch_to_scene(None)
