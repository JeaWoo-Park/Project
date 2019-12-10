from pico2d import *
import game_framework
import reset_state
import start_state

image = None
time = 0
music = None
def enter():
    global image
    global music
    music = load_music('sound\\game-lost.ogg')
    music.set_volume(60)
    music.play()
    image = load_image('image\\lose.png')
    pass


def exit():
    global image
    del image
    pass


def update():
    global time
    time += 1
    if time == 300:
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
