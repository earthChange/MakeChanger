
from random import randint, choice, sample
import math

import pyxel

from game import Game
from input import Input

class App:
    FPS = 10
    TITLE = "Change Maker"

    def __init__(self):
        w = 160
        h = 120
        pyxel.init(w, h, title=self.TITLE, fps=self.FPS)
        pyxel.load("../res/pyxel_resource.pyxres")

        self.input = Input()
        self.game = Game()

        pyxel.mouse(visible=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.game.update(self.input.update())

    def draw(self):
        pyxel.cls(0)
        self.game.draw()

App()
