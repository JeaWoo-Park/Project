from pico2d import *
import object
import life


class Enemy:
    image = None
    slow_effect = None
    poison_effect = None

    def __init__(self):
        if Enemy.poison_effect is None:
            Enemy.poison_effect = load_image("image\\poison_enemy.png")
        if Enemy.image is None:
            Enemy.image = load_image("image\\enemy.png")
        if Enemy.slow_effect is None:
            Enemy.slow_effect = load_image("image\\slow_enemy.png")
        self.x = 124
        self.y = 100
        self.speed = 0.2
        self.hp = 500
        self.drawing_slow_effect = False
        self.poison = False

    def draw(self):
        self.image.draw(self.x, self.y, 110, 110)
        if self.drawing_slow_effect:
            self.slow_effect.draw(self.x, self.y - 5, 110, 110)

    def slow(self):
        self.speed = 0.15
        self.drawing_slow_effect = True

    def die(self):
        object.remove_object(self)
        object.remove_layer(1)

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
            life.life_amount -= 1
        if self.hp < 1:
            self.die()