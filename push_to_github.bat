@echo off
title Push Career Skills to GitHub
echo ========================================================
echo   Pushing to https://github.com/sirichandanamahanty/career_skills.git
echo ========================================================
echo.
cd /d "%~dp0"

echo Current Git status:
git status

echo.
echo Running git push...
git push -u origin main

echo.
echo ========================================================
echo Finished! If it succeeded, check your GitHub repository.
echo ========================================================
pause
