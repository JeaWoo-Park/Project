from pico2d import *
import random
from dice import Dice
from buy_button import Buy_Button
from life import Life
from enemy import Enemy

import object

index = 0
x = 0
y = 0


def Create_Dice():
    global dice
    if dice[0].exist and dice[1].exist and dice[2].exist and dice[3].exist and dice[4].exist and \
            dice[5].exist and dice[6].exist and dice[7].exist and dice[8].exist and dice[9].exist and \
            dice[10].exist and \
            dice[11].exist and dice[12].exist and dice[13].exist and dice[14].exist and dice[15].exist:
        return
    idx = random.randint(0, 15)
    if dice[idx].exist:
        Create_Dice()
        return
    dice[idx].create()


def handle():
    global dice
    global index
    global x
    global y
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            if 365 < event.x < 435 and 599 - 157 < event.y < 599 - 96:
                buy_button.mouse = True
            else:
                buy_button.mouse = False
        if event.type == SDL_MOUSEBUTTONUP:
            print('button UP')
            if event.button == SDL_BUTTON_LEFT:
                if 255 < event.x < 324 and 599 - 452 < event.y < 599 - 383:
                    if dice[0].level == dice[index].level and index != 0:
                        dice[index].off_drag()
                        dice[0].level += 1
                        dice[index].delete()

                    else:
                        dice[index].off_drag()
                        dice[index].go_back()

                elif 363 - 35 < event.x < 363 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:

                    if dice[1].level == dice[index].level and index != 1:
                        dice[index].off_drag()
                        dice[1].level += 1
                        dice[index].delete()

                    else:
                        dice[index].off_drag()
                        dice[index].go_back()

                elif 436 - 35 < event.x < 436 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:

                    if dice[2].level == dice[index].level and index != 2:
                        dice[index].off_drag()
                        dice[2].level += 1
                        dice[index].delete()
                    else:
                        dice[index].off_drag()
                        dice[index].go_back()
                elif 509 - 35 < event.x < 509 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:

                    if dice[3].level == dice[index].level and index != 3:
                        dice[index].off_drag()
                        dice[3].level += 1
                        dice[index].delete()
                    else:
                        dice[index].off_drag()
                        dice[index].go_back()
                elif 290 - 35 < event.x < 290 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                    if dice[4].level == dice[index].level and index != 4:
                        dice[index].off_drag()
                        dice[4].level += 1
                        dice[index].delete()
                    else:
                        dice[index].off_drag()
                        dice[index].go_back()
                elif 363 - 35 < event.x < 363 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:

                    if dice[5].level == dice[index].level and index != 5:
                        dice[index].off_drag()
                        dice[5].level += 1
                        dice[index].delete()
                    else:
                        dice[index].off_drag()
                        dice[index].go_back()
                elif 436 - 35 < event.x < 436 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:

                    if dice[6].level == dice[index].level and index != 6:
                        dice[index].off_drag()
                        dice[6].level += 1
                        dice[index].delete()
                    else:
                        dice[index].off_drag()
                        dice[index].go_back()
                elif 509 - 35 < event.x < 509 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:

                    if dice[7].level == dice[index].level and index != 7:
                        dice[index].off_drag()
                        dice[7].level += 1
                        dice[index].delete()
                    else:
                        dice[index].off_drag()
                        dice[index].go_back()
                elif 290 - 35 < event.x < 290 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:

                    if dice[8].level == dice[index].level and index != 8:
                        dice[index].off_drag()
                        dice[8].level += 1
                        dice[index].delete()
                    else:
                        dice[index].off_drag()
                        dice[index].go_back()
                elif 363 - 35 < event.x < 363 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:

                    if dice[9].level == dice[index].level and index != 9:
                        dice[index].off_drag()
                        dice[9].level += 1
                        dice[index].delete()
                    else:
                        dice[index].off_drag()
                        dice[index].go_back()
                elif 436 - 35 < event.x < 436 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:

                    if dice[10].level == dice[index].level and index != 10:
                        dice[index].off_drag()
                        dice[10].level += 1
                        dice[index].delete()
                    else:
                        dice[index].off_drag()
                        dice[index].go_back()
                elif 509 - 35 < event.x < 509 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:

                    if dice[11].level == dice[index].level and index != 11:
                        dice[index].off_drag()
                        dice[11].level += 1
                        dice[index].delete()
                    else:
                        dice[index].off_drag()
                        dice[index].go_back()
                elif 290 - 35 < event.x < 290 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:

                    if dice[12].level == dice[index].level and index != 12:
                        dice[index].off_drag()
                        dice[12].level += 1
                        dice[index].delete()
                    else:
                        dice[index].off_drag()
                        dice[index].go_back()
                elif 363 - 35 < event.x < 363 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:

                    if dice[13].level == dice[index].level and index != 13:
                        dice[index].off_drag()
                        dice[13].level += 1
                        dice[index].delete()
                    else:
                        dice[index].off_drag()
                        dice[index].go_back()
                elif 436 - 35 < event.x < 436 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:

                    if dice[14].level == dice[index].level and index != 14:
                        dice[index].off_drag()
                        dice[14].level += 1
                        dice[index].delete()
                    else:
                        dice[index].off_drag()
                        dice[index].go_back()
                elif 509 - 35 < event.x < 509 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:

                    if dice[15].level == dice[index].level and index != 15:
                        dice[index].off_drag()
                        dice[15].level += 1
                        dice[index].delete()
                    else:
                        dice[index].off_drag()
                        dice[index].go_back()
                else:
                    for index in range(16):
                        dice[index].off_drag()
                        dice[index].go_back()

        elif event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:

            for i in range(16):
                dice[i].off_drag()

            if 365 < event.x < 435 and 599 - 157 < event.y < 599 - 96:
                Create_Dice()
            elif 255 < event.x < 324 and 599 - 452 < event.y < 599 - 383:
                if not dice[0].exist:
                    break
                index = 0

                x = dice[0].position.x
                y = dice[0].position.y
                dice[0].on_drag()
            elif 363 - 35 < event.x < 363 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:
                if not dice[1].exist:
                    break
                index = 1

                x = dice[1].position.x
                y = dice[1].position.y
                dice[1].on_drag()
            elif 436 - 35 < event.x < 436 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:
                if not dice[2].exist:
                    break
                index = 2

                x = dice[2].position.x
                y = dice[2].position.y
                dice[2].on_drag()
            elif 509 - 35 < event.x < 509 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:
                if not dice[3].exist:
                    break
                index = 3

                x = dice[3].position.x
                y = dice[3].position.y
                dice[3].on_drag()
            elif 290 - 35 < event.x < 290 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                if not dice[4].exist:
                    break
                index = 4

                x = dice[4].position.x
                y = dice[4].position.y
                dice[4].on_drag()
            elif 363 - 35 < event.x < 363 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                if not dice[5].exist:
                    break
                index = 5

                x = dice[5].position.x
                y = dice[5].position.y
                dice[5].on_drag()
            elif 436 - 35 < event.x < 436 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                if not dice[6].exist:
                    break
                index = 6

                x = dice[6].position.x
                y = dice[6].position.y
                dice[6].on_drag()
            elif 509 - 35 < event.x < 509 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                if not dice[7].exist:
                    break
                index = 7

                x = dice[7].position.x
                y = dice[7].position.y
                dice[7].on_drag()
            elif 290 - 35 < event.x < 290 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                if not dice[8].exist:
                    break
                index = 8

                x = dice[8].position.x
                y = dice[8].position.y
                dice[8].on_drag()
            elif 363 - 35 < event.x < 363 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                if not dice[9].exist:
                    break
                index = 9

                x = dice[9].position.x
                y = dice[9].position.y
                dice[9].on_drag()
            elif 436 - 35 < event.x < 436 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                if not dice[10].exist:
                    break
                index = 10

                x = dice[10].position.x
                y = dice[10].position.y
                dice[10].on_drag()
            elif 509 - 35 < event.x < 509 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                if not dice[11].exist:
                    break
                index = 11

                x = dice[11].position.x
                y = dice[11].position.y
                dice[11].on_drag()
            elif 290 - 35 < event.x < 290 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                if not dice[12].exist:
                    break
                index = 12

                x = dice[12].position.x
                y = dice[12].position.y
                dice[12].on_drag()

            elif 363 - 35 < event.x < 363 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                if not dice[13].exist:
                    break
                index = 13

                x = dice[13].position.x
                y = dice[13].position.y
                dice[13].on_drag()

            elif 436 - 35 < event.x < 436 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                if not dice[14].exist:
                    break
                index = 14

                x = dice[14].position.x
                y = dice[14].position.y
                dice[14].on_drag()

            elif 509 - 35 < event.x < 509 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                if not dice[15].exist:
                    break
                index = 15

                x = dice[15].position.x
                y = dice[15].position.y
                dice[15].on_drag()


running = True

open_canvas(800, 600)
life = Life()
buy_button = Buy_Button()
background = load_image("image\\background.png")
dice = [Dice(i) for i in range(16)]
frame = 0
while running:
    if frame % 350 == 0:
        enemy = Enemy()
        object.add_object(enemy, 0)
    frame += 1
    clear_canvas()
    background.draw(400, 300)
    buy_button.draw()
    for d in dice:
        if not d.drag:
            d.draw()
    for d in dice:
        if d.drag:
            d.draw()
    for all_object in object.all_objects():
        all_object.draw()
    life.draw()
    handle()
    for all_object in object.all_objects():
        all_object.update()
    buy_button.update()
    for d in dice:
        d.update()
    update_canvas()

    # delay(0.05)

close_canvas()
