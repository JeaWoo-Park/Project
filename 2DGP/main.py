from pico2d import *
import random
from buy_button import Buy_Button
from life import Life
from enemy import Enemy
from enemy import Boss
from sp_point import SP
import sp_point
import dice_manager
import game_framework

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
    if object.bring_object(3, 0).need_point <= object.bring_object(3, 0).point:
        dice[idx].create()
        object.bring_object(3, 0).point -= object.bring_object(3, 0).need_point
        object.bring_object(3, 0).need_point += 10
    else:
        return

play_time = 300
life = None
buy_button = None
background = None
dice = None
frame = 1
spawn_rate = 200
sp_font = None
boss_timer_font = None
boss_timer = 100
boss_round = False
start_time = 0
music = None
upgrade_sound = None
sp = None
enemy_hp = 100
enemy_count = 1
fire = None
ice = None
poison = None
lock = None
wind = None


def enter():
    global music, life, buy_button, background, dice, frame, spawn_rate, sp_font, sp, boss_timer_font, start_time
    global boss_round, fire, lock, poison, ice, wind, upgrade_sound
    upgrade_sound = load_wav('sound\\upgrade.wav')
    upgrade_sound.set_volume(60)
    fire = load_image('image\\fire_dice.png')
    ice = load_image('image\\ice_dice.png')
    lock = load_image('image\\lock_dice.png')
    poison = load_image('image\\poison_dice.png')
    wind = load_image('image\\wind_dice.png')
    music = load_music('sound\\main.mp3')
    music.set_volume(80)
    music.repeat_play()
    sp = SP()
    start_time = get_time()
    object.add_object(sp, 3)
    boss_round = False
    boss_timer_font = load_font("font\\Cookie.otf", 24)
    life = Life()
    buy_button = Buy_Button()
    background = load_image("image\\background.png")
    dice = [dice_manager.Manager(i) for i in range(16)]
    frame = 1
    spawn_rate = 300
    for d in dice:
        object.add_object(d, 2)
    object.add_object(life, 2)
    object.add_object(buy_button, 2)


def exit():
    global background, music

    del background
    music.stop()
    del music


def pause():
    pass


def resume():
    pass


