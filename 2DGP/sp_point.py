from pico2d import *

LEVEL_1_POINT = 100
LEVEL_2_POINT = 250
LEVEL_3_POINT = 400


fire_upgrade_level = 1
ice_upgrade_level = 1
lock_upgrade_level = 1
poison_upgrade_level = 1
wind_upgrade_level = 1


class SP:
    def __init__(self):
        self.point = 100
        self.need_point = 10
        self.fire_point = 100
        self.ice_point = 100
        self.lock_point = 100
        self.poison_point = 100
        self.wind_point = 100
        self.font = load_font("font\\Cookie.otf", 11)

    def draw(self):
        self.font.draw(200, 105, '%d' % self.point, (255, 255, 255))
        self.font.draw(400, 105, '%d' % self.need_point, (255, 255, 255))
        if fire_upgrade_level < 4:
            self.font.draw(190, 46, '%d' % self.fire_point, (0, 0, 0))
        else:
            self.font.draw(190, 46, 'max', (0, 0, 0))

        if ice_upgrade_level < 4:
            self.font.draw(290, 46, '%d' % self.ice_point, (0, 0, 0))
        else:
            self.font.draw(190, 46, 'max', (0, 0, 0))

        if poison_upgrade_level < 4:
            self.font.draw(390, 46, '%d' % self.poison_point, (0, 0, 0))
        else:
            self.font.draw(190, 46, 'max', (0, 0, 0))

        if lock_upgrade_level < 4:
            self.font.draw(490, 46, '%d' % self.lock_point, (0, 0, 0))
        else:
            self.font.draw(190, 46, 'max', (0, 0, 0))

        if wind_upgrade_level < 4:
            self.font.draw(590, 46, '%d' % self.wind_point, (0, 0, 0))
        else:
            self.font.draw(190, 46, 'max', (0, 0, 0))

    def update(self):
        if wind_upgrade_level == 1:
            self.wind_point = LEVEL_1_POINT
        elif wind_upgrade_level == 2:
            self.wind_point = LEVEL_2_POINT
        elif wind_upgrade_level == 3:
            self.wind_point = LEVEL_3_POINT

        if fire_upgrade_level == 1:
            self.fire_point = LEVEL_1_POINT
        elif fire_upgrade_level == 2:
            self.fire_point = LEVEL_2_POINT
        elif fire_upgrade_level == 3:
            self.fire_point = LEVEL_3_POINT

        if lock_upgrade_level == 1:
            self.lock_point = LEVEL_1_POINT
        elif lock_upgrade_level == 2:
            self.lock_point = LEVEL_2_POINT
        elif lock_upgrade_level == 3:
            self.lock_point = LEVEL_3_POINT

        if poison_upgrade_level == 1:
            self.poison_point = LEVEL_1_POINT
        elif poison_upgrade_level == 2:
            self.poison_point = LEVEL_2_POINT
        elif poison_upgrade_level == 3:
            self.poison_point = LEVEL_3_POINT

        if ice_upgrade_level == 1:
            self.ice_point = LEVEL_1_POINT
        elif ice_upgrade_level == 2:
            self.ice_point = LEVEL_2_POINT
        elif ice_upgrade_level == 3:
            self.ice_point = LEVEL_3_POINT

