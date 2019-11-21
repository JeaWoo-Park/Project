from pico2d import *
import game_framework

image = None
time = 0

def enter():
    global image
    image = load_image('image\\lose.png')
    pass


def exit():
    global image
    del image
    pass


def update():
    global time
    time += 1
    if time == 3000:
        game_framework.quit()
    pass


def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    pass


def handle_events():
    pass


def pause(): pass


def resume(): pass
