# -*- coding: utf-8 -*-
from time import sleep
from copy_plugin import RunTicket
from copy_plugin import RunRoleCopy


class AlderRoleCopy(RunTicket, RunRoleCopy):
    def __init__(self):
        super(AlderRoleCopy, self).__init__()
        article_obj = self

        self.treasure_chest11_pos = "1239 369"
        self.treasure_chest12_pos = "961 384"
        self.treasure_chest21_pos = "840 384"
        self.treasure_chest31_pos = "1504 372"
        self.treasure_chest32_pos = "846 378"
        self.treasure_chest33_pos = "942 375"
        self.treasure_chest41_pos = "1384 386"

        self.any_pos = "1835 386"

        self.floor_num = 0

        self.setup(article_obj)

    def start(self, ticket_type, ticket_num):
        self.run_ticket(ticket_type, ticket_num)

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
        self.swipe("lright", 300)
        self.swipe("ldown", 258)
        # self.swipe("lright", 300)
        sleep(0.3)
        self.touch_pos(self.alder_pos)
        sleep(0.5)

    def set_default_skills(self):
        # 會長 無何有之鄉
        self.touch_pos(self.fight_role1_pos)
        self.touch_pos(self.fight_skill_2)

        # 普攻
        self.touch_pos(self.fight_role2_pos)
        self.touch_pos(self.fight_skill_1)
        self.touch_pos(self.fight_role3_pos)
        self.touch_pos(self.fight_skill_1)
        self.touch_pos(self.fight_role4_pos)
        self.touch_pos(self.fight_skill_1)

    def set_special_fight_skills(self):
        # 喵可可 化妖 貓鉤一閃
        self.touch_pos(self.fight_role3_pos)
        self.touch_pos(self.fight_skill_3)
        # 普攻
        self.touch_pos(self.fight_role1_pos)
        self.touch_pos(self.fight_skill_1)
        self.touch_pos(self.fight_role2_pos)
        self.touch_pos(self.fight_skill_1)
        self.touch_pos(self.fight_role4_pos)
        self.touch_pos(self.fight_skill_1)

    def clear_fighting(self, is_run_copy=True):
        # change role to add mp
        # if self.floor_num == 2:
        #     # self.touch_pos(self.fight_role2_pos)
        #     # self.touch_pos(self.fight_skill_change)
        #     # self.touch_pos(self.fight_role5_pos)
        # else:
        self.touch_pos(self.fight_skill_1)
        if self.floor_num == 3:
            pass
            # sleep(0.2)

        if self.floor_num == 1 and self.floor_fight_count == 0:
            print("set default skills")
            self.set_default_skills()

        if self.floor_num == 3 and self.floor_fight_count == 0:
            print("set alder skills")
            self.set_special_fight_skills()

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
        self.clear_fighting_by_yukino()
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

        # change 雪乃 for boss fighting
        # self.change_member_4_and_5()
        # self.eat_food_in_copy()

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
        self.swipe("left", 4500)
        self.swipe("right", 1600)
        self.swipe("down")
        sleep(0.7)
        self.swipe("left", 1900)
        self.swipe("down")
        sleep(0.7)
        self.swipe("right", 2400)
        self.touch_pos(self.treasure_chest31_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        sleep(0.2)

    def get_treasure_chest_32(self):
        self.swipe("left", 2200)
        self.swipe("up")
        sleep(0.7)
        self.swipe("left", 4500)
        self.swipe("down")
        sleep(0.7)
        self.swipe("left", 2000)
        self.touch_pos(self.treasure_chest32_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        sleep(0.2)

    def get_treasure_chest_33(self):
        self.swipe("right", 1500)
        self.swipe("up")
        sleep(0.7)
        self.swipe("left", 3000)
        self.touch_pos(self.treasure_chest33_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        sleep(0.5)

    def go_floor4(self):
        self.swipe("right", 4000)
        self.swipe("up")
        sleep(0.7)
        self.swipe("left", 2000)
        self.swipe("up")
        sleep(3)

    def run_floor2(self):
        self.floor_num = 2
        self.clear_all_fight("left")
        self.clear_fear_2()
        self.get_treasure_chest_21()

    def clear_fear_2(self):
        self.goto_fighting_fear_2()
        self.clear_fighting_by_yukino()
        sleep(0.3)
        # change 雪乃 to back for add mp in normal fighting
        # self.change_member_4_and_5()

    def goto_fighting_fear_2(self):
        self.swipe("right", 5000)

        # change 雪乃 for fear fighting
        # self.change_member_4_and_5()

        self.swipe("left", 1600)
        self.swipe("up")
        sleep(0.7)
        self.swipe("left", 2500)
        self.swipe("up")
        sleep(5)

        while not self.is_fighting_state():
            print("sleep 3 sec for waiting fear fighting")
            sleep(3)
        print("start fear fighting")

    def clear_fighting_by_yukino(self):
        self.touch_pos(self.fight_role1_pos)
        self.touch_pos(self.fight_skill_4)  # 神速的旋律
        self.touch_pos(self.fight_role2_pos)
        self.touch_pos(self.fight_skill_2)  # 飛雪千里
        self.touch_pos(self.fight_role3_pos)
        self.touch_pos(self.fight_skill_4)  # 貓神的守護
        self.touch_pos(self.fight_role4_pos)
        self.touch_pos(self.fight_skill_2)  # 交叉斬改

        self.touch_pos(self.attack)
        sleep(6)

        self.touch_pos(self.any_pos)
        sleep(2)

    def get_treasure_chest_21(self):
        self.swipe("left", 3100)
        self.swipe("down")
        sleep(0.7)
        self.swipe("left", 3800)
        self.swipe("up")
        sleep(0.7)
        self.swipe("left", 2300)
        self.touch_pos(self.treasure_chest21_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        sleep(0.2)

    def go_floor3(self):
        self.swipe("right", 1500)
        self.swipe("down")
        sleep(0.7)
        self.swipe("right", 2000)
        self.swipe("down")
        sleep(0.7)
        self.swipe("left", 1400)
        self.swipe("up")
        sleep(3)

    def run_floor1(self):
        self.floor_num = 1
        sleep(2)
        # self.change_member_4_and_5()
        self.clear_all_fight("right")
        self.get_treasure_chest_11()
        self.get_treasure_chest_12()

    def get_treasure_chest_11(self):
        self.swipe("right", 3300)
        self.swipe("left", 300)
        self.swipe("up")
        sleep(0.7)
        self.swipe("left", 1200)
        self.swipe("up")
        sleep(0.7)
        self.swipe("left", 1600)
        self.touch_pos(self.treasure_chest11_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        sleep(0.2)

    def get_treasure_chest_12(self):
        self.swipe("right", 1500)
        self.swipe("down")
        sleep(0.7)
        self.swipe("left", 4000)
        self.swipe("up")
        sleep(0.7)
        self.swipe("left", 3300)
        self.swipe("down")
        sleep(0.7)
        self.swipe("left", 4100)
        self.touch_pos(self.treasure_chest12_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        sleep(0.2)

    def go_floor_2(self):
        self.swipe("right", 1500)
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
