@echo off
REM Git Sync script for Python project

echo Checking for updates from GitHub (Pulling)...
git pull origin main

echo.
set /p choice="Do you want to upload your latest changes to GitHub? (y/n): "
if /i "%choice%"=="y" (
    echo Adding files...
    git add .
    set /p msg="Enter a commit message: "
    if "%msg%"=="" set msg="Update project files"
    git commit -m "%msg%"
    echo Pushing changes...
    git push origin main
)

echo.
echo Sync process finished!
pause
