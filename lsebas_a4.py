# -*- coding: utf-8 -*-
from time import sleep
import time
import datetime
from copy_plugin import LSebas


class LittleSebasA4(LSebas):
    def __init__(self):
        super(LittleSebasA4, self).__init__()
        article_obj = self
        self.setup(article_obj)

    def start(self):
        self.moveto_fighting_room()

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
        self.touch_pos(self.fight_skill_2)
        self.touch_pos(self.fight_role2_pos)
        self.touch_pos(self.fight_skill_2)
        self.touch_pos(self.fight_role3_pos)
        self.touch_pos(self.fight_skill_3)
        self.touch_pos(self.fight_role4_pos)
        self.touch_pos(self.fight_skill_2)
        self.touch_pos(self.attack)
        sleep(14)
        self.fight_2()

    def fight_2(self):
        print("start fight 2")
        self.touch_pos(self.attack)
        sleep(9)
        self.touch_pos(self.attack)
        sleep(16)
        self.fight_3()

    def fight_3(self):
        print("start fight 3")
        self.touch_pos(self.af)
        sleep(0.3)
        for i in range(0, 4):
            self.touch_pos(self.fight_skill_3)

        for i in range(0, 10):
            self.touch_pos(self.fight_skill_2)

        sleep(12.5)
        self.touch_pos(self.any_pos)
        sleep(8)
