import sys
from os import path
import enum

VIRTUAL_DISK = 'R:'
VIRTUAL_CREATE_CMD = 'imdisk -a -s 64M -m '+VIRTUAL_DISK+' -o rem -p "/fs:ntfs /v:RamDisk /q /y" > nul'
NO_VD_SCREEN_DUMP_PATH = path.join(sys.path[0], 'screen.dump')
SCREEN_DUMP_PATH = path.join(VIRTUAL_DISK, 'screen.dump')


class RoleEnum(enum.Enum):
    AMI = 'ami'


class TicketEnum(enum.Enum):
    GREEN = 'green'
    RED = 'red'
