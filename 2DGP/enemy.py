from pico2d import *
import object
import life
import game_framework
import win_state
import lose_state


class Enemy:
    image = None
    slow_effect = None
    poison_effect = None
    hp_font = None

    def __init__(self):
        if Enemy.hp_font is None:
            Enemy.hp_font = load_font("font\\Cookie.otf", 15)
        if Enemy.poison_effect is None:
            Enemy.poison_effect = load_image("image\\poison_enemy.png")
        if Enemy.image is None:
            Enemy.image = load_image("image\\enemy.png")
        if Enemy.slow_effect is None:
            Enemy.slow_effect = load_image("image\\slow_enemy.png")
        self.x = 124
        self.y = 100
        self.speed = 90
        self.hp = 500
        self.poison_damage_rate = 0
        self.poison_damage = 0
        self.lock_timer = 0
        self.locking = False
        self.drawing_slow_effect = False
        self.drawing_poison_effect = False

    def draw(self):
        if self.drawing_poison_effect:
            self.poison_effect.draw(self.x, self.y, 110, 110)
        else:
            self.image.draw(self.x, self.y, 110, 110)
        if self.drawing_slow_effect:
            self.slow_effect.draw(self.x, self.y - 5, 110, 110)
        self.hp_font.draw(self.x - 12, self.y, '%d' % self.hp, (255, 255, 255))

    def poison(self, damage):
        self.poison_damage = damage
        self.drawing_poison_effect = True

    def slow(self):
        self.speed = 25
        self.drawing_slow_effect = True

    def lock(self):
        self.speed = 0
        self.locking = True
        self.lock_timer = 0

    def unlock(self):
        if self.drawing_slow_effect:
            self.speed = 25
        else:
            self.speed = 30
        self.locking = False

    def die(self):
        object.remove_object(self)
        object.bring_object(3, 0).point += 10

    def update(self):
        if (self.poison_damage_rate % 60) == 0:
            self.hp -= self.poison_damage
        self.poison_damage_rate += 1
        self.lock_timer += 1
        if (self.lock_timer % 180) == 0:
            if self.locking:
                self.unlock()
        if self.y > 514:
            self.y = 514
        if self.x > 674:
            self.x = 674
        if self.x == 124 and self.y < 514:
            self.y += self.speed * game_framework.frame_time
        elif self.y == 514 and self.x < 674:
            self.x += self.speed * game_framework.frame_time
        elif self.x == 674 and self.y > 100:
            self.y -= self.speed * game_framework.frame_time

        if self.x == 674 and self.y < 100:
            object.remove_object(self)
            life.Life.life_amount -= 1
            if life.Life.life_amount == 0:
                game_framework.change_state(lose_state)
        if self.hp < 1:
            self.die()


class Boss:
    image = None
    slow_effect = None
    poison_effect = None
    hp_font = None

    def __init__(self):
        if Boss.poison_effect is None:
            Boss.poison_effect = load_image("image\\poison_enemy.png")
        if Boss.image is None:
            Boss.image = load_image("image\\enemy.png")
        if Boss.slow_effect is None:
            Boss.slow_effect = load_image("image\\slow_enemy.png")
        if Boss.hp_font is None:
            Boss.hp_font = load_font("font\\Cookie.otf")
        self.x = 124
        self.y = 100
        self.speed = 33
        self.hp = 5000
        self.poison_damage_rate = 0
        self.poison_damage = 0
        self.lock_timer = 0
        self.locking = False
        self.drawing_slow_effect = False
        self.drawing_poison_effect = False

    def die(self):
        object.remove_object(self)
        game_framework.change_state(win_state)

    def update(self):
        if (self.poison_damage_rate % 60) == 0:
            self.hp -= self.poison_damage
        self.poison_damage_rate += 1
        if self.y > 514:
            self.y = 514
        if self.x > 674:
            self.x = 674
        if self.x == 124 and self.y < 514:
            self.y += self.speed * game_framework.frame_time
        elif self.y == 514 and self.x < 674:
            self.x += self.speed * game_framework.frame_time
        elif self.x == 674 and self.y > 100:
            self.y -= self.speed * game_framework.frame_time

        if self.x == 674 and self.y < 100:
            object.remove_object(self)
            game_framework.change_state(lose_state)
        if self.hp < 1:
            self.die()

    def draw(self):
        if self.drawing_poison_effect:
            self.poison_effect.draw(self.x, self.y, 110, 110)
        else:
            self.image.draw(self.x, self.y, 170, 170)
        if self.drawing_slow_effect:
            self.slow_effect.draw(self.x, self.y - 5, 170, 170)
        self.hp_font.draw(self.x - 21, self.y, '%d' % self.hp, (255, 255, 255))

    def poison(self, damage):
        self.poison_damage = damage - 10
        pass

    def slow(self):
        self.speed = 27
        self.drawing_slow_effect = True

    def lock(self):
        pass