def handle_events():
    global stack
    global dice
    global index
    global x
    global y
    global running
    global sp
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            if 365 < event.x < 435 and 599 - 157 < event.y < 599 - 96:
                buy_button.mouse = True
            else:
                buy_button.mouse = False
        if event.type == SDL_MOUSEBUTTONUP:
            if event.button == SDL_BUTTON_LEFT:
                if 255 < event.x < 324 and 599 - 452 < event.y < 599 - 383:
                    if dice[0].unit is not None and dice[index].unit is not None:
                        if dice[0].unit.level == dice[index].unit.level and index != 0 and \
                                dice[0].type == dice[index].type:
                            dice[index].unit.off_drag()
                            dice[0].unit.level += 1
                            dice[index].unit = None
                            dice[index].exist = False

                        else:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                    else:
                        if dice[index].unit is not None:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()

                elif 363 - 35 < event.x < 363 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:
                    if dice[1].unit is not None and dice[index].unit is not None:
                        if dice[1].unit.level == dice[index].unit.level and index != 1 and \
                                dice[1].type == dice[index].type:
                            dice[index].unit.off_drag()
                            dice[1].unit.level += 1
                            dice[index].unit = None
                            dice[index].exist = False
                        else:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                    else:
                        if dice[index].unit is not None:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()

                elif 436 - 35 < event.x < 436 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:
                    if dice[2].unit is not None and dice[index].unit is not None:
                        if dice[2].unit.level == dice[index].unit.level and index != 2 and \
                                dice[2].type == dice[index].type:
                            dice[index].unit.off_drag()
                            dice[2].unit.level += 1
                            dice[index].unit = None
                            dice[index].exist = False
                        else:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                    else:
                        if dice[index].unit is not None:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                elif 509 - 35 < event.x < 509 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:
                    if dice[3].unit is not None and dice[index].unit is not None:
                        if dice[3].unit.level == dice[index].unit.level and index != 3 and \
                                dice[3].type == dice[index].type:
                            dice[index].unit.off_drag()
                            dice[3].unit.level += 1
                            dice[index].unit = None
                            dice[index].exist = False

                        else:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                    else:
                        if dice[index].unit is not None:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                elif 290 - 35 < event.x < 290 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                    if dice[4].unit is not None and dice[index].unit is not None:
                        if dice[4].unit.level == dice[index].unit.level and index != 4 and \
                                dice[4].type == dice[index].type:
                            dice[index].unit.off_drag()
                            dice[4].unit.level += 1
                            dice[index].unit = None
                            dice[index].exist = False

                        else:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                    else:
                        if dice[index].unit is not None:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                elif 363 - 35 < event.x < 363 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                    if dice[5].unit is not None and dice[index].unit is not None:
                        if dice[5].unit.level == dice[index].unit.level and index != 5 and \
                                dice[5].type == dice[index].type:
                            dice[index].unit.off_drag()
                            dice[5].unit.level += 1
                            dice[index].unit = None
                            dice[index].exist = False
                        else:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                    else:
                        if dice[index].unit is not None:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                elif 436 - 35 < event.x < 436 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                    if dice[6].unit is not None and dice[index].unit is not None:
                        if dice[6].unit.level == dice[index].unit.level and index != 6 and \
                                dice[6].type == dice[index].type:
                            dice[index].unit.off_drag()
                            dice[6].unit.level += 1
                            dice[index].unit = None
                            dice[index].exist = False

                        else:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                    else:
                        if dice[index].unit is not None:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                elif 509 - 35 < event.x < 509 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                    if dice[7].unit is not None and dice[index].unit is not None:
                        if dice[7].unit.level == dice[index].unit.level and index != 7 and \
                                dice[7].type == dice[index].type:
                            dice[index].unit.off_drag()
                            dice[7].unit.level += 1
                            dice[index].unit = None
                            dice[index].exist = False

                        else:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                    else:
                        if dice[index].unit is not None:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                elif 290 - 35 < event.x < 290 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                    if dice[8].unit is not None and dice[index].unit is not None:
                        if dice[8].unit.level == dice[index].unit.level and index != 8 and \
                                dice[8].type == dice[index].type:
                            dice[index].unit.off_drag()
                            dice[8].unit.level += 1
                            dice[index].unit = None
                            dice[index].exist = False

                        else:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                    else:
                        if dice[index].unit is not None:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                elif 363 - 35 < event.x < 363 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                    if dice[9].unit is not None and dice[index].unit is not None:
                        if dice[9].unit.level == dice[index].unit.level and index != 9 and \
                                dice[9].type == dice[index].type:
                            dice[index].unit.off_drag()
                            dice[9].unit.level += 1
                            dice[index].unit = None
                            dice[index].exist = False

                        else:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                    else:
                        if dice[index].unit is not None:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                elif 436 - 35 < event.x < 436 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                    if dice[10].unit is not None and dice[index].unit is not None:
                        if dice[10].unit.level == dice[index].unit.level and index != 10 and \
                                dice[10].type == dice[index].type:
                            dice[index].unit.off_drag()
                            dice[10].unit.level += 1
                            dice[index].unit = None
                            dice[index].exist = False

                        else:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                    else:
                        if dice[index].unit is not None:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                elif 509 - 35 < event.x < 509 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                    if dice[11].unit is not None and dice[index].unit is not None:
                        if dice[11].unit.level == dice[index].unit.level and index != 11 and \
                                dice[11].type == dice[index].type:
                            dice[index].unit.off_drag()
                            dice[11].unit.level += 1
                            dice[index].unit = None
                            dice[index].exist = False

                        else:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                    else:
                        if dice[index].unit is not None:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                elif 290 - 35 < event.x < 290 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                    if dice[12].unit is not None and dice[index].unit is not None:
                        if dice[12].unit.level == dice[index].unit.level and index != 12 and \
                                dice[12].type == dice[index].type:
                            dice[index].unit.off_drag()
                            dice[12].unit.level += 1
                            dice[index].unit = None
                            dice[index].exist = False

                        else:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                    else:
                        if dice[index].unit is not None:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                elif 363 - 35 < event.x < 363 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                    if dice[13].unit is not None and dice[index].unit is not None:
                        if dice[13].unit.level == dice[index].unit.level and index != 13 and \
                                dice[13].type == dice[index].type:
                            dice[index].unit.off_drag()
                            dice[13].unit.level += 1
                            dice[index].unit = None
                            dice[index].exist = False

                        else:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                    else:
                        if dice[index].unit is not None:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                elif 436 - 35 < event.x < 436 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                    if dice[14].unit is not None and dice[index].unit is not None:
                        if dice[14].unit.level == dice[index].unit.level and index != 14 and \
                                dice[14].type == dice[index].type:
                            dice[index].unit.off_drag()
                            dice[14].unit.level += 1
                            dice[index].unit = None
                            dice[index].exist = False

                        else:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                    else:
                        if dice[index].unit is not None:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                elif 509 - 35 < event.x < 509 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                    if dice[15].unit is not None and dice[index].unit is not None:
                        if dice[15].unit.level == dice[index].unit.level and index != 15 and \
                                dice[15].type == dice[index].type:
                            dice[index].unit.off_drag()
                            dice[15].unit.level += 1
                            dice[index].unit = None
                            dice[index].exist = False

                        else:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                    else:
                        if dice[index].unit is not None:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()
                else:
                    for index in range(16):
                        if dice[index].unit is not None:
                            dice[index].unit.off_drag()
                            dice[index].unit.go_back()

        elif event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:

            for i in range(16):
                if dice[i].unit is not None:
                    dice[i].unit.off_drag()

            if 365 < event.x < 435 and 599 - 157 < event.y < 599 - 96:
                Create_Dice()
            elif 255 < event.x < 324 and 599 - 452 < event.y < 599 - 383:
                if dice[0].unit is None:
                    break
                index = 0

                x = dice[0].unit.position.x
                y = dice[0].unit.position.y
                dice[0].unit.on_drag()
            elif 363 - 35 < event.x < 363 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:
                if dice[1].unit is None:
                    break
                index = 1

                x = dice[1].unit.position.x
                y = dice[1].unit.position.y
                dice[1].unit.on_drag()
            elif 436 - 35 < event.x < 436 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:
                if dice[2].unit is None:
                    break
                index = 2

                x = dice[2].unit.position.x
                y = dice[2].unit.position.y
                dice[2].unit.on_drag()
            elif 509 - 35 < event.x < 509 + 34 and 599 - 417 - 35 < event.y < 599 - 417 + 34:
                if dice[3].unit is None:
                    break
                index = 3

                x = dice[3].unit.position.x
                y = dice[3].unit.position.y
                dice[3].unit.on_drag()
            elif 290 - 35 < event.x < 290 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                if dice[4].unit is None:
                    break
                index = 4

                x = dice[4].unit.position.x
                y = dice[4].unit.position.y
                dice[4].unit.on_drag()
            elif 363 - 35 < event.x < 363 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                if dice[5].unit is None:
                    break
                index = 5

                x = dice[5].unit.position.x
                y = dice[5].unit.position.y
                dice[5].unit.on_drag()
            elif 436 - 35 < event.x < 436 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                if dice[6].unit is None:
                    break
                index = 6

                x = dice[6].unit.position.x
                y = dice[6].unit.position.y
                dice[6].unit.on_drag()
            elif 509 - 35 < event.x < 509 + 34 and 599 - 344 - 35 < event.y < 599 - 344 + 34:
                if dice[7].unit is None:
                    break
                index = 7

                x = dice[7].unit.position.x
                y = dice[7].unit.position.y
                dice[7].unit.on_drag()
            elif 290 - 35 < event.x < 290 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                if dice[8].unit is None:
                    break

                index = 8

                x = dice[8].unit.position.x
                y = dice[8].unit.position.y
                dice[8].unit.on_drag()
            elif 363 - 35 < event.x < 363 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                if dice[9].unit is None:
                    break
                index = 9

                x = dice[9].unit.position.x
                y = dice[9].unit.position.y
                dice[9].unit.on_drag()
            elif 436 - 35 < event.x < 436 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                if dice[10].unit is None:
                    break
                index = 10

                x = dice[10].unit.position.x
                y = dice[10].unit.position.y
                dice[10].unit.on_drag()
            elif 509 - 35 < event.x < 509 + 34 and 599 - 273 - 35 < event.y < 599 - 273 + 34:
                if dice[11].unit is None:
                    break
                index = 11

                x = dice[11].unit.position.x
                y = dice[11].unit.position.y
                dice[11].unit.on_drag()
            elif 290 - 35 < event.x < 290 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                if dice[12].unit is None:
                    break
                index = 12

                x = dice[12].unit.position.x
                y = dice[12].unit.position.y
                dice[12].unit.on_drag()

            elif 363 - 35 < event.x < 363 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                if dice[13].unit is None:
                    break
                index = 13

                x = dice[13].unit.position.x
                y = dice[13].unit.position.y
                dice[13].unit.on_drag()
            elif 436 - 35 < event.x < 436 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                if dice[14].unit is None:
                    break
                index = 14

                x = dice[14].unit.position.x
                y = dice[14].unit.position.y
                dice[14].unit.on_drag()
            elif 509 - 35 < event.x < 509 + 34 and 599 - 200 - 35 < event.y < 599 - 200 + 34:
                if dice[15].unit is None:
                    break
                index = 15

                x = dice[15].unit.position.x
                y = dice[15].unit.position.y
                dice[15].unit.on_drag()

            elif 198 - 31 < event.x < 198 + 31 and 599 - 46 - 31 < event.y < 599 - 46 + 31:
                if sp_point.fire_upgrade_level < 4 and sp.fire_point <= sp.point:
                    sp_point.fire_upgrade_level += 1
                    sp.point -= sp.fire_point
                    for d in dice:
                        d.upgrade_fire()
                    upgrade_sound.play()
                else:
                    pass
            elif 298 - 31 < event.x < 298 + 31 and 599 - 46 - 31 < event.y < 599 - 46 + 31:
                if sp_point.ice_upgrade_level < 4 and sp.ice_point <= sp.point:
                    sp_point.ice_upgrade_level += 1
                    sp.point -= sp.ice_point
                    for d in dice:
                        d.upgrade_ice()
                    upgrade_sound.play()
                else:
                    pass
            elif 398 - 31 < event.x < 398 + 31 and 599 - 46 - 31 < event.y < 599 - 46 + 31:
                if sp_point.poison_upgrade_level < 4 and sp.poison_point <= sp.point:
                    sp_point.poison_upgrade_level += 1
                    sp.point -= sp.poison_point
                    for d in dice:
                        d.upgrade_poison()
                    upgrade_sound.play()
                else:
                    pass
            elif 498 - 31 < event.x < 498 + 31 and 599 - 46 - 31 < event.y < 599 - 46 + 31:
                if sp_point.lock_upgrade_level < 4 and sp.lock_point <= sp.point:
                    sp_point.lock_upgrade_level += 1
                    sp.point -= sp.lock_point
                    for d in dice:
                        d.upgrade_lock()
                    upgrade_sound.play()
                else:
                    pass
            elif 598 - 31 < event.x < 598 + 31 and 599 - 46 - 31 < event.y < 599 - 46 + 31:
                if sp_point.wind_upgrade_level < 4 and sp.wind_point <= sp.point:
                    sp_point.wind_upgrade_level += 1
                    sp.point -= sp.wind_point
                    for d in dice:
                        d.upgrade_wind()
                    upgrade_sound.play()
                else:
                    pass


