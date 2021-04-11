# -*- coding: utf-8 -*-

from time import sleep
from os import system
import subprocess
from abc import ABC, abstractmethod
import os
import sys
import settings
from settings import TicketEnum
import platform

if platform.system() == "Windows":
    import win32api
    import win32file


class Position(object):
    def __init__(self):
        self.screen_high = 2280
        self.screen_wight = 1080
        self.fight_x = 2039
        self.fight_y = 831
        self.fight_offset = self.screen_high*self.fight_y+self.fight_x

        self.boss_fight_pos = "1586 293"
        self.boss_fight_yes_pos = "1398 600"

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
        self.fight_skill_change = "2039 831"
        self.attack = "1995 936"

        self.treasure_chest12_pos = "703 386"
        self.treasure_chest21_pos = "1216 393"
        self.treasure_chest31_pos = "1565 310"
        self.treasure_chest32_pos = "1141 412"
        self.treasure_chest33_pos = "1201 419"
        self.treasure_chest41_pos = "1484 309"

        self.elevator_to_floor_3_pos = "1013 326"
        self.elevator_to_floor_3_yes_pos = "1398 595"

        self.any_pos = "924 668"
        self.any2_pos = "1294 244"
        self.map_pos = "665 1002"
        self.future_pos = "722 185"
        self.extradimensional_pos = "933 183"
        self.dimension_pos = "1161 600"
        self.yes_pos = "1425 641"
        self.food_pos = "896 120"
        self.door_pos = "928 254"

        self.area_pos = "2025 984"
        self.migunia_area_pos = "789 590"

        self.red_ticket_pos = "1779 533"
        self.green_ticket_pos = "1795 378"
        self.yes_to_move_pos = "1393 965"

        self.ami_pos = "1129 571"
        self.lika_pos = "519 441"

        self.run_right = "332 831 615 842"
        self.run_left = "622 792 323 837"
        self.run_up = "495 657 608 328"
        self.run_down = "1682 400 1711 731"

        self.lmove_right = "395 619 2170 563"
        self.lmove_up = "488 819 870 190"
        self.lmove_left = "2165 567 749 597"
        self.lmove_down = "1391 333 1429 966"


