import random
import fire_dice
import ice_dice
import lock_dice
import wind_dice
import poison_dice
import object


class DicePosition:
    def __init__(self, idx):
        loop = True
        while loop:
            if idx == 1:
                self.x = 290
                self.y = 417
                loop = False
            elif idx == 2:
                self.x = 363
                self.y = 417
                loop = False
            elif idx == 3:
                self.x = 436
                self.y = 417
                loop = False
            elif idx == 4:
                self.x = 509
                self.y = 417
                loop = False
            elif idx == 5:
                self.x = 290
                self.y = 344
                loop = False
            elif idx == 6:
                self.x = 363
                self.y = 344
                loop = False
            elif idx == 7:
                self.x = 436
                self.y = 344
                loop = False
            elif idx == 8:
                self.x = 509
                self.y = 344
                loop = False
            elif idx == 9:
                self.x = 290
                self.y = 273
                loop = False
            elif idx == 10:
                self.x = 363
                self.y = 273
                loop = False
            elif idx == 11:
                self.x = 436
                self.y = 273
                loop = False
            elif idx == 12:
                self.x = 509
                self.y = 273
                loop = False
            elif idx == 13:
                self.x = 290
                self.y = 200
                loop = False
            elif idx == 14:
                self.x = 363
                self.y = 200
                loop = False
            elif idx == 15:
                self.x = 436
                self.y = 200
                loop = False
            elif idx == 16:
                self.x = 509
                self.y = 200
                loop = False
            else:
                pass


class Manager:
    def __init__(self, idx):
        self.exist = False
        self.type = None
        self.index = idx
        self.unit = None
        self.fire_damage = 35
        self.lock_damage = 20
        self.ice_damage = 20
        self.wind_damage = 15
        self.poison_damage = 25

    def create(self):
        self.type = random.randint(0, 4)
        if self.type == 0:
            self.unit = fire_dice.Fire_Dice(self.index)

        elif self.type == 1:
            self.unit = ice_dice.Ice_Dice(self.index)

        elif self.type == 2:
            self.unit = wind_dice.Wind_Dice(self.index)

        elif self.type == 3:
            self.unit = lock_dice.Lock_Dice(self.index)

        elif self.type == 4:
            self.unit = poison_dice.Poison_Dice(self.index)

        self.exist = True

    def upgrade_fire(self):
        self.fire_damage += 20

    def upgrade_ice(self):
        self.ice_damage += 20

    def upgrade_poison(self):
        self.poison_damage += 20

    def upgrade_lock(self):
        self.lock_damage += 20

    def upgrade_wind(self):
        self.wind_damage += 20
