import game_framework
import pico2d
import reset_state
import start_state
import win_state
import lose_state

pico2d.open_canvas(800, 600, sync=True)
game_framework.run(start_state)
pico2d.close_canvas()
