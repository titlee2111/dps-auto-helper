$ErrorActionPreference = "Continue"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$git = Join-Path $root ".git_tools\cmd\git.exe"
$gh = Join-Path $root ".git_tools\cmd\gh.exe"

Set-Location $root

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "   TỰ ĐỘNG ĐẨY CODE & FILE MOD 1-CLICK LÊN GITHUB" -ForegroundColor Cyan
Write-Host "   Repository: https://github.com/titlee2111/dps-auto-helper" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Check authentication
$authCheck = & $gh auth status 2>&1
$isAuthed = ($LASTEXITCODE -eq 0)

if (-not $isAuthed) {
    Write-Host "[!] Cần xác thực GitHub 1 lần để có quyền đẩy file lên repository." -ForegroundColor Yellow
    Write-Host "[*] Chuẩn bị mở trình duyệt đăng nhập GitHub (Nhấn phím Enter để tiếp tục)..." -ForegroundColor Green
    Read-Host
    
    & $gh auth login --hostname github.com -p https --web
    & $gh auth setup-git
}

Write-Host ""
Write-Host "[1/3] Đang kiểm tra và commit các file..." -ForegroundColor Green
& $git add -A
& $git commit -m "update: latest full-width UI and 1-click bundle" 2>$null

Write-Host ""
Write-Host "[2/3] Đang đẩy (Push) code lên nhánh main của GitHub..." -ForegroundColor Green
& $git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "[+] Đã đẩy nhánh main thành công!" -ForegroundColor Green
} else {
    Write-Host "[!] Đang cấu hình xác thực git token và thử lại..." -ForegroundColor Yellow
    & $gh auth setup-git
    & $git push -u origin main
}

# Upload 57MB zip to GitHub Releases
Write-Host ""
Write-Host "[3/3] Đang tải file DPS_Auto_Helper_1Click.zip (57MB) lên GitHub Releases..." -ForegroundColor Green
$zipPath = Join-Path $root "DPS_Auto_Helper_1Click.zip"
if (Test-Path $zipPath) {
    & $gh release view v1.0.0 2>$null
    if ($LASTEXITCODE -eq 0) {
        & $gh release upload v1.0.0 $zipPath --clobber
    } else {
        & $gh release create v1.0.0 $zipPath --title "DPS Auto Helper v1.0.0" --notes "Bản phát hành tự động hóa 1-Click dành cho game DPS Desktop Pension Squad."
    }
    Write-Host "[+] Đã tải file 57MB lên mục Releases thành công!" -ForegroundColor Green
}

Write-Host ""
Write-Host "============================================================" -ForegroundColor Green
Write-Host "  ĐÃ HOÀN TẤT ĐẨY CODE VÀ FILE MOD LÊN GITHUB THÀNH CÔNG!" -ForegroundColor Green
Write-Host "  Link web: https://titlee2111.github.io/dps-auto-helper/" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Green
