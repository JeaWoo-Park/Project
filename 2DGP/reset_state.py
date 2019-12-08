import start_state
import game_framework
import dice_manager
import sp_point


def enter():
    dice_manager.Manager.fire_damage = 35
    dice_manager.Manager.lock_damage = 20
    dice_manager.Manager.ice_damage = 20
    dice_manager.Manager.wind_damage = 15
    dice_manager.Manager.poison_damage = 25
    sp_point.SP.point = 100
    sp_point.SP.need_point = 10
    pass


def exit():
    pass


def update():
    game_framework.change_state(start_state)
    pass


def draw():
    pass


def handle_events():
    pass


def pause(): pass


def resume(): pass
