import pyxel
import game

class Menu:
    def __init__(self, game):
        self.game = game
        self.select_y = 50
        pyxel.stop()
        pyxel.playm(0, loop=True)

    def update(self, input):
        if pyxel.btn(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            self.game.new_game()

    def draw(self):
        pyxel.text(52, 20, "MakeChanger", 10)
        pyxel.text(30, 45, "Move: Arrows or WASD", 13)
        pyxel.text(30, 55, "Attack: Z or N + direction", 13)
        pyxel.text(30, 65, "Pickup: X or M", 13)
        pyxel.text(52, 88, "ENTER to Start", 12)
        pyxel.text(52, 100, "ESC to Exit", 9)
