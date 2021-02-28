import sys
import win32api
import win32file
import os
import time

# print(sys.path[0])


def get_ramdrive_by_label():
    ramdisk_drives = []
    driver_list_str = win32api.GetLogicalDriveStrings()
    for driver in driver_list_str.split('\x00'):
        # 2 is removable driver, im ramdisk is 2
        if win32file.GetDriveType(driver) == 2 and win32api.GetVolumeInformation(driver+'\\')[0] == 'RamDisk':
            ramdisk_drives.append(driver[0:2])

    return ramdisk_drives


def create_ramdrive(driver_name):
    driver_name = driver_name + ':'
    folder_path = os.path.join(sys.path[0], 'ImDiskPortable')

    fpath = os.path.join(folder_path, 'awealloc.sys')
    cmd_str = 'sc create AWEAlloc binPath= '+fpath + ' DisplayName="AWE Memory Allocation Driver" Type= kernel Start= demand'
    print(cmd_str)
    os.system(cmd_str)
    # cmd_str = 'sc create ImDisk binPath= "' + fpath + 'imdisk.sys" DisplayName= "ImDisk Virtual Disk Driver" Type= kernel Start= demand'
    # os.system(cmd_str)
    # cmd_str = 'sc create ImDskSvc binPath= "' + fpath + 'imdsksvc.exe" DisplayName= "ImDisk Virtual Disk Driver Helper" Type= own Start= demand'
    # os.system(cmd_str)
    # os.system('sc description AWEAlloc "Driver for physical memory allocation through AWE"')
    # os.system('sc description ImDisk "Disk emulation driver"')
    # os.system('sc description imdsksvc "Helper service for ImDisk Virtual Disk Driver."')
    # os.system('net start ImDskSvc')
    # os.system('net start AWEAlloc')
    # os.system('net start ImDisk')
    #
    # try:
    #     win32api.GetVolumeInformation(driver_name + '\\')
    #     status = False
    # except:
    #     status = True
    #
    # if status:
    #     cmd_str = '"' + fpath + 'imdisk.exe" -a -s 32M -m ' + driver_name + ' -o rem -p "/fs:ntfs /v:RamDisk /A:512 /q /c /y"'
    #     os.system(cmd_str)
    # else:
    #     return False
    # return True
    #
    # DriveGet, status, Status, %driver_name%
    # If (status = "Invalid")
    # {
    # 	Run, "%fpath%\Extra Tools\ImDisk Portable\imdisk.exe" -a -s 32M -m %driver_name% -o rem -p "/fs:ntfs /v:RamDisk /A:512 /q /c /y",, Hide
    # 	Loop
    # 		DriveGet, status2, Status, %driver_name%
    # 	Until status2 = "Ready"
    # }
    # else
    # {
    #     return False
    # }
    # return True
    # ;MsgBox 0,,%driver_name%
    #

def remove_ramdrive():
    fpath = sys.path[0]
    ramdisk_drives = get_ramdrive_by_label()
    if ramdisk_drives:
        for drive in ramdisk_drives:
            cmd_str = '"'+fpath + r'\Extra Tools\ImDisk Portable\imdisk.exe"' + ' -D -m ' + drive
            # print(cmd_str)
            os.system(cmd_str) #"%fpath%\Extra Tools\ImDisk Portable\imdisk.exe" -D -m %RamDrv%,, Hide
    time.sleep(0.1)
    os.system('sc delete ImDskSvc')
    os.system('sc delete AWEAlloc')
    os.system('sc delete ImDisk')
    os.system('taskkill /f /IM "imdisk.exe"')
    os.system('taskkill /f /IM "imdsksvc.exe"')
    os.system('sc delete ImDskSvc')
    os.system('sc delete AWEAlloc')
    os.system('sc delete ImDisk')
    # RegDelete, HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\ImDskSvc / f
    # RegDelete, HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\AWEAlloc / f
    # RegDelete, HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\ImDisk /f


if __name__ == '__main__':
    # multiprocessing.freeze_support()
    if len(sys.argv) > 1:
        print(1)
        create_ramdrive('X')
    else:
        print(2)
        remove_ramdrive()
