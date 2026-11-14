@echo off
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0Push_Len_GitHub.ps1"
echo.
pause
