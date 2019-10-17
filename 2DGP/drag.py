from pico2d import *
import random


class Dice:
    def __init__(self):
        self.level = 1
        self.image = load_image("fire_dice.png")
        self.bullet = load_image("fire_bullet.png")
        self.x = 100
        self.y = 100

    def draw(self):
        self.image.draw(self.x, self.y)
        if self.level == 1:
            self.bullet.draw(self. x, self. y)
        #elif self.level == 2:

        #elif self.level == 3:

        #elif self.level == 4:

        #elif self.level == 5:

        #elif self.level == 6:




def handle():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


running = True
#background = load_image("background.png")
dice1 = Dice()
dice2 = Dice()
open_canvas(800, 600)
while running:
    clear_canvas()
 #   background.draw(400, 300)
    dice1.draw()
    dice2.draw()
    update_canvas()
