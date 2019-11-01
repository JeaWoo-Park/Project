from pico2d import *
import random
import object

class Enemy:
    image = None

    def __init__(self):
        if Enemy.image is None:
            Enemy.image = load_image("image\\enemy.png")
        self.x = 124
        self.y = 100
        self.speed = 0.2

    def draw(self):
        self.image.draw(self.x, self.y, 110, 110)

    def slow(self):
        self.speed = 0.15

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
