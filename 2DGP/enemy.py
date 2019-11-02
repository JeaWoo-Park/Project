from pico2d import *
import random
import object
from life import Life


class Enemy:
    image = None
    slow_effect = None
    life = None

    def __init__(self):
        if Enemy.life is None:
            Enemy.life = Life()
        if Enemy.image is None:
            Enemy.image = load_image("image\\enemy.png")
        if Enemy.slow_effect is None:
            Enemy.slow_effect = load_image("image\\slow_enemy.png")
        self.x = 124
        self.y = 100
        self.speed = 0.2
        self.drawing_slow_effect = False

    def draw(self):
        self.image.draw(self.x, self.y, 110, 110)
        if self.drawing_slow_effect:
            self.slow_effect.draw(self.x, self.y - 5, 110, 110)
        Enemy.life.draw()

    def slow(self):
        self.speed = 0.15
        self.drawing_slow_effect = True

    def die(self):
        object.remove_object(self)

    def update(self):
        if self.y > 514:
            self.y = 514
        if self.x > 674:
            self.x = 674
        if self.x == 124 and self.y < 514:
            self.y += self.speed
        elif self.y == 514 and self.x < 674:
            self.x += self.speed
        elif self.x == 674 and self.y > 100:
            self.y -= self.speed

        if self.x == 674 and self.y < 100:
            object.remove_object(self)
            Enemy.life.hp -= 1

