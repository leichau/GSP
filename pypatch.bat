@rem if exist .\dist\SerialPort\list.ini copy .\dist\SerialPort\list.ini .\dist\list.ini
rd /s /q E:\workbench\PyQt\GSP\build\SerialPort
@rem -F: generate single file
@rem -w: no console for windows system
@rem -i: set ico file
rem pyinstaller -F -w SerialPort.py
pyinstaller -F -w -i .\resource\icon\hextool.ico SerialPort.py
@rem xcopy "D:\Program Files\Python\Python36\Lib\site-packages\PyQt5\Qt\plugins\styles" .\dist\styles\
pause
