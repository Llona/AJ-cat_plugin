@echo off
set /a x=614
set /a y=833
set /a high=2280
set /a wight=1080

rem set /a offset=%wight%*%y%+%x%
set /a offset=%high%*%y%+%x%
rem set /a offset=%1
rem echo %offset%

adb exec-out screencap > screen.dump

for /f "usebackq tokens=*" %%i in (`"dd if=screen.dump bs=4 count=1 skip=%offset% 2>nul | xxd -ps"`) do set result=%%i
echo %result%
set color=%result:~0,6%
echo %color%

echo start test

adb exec-out screencap | dd bs=4 count=1 skip=%offset% 2>nul | xxd -ps
adb exec-out screencap | dd bs=4 count=1 skip=1899854 2>nul | xxd -ps
rem dd if=screen.dump bs=4 count=1 skip=1896719 2>nul | xxd -ps
rem 78509e
rem 1899854