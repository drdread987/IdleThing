from Scenes.TitleScreen import TitleScene
import pygame
import Tools.Images
import datetime


def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    current_time = datetime.datetime.now()
    time_passed = datetime.datetime.now() - current_time
    active_scene = starting_scene
    pressed_keys = []
    frames = 0
    while active_scene is not None:

        new_time = datetime.datetime.now()
        time_passed += new_time - current_time
        current_time = new_time
        frames += 1
        if time_passed > datetime.timedelta(seconds=1):
            print("FPS: " + str(frames))
            frames = 0
            time_passed = datetime.timedelta(seconds=0)
        # event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pygame.K_LALT in pressed_keys or pygame.K_RALT in pressed_keys
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
                elif event.key not in pressed_keys:
                    pressed_keys.append(event.key)
            elif event.type == pygame.KEYUP:
                if event.key in pressed_keys:
                    pressed_keys.remove(event.key)

            if quit_attempt:
                active_scene.terminate()
            else:
                filtered_events.append(event)

        active_scene.process_input(filtered_events, pressed_keys)
        active_scene.update(screen)
        active_scene.render(screen)

        active_scene = active_scene.next

        pygame.display.flip()
        clock.tick(fps)


il = Tools.Images.ImageLoader()
run_game(1200, 800, 60, TitleScene(il))
