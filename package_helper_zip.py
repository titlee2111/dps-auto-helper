import os
import shutil
import zipfile

BASE_DIR = r"C:\Users\Son\Desktop\dps-auto-helper"
STAGE_DIR = os.path.join(BASE_DIR, "staging")
GAME_DIR = r"g:\SteamLibrary\steamapps\common\DPS Desktop Pension Squad"
SRC_ZIP = os.path.join(GAME_DIR, "DPS-Trainer.zip")
SRC_WINHTTP = os.path.join(GAME_DIR, "winhttp.dll")
SRC_SYNC_DLL = os.path.join(GAME_DIR, "BepInEx", "core", "DPS.RuntimeSync.dll")
SRC_INTEROP_DIR = os.path.join(GAME_DIR, "BepInEx", "interop")
SRC_BIE_CFG = os.path.join(GAME_DIR, "BepInEx", "config", "BepInEx.cfg")
SRC_DLL = os.path.join(GAME_DIR, "BepInEx", "plugins", "DPS.Trainer.dll")
SRC_CFG = os.path.join(GAME_DIR, "BepInEx", "config", "dps_workshop.cfg")
SRC_TRAINER_CFG = os.path.join(GAME_DIR, "BepInEx", "config", "ofx.dps.trainer.cfg")
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

    # 2. Update Build 26724895 compatibility files + DPS.Trainer.dll
    print("[2/5] Cap nhat winhttp.dll, DPS.RuntimeSync.dll, unsealed interop va DPS.Trainer.dll...")
    payload_dir = os.path.join(STAGE_DIR, "payload")
    shutil.copy2(SRC_WINHTTP, os.path.join(payload_dir, "winhttp.dll"))
    shutil.copy2(SRC_SYNC_DLL, os.path.join(payload_dir, "BepInEx", "core", "DPS.RuntimeSync.dll"))

    target_interop_dir = os.path.join(payload_dir, "BepInEx", "interop")
    if os.path.exists(target_interop_dir):
        shutil.rmtree(target_interop_dir)
    shutil.copytree(SRC_INTEROP_DIR, target_interop_dir)

    target_dll = os.path.join(payload_dir, "BepInEx", "plugins", "DPS.Trainer.dll")
    shutil.copy2(SRC_DLL, target_dll)

    # 3. Write release BepInEx.cfg + default plugin configs with safe VIP defaults
    target_cfg_dir = os.path.join(payload_dir, "BepInEx", "config")
    os.makedirs(target_cfg_dir, exist_ok=True)

    with open(SRC_BIE_CFG, "r", encoding="utf-8") as f:
        bie_lines = f.read().splitlines(True)

    in_console = False
    out_lines = []
    for line in bie_lines:
        stripped = line.strip()
        if stripped.startswith("[") and stripped.endswith("]"):
            in_console = (stripped == "[Logging.Console]")
        if stripped.startswith("UpdateInteropAssemblies ="):
            line = "UpdateInteropAssemblies = false\n"
        elif stripped.startswith("PreloadIL2CPPInteropAssemblies ="):
            line = "PreloadIL2CPPInteropAssemblies = false\n"
        elif in_console and stripped.startswith("Enabled ="):
            line = "Enabled = false\n"
        elif stripped.startswith("InstantFlushing ="):
            line = "InstantFlushing = false\n"
        out_lines.append(line)

    with open(os.path.join(target_cfg_dir, "BepInEx.cfg"), "w", encoding="utf-8", newline="") as f:
        f.write("".join(out_lines))

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
# Default value: true
DetectorShield = true

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

    # 4. Create 100% Pure Windows Batch Cai_Dat_1Click.bat (No PowerShell / No AV Flag)
    print("[3/4] Tao Cai_Dat_1Click.bat (100% Pure Batch - Zero AV Flag)...")
    bat_install = r"""@echo off
setlocal enabledelayedexpansion
title Cai Dat DPS Auto Helper (1-Click)
cls
echo ============================================================
echo   DPS AUTO HELPER - CAI DAT 1-CLICK TU DONG
echo ============================================================
echo.

set "GAME_DIR="

:: 1. Check if bat is run directly inside game folder
if exist "%~dp0DPS.exe" if exist "%~dp0GameAssembly.dll" (
    set "GAME_DIR=%~dp0"
    goto :FoundGame
)

:: 2. Check if bat is in a subfolder inside game folder
if exist "%~dp0..\DPS.exe" if exist "%~dp0..\GameAssembly.dll" (
    set "GAME_DIR=%~dp0.."
    goto :FoundGame
)

:: 3. Check Steam registry HKCU
for /f "tokens=2*" %%a in ('reg query "HKCU\Software\Valve\Steam" /v "SteamPath" 2^>nul') do (
    set "STEAMPATH=%%b"
)

:: If not in HKCU, check HKLM 64-bit
if not defined STEAMPATH (
    for /f "tokens=2*" %%a in ('reg query "HKLM\SOFTWARE\WOW6432Node\Valve\Steam" /v "InstallPath" 2^>nul') do (
        set "STEAMPATH=%%b"
    )
)

if defined STEAMPATH (
    set "STEAMPATH=!STEAMPATH:/=\!"
    if exist "!STEAMPATH!\steamapps\common\DPS Desktop Pension Squad\DPS.exe" (
        set "GAME_DIR=!STEAMPATH!\steamapps\common\DPS Desktop Pension Squad"
        goto :FoundGame
    )
    if exist "!STEAMPATH!\steamapps\libraryfolders.vdf" (
        for /f "tokens=1,2 delims=	" %%i in ('findstr /i "\"path\"" "!STEAMPATH!\steamapps\libraryfolders.vdf" 2^>nul') do (
            set "LIBPATH=%%j"
            set "LIBPATH=!LIBPATH:"=!"
            set "LIBPATH=!LIBPATH:\\=\!"
            if exist "!LIBPATH!\steamapps\common\DPS Desktop Pension Squad\DPS.exe" (
                set "GAME_DIR=!LIBPATH!\steamapps\common\DPS Desktop Pension Squad"
                goto :FoundGame
            )
        )
    )
)

:: 4. Check common drives
for %%d in (C D E F G H) do (
    if not defined GAME_DIR (
        if exist "%%d:\SteamLibrary\steamapps\common\DPS Desktop Pension Squad\DPS.exe" (
            set "GAME_DIR=%%d:\SteamLibrary\steamapps\common\DPS Desktop Pension Squad"
            goto :FoundGame
        )
        if exist "%%d:\Program Files (x86)\Steam\steamapps\common\DPS Desktop Pension Squad\DPS.exe" (
            set "GAME_DIR=%%d:\Program Files (x86)\Steam\steamapps\common\DPS Desktop Pension Squad"
            goto :FoundGame
        )
        if exist "%%d:\Steam\steamapps\common\DPS Desktop Pension Squad\DPS.exe" (
            set "GAME_DIR=%%d:\Steam\steamapps\common\DPS Desktop Pension Squad"
            goto :FoundGame
        )
    )
)

:PromptUser
if not defined GAME_DIR (
    echo [!] Khong tim thay thu muc game Steam tu dong.
    echo.
    set /p "GAME_DIR=Vui long dan duong dan thu muc chua DPS.exe vao day: "
    set "GAME_DIR=!GAME_DIR:"=!"
    if not exist "!GAME_DIR!\DPS.exe" (
        echo.
        echo [LOI] Duong dan khong hop le! Khong tim thay file DPS.exe.
        echo.
        pause
        exit /b 1
    )
)

:FoundGame
echo [+] Da tim thay thu muc game:
echo     "!GAME_DIR!"
echo.

:: Check payload folder
if not exist "%~dp0payload" (
    echo [LOI] Khong tim thay thu muc 'payload'!
    echo Vui long giai nen toan bo file ZIP truoc khi chay Cai_Dat_1Click.bat.
    echo.
    pause
    exit /b 1
)

:: Check if game is running and close it safely
tasklist /fi "imagename eq DPS.exe" 2>nul | findstr /i "DPS.exe" >nul
if not errorlevel 1 (
    echo [!] Game DPS dang chay. Dang tat game de cap nhat file mod...
    taskkill /f /im DPS.exe >nul 2>&1
    timeout /t 1 /nobreak >nul
)

:: Copy payload files into game folder
echo [+] Dang sao chep cac file mod vao thu muc game...
xcopy "%~dp0payload\*" "!GAME_DIR!\" /E /I /Y /Q >nul

if errorlevel 1 (
    echo [LOI] Co loi xay ra khi sao chep file!
    echo Vui long thu chay bang quyen Administrator hoac kiem tra dung luong o cung.
    echo.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo   CAI DAT THANH CONG DPS AUTO HELPER!
echo ============================================================
echo.
echo CAC BUOC TIEP THEO:
echo   1. Mo game DPS Desktop Pension Squad tren Steam.
echo   2. Mo trinh duyet va truy cap link giao dien sau de dieu khien:
echo      https://titlee2111.github.io/dps-auto-helper/
echo   3. Phim tat trong game: F6 (Tu Dong Cat Do), F7 (Tu Dong Hop Thanh).
echo.
pause
"""
    with open(os.path.join(STAGE_DIR, "Cai_Dat_1Click.bat"), "w", encoding="ascii") as f:
        f.write(bat_install)

    # Clean up any HTML, powershell or unnecessary batch files
    print("[4/4] Don dep file thua...")
    for root, dirs, files in os.walk(STAGE_DIR):
        for f in files:
            if f.endswith(".html") or f.endswith(".ps1") or f == "Mo_Giao_Dien_Web.bat":
                f_path = os.path.join(root, f)
                print(f"[XOA FILE THUA] {f_path}")
                os.remove(f_path)

    for unnecessary in ["install.ps1", "Go_Cai_Dat.bat", "Huong_Dan.txt", "README.txt", "install.bat", "Cai_Dat_Tu_Dong.bat", "open-ui.bat", "remove.bat"]:
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
