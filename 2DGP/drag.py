from pico2d import *
import os
import random

os.chdir("D:\\Programming\\Project\\2DGP")


class Dice:
    def __init__(self, index):
        self.locate = False
        self.level = 1
        self.index = index + 1
        self.image = load_image('image\\fire_dice.png')
        self.bullet = load_image('image\\fire_bullet.png')
        loop = True
        while loop:
            if self.index == 1:
                self.x = 290
                self.y = 417
                loop = False
            elif self.index == 2:
                self.x = 363
                self.y = 417
                loop = False
            elif self.index == 3:
                self.x = 436
                self.y = 417
                loop = False
            elif self.index == 4:
                self.x = 509
                self.y = 417
                loop = False
            elif self.index == 5:
                self.x = 290
                self.y = 344
                loop = False
            elif self.index == 6:
                self.x = 363
                self.y = 344
                loop = False
            elif self.index == 7:
                self.x = 436
                self.y = 344
                loop = False
            elif self.index == 8:
                self.x = 509
                self.y = 344
                loop = False
            elif self.index == 9:
                self.x = 290
                self.y = 273
                loop = False
            elif self.index == 10:
                self.x = 363
                self.y = 273
                loop = False
            elif self.index == 11:
                self.x = 436
                self.y = 273
                loop = False
            elif self.index == 12:
                self.x = 509
                self.y = 273
                loop = False
            elif self.index == 13:
                self.x = 290
                self.y = 200
                loop = False
            elif self.index == 14:
                self.x = 363
                self.y = 200
                loop = False
            elif self.index == 15:
                self.x = 436
                self.y = 200
                loop = False
            elif self.index == 16:
                self.x = 509
                self.y = 200
                loop = False
            else:
                pass

    def create(self):
        self.locate = True

    def delete(self):
        self.locate = False

    def draw(self):
        if self.locate:
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
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if 255 < event.x < 324 and 599 - 452 < event.y < 599 - 383:
                dice[0].delete()
            elif 363 - 35 < event.x < 363 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:
                dice[1].delete()
            elif 436 - 35 < event.x < 436 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:
                dice[2].delete()
            elif 509 - 35 < event.x < 509 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:
                dice[3].delete()
            elif 290 - 35 < event.x < 290 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                dice[4].delete()
            elif 363 - 35 < event.x < 363 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                dice[5].delete()
            elif 436 - 35 < event.x < 436 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                dice[6].delete()
            elif 509 - 35 < event.x < 509 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                dice[7].delete()
            elif 290 - 35 < event.x < 290 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                dice[8].delete()
            elif 363 - 35 < event.x < 363 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                dice[9].delete()
            elif 436 - 35 < event.x < 436 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                dice[10].delete()
            elif 509 - 35 < event.x < 509 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                dice[11].delete()
            elif 290 - 35 < event.x < 290 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                dice[12].delete()
            elif 363 - 35 < event.x < 363 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                dice[13].delete()
            elif 436 - 35 < event.x < 436 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                dice[14].delete()
            elif 509 - 35 < event.x < 509 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                dice[15].delete()




running = True

open_canvas(800, 600)

background = load_image("image\\background.png")
dice = [Dice(i) for i in range(16)]
for i in range(16):
    dice[i].create()
while running:
    handle()
    clear_canvas()
    background.draw(400, 300)
    for d in dice:
        d.draw()
    update_canvas()

    delay(0.05)
close_canvas()
