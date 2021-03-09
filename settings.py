import sys
from os import path
import enum
import platform

if platform.system() == 'Windows':
    VIRTUAL_DISK = 'R:'
    VIRTUAL_CREATE_CMD = 'imdisk -a -s 64M -m '+VIRTUAL_DISK+' -o rem -p "/fs:ntfs /v:RamDisk /q /y" > nul'
else:
    VIRTUAL_DISK = '/tmp/ramdisk/'
    VIRTUAL_MOUNT_CMD = 'echo Aa112233 | sudo -S mount -t tmpfs -o size=64M tmpfs ' + VIRTUAL_DISK
    VIRTUAL_UMOUNT_CMD = 'echo Aa112233 | sudo -S umount ' + VIRTUAL_DISK

NO_VD_SCREEN_DUMP_PATH = path.join(sys.path[0], 'screen.dump')
SCREEN_DUMP_PATH = path.join(VIRTUAL_DISK, 'screen.dump')

FIGHTING_COLOR = "664688"


class RoleEnum(enum.Enum):
    AMI = 'ami'


class TicketEnum(enum.Enum):
    GREEN = 'green'
    RED = 'red'
