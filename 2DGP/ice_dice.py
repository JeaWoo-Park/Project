from pico2d import *
import object
import dice_manager


class Ice_Dice:
    def __init__(self, index, attack_power):
        self.drag = False
        self.level = 1
        self.index = index + 1
        self.image = load_image('image\\ice_dice.png')
        self.bullet = load_image('image\\ice_bullet.png')
        self.position = dice_manager.DicePosition(self.index)
        self.x = self.position.x
        self.y = self.position.y
        self.timer = 90
        self.attack_speed = 90
        self.attack_power = attack_power
        self.sp_upgrade_level = 1

    def check(self):
        if self.sp_upgrade_level == 1:
            self.attack_power = 20
        elif self.sp_upgrade_level == 2:
            self.attack_power = 40
        elif self.sp_upgrade_level == 3:
            self.attack_power = 60

        if self.level == 1:
            self.attack_speed = 90
        elif self.level == 2:
            self.attack_speed = 87
        elif self.level == 3:
            self.attack_speed = 84
        elif self.level == 4:
            self.attack_speed = 81
        elif self.level == 5:
            self.attack_speed = 78
        elif self.level == 6:
            self.attack_speed = 75

    def update(self):
        self.timer = (self.timer + 1) % self.attack_speed
        if self.timer == 0 and len(object.objects[0]) != 0:
            self.attack()
        if self.drag:
            i = get_events()
            for event in i:
                if event.type == SDL_MOUSEMOTION:
                    self.x = event.x
                    self.y = 599 - event.y
        elif not self.drag:
            self.go_back()
        self.check()

    def go_back(self):
        self.x = self.position.x
        self.y = self.position.y
        self.drag = False

    def on_drag(self):
        self.drag = True

    def off_drag(self):
        self.drag = False

    def draw(self):
        if self.level == 1:
            self.image.draw(self.x, self.y, 95, 95)
            self.bullet.draw(self.x + 2, self.y, 95, 95)
        elif self.level == 2:
            self.image.draw(self.x, self.y, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y + 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y - 15, 95, 95)
        elif self.level == 3:
            self.image.draw(self.x, self.y, 95, 95)
            self.bullet.draw(self.x + 2, self.y, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y + 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y - 15, 95, 95)
        elif self.level == 4:
            self.image.draw(self.x, self.y, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y + 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y - 15, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y - 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y + 15, 95, 95)
        elif self.level == 5:
            self.image.draw(self.x, self.y, 95, 95)
            self.bullet.draw(self.x + 2, self.y, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y + 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y - 15, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y - 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y + 15, 95, 95)
        elif self.level == 6:
            self.image.draw(self.x, self.y, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y + 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y - 15, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y - 15, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y + 15, 95, 95)
            self.bullet.draw(self.x + 15 + 2, self.y, 95, 95)
            self.bullet.draw(self.x - 15 + 2, self.y, 95, 95)

    def attack(self):

        if self.level == 1:
            bullet = Ice_Bullet(self.x + 2, self.y, self.attack_power)
            object.add_object(bullet, 1)
            pass
        elif self.level == 2:
            bullet = Ice_Bullet(self.x + 15 + 2, self.y + 15, self.attack_power)
            object.add_object(bullet, 1)
            bullet = Ice_Bullet(self.x - 15 + 2, self.y - 15, self.attack_power)
            object.add_object(bullet, 1)
            pass
        elif self.level == 3:
            bullet = Ice_Bullet(self.x + 15 + 2, self.y + 15, self.attack_power)
            object.add_object(bullet, 1)
            bullet = Ice_Bullet(self.x - 15 + 2, self.y - 15, self.attack_power)
            object.add_object(bullet, 1)
            bullet = Ice_Bullet(self.x + 2, self.y, self.attack_power)
            object.add_object(bullet, 1)
            pass
        elif self.level == 4:
            bullet = Ice_Bullet(self.x + 15 + 2, self.y + 15, self.attack_power)
            object.add_object(bullet, 1)
            bullet = Ice_Bullet(self.x - 15 + 2, self.y - 15, self.attack_power)
            object.add_object(bullet, 1)
            bullet = Ice_Bullet(self.x - 15 + 2, self.y + 15, self.attack_power)
            object.add_object(bullet, 1)
            bullet = Ice_Bullet(self.x + 15 + 2, self.y - 15, self.attack_power)
            object.add_object(bullet, 1)
            pass
        elif self.level == 5:
            bullet = Ice_Bullet(self.x + 2, self.y, self.attack_power)
            object.add_object(bullet, 1)
            bullet = Ice_Bullet(self.x + 15 + 2, self.y + 15, self.attack_power)
            object.add_object(bullet, 1)
            bullet = Ice_Bullet(self.x - 15 + 2, self.y - 15, self.attack_power)
            object.add_object(bullet, 1)
            bullet = Ice_Bullet(self.x - 15 + 2, self.y + 15, self.attack_power)
            object.add_object(bullet, 1)
            bullet = Ice_Bullet(self.x + 15 + 2, self.y - 15, self.attack_power)
            object.add_object(bullet, 1)
            pass
        elif self.level == 6:
            bullet = Ice_Bullet(self.x + 15 + 2, self.y + 15, self.attack_power)
            object.add_object(bullet, 1)
            bullet = Ice_Bullet(self.x - 15 + 2, self.y - 15, self.attack_power)
            object.add_object(bullet, 1)
            bullet = Ice_Bullet(self.x - 15 + 2, self.y + 15, self.attack_power)
            object.add_object(bullet, 1)
            bullet = Ice_Bullet(self.x + 15 + 2, self.y - 15, self.attack_power)
            object.add_object(bullet, 1)
            bullet = Ice_Bullet(self.x - 15 + 2, self.y, self.attack_power)
            object.add_object(bullet, 1)
            bullet = Ice_Bullet(self.x + 15 + 2, self.y, self.attack_power)
            object.add_object(bullet, 1)
            pass


class Ice_Bullet:

    def __init__(self, x, y, attack_power):
        self.image = load_image("image\\ice_bullet.png")
        self.attack_power = attack_power
        self.frame = 0
        self.target = object.bring_object(0, 0)
        self.fire_bgm = load_wav('sound\\shot.wav')
        self.struck_bgm = load_wav('sound\\shot-struck.wav')
        self.fire_bgm.set_volume(50)
        self.struck_bgm.set_volume(50)
        self.fire_bgm.play()
        if self.target.locking:
            if len(object.objects[0]) > 1:
                self.target = object.bring_object(0, 1)
        if self.target.x == 124 and self.target.y < 514:
            self.target_x = self.target.x
            self.target_y = self.target.y + 20
        elif self.target.y == 514 and self.target.x < 674:
            self.target_x = self.target.x + 20
            self.target_y = self.target.y
        elif self.target.x == 674 and self.target.y > 100:
            self.target_x = self.target.x
            self.target_y = self.target.y - 20

        self.x = x
        self.y = y

    def fire(self):
        t = self.frame / 100
        self.x = (1 - t) * self.x + t * self.target_x
        self.y = (1 - t) * self.y + t * self.target_y
        self.image.draw(self.x, self.y, 95, 95)

    def draw(self):
        self.image.draw(self.x, self.y, 95, 95)

    def update(self):
        self.frame += 1
        self.fire()
        if self.target_x - 30 < self.x < self.target_x + 30 and self.target_y - 30 < self.y < self.target_y + 30:
            object.remove_object(self)
            self.target.hp -= self.attack_power
            self.struck_bgm.play()
            if not self.target.drawing_slow_effect:
                self.target.slow()
        if self.target.hp < 1:
            object.remove_object(self)
