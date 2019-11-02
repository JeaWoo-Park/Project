from pico2d import *

hp = 3


class Life:
    global hp

    def __init__(self):
        self.image = load_image("image\\life.png")

    def draw(self):
        if hp > 0:
            self.image.draw(750, 540)
        if hp > 1:
            self.image.draw(750, 540 - 25)
        if hp > 2:
            self.image.draw(750, 540 - 50)
