from pico2d import *
import os
import random

os.chdir("D:\\Programming\\Project\\2DGP")


class Dice_Position:
    def __init__(self, idx):
        loop = True
        while loop:
            if idx == 1:
                self.x = 290
                self.y = 417
                loop = False
            elif idx == 2:
                self.x = 363
                self.y = 417
                loop = False
            elif idx == 3:
                self.x = 436
                self.y = 417
                loop = False
            elif idx == 4:
                self.x = 509
                self.y = 417
                loop = False
            elif idx == 5:
                self.x = 290
                self.y = 344
                loop = False
            elif idx == 6:
                self.x = 363
                self.y = 344
                loop = False
            elif idx == 7:
                self.x = 436
                self.y = 344
                loop = False
            elif idx == 8:
                self.x = 509
                self.y = 344
                loop = False
            elif idx == 9:
                self.x = 290
                self.y = 273
                loop = False
            elif idx == 10:
                self.x = 363
                self.y = 273
                loop = False
            elif idx == 11:
                self.x = 436
                self.y = 273
                loop = False
            elif idx == 12:
                self.x = 509
                self.y = 273
                loop = False
            elif idx == 13:
                self.x = 290
                self.y = 200
                loop = False
            elif idx == 14:
                self.x = 363
                self.y = 200
                loop = False
            elif idx == 15:
                self.x = 436
                self.y = 200
                loop = False
            elif idx == 16:
                self.x = 509
                self.y = 200
                loop = False
            else:
                pass


class Buy_Button:
    def __init__(self):
        self.szie = 79
        self.image = load_image("image\\buy_button.png")
        self.x = 400
        self.y = 122
        self.size = 79
        self.mouse = False

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)

    def update(self):
        if self.mouse:
            self.size = 82
        else:
            self.size = 79


class Dice:
    def __init__(self, index):
        self.drag = False
        self.locate = False
        self.level = 0
        self.index = index + 1
        self.image = load_image('image\\fire_dice.png')
        self.bullet = load_image('image\\fire_bullet.png')
        self.position = Dice_Position(self.index)
        self.x = self.position.x
        self.y = self.position.y

    def create(self):
        self.locate = True
        self.level = 1

    def delete(self):
        self.locate = False
        self.level = 0

    def update(self):
        if self.drag:
            i = get_events()
            for event in i:
                if event.type == SDL_MOUSEMOTION:
                    self.x = event.x
                    self.y = 599 - event.y
        elif not self.drag:
            self.go_back()

    def go_back(self):
        self.x = self.position.x
        self.y = self.position.y
        self.drag = False

    def on_drag(self):
        self.drag = True

    def off_drag(self):
        self.drag = False

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


index = 0
x = 0
y = 0


def Create_Dice():
    global dice
    if dice[0].locate and dice[1].locate and dice[2].locate and dice[3].locate and dice[4].locate and \
            dice[5].locate and dice[6].locate and dice[7].locate and dice[8].locate and dice[9].locate and \
            dice[10].locate and \
            dice[11].locate and dice[12].locate and dice[13].locate and dice[14].locate and dice[15].locate:
        return
        pass
    idx = random.randint(0, 15)
    if dice[idx].locate:
        Create_Dice()
        return
    dice[idx].create()


