from pico2d import *

life_amount = 3


class Life:
    global life_amount

    def __init__(self):
        self.image = load_image("image\\life.png")

    def draw(self):
        if life_amount > 0:
            self.image.draw(750, 540)
        if life_amount > 1:
            self.image.draw(750, 540 - 25)
        if life_amount > 2:
            self.image.draw(750, 540 - 50)
