# -*- coding: utf-8 -*-
from time import sleep
from copy_plugin import RunTicket
from copy_plugin import RunRoleCopy


class MoonRoleCopy(RunTicket, RunRoleCopy):
    def __init__(self):
        super(MoonRoleCopy, self).__init__()
        article_obj = self

        self.treasure_chest11_pos = "1141 404"
        self.treasure_chest12_pos = "1241 374"
        self.treasure_chest21_pos = "572 377"
        self.treasure_chest31_pos = "1223 370"
        self.treasure_chest32_pos = "1214 405"
        self.treasure_chest33_pos = "1185 365"
        self.treasure_chest41_pos = "1449 238"

        self.moon_after_second_pos = "1190 541"

        self.floor_num = 0

        self.setup(article_obj)

    def start(self, ticket_type, ticket_num):
        self.run_ticket(ticket_type, ticket_num)

    def goto_dimension(self):
        if self.run_count == 1:
            self.touch_pos(self.map_pos)
            sleep(1)
            self.touch_pos(self.future_pos)
            sleep(0.5)
            self.touch_pos(self.extradimensional_pos)
            sleep(0.5)
            self.touch_pos(self.dimension_pos)
            sleep(0.3)
            self.touch_pos(self.yes_pos)
            sleep(2)
        else:
            return

    def eat_tree_food(self):
        if self.run_count == 1:
            self.touch_pos(self.food_pos)
            sleep(0.5)
            self.touch_pos(self.any_pos)
            sleep(1)
            self.touch_pos(self.yes_pos)
            sleep(2)
            self.touch_pos(self.any_pos)
            sleep(1)
            self.touch_pos(self.any_pos)
            sleep(0.5)
            self.touch_pos(self.any_pos)
            sleep(0.5)
        else:
            # no need to eat
            return

    def moveto_copy_map(self):
        # into door
        if self.run_count == 1:
            self.swipe("left", 500)
            self.touch_pos(self.door_pos)
            sleep(1)

            self.touch_pos(self.future_pos)
            sleep(0.5)
            self.touch_pos(self.modern_pos)
            sleep(0.5)
            self.touch_pos(self.area_pos)
            sleep(0.5)
            self.touch_pos(self.migunia_area_pos)
            sleep(0.5)
            self.swipe("lright", 300)
            self.swipe("lright", 300)
            self.swipe("ldown", 258)
            self.swipe("ldown", 300)

            sleep(0.3)
            self.touch_pos(self.moon_pos)

        else:
            self.touch_pos(self.door_after_second_pos)
            sleep(1)

            self.touch_pos(self.moon_after_second_pos)
        sleep(0.5)

    def set_default_skills(self):
        # 普攻
        self.touch_pos(self.fight_role1_pos)
        self.touch_pos(self.fight_skill_1)
        self.touch_pos(self.fight_role2_pos)
        self.touch_pos(self.fight_skill_1)
        self.touch_pos(self.fight_role3_pos)
        self.touch_pos(self.fight_skill_1)
        self.touch_pos(self.fight_role4_pos)
        self.touch_pos(self.fight_skill_1)

    def clear_fighting(self, is_run_copy=True):
        # self.touch_pos(self.fight_skill_1)

        if self.floor_num == 1 and self.floor_fight_count == 0:
            print("set default skills")
            self.set_default_skills()
        elif self.floor_num == 3 and self.floor_fight_count == 0:
            print("set default skills")
            self.set_default_skills()

        self.touch_pos(self.attack)

        if self.floor_num == 3:
            sleep(3.8)
        else:
            sleep(4.3)

        self.touch_pos(self.any_pos)
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
        self.clear_fighting_boss_fear()
        sleep(6)

        self.touch_pos(self.any_pos)
        sleep(10)
        self.touch_pos(self.any_pos)    # get item
        sleep(5)
        self.touch_pos(self.any_pos)    # may up sky level
        sleep(5)
        self.touch_pos(self.any_pos)    # may get white key
        sleep(2)

    def run_floor4(self):
        self.floor_num = 4
        self.swipe("left", 1600)
        self.touch_pos(self.treasure_chest41_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        sleep(0.2)

        # go to boss room
        self.swipe("left", 4000)
        self.touch_pos(self.boss_fight_yes_pos)
        sleep(4)

    def run_floor3(self):
        self.floor_num = 3
        self.clear_all_fight("right")
        self.get_treasure_chest_31()
        self.get_treasure_chest_32()
        self.get_treasure_chest_33()

    def get_treasure_chest_31(self):
        self.swipe("right", 11000)
        self.swipe("left", 1500)
        self.swipe("up")
        sleep(0.7)
        self.swipe("left", 4000)
        self.touch_pos(self.treasure_chest31_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        sleep(0.2)

    def get_treasure_chest_32(self):
        self.swipe("right", 1200)
        self.swipe("down")
        sleep(0.7)
        self.swipe("left", 1200)
        self.swipe("down")
        sleep(0.7)
        self.swipe("right", 2600)
        self.touch_pos(self.treasure_chest32_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        sleep(0.2)

    def get_treasure_chest_33(self):
        self.swipe("left", 2500)
        self.swipe("up")
        sleep(0.7)
        self.swipe("left", 5100)
        self.swipe("up")
        sleep(0.7)
        self.swipe("left", 1300)
        self.touch_pos(self.treasure_chest33_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        sleep(0.5)

    def go_floor4(self):
        self.swipe("right", 1300)
        self.swipe("down")
        sleep(0.7)
        self.swipe("right", 1300)
        self.swipe("down")
        sleep(0.7)
        self.swipe("left", 3100)
        self.swipe("up")
        sleep(3)

    def run_floor2(self):
        self.floor_num = 2
        self.clear_all_fight("left")
        self.get_treasure_chest_21()
        self.clear_fear_2()

    def clear_fear_2(self):
        self.goto_fighting_fear_2()
        self.clear_fighting_boss_fear()
        sleep(0.3)

    def goto_fighting_fear_2(self):
        self.swipe("right", 2200)
        self.swipe("down")
        sleep(0.7)
        self.swipe("right", 600)
        self.swipe("down")
        sleep(0.7)
        self.swipe("left", 5700)
        self.swipe("up")
        sleep(5)

        while not self.is_fighting_state():
            print("sleep 3 sec for waiting fear fighting")
            sleep(3)
        print("start fear fighting")

    def clear_fighting_boss_fear(self):
        self.touch_pos(self.fight_role1_pos)
        self.touch_pos(self.fight_skill_2)
        self.touch_pos(self.fight_role2_pos)
        self.touch_pos(self.fight_skill_2)
        self.touch_pos(self.fight_role3_pos)
        self.touch_pos(self.fight_skill_2)
        self.touch_pos(self.fight_role4_pos)
        self.touch_pos(self.fight_skill_2)

        self.touch_pos(self.attack)
        sleep(6)

        self.touch_pos(self.any_pos)
        sleep(2)

    def get_treasure_chest_21(self):
        self.swipe("left", 2800)
        self.swipe("up")
        sleep(0.7)
        self.swipe("left", 2400)
        self.swipe("up")
        sleep(0.7)
        self.swipe("left", 2200)
        self.touch_pos(self.treasure_chest21_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        sleep(0.2)

    def go_floor3(self):
        self.swipe("left", 1300)
        self.swipe("up")
        sleep(0.7)
        self.swipe("left", 1300)
        self.swipe("up")
        sleep(3)

    def run_floor1(self):
        self.floor_num = 1
        sleep(2)

        self.clear_all_fight("right")
        self.get_treasure_chest_11()
        self.get_treasure_chest_12()

    def get_treasure_chest_11(self):
        self.swipe("left", 8000)
        self.swipe("up")
        sleep(0.7)
        self.swipe("right", 2000)
        self.touch_pos(self.treasure_chest11_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        sleep(0.2)

    def get_treasure_chest_12(self):
        self.swipe("left", 5000)
        self.swipe("down")
        sleep(0.7)
        self.swipe("right", 1500)
        self.touch_pos(self.treasure_chest12_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        sleep(0.2)

    def go_floor_2(self):
        self.swipe("left", 1500)
        self.swipe("up")
        sleep(0.7)
        self.swipe("right", 1850)
        self.swipe("up")
        sleep(0.7)
        self.swipe("left", 1800)
        self.swipe("up")
        sleep(3)

    def change_member_4_and_5(self):
        self.open_member_list()
        self.swipe_by_position(self.copy_team_list_4, self.copy_team_list_5)
        sleep(0.1)
        self.touch_pos(self.copy_team_list_close)
        sleep(0.4)

    def open_member_list(self):
        self.touch_pos(self.copy_menu_btn)
        sleep(0.2)
        self.touch_pos(self.copy_team_btn)
        sleep(0.5)
