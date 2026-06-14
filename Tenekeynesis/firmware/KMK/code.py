from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
import board

keyboard = KMKKeyboard()

keyboard.direct_pins = [
    board.D0,
    board.D1,
    board.D2,
    board.D3,
    board.D4,
    board.D5,
    board.D6,
    board.D10,
    board.D9,
    board.D8,
]

keyboard.keymap = [[
    KC.W,
    KC.F,
    KC.S,
    KC.A,
    KC.SPC,
    KC.V,
    KC.D,
    KC.E,
    KC.Q,
    KC.TAB,
]]

keyboard.go()