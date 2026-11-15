import os
import shutil
import zipfile

BASE_DIR = r"C:\Users\Son\Desktop\dps-auto-helper"
STAGE_DIR = os.path.join(BASE_DIR, "staging")
SRC_ZIP = r"g:\SteamLibrary\steamapps\common\DPS Desktop Pension Squad\DPS-Trainer.zip"
SRC_DLL_NEW = r"g:\SteamLibrary\steamapps\common\DPS Desktop Pension Squad\BepInEx\plugins\DPS.Trainer.dll.new"
SRC_DLL_ORIG = r"g:\SteamLibrary\steamapps\common\DPS Desktop Pension Squad\BepInEx\plugins\DPS.Trainer.dll"
SRC_DLL = SRC_DLL_NEW if os.path.exists(SRC_DLL_NEW) else SRC_DLL_ORIG
SRC_CFG = r"g:\SteamLibrary\steamapps\common\DPS Desktop Pension Squad\BepInEx\config\dps_workshop.cfg"
SRC_HTML = os.path.join(BASE_DIR, "index.html")
OUT_ZIP = os.path.join(BASE_DIR, "DPS_Auto_Helper_1Click.zip")

def build_package():
    print("=== Dang dong goi DPS_Auto_Helper_1Click.zip ===")
    if os.path.exists(STAGE_DIR):
        shutil.rmtree(STAGE_DIR)
    os.makedirs(STAGE_DIR, exist_ok=True)

    # 1. Unpack source zip
    print("[1/6] Giai nen template BepInEx tu DPS-Trainer.zip...")
    with zipfile.ZipFile(SRC_ZIP, 'r') as z:
        for item in z.infolist():
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
    print("[2/6] Cap nhat ban build DPS.Trainer.dll moi nhat (CORS + OPTIONS + F6/F7 fix)...")
    target_dll = os.path.join(STAGE_DIR, "payload", "BepInEx", "plugins", "DPS.Trainer.dll")
    shutil.copy2(SRC_DLL, target_dll)

    # Update config if exists
    target_cfg_dir = os.path.join(STAGE_DIR, "payload", "BepInEx", "config")
    os.makedirs(target_cfg_dir, exist_ok=True)
    if os.path.exists(SRC_CFG):
        shutil.copy2(SRC_CFG, os.path.join(target_cfg_dir, "dps_workshop.cfg"))

    # Copy mod_web_ui.html
    if os.path.exists(SRC_HTML):
        shutil.copy2(SRC_HTML, os.path.join(STAGE_DIR, "mod_web_ui.html"))
        shutil.copy2(SRC_HTML, os.path.join(STAGE_DIR, "payload", "mod_web_ui.html"))

    # 3. Create Cai_Dat_1Click.bat
    print("[3/6] Tao Cai_Dat_1Click.bat va Mo_Giao_Dien_Web.bat...")
    bat_install = """@echo off
chcp 65001 >nul
title Cai Dat DPS Auto Helper (1-Click)
cls
echo ============================================================
echo   DPS AUTO HELPER - CAI DAT 1-CLICK TU DONG
echo ============================================================
echo.

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0install.ps1"

echo.
pause
"""
    with open(os.path.join(STAGE_DIR, "Cai_Dat_1Click.bat"), "w", encoding="utf-8") as f:
        f.write(bat_install)

    bat_open_ui = """@echo off
title DPS Auto Helper - Giao Dien Web
echo ============================================================
echo   DANG MO BANG DIEU KHIEN DPS AUTO HELPER TREN WEB...
echo ============================================================
echo.
echo Dia chi: http://127.0.0.1:47900/
start http://127.0.0.1:47900/
timeout /t 2 >nul
exit
"""
    with open(os.path.join(STAGE_DIR, "Mo_Giao_Dien_Web.bat"), "w", encoding="utf-8") as f:
        f.write(bat_open_ui)
    with open(os.path.join(STAGE_DIR, "payload", "Mo_Giao_Dien_Web.bat"), "w", encoding="utf-8") as f:
        f.write(bat_open_ui)

    # 4. Create bulletproof install.ps1 (Safe ASCII strings, 0% syntax error on any PowerShell)
    print("[4/6] Tao install.ps1 an toan tuyet doi...")
    ps1_content = """<#
  DPS Auto Helper - 1-Click Installer
#>
$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$payload = Join-Path $root "payload"

if (-not (Test-Path $payload)) {
    Write-Host "[LOI] Khong tim thay thu muc payload! Hay giai nen toan bo file zip truoc." -ForegroundColor Red
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
    Write-Host "[!] Khong tim thay thu muc cai game tu dong." -ForegroundColor Yellow
    $GamePath = Read-Host "Vui long dan duong dan thu muc chua DPS.exe vao day"
    if (-not (Test-GameFolder $GamePath)) {
        Write-Host "[LOI] Thu muc khong hop le! Khong tim thay DPS.exe va GameAssembly.dll." -ForegroundColor Red
        exit 1
    }
}

Write-Host "[+] Da tim thay game tai: " -NoNewline
Write-Host "$GamePath" -ForegroundColor Cyan

# Kiem tra neu game dang chay
$running = Get-Process "DPS" -ErrorAction SilentlyContinue
if ($running) {
    Write-Host "[!] Phat hien game DPS dang chay. Dang dong game de cap nhat file..." -ForegroundColor Yellow
    Stop-Process -Name "DPS" -Force -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 1
}

# Sao chep payload
Write-Host "[+] Dang cai dat cac file mod vao thu muc game..." -ForegroundColor Green
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

# Copy Mo_Giao_Dien_Web.bat
$openBatSrc = Join-Path $root "Mo_Giao_Dien_Web.bat"
if (Test-Path $openBatSrc) {
    Copy-Item $openBatSrc (Join-Path $GamePath "Mo_Giao_Dien_Web.bat") -Force
}

# Copy mod_web_ui.html
$uiHtmlSrc = Join-Path $root "mod_web_ui.html"
if (Test-Path $uiHtmlSrc) {
    Copy-Item $uiHtmlSrc (Join-Path $GamePath "mod_web_ui.html") -Force
}

Write-Host "============================================================" -ForegroundColor Green
Write-Host ("  CAI DAT THANH CONG DPS AUTO HELPER! [" + $copied + " files]") -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host ""
Write-Host "CAC BUOC TIEP THEO:" -ForegroundColor Yellow
Write-Host "  1. Mo game DPS Desktop Pension Squad tren Steam."
Write-Host "  2. Nhan dup vao file 'Mo_Giao_Dien_Web.bat' de mo bang dieu khien."
Write-Host "  3. Phim tat trong game: F6 (Tu dong Cat Do), F7 (Tu dong Hop Thanh)."
Write-Host ""
"""
    with open(os.path.join(STAGE_DIR, "install.ps1"), "w", encoding="utf-8-sig") as f:
        f.write(ps1_content)

    # Clean up unnecessary files
    for unnecessary in ["Go_Cai_Dat.bat", "Huong_Dan.txt", "README.txt", "install.bat", "Cai_Dat_Tu_Dong.bat", "open-ui.bat", "remove.bat"]:
        target_f = os.path.join(STAGE_DIR, unnecessary)
        if os.path.exists(target_f):
            os.remove(target_f)

    # 5. Zip package
    print("[5/6] Dang nen thanh DPS_Auto_Helper_1Click.zip...")
    if os.path.exists(OUT_ZIP):
        os.remove(OUT_ZIP)

    with zipfile.ZipFile(OUT_ZIP, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for root, dirs, files in os.walk(STAGE_DIR):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, STAGE_DIR)
                zf.write(abs_path, arcname=rel_path)

    zip_size_mb = os.path.getsize(OUT_ZIP) / (1024 * 1024)
    print(f"[6/6] Hoan tat! File: {OUT_ZIP} ({zip_size_mb:.2f} MB)")

    # Clean up stage dir
    shutil.rmtree(STAGE_DIR)
    print("=== DA DONG GOI XONG THANH CONG! ===")

if __name__ == "__main__":
    build_package()
