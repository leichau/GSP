rd /s /q .\build\GSP
@rem -F: generate single file
@rem -w: no console for windows system. Helpful for running exception.
@rem -i: icon file
@rem --version-file: soft version information.
@rem -n: Name to assign to the bundled app.
pyinstaller -F -w -i .\resource\icon\serial256.ico --version-file file_version_info.txt -n GSP SerialPort.py
@rem pyinstaller -F -w -i .\resource\icon\codec256.ico --version-file codec_version_info.txt Codec.py
@rem xcopy "D:\Program Files\Python\Python36\Lib\site-packages\PyQt5\Qt\plugins\styles" .\dist\styles\
pause
