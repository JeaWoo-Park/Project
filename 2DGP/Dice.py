from pico2d import *


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