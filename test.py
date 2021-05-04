import os
import re
import platform
from copy_plugin import RunTicket
from alder_role import AlderRoleCopy
import glob


# test2 = RunTicket()
# test2.setup(None)
# test2.goto_dimension_eat()

# test = AlderRoleCopy()
# print("=====Go to floor 1=====")
# test.run_floor1()
# test.go_floor_2()
# print("=====Go to floor 2=====")
# test.run_floor2()
# test.go_floor3()
# print("=====Go to floor 3=====")
# test.run_floor3()
# test.go_floor4()
# print("=====Go to Boss Room=====")
# test.run_floor4()
# print("=====Start Boss fighting=====")
# test.boss_fighting()
screen_dump_file_list = os.listdir("R:")
print(len(screen_dump_file_list))
# for screen_dump_file in screen_dump_file_list:
#     os.remove(screen_dump_file)
