from pico2d import *
import game_framework
import start_state

time = 0
image = None
music = None


def enter():
    global image, music
    image = load_image('image\\win.png')
    music = load_music('sound\\victory.mp3')
    music.set_volume(100)
    music.play()
    pass


def exit():
    global image, music
    del music
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
