from pico2d import *
import object


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
        self.exist = False
        self.level = 0
        self.index = index + 1
        self.image = load_image('image\\fire_dice.png')
        self.bullet = load_image('image\\fire_bullet.png')
        self.position = Dice_Position(self.index)
        self.x = self.position.x
        self.y = self.position.y
        self.timer = 0

    def create(self):
        self.exist = True
        self.level = 1
        self.timer = 0

    def delete(self):
        self.exist = False
        self.level = 0
        self.timer = 0

    def update(self):
        if self.exist:
            self.timer = (self.timer + 1) % 1000
            if self.timer == 0:
                self.attack(self, object.bring_object(0, 0))
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
        if self.exist:
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

    def attack(self, dice, target):
        if self.exist:
            if self.level == 1:
                bullet = Bullet(self.x + 2, self.y)
                object.add_object(bullet, 1)
                pass
            elif self.level == 2:
                bullet = Bullet(self.x + 15 + 2, self.y + 15)
                object.add_object(bullet, 1)
                bullet = Bullet(self.x - 15 + 2, self.y - 15)
                object.add_object(bullet, 1)
                pass
            elif self.level == 3:
                bullet = Bullet(self.x + 15 + 2, self.y + 15)
                object.add_object(bullet, 1)
                bullet = Bullet(self.x - 15 + 2, self.y - 15)
                object.add_object(bullet, 1)
                bullet = Bullet(self.x + 2, self.y)
                object.add_object(bullet, 1)
                pass
            elif self.level == 4:
                bullet = Bullet(self.x + 15 + 2, self.y + 15)
                object.add_object(bullet, 1)
                bullet = Bullet(self.x - 15 + 2, self.y - 15)
                object.add_object(bullet, 1)
                bullet = Bullet(self.x - 15 + 2, self.y + 15)
                object.add_object(bullet, 1)
                bullet = Bullet(self.x + 15 + 2, self.y - 15)
                object.add_object(bullet, 1)
                pass
            elif self.level == 5:
                bullet = Bullet(self.x + 2, self.y)
                object.add_object(bullet, 1)
                bullet = Bullet(self.x + 15 + 2, self.y + 15)
                object.add_object(bullet, 1)
                bullet = Bullet(self.x - 15 + 2, self.y - 15)
                object.add_object(bullet, 1)
                bullet = Bullet(self.x - 15 + 2, self.y + 15)
                object.add_object(bullet, 1)
                bullet = Bullet(self.x + 15 + 2, self.y - 15)
                object.add_object(bullet, 1)
                pass
            elif self.level == 6:
                bullet = Bullet(self.x + 15 + 2, self.y + 15)
                object.add_object(bullet, 1)
                bullet = Bullet(self.x - 15 + 2, self.y - 15)
                object.add_object(bullet, 1)
                bullet = Bullet(self.x - 15 + 2, self.y + 15)
                object.add_object(bullet, 1)
                bullet = Bullet(self.x + 15 + 2, self.y - 15)
                object.add_object(bullet, 1)
                bullet = Bullet(self.x - 15 + 2, self.y)
                object.add_object(bullet, 1)
                bullet = Bullet(self.x + 15 + 2, self.y)
                object.add_object(bullet, 1)
                pass
        pass


class Bullet:

    def __init__(self, x, y):
        self.image = load_image("image\\fire_bullet.png")
        self.timer = 0
        self.speed = 0
        self.x = x
        self.y = y

    def fire(self, target):
        t = self.speed / 100
        self.x = (1 - t) * self.x + t * target.x
        self.y = (1 - t) * self.y + t * target.y
        self.image.draw(self.x, self.y, 95, 95)

    def draw(self):
        self.image.draw(self.x, self.y, 95, 95)

    def update(self):
        self.timer = (self.timer + 1) % 1000

        if self.timer % 20 == 0:
            self.speed += 1
            self.fire(object.bring_object(0, 0))
        if object.bring_object(0, 0).x - 30 < self.x < object.bring_object(0, 0).x + 30 and \
                object.bring_object(0, 0).y - 30 < self.y < object.bring_object(0, 0).y + 30:
            object.remove_object(self)
            object.bring_object(0, 0).hp -= 100
