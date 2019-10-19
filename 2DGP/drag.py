from pico2d import *
import os
import random

os.chdir("D:\\Programming\\Project\\2DGP")


class Dice:
    def __init__(self):
        self.level = 1
        self.image = load_image('image\\fire_dice.png')
        self.bullet = load_image('image\\fire_bullet.png')
        self.x = 509
        self.y = 417
        self.location = random.randint(0, 15)
        if self.location == 1:
            self.x = 290
            self.y = 417
        elif self.location == 2:
            self.x = 363
            self.y = 417
        elif self.location == 3:
            self.x = 436
            self.y = 417
        elif self.location == 4:
            self.x = 509
            self.y = 417
        elif self.location == 5:
            self.x = 290
            self.y = 344
        elif self.location == 6:
            self.x = 363
            self.y = 344
        elif self.location == 7:
            self.x = 436
            self.y = 344
        elif self.location == 8:
            self.x = 509
            self.y = 344
        elif self.location == 9:
            self.x = 290
            self.y = 273
        elif self.location == 10:
            self.x = 363
            self.y = 273
        elif self.location == 11:
            self.x = 436
            self.y = 273
        elif self.location == 12:
            self.x = 509
            self.y = 273
        elif self.location == 13:
            self.x = 290
            self.y = 200
        elif self.location == 14:
            self.x = 363
            self.y = 200
        elif self.location == 15:
            self.x = 436
            self.y = 200
        elif self.location == 16:
            self.x = 509
            self.y = 200

    def draw(self):
        self.image.draw(self.x, self.y, 95, 95)
        if self.level == 1:
            self.bullet.draw(self.x + 2, self.y, 95, 95)
        elif self.level == 2:
            self.bullet.draw(self.x + 15 + 2, self.y + 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y - 15, 95, 95)
        elif self.level == 3:
            self.bullet.draw(self.x + 2, self.y, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y + 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y - 15, 95, 95)
        elif self.level == 4:
            self.bullet.draw(self.x + 15 + 2, self.y + 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y - 15, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y - 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y + 15, 95, 95)
        elif self.level == 5:
            self.bullet.draw(self.x + 2, self.y, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y + 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y - 15, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y - 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y + 15, 95, 95)
        elif self.level == 6:
            self.bullet.draw(self.x + 15 + 2, self.y + 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y - 15, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y - 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y + 15, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y, 95, 95)


def handle():
    global location
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.key == SDL_BUTTON_LEFT:
            pass


location = [False for i in range(16)]
running = True

open_canvas(800, 600)

background = load_image("image\\background.png")
dice_1 = Dice()
dice_2 = Dice()

while running:
    handle()
    clear_canvas()
    background.draw(400, 300)
    dice_1.draw()
    dice_2.draw()
    update_canvas()

    delay(0.05)
close_canvas()
