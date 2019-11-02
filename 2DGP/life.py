from pico2d import *


class Life:
    def __init__(self):
        self.hp = 3
        self.image = load_image("image\\life.png")

    def draw(self):
        if self.hp > 0:
            self.image.draw(750, 540)
        if self.hp > 1:
            self.image.draw(750, 540 - 25)
        if self.hp > 2:
            self.image.draw(750, 540 - 50)



