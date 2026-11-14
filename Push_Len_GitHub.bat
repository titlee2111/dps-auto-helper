@echo off
setlocal
cd /d "%~dp0"
set "PATH=%~dp0.git_tools\cmd;%~dp0.git_tools\ucrt64\bin;%PATH%"

echo ============================================================
echo   DPS AUTO HELPER - PUSH LEN GITHUB
echo ============================================================
echo.

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0Push_Len_GitHub.ps1"

echo.
pause
