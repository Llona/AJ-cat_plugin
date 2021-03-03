from settings import RoleEnum
from ami_role import AmiRoleCopy
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
    if sys.argv[1] == RoleEnum.AMI.value:
        role_run = AmiRoleCopy()
        role_run.start(TicketEnum.RED, get_ticket_num(TicketEnum.RED))
        role_run.start(TicketEnum.GREEN, get_ticket_num(TicketEnum.GREEN))
    else:
        print('Error!! Your Role: '+sys.argv[1]+' is not support, please check it\n')
