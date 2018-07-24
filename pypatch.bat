rem if exist .\dist\SerialPort\list.ini copy .\dist\SerialPort\list.ini .\dist\list.ini
rd /s /q C:\Users\Administrator\Desktop\PyQt5\SerialPort\build\SerialPort
rem rd /s /q C:\Users\Administrator\Desktop\PyQt5\SerialPort\dist\SerialPort
pyinstaller -F -w SerialPort.py
xcopy "D:\Program Files\Python\Python36\Lib\site-packages\PyQt5\Qt\plugins\styles" .\dist\styles\
rem if exist .\dist\list.ini copy .\dist\list.ini .\dist\SerialPort\list.ini
pause