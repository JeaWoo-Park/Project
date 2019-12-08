from pico2d import *


class Life:
    life_amount = 3

    def __init__(self):
        self.image = load_image("image\\life.png")

    def update(self):
        pass

    def draw(self):
        if self.life_amount > 0:
            self.image.draw(750, 540)
        if self.life_amount > 1:
            self.image.draw(750, 540 - 25)
        if self.life_amount > 2:
            self.image.draw(750, 540 - 50)
