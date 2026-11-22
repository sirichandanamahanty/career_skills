@echo off
title Push Career Skill Gap AI to GitHub
echo ========================================================
echo       Push Career Skill Gap AI to GitHub
echo ========================================================
echo.
cd /d "%~dp0"

echo 1. Staging files...
git add .

echo 2. Checking commit status...
git status

set /p COMMIT_MSG="Enter commit message (Press Enter for 'Initial commit'): "
if "%COMMIT_MSG%"=="" set COMMIT_MSG=Initial commit: Career Skill Gap AI

git commit -m "%COMMIT_MSG%"

echo.
git branch -M main

echo.
echo --------------------------------------------------------
echo Paste your GitHub repository URL below.
echo Example: https://github.com/your-username/career-skillgap-ai.git
echo --------------------------------------------------------
set /p REPO_URL="GitHub Repository URL: "

if not "%REPO_URL%"=="" (
    git remote remove origin 2>nul
    git remote add origin %REPO_URL%
    echo.
    echo Pushing to GitHub...
    git push -u origin main
) else (
    echo No repository URL provided. Skipping push.
)

echo.
echo Done!
pause
