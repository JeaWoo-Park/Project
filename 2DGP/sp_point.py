from pico2d import *


class SP:
    def __init__(self):
        self.point = 100
        self.need_point = 10
        self.font = load_font("font\\Cookie.otf", 11)

    def draw(self):
        self.font.draw(200, 105, '%d' % self.point, (255, 255, 255))
        self.font.draw(400, 105, '%d' % self.need_point, (255, 255, 255))
        pass

    def update(self):
        pass
