from settings import RoleEnum
from ami_role import AmiRoleCopy
from lika_role import LikaRoleCopy
from alder_role import AlderRoleCopy
from lsebas_a4 import LittleSebasA4
from moon_role import MoonRoleCopy
from benandark_frog import BenandarkFrog
from settings import TicketEnum
import sys


def get_ticket_num(ticket_type):
    try:
        green_num = int(sys.argv[2])
        red_num = int(sys.argv[3])
    except Exception as e:
        print("Error!! Green and Red ticket number is wrong\n")
        str(e)
        raise

    if ticket_type == TicketEnum.GREEN:
        return green_num
    else:
        return red_num


if __name__ == '__main__':
    is_copy = True

    if sys.argv[1] == RoleEnum.AMI.value:
        role_run = AmiRoleCopy()
    elif sys.argv[1] == RoleEnum.LIKA.value:
        role_run = LikaRoleCopy()
    elif sys.argv[1] == RoleEnum.ALDER.value:
        role_run = AlderRoleCopy()
    elif sys.argv[1] == RoleEnum.MOON.value:
        role_run = MoonRoleCopy()
    elif sys.argv[1] == RoleEnum.LSebas_A4.value:
        role_run = LittleSebasA4()
        is_copy = False
    elif sys.argv[1] == RoleEnum.Benandark.value:
        role_run = BenandarkFrog()
        is_copy = False
    else:
        print('Error!! Your Role: '+sys.argv[1]+' is not support, Role list:')
        for i in RoleEnum:
            print(i.value)
        sys.exit()

    if is_copy:
        role_run.start(TicketEnum.RED, get_ticket_num(TicketEnum.RED))
        role_run.start(TicketEnum.GREEN, get_ticket_num(TicketEnum.GREEN))
    else:
        role_run.start()