class RunTicket(Position):
    def __init__(self, fight_type='joker'):
        super(RunTicket, self).__init__()
        self.fight_type = fight_type

        self.get_pixel_color_cmd = ''
        self.dump_screen_buffer_cmd = ''
        self.role_obj = None

        self.dd_path = ''
        self.xxd_path = ''
        self.adb_path = ''

        self.device_id = ''

        # self.setup()

    def setup(self, obj):
        if platform.system() == "Windows":
            self.dd_path = os.path.join(sys.path[0], 'dd.exe')
            self.xxd_path = os.path.join(sys.path[0], 'xxd.exe')
            self.adb_path = os.path.join(sys.path[0], 'adb.exe')
        else:
            self.dd_path = 'dd'
            self.xxd_path = 'xxd'
            self.adb_path = 'adb'

        self.get_pixel_color_cmd = \
            self.dd_path+" if="+settings.SCREEN_DUMP_PATH + " bs=4 count=1 skip=" + \
            str(self.fight_offset)+" 2>" + settings.NULL_DEV + " | "+self.xxd_path+" -ps"
        # print(self.get_pixel_color_cmd)

        self.role_obj = obj

        if platform.system() == 'Windows':
            self.create_virtual_disk_windows()
        else:
            self.create_virtual_disk_linux()

        self.get_device_id()

        self.dump_screen_buffer_cmd = \
            self.adb_path + " -s " + self.device_id + " exec-out screencap > " + settings.SCREEN_DUMP_PATH

    def get_device_id(self):
        res = self.run_wait(self.adb_path + ' devices')
        res = res.replace('List of devices attached\n', '')
        res = res.replace('device', '')
        res = res.strip()
        self.device_id = res
        print("Device ID: " + self.device_id)

    @staticmethod
    def create_virtual_disk_linux():
        if not os.path.exists(settings.VIRTUAL_DISK):
            os.system('mkdir ' + settings.VIRTUAL_DISK)

        print('create virtual disk '+settings.VIRTUAL_DISK)
        try:
            os.system(settings.VIRTUAL_UMOUNT_CMD)
            os.system(settings.VIRTUAL_MOUNT_CMD)
            print('create done')
        except Exception as e:
            print("can't create virtual disk, please check " + settings.VIRTUAL_DISK +
                  "use virtual disk can protect your HDD")
            settings.SCREEN_DUMP_PATH = settings.NO_VD_SCREEN_DUMP_PATH
            str(e)

    def create_virtual_disk_windows(self):
        # if len(self.get_ramdrive_by_label()) == 0:
        for drive in self.get_ramdrive_by_label():
            if drive == settings.VIRTUAL_DISK:
                return
        print('create virtual disk '+settings.VIRTUAL_DISK)
        try:
            os.system(settings.VIRTUAL_CREATE_CMD)
            print('create done')
        except Exception as e:
            print("can't create virtual disk, please make sure install IMdisk, "
                  "use virtual disk can protect your HDD")
            settings.SCREEN_DUMP_PATH = settings.NO_VD_SCREEN_DUMP_PATH
            str(e)

    def run_ticket(self, ticket_type, ticket_num):
        system(self.adb_path + " wait-for-device")
        run_count = 0

        while run_count < ticket_num:

            # return
            self.goto_dimension_eat()

            # into door
            self.swipe("left", 500)
            self.touch_pos(self.door_pos)
            sleep(1)

            # move map to copy
            moveto_copy_map(self.role_obj)
            # break

            if ticket_type == TicketEnum.RED:
                print("red ticket")
                self.touch_pos(self.red_ticket_pos)
            else:
                print("green ticket")
                self.touch_pos(self.green_ticket_pos)

            sleep(0.5)
            self.touch_pos(self.yes_to_move_pos)
            sleep(2)

            run_role_copy(self.role_obj)

            run_count += 1

    def clear_all_fight(self, door_direction, fight_total_count=settings.COPY_FIGHT_TOTAL_COUNT):
        current_direction = door_direction
        go_run_fight = False
        count = 0

        if fight_total_count == 0:
            is_run_copy = False
        else:
            is_run_copy = True

        if fight_total_count == 0 or count < fight_total_count:
            go_run_fight = True

        while go_run_fight:
            if current_direction == "right":
                self.swipe("left", 3000)
                current_direction = "left"
            else:
                self.swipe("right", 3000)
                current_direction = "right"

            if self.is_fighting_state():
                print("is in fight state")
                self.clear_fighting(is_run_copy)
                count += 1
                print("fight count:" + str(count))
            else:
                continue

            if fight_total_count != 0 and count >= fight_total_count:
                go_run_fight = False

    def clear_fighting(self, is_run_copy=True):
        if self.fight_type == 'joker':
            self.touch_pos(self.fight_role2_pos)
            sleep(0.2)
            self.touch_pos(self.fight_skill_change)
            sleep(0.2)
            self.touch_pos(self.fight_role5_pos)
            sleep(0.2)
        else:
            self.touch_pos(self.any_pos)
            sleep(0.2)

        self.touch_pos(self.attack)
        if is_run_copy:
            sleep(8.5)
        else:
            sleep(5)
        self.touch_pos(self.any_pos)

    def is_fighting_state(self):
        self.touch_pos(self.fight_role4_pos)
        sleep(0.2)
        pixel_color = self.get_fighting_pixel_color()

        if pixel_color == settings.FIGHTING_COLOR:
            return True
        else:
            return False

    def get_fighting_pixel_color(self):
        pixel_color = ""
        system('echo "" > ' + settings.SCREEN_DUMP_PATH)
        try:
            subprocess.check_output(self.dump_screen_buffer_cmd, shell=True, timeout=10)
            # system(self.adb_path + " -s " + self.device_id + " exec-out screencap > " + settings.SCREEN_DUMP_PATH)
        except Exception as e:
            print("adb timeout, re-get again")
            subprocess.check_output(self.dump_screen_buffer_cmd, shell=True, timeout=10)
            str(e)

        try:
            pixel_color = self.run_wait(self.get_pixel_color_cmd)
            # print(pixel_color)

            pixel_color = pixel_color[0:6]
        except Exception as e:
            sleep(3)
            self.get_fighting_pixel_color()
            str(e)

        # print(pixel_color)
        return pixel_color

    def goto_dimension_eat(self):
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
        self.eat_tree_food()

    def eat_tree_food(self):
        self.touch_pos(self.food_pos)
        sleep(0.5)
        self.touch_pos(self.any_pos)
        sleep(1)
        self.touch_pos(self.yes_pos)
        sleep(2)
        self.touch_pos(self.any_pos)
        sleep(1)

    def swipe(self, swipe_type, duration=70):
        run_direction = "left"

        if swipe_type == "left":
            run_direction = self.run_left
        elif swipe_type == "right":
            run_direction = self.run_right
        elif swipe_type == "up":
            run_direction = self.run_up
        elif swipe_type == "down":
            run_direction = self.run_down
        elif swipe_type == "lright":
            run_direction = self.lmove_right
        elif swipe_type == "lup":
            run_direction = self.lmove_up
        elif swipe_type == "lleft":
            run_direction = self.lmove_left
        elif swipe_type == "ldown":
            run_direction = self.lmove_down

        system("adb -s " + self.device_id + " shell \"input swipe " + run_direction + " " + str(duration) + "\"")

    def touch_pos(self, pos):
        system("adb -s " + self.device_id + " shell \"input tap " + pos + "\"")

    @staticmethod
    def run_wait(command):
        r = os.popen(command)
        text = r.read()
        r.close()
        return text

    @staticmethod
    def get_ramdrive_by_label():
        ramdisk_drives = []
        driver_list_str = win32api.GetLogicalDriveStrings()
        for driver in driver_list_str.split('\x00'):
            # 2 is removable driver, im ramdisk is 2
            if win32file.GetDriveType(driver) == 2 and win32api.GetVolumeInformation(driver+'\\')[0] == 'RamDisk':
                ramdisk_drives.append(driver[0:2])

        return ramdisk_drives


class RunRoleCopy(ABC):
    @abstractmethod
    def moveto_copy_map(self):
        return

    @abstractmethod
    def run_role_copy(self):
        return


def moveto_copy_map(obj):
    obj.moveto_copy_map()
    # return article_next_page_url


def run_role_copy(obj):
    obj.run_role_copy()
