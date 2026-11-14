import os
import shutil
import zipfile

BASE_DIR = r"C:\Users\Son\Desktop\dps-auto-helper"
STAGE_DIR = os.path.join(BASE_DIR, "staging")
SRC_ZIP = r"g:\SteamLibrary\steamapps\common\DPS Desktop Pension Squad\DPS-Trainer.zip"
SRC_DLL = r"g:\SteamLibrary\steamapps\common\DPS Desktop Pension Squad\BepInEx\plugins\DPS.Trainer.dll"
SRC_CFG = r"g:\SteamLibrary\steamapps\common\DPS Desktop Pension Squad\BepInEx\config\dps_workshop.cfg"
OUT_ZIP = os.path.join(BASE_DIR, "DPS_Auto_Helper_1Click.zip")

def build_package():
    print("=== Đang đóng gói DPS_Auto_Helper_1Click.zip ===")
    if os.path.exists(STAGE_DIR):
        shutil.rmtree(STAGE_DIR)
    os.makedirs(STAGE_DIR, exist_ok=True)

    # 1. Unpack source zip
    print("[1/5] Giải nén template BepInEx từ DPS-Trainer.zip...")
    with zipfile.ZipFile(SRC_ZIP, 'r') as z:
        for item in z.infolist():
            # item.filename has 'DPS-Trainer/...' prefix
            parts = item.filename.split('/', 1)
            if len(parts) > 1 and parts[1]:
                rel_path = parts[1]
                target_path = os.path.join(STAGE_DIR, rel_path.replace('/', os.sep))
                if item.is_dir():
                    os.makedirs(target_path, exist_ok=True)
                else:
                    os.makedirs(os.path.dirname(target_path), exist_ok=True)
                    with z.open(item) as src_f, open(target_path, 'wb') as dst_f:
                        dst_f.write(src_f.read())

    # 2. Update DPS.Trainer.dll
    print("[2/5] Cập nhật bản build DPS.Trainer.dll mới nhất (F6/F7 fix)...")
    target_dll = os.path.join(STAGE_DIR, "payload", "BepInEx", "plugins", "DPS.Trainer.dll")
    shutil.copy2(SRC_DLL, target_dll)

    # Update config if exists
    target_cfg_dir = os.path.join(STAGE_DIR, "payload", "BepInEx", "config")
    os.makedirs(target_cfg_dir, exist_ok=True)
    if os.path.exists(SRC_CFG):
        shutil.copy2(SRC_CFG, os.path.join(target_cfg_dir, "dps_workshop.cfg"))

    # 3. Create Cai_Dat_Tu_Dong.bat
    print("[3/5] Tạo script cài đặt 1-Click tiếng Việt...")
    bat_content = """@echo off
chcp 65001 >nul
title Cài Đặt DPS Auto Helper (1-Click)
cls
echo ============================================================
echo   DPS AUTO HELPER - CÀI ĐẶT 1-CLICK TỰ ĐỘNG
echo ============================================================
echo.

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0install.ps1"

echo.
pause
"""
    with open(os.path.join(STAGE_DIR, "Cai_Dat_Tu_Dong.bat"), "w", encoding="utf-8") as f:
        f.write(bat_content)

    # 4. Create optimized install.ps1
    ps1_content = """<#
  DPS Auto Helper - 1-Click Installer
#>
$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$payload = Join-Path $root "payload"

if (-not (Test-Path $payload)) {
    Write-Host "[LỖI] Không tìm thấy thư mục payload! Hãy giải nén toàn bộ file zip trước." -ForegroundColor Red
    exit 1
}

function Test-GameFolder([string]$path) {
    if ([string]::IsNullOrWhiteSpace($path)) { return $false }
    return (Test-Path (Join-Path $path "DPS.exe")) -and (Test-Path (Join-Path $path "GameAssembly.dll"))
}

function Find-SteamLibraries {
    $libraries = New-Object System.Collections.Generic.List[string]
    $steam = (Get-ItemProperty "HKCU:\\Software\\Valve\\Steam" -ErrorAction SilentlyContinue).SteamPath
    if (-not $steam) { $steam = (Get-ItemProperty "HKLM:\\SOFTWARE\\WOW6432Node\\Valve\\Steam" -ErrorAction SilentlyContinue).InstallPath }

    if ($steam -and (Test-Path $steam)) {
        $libraries.Add($steam)
        $vdf = Join-Path $steam "steamapps\\libraryfolders.vdf"
        if (Test-Path $vdf) {
            foreach ($line in Get-Content $vdf) {
                if ($line -match '"path"\\s+"([^"]+)"') {
                    $cand = $matches[1] -replace '\\\\\\\\', '\\'
                    if (Test-Path $cand) { $libraries.Add($cand) }
                }
            }
        }
    }
    return $libraries | Select-Object -Unique
}

function Find-Game {
    if (Test-GameFolder $root) { return $root }
    # Parent dir check
    $parent = Split-Path -Parent $root
    if (Test-GameFolder $parent) { return $parent }

    foreach ($library in Find-SteamLibraries) {
        $candidate = Join-Path $library "steamapps\\common\\DPS Desktop Pension Squad"
        if (Test-GameFolder $candidate) { return $candidate }
    }
    return $null
}

$GamePath = Find-Game
if (-not $GamePath) {
    Write-Host "[!] Không tìm thấy thư mục cài game tự động." -ForegroundColor Yellow
    $GamePath = Read-Host "Vui lòng dán đường dẫn thư mục chứa DPS.exe vào đây"
    if (-not (Test-GameFolder $GamePath)) {
        Write-Host "[LỖI] Thư mục không hợp lệ! Không tìm thấy DPS.exe và GameAssembly.dll." -ForegroundColor Red
        exit 1
    }
}

Write-Host "[+] Đã tìm thấy game tại: " -NoNewline
Write-Host "$GamePath" -ForegroundColor Cyan

# Kiểm tra nếu game đang bật
$running = Get-Process "DPS" -ErrorAction SilentlyContinue
if ($running) {
    Write-Host "[!] Phát hiện game DPS đang chạy. Đang đóng game để cập nhật file..." -ForegroundColor Yellow
    Stop-Process -Name "DPS" -Force -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 1
}

# Sao chép payload
Write-Host "[+] Đang cài đặt các file mod hỗ trợ vào game..." -ForegroundColor Green
$copied = 0
function Copy-Tree([string]$src, [string]$dst) {
    if (-not (Test-Path $dst)) { New-Item -ItemType Directory -Path $dst -Force | Out-Null }
    foreach ($item in Get-ChildItem $src -Force) {
        $target = Join-Path $dst $item.Name
        if ($item.PSIsContainer) {
            Copy-Tree $item.FullName $target
        } else {
            Copy-Item $item.FullName $target -Force
            $script:copied++
        }
    }
}

Copy-Tree $payload $GamePath

Write-Host "============================================================" -ForegroundColor Green
Write-Host "  CÀI ĐẶT THÀNH CÔNG DPS AUTO HELPER! ($copied files)" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host ""
Write-Host "CÁC BƯỚC TIẾP THEO:" -ForegroundColor Yellow
Write-Host "  1. Mở game DPS Desktop Pension Squad bình thường trên Steam."
Write-Host "  2. Mở trang web điều khiển để Bật/Tắt Tự động Cất Đồ (F6) & Tự động Hợp Thành (F7)."
Write-Host ""
"""
    with open(os.path.join(STAGE_DIR, "install.ps1"), "w", encoding="utf-8") as f:
        f.write(ps1_content)

    # 5. Create Go_Cai_Dat.bat
    uninstall_bat = """@echo off
chcp 65001 >nul
title Gỡ Cài Đặt DPS Auto Helper
cls
echo ============================================================
echo   GỠ CÀI ĐẶT DPS AUTO HELPER
echo ============================================================
echo.
powershell -NoProfile -ExecutionPolicy Bypass -Command "
$game = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not (Test-Path (Join-Path $game 'DPS.exe'))) {
    $game = 'G:\\SteamLibrary\\steamapps\\common\\DPS Desktop Pension Squad'
}
if (Test-Path (Join-Path $game 'winhttp.dll')) { Remove-Item (Join-Path $game 'winhttp.dll') -Force; Write-Host 'Đã xóa winhttp.dll' -ForegroundColor Yellow }
if (Test-Path (Join-Path $game 'doorstop_config.ini')) { Remove-Item (Join-Path $game 'doorstop_config.ini') -Force }
if (Test-Path (Join-Path $game 'BepInEx')) { Remove-Item (Join-Path $game 'BepInEx') -Recurse -Force; Write-Host 'Đã xóa thư mục BepInEx' -ForegroundColor Yellow }
Write-Host 'ĐÃ GỠ HOÀN TOÀN MOD! Game đã trở về nguyên bản.' -ForegroundColor Green
"
echo.
pause
"""
    with open(os.path.join(STAGE_DIR, "Go_Cai_Dat.bat"), "w", encoding="utf-8") as f:
        f.write(uninstall_bat)

    # 6. Create Huong_Dan.txt
    guide_txt = """DPS AUTO HELPER - HỖ TRỢ TỰ ĐỘNG HÓA KHO & XƯỞNG
============================================================
TÍNH NĂNG:
- F6: Tự động cất đồ từ túi đồ vào các Kho tùy chọn (Kho 1 -> Kho 5, v.v.)
- F7: Tự động hợp thành đồ trong Xưởng theo chu kỳ thời gian
- Zero Coordinates: Điều khiển ngầm bằng logic code nội bộ, KHÔNG chiếm chuột, KHÔNG lệch tọa độ màn hình.

HƯỚNG DẪN CÀI ĐẶT:
1. Giải nén toàn bộ thư mục này ra.
2. Chạy file 'Cai_Dat_Tu_Dong.bat' (nó sẽ tự tìm thư mục cài game Steam của bạn và cài trong 2 giây).
3. Mở game DPS Desktop Pension Squad trên Steam.
4. Mở trang web điều khiển trên trình duyệt là có thể sử dụng ngay!

Nếu muốn gỡ bỏ mod:
- Chạy file 'Go_Cai_Dat.bat' là game trở về nguyên bản 100%.
"""
    with open(os.path.join(STAGE_DIR, "Huong_Dan.txt"), "w", encoding="utf-8") as f:
        f.write(guide_txt)

    # Remove old install.bat if present to avoid confusion
    old_inst = os.path.join(STAGE_DIR, "install.bat")
    if os.path.exists(old_inst):
        os.remove(old_inst)

    # 7. Zip package
    print("[4/5] Đang nén thành DPS_Auto_Helper_1Click.zip...")
    if os.path.exists(OUT_ZIP):
        os.remove(OUT_ZIP)

    with zipfile.ZipFile(OUT_ZIP, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for root, dirs, files in os.walk(STAGE_DIR):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, STAGE_DIR)
                zf.write(abs_path, arcname=rel_path)

    zip_size_mb = os.path.getsize(OUT_ZIP) / (1024 * 1024)
    print(f"[5/5] Hoàn tất! File: {OUT_ZIP} ({zip_size_mb:.2f} MB)")

    # Clean up stage dir
    shutil.rmtree(STAGE_DIR)
    print("=== ĐÃ ĐÓNG GÓI XONG THÀNH CÔNG! ===")

if __name__ == "__main__":
    build_package()
