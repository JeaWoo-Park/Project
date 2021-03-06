from pico2d import *
import game_framework
import main

image = None
music = None
help_image = None
time = 0
draw_help = False

def enter():
    global image, music, help_image
    help_image = load_image('image\\help.png')
    image = load_image('image\\start_image.png')
    music = load_music('sound\\menu.mp3')
    music.set_volume(80)
    music.repeat_play()
    pass


def exit():
    global image, music
    music.stop()
    del image
    del music
    pass


def update():
    pass


def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    if draw_help:
        help_image.draw(400, 300)
    update_canvas()
    pass


def handle_events():
    global draw_help
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            if 274 < event.x < 523 and 599 - 280 < event.y < 599 - 217 and not draw_help:
                game_framework.change_state(main)
            elif 274 < event.x < 523 and 599 - 135 < event.y < 599 - 72 and not draw_help:
                game_framework.quit()
            elif 274 < event.x < 523 and 599 - 206 < event.y < 599 - 143 and not draw_help:
                draw_help = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            draw_help = False
    pass


def pause(): pass


def resume(): pass