def handle():
    global dice
    global index
    global x
    global y
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            if 365 < event.x < 435 and 599 - 157 < event.y < 599 - 96:
                buy_button.mouse = True
            else:
                buy_button.mouse = False
        if event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:

            if 255 < event.x < 324 and 599 - 452 < event.y < 599 - 383 and dice[0].locate:
                if dice[0].level == dice[index].level and index != 0:
                    dice[index].off_drag()
                    dice[0].level += 1
                    dice[index].delete()

                else:
                    dice[index].off_drag()
                    dice[index].go_back()

            elif 363 - 35 < event.x < 363 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:

                if dice[1].level == dice[index].level and index != 1:
                    dice[index].off_drag()
                    dice[1].level += 1
                    dice[index].delete()

                else:
                    dice[index].off_drag()
                    dice[index].go_back()

            elif 436 - 35 < event.x < 436 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:

                if dice[2].level == dice[index].level and index != 2:
                    dice[index].off_drag()
                    dice[2].level += 1
                    dice[index].delete()
                else:
                    dice[index].off_drag()
                    dice[index].go_back()
            elif 509 - 35 < event.x < 509 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:

                if dice[3].level == dice[index].level and index != 3:
                    dice[index].off_drag()
                    dice[3].level += 1
                    dice[index].delete()
                else:
                    dice[index].off_drag()
                    dice[index].go_back()
            elif 290 - 35 < event.x < 290 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                if dice[4].level == dice[index].level and index != 4:
                    dice[index].off_drag()
                    dice[4].level += 1
                    dice[index].delete()
                else:
                    dice[index].off_drag()
                    dice[index].go_back()
            elif 363 - 35 < event.x < 363 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:

                if dice[5].level == dice[index].level and index != 5:
                    dice[index].off_drag()
                    dice[5].level += 1
                    dice[index].delete()
                else:
                    dice[index].off_drag()
                    dice[index].go_back()
            elif 436 - 35 < event.x < 436 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:

                if dice[6].level == dice[index].level and index != 6:
                    dice[index].off_drag()
                    dice[6].level += 1
                    dice[index].delete()
                else:
                    dice[index].off_drag()
                    dice[index].go_back()
            elif 509 - 35 < event.x < 509 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:

                if dice[7].level == dice[index].level and index != 7:
                    dice[index].off_drag()
                    dice[7].level += 1
                    dice[index].delete()
                else:
                    dice[index].off_drag()
                    dice[index].go_back()
            elif 290 - 35 < event.x < 290 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:

                if dice[8].level == dice[index].level and index != 8:
                    dice[index].off_drag()
                    dice[8].level += 1
                    dice[index].delete()
                else:
                    dice[index].off_drag()
                    dice[index].go_back()
            elif 363 - 35 < event.x < 363 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:

                if dice[9].level == dice[index].level and index != 9:
                    dice[index].off_drag()
                    dice[9].level += 1
                    dice[index].delete()
                else:
                    dice[index].off_drag()
                    dice[index].go_back()
            elif 436 - 35 < event.x < 436 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:

                if dice[10].level == dice[index].level and index != 10:
                    dice[index].off_drag()
                    dice[10].level += 1
                    dice[index].delete()
                else:
                    dice[index].off_drag()
                    dice[index].go_back()
            elif 509 - 35 < event.x < 509 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:

                if dice[11].level == dice[index].level and index != 11:
                    dice[index].off_drag()
                    dice[11].level += 1
                    dice[index].delete()
                else:
                    dice[index].off_drag()
                    dice[index].go_back()
            elif 290 - 35 < event.x < 290 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:

                if dice[12].level == dice[index].level and index != 12:
                    dice[index].off_drag()
                    dice[12].level += 1
                    dice[index].delete()
                else:
                    dice[index].off_drag()
                    dice[index].go_back()
            elif 363 - 35 < event.x < 363 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:

                if dice[13].level == dice[index].level and index != 13:
                    dice[index].off_drag()
                    dice[13].level += 1
                    dice[index].delete()
                else:
                    dice[index].off_drag()
                    dice[index].go_back()
            elif 436 - 35 < event.x < 436 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:

                if dice[14].level == dice[index].level and index != 14:
                    dice[index].off_drag()
                    dice[14].level += 1
                    dice[index].delete()
                else:
                    dice[index].off_drag()
                    dice[index].go_back()
            elif 509 - 35 < event.x < 509 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:

                if dice[15].level == dice[index].level and index != 15:
                    dice[index].off_drag()
                    dice[15].level += 1
                    dice[index].delete()
                else:
                    dice[index].off_drag()
                    dice[index].go_back()
            else:
                dice[index].off_drag()
                dice[index].go_back()
        elif event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:

            for i in range(16):
                dice[i].off_drag()

            if 365 < event.x < 435 and 599 - 157 < event.y < 599 - 96:
                Create_Dice()
            elif 255 < event.x < 324 and 599 - 452 < event.y < 599 - 383:
                if not dice[0].locate:
                    break
                index = 0

                x = dice[0].position.x
                y = dice[0].position.y
                dice[0].on_drag()
            elif 363 - 35 < event.x < 363 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:
                if not dice[1].locate:
                    break
                index = 1

                x = dice[1].position.x
                y = dice[1].position.y
                dice[1].on_drag()
            elif 436 - 35 < event.x < 436 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:
                if not dice[2].locate:
                    break
                index = 2

                x = dice[2].position.x
                y = dice[2].position.y
                dice[2].on_drag()
            elif 509 - 35 < event.x < 509 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:
                if not dice[3].locate:
                    break
                index = 3

                x = dice[3].position.x
                y = dice[3].position.y
                dice[3].on_drag()
            elif 290 - 35 < event.x < 290 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                if not dice[4].locate:
                    break
                index = 4

                x = dice[4].position.x
                y = dice[4].position.y
                dice[4].on_drag()
            elif 363 - 35 < event.x < 363 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                if not dice[5].locate:
                    break
                index = 5

                x = dice[5].position.x
                y = dice[5].position.y
                dice[5].on_drag()
            elif 436 - 35 < event.x < 436 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                if not dice[6].locate:
                    break
                index = 6

                x = dice[6].position.x
                y = dice[6].position.y
                dice[6].on_drag()
            elif 509 - 35 < event.x < 509 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                if not dice[7].locate:
                    break
                index = 7

                x = dice[7].position.x
                y = dice[7].position.y
                dice[7].on_drag()
            elif 290 - 35 < event.x < 290 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                if not dice[8].locate:
                    break
                index = 8

                x = dice[8].position.x
                y = dice[8].position.y
                dice[8].on_drag()
            elif 363 - 35 < event.x < 363 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                if not dice[9].locate:
                    break
                index = 9

                x = dice[9].position.x
                y = dice[9].position.y
                dice[9].on_drag()
            elif 436 - 35 < event.x < 436 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                if not dice[10].locate:
                    break
                index = 10

                x = dice[10].position.x
                y = dice[10].position.y
                dice[10].on_drag()
            elif 509 - 35 < event.x < 509 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                if not dice[11].locate:
                    break
                index = 11

                x = dice[11].position.x
                y = dice[11].position.y
                dice[11].on_drag()
            elif 290 - 35 < event.x < 290 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                if not dice[12].locate:
                    break
                index = 12

                x = dice[12].position.x
                y = dice[12].position.y
                dice[12].on_drag()

            elif 363 - 35 < event.x < 363 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                if not dice[13].locate:
                    break
                index = 13

                x = dice[13].position.x
                y = dice[13].position.y
                dice[13].on_drag()

            elif 436 - 35 < event.x < 436 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                if not dice[14].locate:
                    break
                index = 14

                x = dice[14].position.x
                y = dice[14].position.y
                dice[14].on_drag()

            elif 509 - 35 < event.x < 509 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                if not dice[15].locate:
                    break
                index = 15

                x = dice[15].position.x
                y = dice[15].position.y
                dice[15].on_drag()


running = True

open_canvas(800, 600)

buy_button = Buy_Button()
background = load_image("image\\background.png")
dice = [Dice(i) for i in range(16)]

while running:

    clear_canvas()

    handle()
    background.draw(400, 300)
    buy_button.draw()
    for d in dice:
        if not d.drag:
            d.draw()
    for d in dice:
        if d.drag:
            d.draw()
    buy_button.update()
    for d in dice:
        d.update()
    update_canvas()

    # delay(0.05)

close_canvas()
