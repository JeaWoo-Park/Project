from pico2d import *
import object
import dice_manager


class Poison_Dice:
    def __init__(self, index):
        self.drag = False
        self.level = 1
        self.index = index + 1
        self.image = load_image('image\\poison_dice.png')
        self.bullet = load_image('image\\poison_bullet.png')
        self.position = dice_manager.DicePosition(self.index)
        self.x = self.position.x
        self.y = self.position.y
        self.timer = 0

    def update(self):

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

        if self.level == 1:
            self.image.draw(self.x, self.y, 95, 95)
            self.bullet.draw(self.x + 2, self.y, 95, 95)
        elif self.level == 2:
            self.image.draw(self.x, self.y, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y + 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y - 15, 95, 95)
        elif self.level == 3:
            self.image.draw(self.x, self.y, 95, 95)
            self.bullet.draw(self.x + 2, self.y, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y + 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y - 15, 95, 95)
        elif self.level == 4:
            self.image.draw(self.x, self.y, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y + 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y - 15, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y - 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y + 15, 95, 95)
        elif self.level == 5:
            self.image.draw(self.x, self.y, 95, 95)
            self.bullet.draw(self.x + 2, self.y, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y + 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y - 15, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y - 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y + 15, 95, 95)
        elif self.level == 6:
            self.image.draw(self.x, self.y, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y + 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y - 15, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y - 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y + 15, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y, 95, 95)

    def attack(self, dice, target):

        if self.level == 1:
            bullet = Poison_Bullet(self.x + 2, self.y)
            object.add_object(bullet, 1)
            pass
        elif self.level == 2:
            bullet = Poison_Bullet(self.x + 15 + 2, self.y + 15)
            object.add_object(bullet, 1)
            bullet = Poison_Bullet(self.x - 15 + 2, self.y - 15)
            object.add_object(bullet, 1)
            pass
        elif self.level == 3:
            bullet = Poison_Bullet(self.x + 15 + 2, self.y + 15)
            object.add_object(bullet, 1)
            bullet = Poison_Bullet(self.x - 15 + 2, self.y - 15)
            object.add_object(bullet, 1)
            bullet = Poison_Bullet(self.x + 2, self.y)
            object.add_object(bullet, 1)
            pass
        elif self.level == 4:
            bullet = Poison_Bullet(self.x + 15 + 2, self.y + 15)
            object.add_object(bullet, 1)
            bullet = Poison_Bullet(self.x - 15 + 2, self.y - 15)
            object.add_object(bullet, 1)
            bullet = Poison_Bullet(self.x - 15 + 2, self.y + 15)
            object.add_object(bullet, 1)
            bullet = Poison_Bullet(self.x + 15 + 2, self.y - 15)
            object.add_object(bullet, 1)
            pass
        elif self.level == 5:
            bullet = Poison_Bullet(self.x + 2, self.y)
            object.add_object(bullet, 1)
            bullet = Poison_Bullet(self.x + 15 + 2, self.y + 15)
            object.add_object(bullet, 1)
            bullet = Poison_Bullet(self.x - 15 + 2, self.y - 15)
            object.add_object(bullet, 1)
            bullet = Poison_Bullet(self.x - 15 + 2, self.y + 15)
            object.add_object(bullet, 1)
            bullet = Poison_Bullet(self.x + 15 + 2, self.y - 15)
            object.add_object(bullet, 1)
            pass
        elif self.level == 6:
            bullet = Poison_Bullet(self.x + 15 + 2, self.y + 15)
            object.add_object(bullet, 1)
            bullet = Poison_Bullet(self.x - 15 + 2, self.y - 15)
            object.add_object(bullet, 1)
            bullet = Poison_Bullet(self.x - 15 + 2, self.y + 15)
            object.add_object(bullet, 1)
            bullet = Poison_Bullet(self.x + 15 + 2, self.y - 15)
            object.add_object(bullet, 1)
            bullet = Poison_Bullet(self.x - 15 + 2, self.y)
            object.add_object(bullet, 1)
            bullet = Poison_Bullet(self.x + 15 + 2, self.y)
            object.add_object(bullet, 1)
            pass


class Poison_Bullet:

    def __init__(self, x, y):
        self.image = load_image("image\\poison_bullet.png")
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
