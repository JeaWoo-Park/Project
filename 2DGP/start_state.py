from pico2d import *
import game_framework
import main

image = None
music = None
time = 0

def enter():
    global image, music
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
    update_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            if 274 < event.x < 523 and 599 - 280 < event.y < 599 - 217:
                game_framework.change_state(main)
            elif 274 < event.x < 523 and 599 - 135 < event.y < 599 - 72:
                game_framework.quit()
    pass


def pause(): pass


def resume(): pass