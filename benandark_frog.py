# -*- coding: utf-8 -*-
from time import sleep
import time
import datetime
from copy_plugin import LSebas


class BenandarkFrog(LSebas):
    def __init__(self):
        super(BenandarkFrog, self).__init__()
        article_obj = self
        self.setup(article_obj)
        self.screen_high = 2280
        self.screen_wight = 1080

        self.fight_x = 614
        self.fight_y = 833
        self.fight_offset = self.screen_high*self.fight_y+self.fight_x

        self.fight_role1_pos = "398 1000"
        self.fight_role2_pos = "646 995"
        self.fight_role3_pos = "892 988"
        self.fight_role4_pos = "1135 989"
        self.fight_role5_pos = "1442 988"
        self.fight_role6_pos = "1696 995"

        self.fight_skill_1 = "450 819"
        self.fight_skill_2 = "830 822"
        self.fight_skill_3 = "1194 822"
        self.fight_skill_4 = "1556 819"

        self.fight_skill_change = "1954 992"
        self.attack = "1995 936"
        self.af = "2051 107"

        self.sebas_a_4_pos = "622 429"
        self.yes_to_move_pos = "1393 965"

        self.lmove_left = "2197 443 749 597"

        self.any_pos = "924 668"

    def start(self):
        # self.moveto_fighting_room()
        print('into benandark')
        return

        count = 1
        while True:
            start_time = datetime.datetime.now()
            print('=====start count: %s =====' % count)

            self.into_room_4()
            sleep(7)
            self.fight_1()

            end_time = datetime.datetime.now()
            self.print_time(start_time, end_time)
            print("=====Done=====")
            count += 1

    @staticmethod
    def print_time(start_time, end_time):
        print("")
        print(start_time.strftime("%H:%M:%S")+' - '+end_time.strftime("%H:%M:%S"))
        count_time = (end_time - start_time).seconds
        count_time = int(count_time)
        print("Total time: %s" % time.strftime("%H:%M:%S", time.gmtime(count_time)))

    def fight_1(self):
        print("start fight 1")
        self.touch_pos(self.fight_role1_pos)
        self.touch_pos(self.fight_skill_3)
        self.touch_pos(self.fight_role2_pos)
        self.touch_pos(self.fight_skill_2)
        self.touch_pos(self.fight_role3_pos)
        self.touch_pos(self.fight_skill_3)
        self.touch_pos(self.fight_role4_pos)
        self.touch_pos(self.fight_skill_2)
        self.touch_pos(self.attack)
        sleep(13)
        self.fight_2()

    def fight_2(self):
        print("start fight 2")
        self.touch_pos(self.attack)
        sleep(9)
        self.touch_pos(self.attack)
        sleep(14)
        self.fight_3()

    def fight_3(self):
        print("start fight 3")
        self.touch_pos(self.af)
        sleep(0.3)
        for i in range(0, 4):
            self.touch_pos(self.fight_skill_3)

        for i in range(0, 8):
            self.touch_pos(self.fight_skill_2)

        sleep(6)
        self.touch_pos(self.any_pos)
        sleep(8)
