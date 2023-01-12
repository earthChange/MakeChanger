import pyxel

from world import World
from hud import Hud
from journal import Journal
from menu import Menu

class Game:
    STATE_MENU = 0
    STATE_MAP = 1

    def __init__(self):
        self.state = self.STATE_MENU
        self.menu = Menu(self)
        self.world = None
        self.hud = None
        #self.new_game()

    def new_game(self):
        pyxel.stop()
        pyxel.playm(1, loop=False)
        self.menu = None
        self.state = self.STATE_MAP
        self.world = World(self)
        self.hud = Hud(self.world)

    def game_over(self):
        self.state = self.STATE_MENU
        self.menu = Menu(self)

    def update(self, inputs):
        if self.state is self.STATE_MAP:
            self.world.update(inputs)
            self.hud.update()
        elif self.state is self.STATE_MENU:
            self.menu.update(inputs)

    def draw(self):
        if self.state is self.STATE_MAP:
            self.world.draw()
            self.hud.draw()
        elif self.state is self.STATE_MENU:
            self.menu.draw()
