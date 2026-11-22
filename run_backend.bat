@echo off
title Career Skill Gap AI Server
echo ========================================================
echo   Starting Career Skill Gap AI Local Server
echo ========================================================
cd /d "%~dp0"

set PYTHON_EXE="%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
if exist %PYTHON_EXE% (
    echo Using Python at %PYTHON_EXE%
    %PYTHON_EXE% server.py
) else (
    echo Using standard python from PATH...
    python server.py
)

pause
