from pico2d import *
import os
import random

os.chdir("D:\\Programming\\Project\\2DGP")



class Dice:
    def __init__(self):
        self.level = 6
        self.image = load_image('image\\fire_dice.png')
        self.bullet = load_image('image\\fire_bullet.png')
        self.x = 509
        self.y = 417

    def draw(self):
        self.image.draw(self.x, self.y, 95, 95)
        if self.level == 1:
            self.bullet.draw(self.x+2, self.y, 95, 95)
        elif self.level == 2:
            self.bullet.draw(self.x+15+2,self.y+15,95,95)
            self.bullet.draw(self.x-15+2,self.y-15,95,95)
        elif self.level == 3:
            self.bullet.draw(self.x+2, self.y, 95, 95)
            self.bullet.draw(self.x + 15+2, self.y + 15, 95, 95)
            self.bullet.draw(self.x - 15+2, self.y - 15, 95, 95)
        elif self.level == 4:
            self.bullet.draw(self.x + 15+2, self.y + 15, 95, 95)
            self.bullet.draw(self.x - 15+2, self.y - 15, 95, 95)
            self.bullet.draw(self.x + 15+2, self.y - 15, 95, 95)
            self.bullet.draw(self.x - 15+2, self.y + 15, 95, 95)
        elif self.level == 5:
            self.bullet.draw(self.x+2, self.y, 95, 95)
            self.bullet.draw(self.x + 15+2, self.y + 15, 95, 95)
            self.bullet.draw(self.x - 15+2, self.y - 15, 95, 95)
            self.bullet.draw(self.x + 15+2, self.y - 15, 95, 95)
            self.bullet.draw(self.x - 15+2, self.y + 15, 95, 95)
        elif self.level == 6:
            self.bullet.draw(self.x + 15+2, self.y + 15, 95, 95)
            self.bullet.draw(self.x - 15+2, self.y - 15, 95, 95)
            self.bullet.draw(self.x + 15+2, self.y - 15, 95, 95)
            self.bullet.draw(self.x - 15+2, self.y + 15, 95, 95)
            self.bullet.draw(self.x + 15+2, self.y, 95, 95)
            self.bullet.draw(self.x - 15+2, self.y, 95, 95)

def handle():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


running = True

open_canvas(800, 600)

background = load_image("image\\background.png")
dice_1 = Dice()

while running:
    handle()
    clear_canvas()
    background.draw(400, 300)
    dice_1.draw()

    update_canvas()

    delay(0.05)
close_canvas()
