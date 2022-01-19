import sys
from os import path
import enum
import platform

DEVICE_ID = 'RF8N32YBMGG'
# FIGHTING_COLOR = "528cca"
FIGHTING_COLOR = "5995d2"
# DEVICE_ID = '2785a241e41c7ece'
# FIGHTING_COLOR = "3c5e85"
COPY_FIGHT_TOTAL_COUNT = 5

if platform.system() == 'Windows':
    VIRTUAL_DISK = 'R:'
    VIRTUAL_CREATE_CMD = 'imdisk -a -s 64M -m '+VIRTUAL_DISK+' -o rem -p "/fs:ntfs /v:RamDisk /q /y" > nul'
    VIRTUAL_DELETE_CMD = 'imdisk -D -m '+VIRTUAL_DISK
    NULL_DEV = 'nul'
else:
    VIRTUAL_DISK = '/tmp/ramdisk/'
    VIRTUAL_MOUNT_CMD = 'echo Aa112233 | sudo -S mount -t tmpfs -o size=64M tmpfs ' + VIRTUAL_DISK
    VIRTUAL_UMOUNT_CMD = 'echo Aa112233 | sudo -S umount ' + VIRTUAL_DISK
    NULL_DEV = '/dev/null'

NO_VD_SCREEN_DUMP_PATH = path.join(sys.path[0], 'screen.dump')
SCREEN_DUMP_PATH = path.join(VIRTUAL_DISK, 'screen.dump')


class RoleEnum(enum.Enum):
    AMI = 'ami'
    LIKA = 'lika'
    ALDER = 'alder'
    MOON = 'moon'
    LSebas_A4 = 'lsa4'
    Benandark = 'benandark'


class TicketEnum(enum.Enum):
    GREEN = 'green'
    RED = 'red'
