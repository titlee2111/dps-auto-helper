@echo off
chcp 65001 >nul
title Đẩy Code & Mod Lên GitHub (titlee2111/dps-auto-helper)
cd /d "%~dp0"
cls
echo ============================================================
echo   TỰ ĐỘNG ĐẨY TOÀN BỘ FILE LÊN GITHUB REPOSITORY
echo   Repo: https://github.com/titlee2111/dps-auto-helper
echo ============================================================
echo.

if not exist ".git_tools\cmd\git.exe" (
    echo [LỖI] Không tìm thấy git portable!
    pause
    exit /b 1
)

echo [+] Đang kiểm tra và commit các file thay đổi...
.git_tools\cmd\git.exe add -A
.git_tools\cmd\git.exe commit -m "feat: modern UI with game logo, top download hero, and scrollable guide"

echo.
echo [+] Đang đẩy (Push) lên nhánh main của GitHub...
echo [!] Nếu trình duyệt hiện cửa sổ xác thực GitHub, bạn chỉ cần bấm "Authorize".
echo.
.git_tools\cmd\git.exe push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ============================================================
    echo   ĐÃ ĐẨY LÊN GITHUB THÀNH CÔNG 100%!
    echo   Trang web của bạn: https://titlee2111.github.io/dps-auto-helper/
    echo ============================================================
) else (
    echo.
    echo [!] Nếu push yêu cầu đăng nhập hoặc báo lỗi:
    echo     Bạn hãy mở https://github.com/titlee2111/dps-auto-helper/upload/main
    echo     rồi kéo thả 3 file sau vào web là xong ngay:
    echo     1. index.html
    echo     2. README.md
    echo     3. game-icon.png
)

echo.
pause
