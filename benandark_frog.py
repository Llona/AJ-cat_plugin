# -*- coding: utf-8 -*-
from time import sleep
import time
import datetime
import settings
from copy_plugin import LSebas


def reset_position_setting(obj):
    obj.device_id = '2785a241e41c7ece'
    settings.FIGHTING_COLOR = "010203"
    obj.screen_high = 2220
    obj.screen_wight = 1080

    obj.fight_x = 554
    obj.fight_y = 833
    obj.fight_offset = obj.screen_high*obj.fight_y+obj.fight_x

    obj.boss_fight_pos = "1526 293"
    obj.boss_fight_yes_pos = "1338 600"

    obj.fight_role1_pos = "338 1000"
    obj.fight_role2_pos = "586 995"
    obj.fight_role3_pos = "832 988"
    obj.fight_role4_pos = "1075 989"
    obj.fight_role5_pos = "1382 988"
    obj.fight_role6_pos = "1636 995"

    obj.fight_skill_1 = "390 819"
    obj.fight_skill_2 = "770 822"
    obj.fight_skill_3 = "1134 822"
    obj.fight_skill_4 = "1496 819"

    obj.fight_skill_change = "1894 992"
    obj.attack = "1965 936"
    obj.af = "1991 107"

    obj.copy_menu_btn = "309 965"
    obj.copy_food_btn = "1043 905"
    obj.copy_team_btn = "870 907"
    obj.copy_team_list_4 = "1228 569"
    obj.copy_team_list_5 = "1579 551"
    obj.copy_team_list_close = "2056 36"
    obj.copy_eat_food_yes_ben = "1310 637"

    obj.elevator_to_floor_3_pos = "953 326"
    obj.elevator_to_floor_3_yes_pos = "1338 595"

    obj.any_pos = "864 668"
    obj.any2_pos = "1234 244"
    obj.map_pos = "605 1002"
    obj.extradimensional_pos = "873 183"
    obj.dimension_pos = "1101 600"
    obj.yes_pos = "1365 641"
    obj.food_pos = "836 120"
    obj.door_pos = "868 254"

    obj.future_pos = "662 185"
    obj.modern_pos = "480 201"
    obj.area_pos = "1965 984"
    obj.migunia_area_pos = "729 590"

    obj.eluzion_pos = "545 1013"
    obj.sebas_pos = "1675 672"
    obj.sebas_door_pos = "1155 228"
    obj.sebas_a_pos = "434 577"
    obj.sebas_a_4_pos = "562 429"

    obj.ami_pos = "1069 571"
    obj.lika_pos = "459 441"
    obj.alder_pos = "2125 1043"

    obj.red_ticket_pos = "1719 533"
    obj.green_ticket_pos = "1735 378"
    obj.yes_to_move_pos = "1333 965"

    obj.run_right = "272 831 555 842"
    obj.run_left = "562 792 263 837"
    obj.run_up = "435 657 548 328"
    obj.run_down = "1622 400 1651 731"

    obj.lmove_right = "335 619 2110 563"
    obj.lmove_up = "428 819 810 190"
    obj.lmove_left = "2137 443 689 597"
    obj.lmove_down = "1331 333 1369 966"


class BenandarkFrog(LSebas):
    def __init__(self):
        super(BenandarkFrog, self).__init__()
        article_obj = self
        self.setup(article_obj)
        reset_position_setting(self)

    def start(self):
        # self.moveto_fighting_room()
        print('change device id to:' + self.device_id)
        print('start benandark frog fighting')

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
        self.touch_pos(self.fight_skill_4)
        self.touch_pos(self.attack)
        sleep(16)
        self.fight_2()

    def fight_2(self):
        print("start fight 2")
        # self.touch_pos(self.attack)
        # sleep(9)
        self.touch_pos(self.attack)
        sleep(17)
        self.fight_3()

    def fight_3(self):
        print("start fight 3")
        # self.touch_pos(self.af)
        # sleep(0.3)
        # for i in range(0, 4):
        #     self.touch_pos(self.fight_skill_3)
        #
        # for i in range(0, 8):
        #     self.touch_pos(self.fight_skill_2)
        self.touch_pos(self.attack)
        sleep(7)
        self.touch_pos(self.any_pos)
        sleep(8)
