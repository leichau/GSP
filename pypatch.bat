rd /s /q .\build\GSP
@REM -F: generate single file
@REM -w: no console for windows system. Helpful for running exception.
@REM -i: icon file
@REM --version-file: soft version information.
@REM -n: Name to assign to the bundled app.
pyinstaller -F -w -i .\resource\icon\serial256.ico --version-file file_version_info.txt -n GSP SerialPort.py
@REM pyinstaller -F -w -i .\resource\icon\codec256.ico --version-file codec_version_info.txt -n Codec Codec.py
@REM xcopy "D:\Program Files\Python\Python36\Lib\site-packages\PyQt5\Qt\plugins\styles" .\dist\styles\
pause
 