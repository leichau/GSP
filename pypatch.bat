@rem if exist .\dist\SerialPort\list.ini copy .\dist\SerialPort\list.ini .\dist\list.ini
rd /s /q E:\workbench\PyQt\GSP\build\SerialPort
@rem -F: generate single file
@rem -w: no console for windows system. Helpful for running exception.
@rem -i: icon file
@rem --version-file: soft version information.
@rem -n: Name to assign to the bundled app.
pyinstaller -F -w -i .\resource\icon\serial256.ico --version-file file_version_info.txt -n GSP SerialPort.py
REM pyinstaller -F -w -i .\resource\icon\codec256.ico Codec.py
@rem xcopy "D:\Program Files\Python\Python36\Lib\site-packages\PyQt5\Qt\plugins\styles" .\dist\styles\
pause
