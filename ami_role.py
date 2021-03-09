# -*- coding: utf-8 -*-
from time import sleep
from copy_plugin import RunTicket
from copy_plugin import RunRoleCopy


class AmiRoleCopy(RunTicket, RunRoleCopy):
    def __init__(self):
        super(AmiRoleCopy, self).__init__()
        article_obj = self
        self.setup(article_obj)

    def start(self, ticket_type, ticket_num):
        self.run_ticket(ticket_type, ticket_num)

    def moveto_copy_map(self):
        self.touch_pos(self.future_pos)

        sleep(0.5)
        self.swipe("lright", 300)
        self.swipe("lup", 258)
        sleep(0.5)
        self.touch_pos(self.ami_pos)
        sleep(0.5)

    def run_role_copy(self):
        print("=====Go to floor 1=====")
        self.run_floor1()
        self.go_floor_2()
        print("=====Go to floor 2=====")
        self.run_floor2()
        self.go_floor3()
        print("=====Go to floor 3=====")
        self.run_floor3()
        self.go_floor4()
        print("=====Go to Boss Room=====")
        self.run_floor4()
        print("=====Start Boss fighting=====")
        self.boss_fighting()

    def boss_fighting(self):
        # fight 1
        self.touch_pos(self.fight_role1_pos)
        sleep(0.1)
        self.touch_pos(self.fight_skill_2)
        sleep(0.1)
        self.touch_pos(self.fight_role2_pos)
        sleep(0.1)
        self.touch_pos(self.fight_skill_2)
        sleep(0.1)
        self.touch_pos(self.fight_role3_pos)
        sleep(0.1)
        self.touch_pos(self.fight_skill_2)
        sleep(0.1)
        self.touch_pos(self.fight_role4_pos)
        sleep(0.1)
        self.touch_pos(self.fight_skill_2)
        sleep(0.1)
        self.touch_pos(self.attack)
        sleep(3)
        self.touch_pos(self.any_pos)
        sleep(10)
        self.touch_pos(self.attack)
        sleep(14)
        self.touch_pos(self.any_pos)
        sleep(12)
        self.touch_pos(self.any_pos)    # get item
        sleep(5)
        self.touch_pos(self.any_pos)    # may up sky level
        sleep(5)
        self.touch_pos(self.any_pos)    # may get white key
        sleep(2)

    def run_floor4(self):
        self.swipe("left", 3000)
        self.touch_pos(self.treasure_chest41_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        sleep(0.2)
        self.swipe("left", 3000)
        self.touch_pos(self.boss_fight_pos)
        sleep(0.5)
        self.touch_pos(self.boss_fight_yes_pos)
        sleep(5)

    def run_floor3(self):
        self.clear_all_fight("right")
        self.get_treasure_chest_31()
        self.get_treasure_chest_32()
        self.get_treasure_chest_33()

    def get_treasure_chest_31(self):
        self.swipe("right", 6300)
        self.swipe("left", 3000)
        self.swipe("down")
        sleep(0.5)
        self.swipe("left", 3600)
        self.swipe("up")
        sleep(1)
        self.swipe("right", 800)
        self.touch_pos(self.treasure_chest31_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        self.swipe("left", 500)
        self.swipe("down")
        sleep(0.6)

    def get_treasure_chest_32(self):
        self.swipe("left", 1500)
        self.swipe("up")
        sleep(0.3)
        self.swipe("left", 2500)
        self.swipe("down")
        sleep(0.3)
        self.swipe("left", 2800)
        self.touch_pos(self.treasure_chest32_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        sleep(0.2)

    def get_treasure_chest_33(self):
        self.swipe("right", 600)
        self.swipe("down")
        sleep(0.3)
        self.swipe("right", 3100)
        self.swipe("up")
        sleep(1)
        self.swipe("left", 1200)
        self.touch_pos(self.treasure_chest33_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        sleep(0.2)
        self.swipe("right", 1200)
        self.swipe("down")
        sleep(0.6)

    def go_floor4(self):
        self.swipe("right", 8300)
        self.swipe("up")
        sleep(2)

    def run_floor2(self):
        self.clear_all_fight("left")
        self.get_treasure_chest_21()

    def get_treasure_chest_21(self):
        self.swipe("right", 6300)
        self.swipe("left", 2000)
        self.swipe("up")
        sleep(0.3)
        self.swipe("right", 6000)
        self.swipe("down")
        sleep(0.3)
        self.swipe("left", 3000)
        self.touch_pos(self.treasure_chest21_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        sleep(0.2)

    def go_floor3(self):
        self.swipe("right", 2600)
        self.swipe("up")
        sleep(0.3)
        self.swipe("right", 3000)
        self.touch_pos(self.elevator_to_floor_3_pos)
        sleep(1)
        self.touch_pos(self.elevator_to_floor_3_yes_pos)
        sleep(5)

    def run_floor1(self):
        self.clear_all_fight("right")
        self.get_treasure_chest_12()

    def get_treasure_chest_12(self):
        self.swipe("left", 9000)
        self.swipe("up")
        sleep(1)
        self.swipe("left", 1000)
        self.touch_pos(self.treasure_chest12_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        sleep(0.2)
        self.swipe("right", 500)
        self.swipe("down")
        sleep(1)

    def go_floor_2(self):
        self.swipe("right", 2500)
        self.swipe("up")
        sleep(1)
        self.swipe("left", 6000)
        self.swipe("up")
        sleep(1.5)
