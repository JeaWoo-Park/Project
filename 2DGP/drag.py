from pico2d import *
import os
import random

os.chdir("D:\\Programming\\Project\\2DGP")

class Locate:
    def __init__(self):
        self.location = False
        self.dice = None


class Dice:
    def __init__(self):
        global location
        self.level = 1
        self.image = load_image('image\\fire_dice.png')
        self.bullet = load_image('image\\fire_bullet.png')
        loop = True
        while loop:
            self.location = random.randint(0, 15)
            if self.location == 1 and location[0] == False:
                self.x = 290
                self.y = 417
                location[0] = True
                loop = False
            elif self.location == 2 and location[1] == False:
                self.x = 363
                self.y = 417
                location[1] = True
                loop = False
            elif self.location == 3 and location[2] == False:
                self.x = 436
                self.y = 417
                location[2] = True
                loop = False
            elif self.location == 4 and location[3] == False:
                self.x = 509
                self.y = 417
                location[3] = True
                loop = False
            elif self.location == 5 and location[4] == False:
                self.x = 290
                self.y = 344
                location[4] = True
                loop = False
            elif self.location == 6 and location[5] == False:
                self.x = 363
                self.y = 344
                location[5] = True
                loop = False
            elif self.location == 7 and location[6] == False:
                self.x = 436
                self.y = 344
                location[6] = True
                loop = False
            elif self.location == 8 and location[7] == False:
                self.x = 509
                self.y = 344
                location[7] = True
                loop = False
            elif self.location == 9 and location[8] == False:
                self.x = 290
                self.y = 273
                location[8] = True
                loop = False
            elif self.location == 10 and location[9] == False:
                self.x = 363
                self.y = 273
                location[9] = True
                loop = False
            elif self.location == 11 and location[10] == False:
                self.x = 436
                self.y = 273
                location[10] = True
                loop = False
            elif self.location == 12 and location[11] == False:
                self.x = 509
                self.y = 273
                location[11] = True
                loop = False
            elif self.location == 13 and location[12] == False:
                self.x = 290
                self.y = 200
                location[12] = True
                loop = False
            elif self.location == 14 and location[13] == False:
                self.x = 363
                self.y = 200
                location[13] = True
                loop = False
            elif self.location == 15 and location[14] == False:
                self.x = 436
                self.y = 200
                location[14] = True
                loop = False
            elif self.location == 16 and location[15] == False:
                self.x = 509
                self.y = 200
                location[15] = True
                loop = False
            else:
                pass

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
            if location[0]:
                pass


location = [False for i in range(16)]
running = True

open_canvas(800, 600)

background = load_image("image\\background.png")
dice_1 = Dice()
dice_3 = Dice()
dice_2 = Dice()
dice_4 = Dice()
dice_5 = Dice()
while running:
    handle()
    clear_canvas()
    background.draw(400, 300)
    dice_1.draw()
    dice_2.draw()
    dice_3.draw()
    dice_4.draw()
    dice_5.draw()
    update_canvas()

    delay(0.05)
close_canvas()
