import os
import shutil
import zipfile

BASE_DIR = r"C:\Users\Son\Desktop\dps-auto-helper"
STAGE_DIR = os.path.join(BASE_DIR, "staging")
SRC_ZIP = r"g:\SteamLibrary\steamapps\common\DPS Desktop Pension Squad\DPS-Trainer.zip"
SRC_DLL = r"g:\SteamLibrary\steamapps\common\DPS Desktop Pension Squad\BepInEx\plugins\DPS.Trainer.dll"
SRC_CFG = r"g:\SteamLibrary\steamapps\common\DPS Desktop Pension Squad\BepInEx\config\dps_workshop.cfg"
SRC_TRAINER_CFG = r"g:\SteamLibrary\steamapps\common\DPS Desktop Pension Squad\BepInEx\config\ofx.dps.trainer.cfg"
OUT_ZIP = os.path.join(BASE_DIR, "DPS_Auto_Helper_1Click.zip")

def build_package():
    print("=== Dang dong goi DPS_Auto_Helper_1Click.zip (Clean 1-Click - No HTML / No Extra Bats) ===")
    if os.path.exists(STAGE_DIR):
        shutil.rmtree(STAGE_DIR)
    os.makedirs(STAGE_DIR, exist_ok=True)

    # 1. Unpack source zip template
    print("[1/5] Giai nen template BepInEx tu DPS-Trainer.zip...")
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
    print("[2/5] Cap nhat ban build DPS.Trainer.dll moi nhat (AutoOpen + VIP defaults OFF + Realtime HUD)...")
    target_dll = os.path.join(STAGE_DIR, "payload", "BepInEx", "plugins", "DPS.Trainer.dll")
    shutil.copy2(SRC_DLL, target_dll)

    # 3. Write default configs with safe VIP defaults
    target_cfg_dir = os.path.join(STAGE_DIR, "payload", "BepInEx", "config")
    os.makedirs(target_cfg_dir, exist_ok=True)

    default_trainer_cfg = """## Settings file was created by plugin DPS Trainer v0.6.0
## Plugin GUID: ofx.dps.trainer

[Power]

## Damage multiplier, applied at DamageSpec.FactorAt.
# Setting type: Single
# Default value: 1
# Acceptable value range: From 1 to 1000
DamageMultiplier = 1

## Attack speed multiplier, applied through the stat node.
# Setting type: Single
# Default value: 1
# Acceptable value range: From 1 to 20
AttackSpeedMultiplier = 1

[Startup]

## Block incoming damage for player characters.
# Setting type: Boolean
# Default value: false
GodMode = false

## Neutralise the three integrity probes. Keep this on: tripping one blocks trading.
# Setting type: Boolean
# Default value: false
DetectorShield = false

## Force treasure boxes to open automatically.
# Setting type: Boolean
# Default value: true
AutoOpenBoxes = true

## Experimental IMGUI overlay. Off by default: this build is display-stripped.
# Setting type: Boolean
# Default value: false
Overlay = false

## Report every DLC pack as owned client-side. Server entitlement sync is suppressed while active.
# Setting type: Boolean
# Default value: false
UnlockDlc = false

## F1 god, F2 shield, F3 auto-open, F5 dlc, F12 panic.
# Setting type: Boolean
# Default value: true
Hotkeys = true
"""
    with open(os.path.join(target_cfg_dir, "ofx.dps.trainer.cfg"), "w", encoding="utf-8") as f:
        f.write(default_trainer_cfg)

    default_workshop_cfg = """[Workshop]
AutoCombineEnabled = 0
CombineIntervalMinutes = 5
AutoStashEnabled = 0
StashIntervalSeconds = 60
StashStartTab = 1
StashEndTab = 5
"""
    with open(os.path.join(target_cfg_dir, "dps_workshop.cfg"), "w", encoding="utf-8") as f:
        f.write(default_workshop_cfg)

    # 4. Create pure ASCII Cai_Dat_1Click.bat
    print("[3/5] Tao Cai_Dat_1Click.bat...")
    bat_install = """@echo off
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
    with open(os.path.join(STAGE_DIR, "Cai_Dat_1Click.bat"), "w", encoding="ascii") as f:
        f.write(bat_install)

    # 5. Create 100% pure ASCII bulletproof install.ps1
    print("[4/5] Tao install.ps1 (100% Pure ASCII - 0% parse error on any locale)...")
    ps1_content = """<#
  DPS Auto Helper - 1-Click Installer
  100% Pure ASCII script to guarantee 0% syntax errors across all Windows language locales
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

Write-Host "============================================================" -ForegroundColor Green
Write-Host ("  CAI DAT THANH CONG DPS AUTO HELPER! [" + $copied + " files]") -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host ""
Write-Host "CAC BUOC TIEP THEO:" -ForegroundColor Yellow
Write-Host "  1. Mo game DPS Desktop Pension Squad tren Steam."
Write-Host "  2. Mo trinh duyet va truy cap link giao dien sau de dieu khien:"
Write-Host "     https://titlee2111.github.io/dps-auto-helper/" -ForegroundColor Cyan
Write-Host "  3. Phim tat trong game: F6 (Tu Dong Cat Do), F7 (Tu Dong Hop Thanh)."
Write-Host ""
"""
    with open(os.path.join(STAGE_DIR, "install.ps1"), "w", encoding="ascii") as f:
        f.write(ps1_content)

    # Clean up any HTML or batch files that shouldn't be in the zip
    for root, dirs, files in os.walk(STAGE_DIR):
        for f in files:
            if f.endswith(".html") or f == "Mo_Giao_Dien_Web.bat":
                f_path = os.path.join(root, f)
                print(f"[XOA FILE THUA] {f_path}")
                os.remove(f_path)

    for unnecessary in ["Go_Cai_Dat.bat", "Huong_Dan.txt", "README.txt", "install.bat", "Cai_Dat_Tu_Dong.bat", "open-ui.bat", "remove.bat"]:
        target_f = os.path.join(STAGE_DIR, unnecessary)
        if os.path.exists(target_f):
            os.remove(target_f)

    # 6. Zip package
    print("[5/5] Dang nen thanh DPS_Auto_Helper_1Click.zip...")
    if os.path.exists(OUT_ZIP):
        os.remove(OUT_ZIP)

    with zipfile.ZipFile(OUT_ZIP, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for root, dirs, files in os.walk(STAGE_DIR):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, STAGE_DIR)
                zf.write(abs_path, arcname=rel_path)

    zip_size_mb = os.path.getsize(OUT_ZIP) / (1024 * 1024)
    print(f"Hoan tat! File: {OUT_ZIP} ({zip_size_mb:.2f} MB)")

    # Clean up stage dir
    shutil.rmtree(STAGE_DIR)
    print("=== DA DONG GOI XONG THANH CONG! ===")

if __name__ == "__main__":
    build_package()
