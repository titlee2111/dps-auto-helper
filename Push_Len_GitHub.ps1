$ErrorActionPreference = "Continue"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$git = Join-Path $root ".git_tools\cmd\git.exe"
$gh = Join-Path $root ".git_tools\cmd\gh.exe"
$ucrt = Join-Path $root ".git_tools\ucrt64\bin"
$cmd = Join-Path $root ".git_tools\cmd"

$env:PATH = "$cmd;$ucrt;$env:PATH"
Set-Location $root

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "   TOOL TỰ ĐỘNG ĐẨY CODE & FILE 1-CLICK LÊN GITHUB" -ForegroundColor Cyan
Write-Host "   Repo: https://github.com/titlee2111/dps-auto-helper" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# 1. Kiểm tra trạng thái đăng nhập
$authCheck = & $gh auth status 2>&1
$isAuthed = ($LASTEXITCODE -eq 0)

if (-not $isAuthed) {
    Write-Host "[!] Bạn chưa đăng nhập GitHub trên máy tính." -ForegroundColor Yellow
    Write-Host "    Để có quyền tải file và đẩy code lên repo, chọn cách xác thực:" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "    [1] Đăng nhập tự động qua Trình Duyệt Web (Dễ nhất, khuyên dùng)" -ForegroundColor Green
    Write-Host "    [2] Dán mã GitHub Personal Access Token (PAT)" -ForegroundColor White
    Write-Host ""
    $choice = Read-Host "Nhập lựa chọn của bạn (mặc định là 1)"
    
    if ($choice -eq "2") {
        Write-Host ""
        $token = Read-Host "Dán mã Token GitHub của bạn vào đây"
        if ($token) {
            $token | & $gh auth login --with-token
            & $gh auth setup-git
        }
    } else {
        Write-Host ""
        Write-Host "[*] Đang mở trình duyệt GitHub để xác thực..." -ForegroundColor Green
        Write-Host "    (Một mã xác thực 8 chữ số sẽ hiện ra, bạn chỉ cần nhập vào web và bấm Authorize)" -ForegroundColor Gray
        & $gh auth login --hostname github.com -p https --web
        & $gh auth setup-git
    }
}

Write-Host ""
Write-Host "[1/3] Đang cập nhật và commit các file mới..." -ForegroundColor Green
& $git add -A
& $git commit -m "update: split layout with controls on left and realtime action log on right" 2>$null

Write-Host ""
Write-Host "[2/3] Đang đẩy (Push) toàn bộ code và file lên nhánh main của GitHub..." -ForegroundColor Green
& $git push -u origin main

if ($LASTEXITCODE -ne 0) {
    Write-Host "[!] Đang thử lại với cấu hình git credential từ gh..." -ForegroundColor Yellow
    & $gh auth setup-git
    & $git push -u origin main
}

Write-Host ""
Write-Host "[3/3] Đang tải file DPS_Auto_Helper_1Click.zip (57MB) lên mục Releases..." -ForegroundColor Green
$zipPath = Join-Path $root "DPS_Auto_Helper_1Click.zip"
if (Test-Path $zipPath) {
    & $gh release view v1.0.0 2>$null
    if ($LASTEXITCODE -eq 0) {
        & $gh release upload v1.0.0 $zipPath --clobber
    } else {
        & $gh release create v1.0.0 $zipPath --title "DPS Auto Helper v1.0.0" --notes "Bản phát hành tự động hóa 1-Click trọn gói dành cho game DPS Desktop Pension Squad."
    }
    Write-Host "[+] Đã phát hành file cài đặt 1-Click lên GitHub Releases thành công!" -ForegroundColor Green
}

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "   HOÀN TẤT! Bạn có thể vào xem repo tại:" -ForegroundColor Green
Write-Host "   https://github.com/titlee2111/dps-auto-helper" -ForegroundColor Yellow
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
