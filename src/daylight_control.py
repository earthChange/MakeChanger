
import pyxel

DAY_SECS = 90
MAX_SECS = DAY_SECS * 2
ONE_THIRD_of_a_DAY = 1 * int(MAX_SECS/3)
TWO_THIRDS_of_a_DAY = 2 * int(MAX_SECS/3)

class DaylightControl:

    def __init__(self):
        self.frame_cnt = 0
        self.sec_cnt = 0

    def update(self, world):
        # 0-27 = day = all normal tile colours
        # 28 = early dusk = all orange except nearest
        # 29 = late dusk = all dark red except nearest
        # 30-57 = night = all dark blue except nearest
        # 58 = early dawn = all dark red except nearest
        # 59 = late dawn = all orange except nearest

        def msg(txt, col=9):
            world.journal.push_new_line(txt, col)

        self.frame_cnt += 1
        if self.frame_cnt == 10:
            self.frame_cnt = 0
            self.sec_cnt += 1
            if self.sec_cnt == MAX_SECS:
                self.sec_cnt = 0

        if self.frame_cnt == 0:
            # night time spooky music
            if self.sec_cnt == ONE_THIRD_of_a_DAY:
                pyxel.playm(2, loop=False)
                msg("The sun is setting.")
            # happy end of night
            elif self.sec_cnt == TWO_THIRDS_of_a_DAY:
                msg("The sun is rising.")
                pyxel.playm(3, loop=False)
            elif self.sec_cnt == 0:
                pyxel.playm(1, loop=False)

        if self.sec_cnt > ONE_THIRD_of_a_DAY and self.sec_cnt < TWO_THIRDS_of_a_DAY:
            for i in range(2, 16):
                pyxel.pal(i, 1)
        elif self.sec_cnt == ONE_THIRD_of_a_DAY - 1 or self.sec_cnt == TWO_THIRDS_of_a_DAY + 1:
            for i in range(2, 16):
                pyxel.pal(i, 9)
        elif self.sec_cnt == ONE_THIRD_of_a_DAY or self.sec_cnt == TWO_THIRDS_of_a_DAY:
            for i in range(2, 16):
                pyxel.pal(i, 2)

    def is_night(self):
        return not (self.sec_cnt >= 0 and
                    self.sec_cnt <= ONE_THIRD_of_a_DAY)
