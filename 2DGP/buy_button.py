from pico2d import *


class Buy_Button:
    def __init__(self):
        self.image = load_image("image\\buy_button.png")
        self.x = 400
        self.y = 122
        self.size = 79
        self.mouse = False

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)

    def update(self):
        if self.mouse:
            self.size = 82
        else:
            self.size = 79