def update():
    global frame
    global spawn_rate
    global boss_timer
    global boss_round
    global enemy_hp
    global enemy_count

    if boss_timer - get_time() > 0:
        boss_timer -= get_time()

    else:
        boss_round = True
    if not boss_round:
        if frame % spawn_rate == 0:
            frame = 1
            enemy_count = ((enemy_count + 1) % 5)
            spawn_rate = 120
            enemy = Enemy(enemy_hp)
            object.add_object(enemy, 0)
            if enemy_count == 0:
                enemy_hp += 30

    elif boss_round and len(object.objects[0]) == 0:
        enemy = Boss()
        object.add_object(enemy, 0)
    frame += 1
    for all_object in object.all_objects():
        all_object.update()
    buy_button.update()
    for d in dice:
        if d.unit is not None:
            d.unit.update()


def draw():
    global sp
    global boss_timer
    clear_canvas()
    background.draw(400, 300)
    buy_button.draw()
    fire.draw(198, 46, 90, 90)
    ice.draw(298, 46, 90, 90)
    poison.draw(398, 46, 90, 90)
    lock.draw(498, 46, 90, 90)
    wind.draw(598, 46, 90, 90)

    if not boss_round:
        boss_timer_font.draw(390, 585, '%d' % boss_timer, (255, 255, 255))
        boss_timer = play_time + start_time
    else:
        boss_timer_font.draw(350, 585, '!!!BOSS!!!', (255, 0, 0))

    for d in dice:
        if d.unit is not None:
            if not d.unit.drag:
                d.unit.draw()

    for d in dice:
        if d.unit is not None:
            if d.unit.drag:
                d.unit.draw()
    for all_object in object.all_objects():
        all_object.draw()
    life.draw()


    update_canvas()
