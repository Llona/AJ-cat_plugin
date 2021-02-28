@echo off
set /a x=2039
set /a y=831
set /a high=2280
set /a wight=1080

rem set /a offset=%wight%*%y%+%x%
set /a offset=%high%*%y%+%x%
rem set /a offset=%1
rem echo %offset%

adb exec-out screencap > screen.dump

for /f "usebackq tokens=*" %%i in (`"dd if=screen.dump bs=4 count=1 skip=%offset% 2>nul | xxd -C"`) do set result=%%i
rem echo %result%
set color=%result:~8,2%%result:~11,2%%result:~14,2%
echo %color%

rem dd if=screen.dump bs=4 count=1 skip=1896719 2>nul | xxd -ps
rem 78509e