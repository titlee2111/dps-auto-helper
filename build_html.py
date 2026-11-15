import os

BASE_DIR = r"C:\Users\Son\Desktop\dps-auto-helper"
ICON_B64_FILE = os.path.join(BASE_DIR, "game_icon_b64.txt")
SOUL_B64_FILE = os.path.join(BASE_DIR, "soul_icon_b64.txt")
GEM_B64_FILE = os.path.join(BASE_DIR, "gem_icon_b64.txt")
QR0_FILE = os.path.join(BASE_DIR, "qr_0.txt")
QR1_FILE = os.path.join(BASE_DIR, "qr_1.txt")
GUIDE_B64_FILE = os.path.join(BASE_DIR, "guide_icon_b64.txt")
HTML_FILE = os.path.join(BASE_DIR, "index.html")

with open(ICON_B64_FILE, "r", encoding="utf-8") as f:
    b64_icon = f.read().strip()

with open(SOUL_B64_FILE, "r", encoding="utf-8") as f:
    b64_soul = f.read().strip()

with open(GEM_B64_FILE, "r", encoding="utf-8") as f:
    b64_gem = f.read().strip()

with open(GUIDE_B64_FILE, "r", encoding="utf-8") as f:
    b64_guide = f.read().strip()

with open(QR0_FILE, "r", encoding="utf-8") as f:
    mb_qr_src = f.read().strip()

with open(QR1_FILE, "r", encoding="utf-8") as f:
    binance_qr_src = f.read().strip()

html_template = """<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>DPS Auto Helper - Tự Động Hóa Kho & Xưởng</title>
  <link rel="icon" type="image/png" href="data:image/png;base64,__B64_ICON__">
  <style>
    :root {
      --bg: #090d16;
      --bg-card: #0f172a;
      --line: #1e293b;
      --line-light: #334155;
      --ink: #f8fafc;
      --dim: #94a3b8;
      --dimmer: #64748b;

      /* Clean Accent Colors (Crisp, No Blurry Glow) */
      --cyan: #0ea5e9;
      --cyan-border: rgba(14, 165, 233, 0.35);

      --emerald: #10b981;
      --emerald-border: rgba(16, 185, 129, 0.35);

      --purple: #a855f7;
      --purple-border: rgba(168, 85, 247, 0.35);

      --amber: #f59e0b;
      --amber-border: rgba(245, 158, 11, 0.35);

      --rose: #f43f5e;
      --blue: #3b82f6;

      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --radius-full: 9999px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    
    body {
      background: var(--bg);
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(14, 165, 233, 0.05) 0%, transparent 40%),
        radial-gradient(circle at 85% 85%, rgba(168, 85, 247, 0.04) 0%, transparent 40%);
      background-attachment: fixed;
      color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      width: 100%;
      overflow-x: hidden;
    }

    /* ==================== HEADER ==================== */
    header {
      background: rgba(15, 23, 42, 0.95);
      border-bottom: 1px solid var(--line);
      padding: 12px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.35);
      width: 100%;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      flex-shrink: 0;
    }
    .game-logo {
      width: 44px;
      height: 44px;
      border-radius: var(--radius-md);
      border: 1px solid rgba(255, 255, 255, 0.15);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
      object-fit: cover;
      background: #141c2b;
      display: block;
      transition: transform 0.2s ease;
    }
    .game-logo:hover {
      transform: scale(1.05);
    }
    .brand-titles {
      display: flex;
      flex-direction: column;
    }
    .brand-titles h1 {
      font-size: 15px;
      font-weight: 800;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: #f8fafc;
      line-height: 1.2;
    }
    .brand-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      color: var(--cyan);
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      margin-top: 2px;
    }

    /* ==================== CENTER HUD BAR ==================== */
    .header-hud {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      flex-wrap: wrap;
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid var(--line);
      border-radius: var(--radius-full);
      padding: 6px 20px;
      box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.06), 0 4px 14px rgba(0, 0, 0, 0.25);
    }

    .hud-item {
      display: flex;
      align-items: center;
      gap: 9px;
      padding: 3px 12px;
      border-right: 1px solid rgba(255, 255, 255, 0.08);
      position: relative;
    }
    .hud-item:last-child {
      border-right: none;
    }

    .hud-icon {
      font-size: 17px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .hud-img-icon {
      width: 22px;
      height: 22px;
      object-fit: contain;
      display: block;
    }

    .hud-info {
      display: flex;
      flex-direction: column;
      line-height: 1.15;
    }
    .hud-label {
      font-size: 9.5px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.07em;
      color: var(--dimmer);
    }
    .hud-val {
      font-size: 13.5px;
      font-weight: 700;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      letter-spacing: 0.02em;
    }
    .hud-soul .hud-val { color: #67e8f9; }
    .hud-stone .hud-val { color: #d07eff; }
    .hud-cap .hud-val { color: #6ee7b7; }

    .hud-mini-bar {
      width: 48px;
      height: 6px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: var(--radius-full);
      overflow: hidden;
      margin-left: 4px;
      border: 1px solid rgba(255, 255, 255, 0.05);
    }
    .hud-mini-fill {
      height: 100%;
      background: #10b981;
      border-radius: var(--radius-full);
      transition: width 0.4s ease;
    }

    .header-status {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
      flex-shrink: 0;
    }
    .chip {
      font-size: 12px;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: var(--radius-full);
      background: #141b2a;
      color: var(--dim);
      border: 1px solid rgba(255, 255, 255, 0.1);
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }
    .chip.status-live {
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border-color: rgba(16, 185, 129, 0.4);
    }
    .chip.status-dead {
      background: rgba(239, 68, 68, 0.15);
      color: #f87171;
      border-color: rgba(239, 68, 68, 0.4);
    }
    .dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: currentColor;
      display: inline-block;
    }
    .dot.pulse {
      animation: pulse 1.6s infinite;
    }

    /* Support Button (Exact War of Genesis Style) */
    .support-tab-btn {
      background: linear-gradient(135deg, rgba(227, 179, 65, 0.12) 0%, rgba(255, 166, 87, 0.18) 100%);
      border: 1px solid rgba(227, 179, 65, 0.45);
      color: #f0c674;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
      padding: 7px 15px;
      border-radius: 6px;
      font-weight: 600;
      cursor: pointer;
      font-size: 13px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
      text-decoration: none;
    }
    .support-tab-btn:hover {
      background: linear-gradient(135deg, #e3b341 0%, #ffa657 100%);
      color: #0d1117;
      border-color: #ffa657;
      transform: translateY(-1px);
      box-shadow: 0 4px 14px rgba(227, 179, 65, 0.35);
    }
    .support-tab-btn:active {
      transform: translateY(0);
    }

    /* Modal Tab Buttons */
    .modal-tab-btn {
      background: transparent;
      border: 1px solid transparent;
      color: #8b949e;
      padding: 9px 16px;
      border-radius: 6px;
      font-weight: 700;
      cursor: pointer;
      font-size: 13px;
      transition: all 0.2s;
      white-space: nowrap;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      flex: 1 1 auto;
    }
    .modal-tab-btn:hover {
      color: #f0f6fc;
      background: #21262d;
    }
    .modal-tab-btn.active {
      color: #fff;
      background: #1f6feb;
      border-color: #388bfd;
    }

    /* Small Copy Buttons */
    .small-copy-btn {
      padding: 4px 10px;
      font-size: 11.5px;
      border-radius: 4px;
      border: none;
      cursor: pointer;
      font-weight: 700;
      transition: all 0.15s ease;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }

    @keyframes pulse {
      0% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.3; transform: scale(1.2); }
      100% { opacity: 1; transform: scale(1); }
    }

    /* ==================== MAIN CONTAINER ==================== */
    .container {
      max-width: 100%;
      width: 100%;
      margin: 0;
      padding: 22px 28px;
      display: flex;
      flex-direction: column;
      gap: 20px;
      flex: 1;
    }

    /* Dismissible Alert Banner */
    .alert-banner {
      background: rgba(245, 158, 11, 0.1);
      border: 1px solid rgba(245, 158, 11, 0.3);
      border-radius: var(--radius-md);
      padding: 12px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    .alert-banner-content {
      display: flex;
      align-items: center;
      gap: 12px;
      color: #fcd34d;
      font-size: 13px;
      line-height: 1.4;
      flex: 1;
    }
    .alert-banner-btn {
      background: rgba(245, 158, 11, 0.2);
      border: 1px solid #f59e0b;
      color: #fde68a;
      font-size: 12px;
      font-weight: 700;
      padding: 7px 16px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .alert-banner-btn:hover {
      background: #f59e0b;
      color: #000;
    }
    .alert-close-btn {
      background: none;
      border: none;
      color: #f59e0b;
      font-size: 18px;
      cursor: pointer;
      opacity: 0.7;
      padding: 0 4px;
      transition: opacity 0.15s;
    }
    .alert-close-btn:hover { opacity: 1; }

    /* Horizontal Download Bar */
    .download-strip {
      background: #0f172a;
      border: 1px solid var(--line);
      border-radius: var(--radius-md);
      padding: 16px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25);
    }
    .download-strip-info {
      display: flex;
      align-items: center;
      gap: 16px;
    }
    .download-strip-icon {
      width: 44px;
      height: 44px;
      border-radius: var(--radius-md);
      background: rgba(14, 165, 233, 0.15);
      border: 1px solid rgba(14, 165, 233, 0.3);
      color: #38bdf8;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
      flex-shrink: 0;
    }
    .download-strip-text h3 {
      font-size: 14px;
      font-weight: 700;
      color: #f8fafc;
      letter-spacing: 0.02em;
    }
    .download-strip-text p {
      font-size: 12px;
      color: var(--dim);
      margin-top: 3px;
    }
    .btn-download-trigger {
      background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%);
      color: #fff;
      font-size: 13px;
      font-weight: 700;
      padding: 10px 22px;
      border-radius: var(--radius-sm);
      border: 1px solid rgba(56, 189, 248, 0.5);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
      transition: all 0.2s ease;
    }
    .btn-download-trigger:hover {
      background: linear-gradient(135deg, #0369a1 0%, #1d4ed8 100%);
      transform: translateY(-1px);
    }

    /* Top Mini Action Bar */
    .mini-actions-bar {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }
    .btn-mini-action {
      background: #1e293b;
      border: 1px solid var(--line-light);
      color: #e2e8f0;
      font-size: 12px;
      font-weight: 600;
      padding: 8px 16px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      transition: all 0.2s ease;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
    }
    .btn-mini-action.btn-mini-comb:hover {
      background: rgba(14, 165, 233, 0.15);
      border-color: #0ea5e9;
      color: #38bdf8;
    }
    .btn-mini-action.btn-mini-stash:hover {
      background: rgba(16, 185, 129, 0.15);
      border-color: #10b981;
      color: #34d399;
    }

    /* ==================== SPLIT LAYOUT ==================== */
    .split-layout {
      display: grid;
      grid-template-columns: 0.8fr 1.2fr;
      gap: 20px;
      width: 100%;
      align-items: start;
    }
    @media (max-width: 1024px) {
      .split-layout {
        grid-template-columns: 1fr;
      }
    }

    .controls-column {
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    /* ==================== NAV TABS ==================== */
    .nav-tabs-bar {
      display: flex;
      gap: 10px;
      margin-bottom: 4px;
      width: 100%;
    }
    .nav-tab-btn {
      flex: 1;
      background: #161b22;
      border: 1px solid #30363d;
      border-radius: var(--radius-sm);
      padding: 10px 14px;
      color: #8b949e;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.2s ease;
    }
    .nav-tab-btn:hover {
      background: #21262d;
      color: #f0f6fc;
      border-color: #484f58;
    }
    .nav-tab-btn.active {
      background: linear-gradient(135deg, rgba(31, 111, 235, 0.25) 0%, rgba(56, 139, 253, 0.08) 100%);
      border-color: #388bfd;
      color: #58a6ff;
      box-shadow: 0 0 14px rgba(56, 139, 253, 0.2);
    }
    .nav-tab-btn.nav-tab-vip.active {
      background: linear-gradient(135deg, rgba(210, 153, 34, 0.28) 0%, rgba(245, 158, 11, 0.1) 100%);
      border-color: #f59e0b;
      color: #fbbf24;
      box-shadow: 0 0 16px rgba(245, 158, 11, 0.25);
    }
    .vip-lock-badge {
      font-size: 11px;
      padding: 2px 7px;
      border-radius: 12px;
      font-weight: 600;
      background: rgba(248, 81, 73, 0.18);
      border: 1px solid rgba(248, 81, 73, 0.4);
      color: #ff7b72;
    }
    .vip-lock-badge.unlocked {
      background: rgba(35, 134, 54, 0.2);
      border-color: rgba(46, 160, 67, 0.5);
      color: #7ee787;
    }
    .btn-preset {
      background: #21262d;
      border: 1px solid #30363d;
      color: #c9d1d9;
      font-size: 11.5px;
      font-weight: 600;
      padding: 4px 10px;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .btn-preset:hover {
      background: #30363d;
      color: #fff;
      border-color: #58a6ff;
    }

    .log-column {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    /* ==================== CLEAN ACCENT CARDS ==================== */
    .card {
      background: var(--bg-card);
      border-radius: var(--radius-md);
      padding: 16px 18px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
      position: relative;
      border: 1px solid var(--card-border);
      transition: all 0.2s ease;
    }
    .card::before {
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 3px;
      background: var(--card-accent);
      border-radius: var(--radius-md) var(--radius-md) 0 0;
    }
    .card:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 26px rgba(0, 0, 0, 0.35);
    }

    /* THEME 1: COMBINE (Cyan) */
    .card-cyan {
      --card-border: rgba(14, 165, 233, 0.3);
      --card-accent: #0ea5e9;
    }
    .card-cyan .card-title { color: #38bdf8; }

    /* THEME 2: STASH (Emerald) */
    .card-emerald {
      --card-border: rgba(16, 185, 129, 0.3);
      --card-accent: #10b981;
    }
    .card-emerald .card-title { color: #34d399; }

    /* THEME 3: AUTO BOX (Purple) */
    .card-purple {
      --card-border: rgba(168, 85, 247, 0.3);
      --card-accent: #a855f7;
    }
    .card-purple .card-title { color: #c084fc; }

    /* THEME 4: DLC FORGE (Amber) */
    .card-amber {
      --card-border: rgba(245, 158, 11, 0.3);
      --card-accent: #f59e0b;
      background: #141824;
    }
    .card-amber .card-title { color: #fbbf24; }

    .card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 16px;
      gap: 12px;
    }
    .card-title {
      font-size: 14px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 9px;
      letter-spacing: 0.03em;
      text-transform: uppercase;
    }
    .card-icon {
      font-size: 18px;
    }
    .status-badge {
      font-size: 11px;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: var(--radius-full);
      background: #1e293b;
      color: var(--dimmer);
      border: 1px solid rgba(255, 255, 255, 0.08);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .status-badge.active {
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border-color: rgba(16, 185, 129, 0.4);
    }

    .form-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      padding: 12px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }
    .form-row:last-child {
      border-bottom: none;
      padding-bottom: 0;
    }
    .form-label {
      font-size: 13.5px;
      font-weight: 600;
      color: #f1f5f9;
    }
    .form-sublabel {
      font-size: 12px;
      color: var(--dim);
      margin-top: 3px;
    }

    /* Switch - Clean Modern */
    .switch {
      position: relative;
      display: inline-block;
      width: 48px;
      height: 26px;
      flex-shrink: 0;
    }
    .switch input { opacity: 0; width: 0; height: 0; }
    .slider {
      position: absolute;
      cursor: pointer;
      top: 0; left: 0; right: 0; bottom: 0;
      background-color: #334155;
      transition: .2s ease;
      border-radius: 34px;
    }
    .slider:before {
      position: absolute;
      content: "";
      height: 18px;
      width: 18px;
      left: 4px;
      bottom: 4px;
      background-color: #ffffff;
      transition: .2s ease;
      border-radius: 50%;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
    }
    input:checked + .slider {
      background-color: #0284c7;
    }
    .card-emerald input:checked + .slider {
      background-color: #10b981;
    }
    .card-purple input:checked + .slider {
      background-color: #9333ea;
    }
    .card-amber input:checked + .slider {
      background-color: #d97706;
    }
    input:checked + .slider:before {
      transform: translateX(22px);
    }

    .config-row {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-top: 14px;
      background: rgba(10, 15, 26, 0.7);
      padding: 10px 16px;
      border-radius: var(--radius-sm);
      border: 1px solid rgba(255, 255, 255, 0.06);
      flex-wrap: wrap;
    }
    .config-group {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .config-label {
      font-size: 12.5px;
      color: var(--dim);
      font-weight: 600;
    }
    .num-input {
      width: 58px;
      background: #1e293b;
      border: 1px solid var(--line-light);
      color: #fff;
      font-size: 13px;
      font-weight: 700;
      padding: 5px 8px;
      border-radius: var(--radius-sm);
      text-align: center;
      outline: none;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      transition: border-color 0.2s;
    }
    .num-input:focus {
      border-color: #38bdf8;
    }
    .config-unit {
      font-size: 12px;
      color: var(--dimmer);
    }

    /* Capacity Progress Box */
    .capacity-box {
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(16, 185, 129, 0.3);
      border-radius: var(--radius-md);
      padding: 14px 16px;
      margin-top: 14px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    }
    .capacity-placeholder {
      background: rgba(15, 23, 42, 0.6);
      border: 1px dashed rgba(255, 255, 255, 0.12);
      border-radius: var(--radius-md);
      padding: 14px 16px;
      margin-top: 14px;
      font-size: 12.5px;
      color: var(--dimmer);
      text-align: center;
    }
    .cap-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 12.5px;
    }
    .cap-title {
      color: #e2e8f0;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .cap-stat {
      color: #34d399;
      font-weight: 700;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }
    .cap-progress-track {
      width: 100%;
      height: 8px;
      background: rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-full);
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.05);
    }
    .cap-progress-bar {
      height: 100%;
      background: #10b981;
      border-radius: var(--radius-full);
      transition: width 0.4s ease;
    }
    .cap-details {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11.5px;
      color: var(--dim);
      flex-wrap: wrap;
      gap: 8px;
      padding-top: 2px;
    }
    .cap-details b {
      color: #38bdf8;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }

    /* DLC Warning */
    .dlc-warning-box {
      background: rgba(245, 158, 11, 0.1);
      border: 1px solid rgba(245, 158, 11, 0.35);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      font-size: 12.5px;
      line-height: 1.5;
      color: #fde68a;
      margin-bottom: 14px;
    }
    .dlc-warning-title {
      font-weight: 700;
      color: #fbbf24;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .dlc-warning-highlight {
      margin-top: 8px;
      padding: 8px 12px;
      background: rgba(239, 68, 68, 0.15);
      border-left: 3px solid #ef4444;
      color: #fca5a5;
      font-size: 12px;
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      font-weight: 600;
    }
    .dlc-toggle-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      padding: 10px 0;
    }
    .dlc-toggle-name {
      font-size: 13.5px;
      font-weight: 700;
      color: #fff;
    }
    .dlc-toggle-desc {
      font-size: 12px;
      color: var(--dim);
      margin-top: 3px;
    }

    .box-count-badge {
      background: rgba(168, 85, 247, 0.15);
      color: #c084fc;
      border: 1px solid rgba(168, 85, 247, 0.3);
      font-size: 12px;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: var(--radius-full);
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }

    /* ==================== REALTIME LOG BOX ==================== */
    .log-container {
      background: #161b22;
      border: 1px solid #30363d;
      border-radius: var(--radius-md);
      display: flex;
      flex-direction: column;
      height: 640px;
      padding: 14px 16px 16px 16px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }
    @media (max-width: 1024px) {
      .log-container {
        height: 480px;
      }
    }
    .log-header {
      padding: 0 0 10px 0;
      background: transparent;
      border-bottom: 1px solid #21262d;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .log-title {
      font-size: 13.5px;
      font-weight: 700;
      color: #f0f6fc;
      display: flex;
      align-items: center;
      gap: 8px;
      letter-spacing: 0.02em;
    }
    .btn-clear-log {
      background: #21262d;
      border: 1px solid #30363d;
      color: #8b949e;
      font-size: 11px;
      font-weight: 600;
      padding: 3px 10px;
      border-radius: 5px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .btn-clear-log:hover {
      background: #30363d;
      color: #fff;
      border-color: #58a6ff;
    }
    .log-feed {
      flex: 1;
      background: #000000;
      border: 1px solid #21262d;
      border-radius: 6px;
      padding: 12px 14px;
      overflow-y: auto;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
      font-size: 12px;
      line-height: 1.65;
      display: flex;
      flex-direction: column;
      gap: 5px;
      box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.85);
      min-height: 200px;
    }
    .log-feed::-webkit-scrollbar {
      width: 7px;
    }
    .log-feed::-webkit-scrollbar-track {
      background: #000000;
      border-radius: 4px;
    }
    .log-feed::-webkit-scrollbar-thumb {
      background: #21262d;
      border-radius: 4px;
    }
    .log-feed::-webkit-scrollbar-thumb:hover {
      background: #388bfd;
    }
    .log-entry {
      display: flex;
      align-items: flex-start;
      gap: 8px;
      animation: fadeIn 0.15s ease-in;
    }
    .log-time {
      color: #58a6ff;
      flex-shrink: 0;
      font-size: 11.5px;
      font-weight: 600;
    }
    .log-tag {
      padding: 1px 7px;
      border-radius: 4px;
      font-size: 10.5px;
      font-weight: 700;
      flex-shrink: 0;
      letter-spacing: 0.03em;
    }
    .log-tag.tag-ok { background: rgba(35, 134, 54, 0.25); color: #7ee787; border: 1px solid rgba(35, 134, 54, 0.45); }
    .log-tag.tag-info { background: rgba(31, 111, 235, 0.2); color: #58a6ff; border: 1px solid rgba(56, 139, 253, 0.35); }
    .log-tag.tag-warn { background: rgba(210, 153, 34, 0.2); color: #e3b341; border: 1px solid rgba(210, 153, 34, 0.45); }
    .log-tag.tag-err { background: rgba(248, 81, 73, 0.2); color: #ff7b72; border: 1px solid rgba(248, 81, 73, 0.45); }
    .log-tag.tag-box { background: rgba(163, 113, 247, 0.2); color: #d2a8ff; border: 1px solid rgba(163, 113, 247, 0.45); }
    .log-msg {
      color: #e6edf3;
      word-break: break-word;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(4px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* MODAL OVERLAY */
    .modal-overlay {
      display: none;
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(4, 7, 14, 0.8);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      z-index: 9999;
      align-items: center;
      justify-content: center;
      padding: 20px;
      animation: fadeIn 0.2s ease;
    }
    .modal-card {
      background: #0f172a;
      border: 1px solid var(--line);
      border-radius: var(--radius-lg);
      width: 100%;
      max-width: 680px;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.7);
      overflow: hidden;
    }
    .modal-header {
      padding: 16px 24px;
      background: #1e293b;
      border-bottom: 1px solid var(--line);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .modal-title {
      font-size: 15px;
      font-weight: 700;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .modal-close-btn {
      background: none;
      border: none;
      color: var(--dim);
      font-size: 22px;
      cursor: pointer;
      line-height: 1;
      transition: color 0.15s;
    }
    .modal-close-btn:hover { color: #fff; }
    .modal-body {
      padding: 24px;
      overflow-y: auto;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    .modal-dl-row {
      background: #1e293b;
      border: 1px solid var(--line-light);
      border-radius: var(--radius-md);
      padding: 18px 22px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }
    .modal-dl-row-left {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .btn-download-rect {
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      color: #fff;
      font-size: 13px;
      font-weight: 700;
      padding: 11px 24px;
      border-radius: var(--radius-sm);
      border: 1px solid #34d399;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
      transition: all 0.2s ease;
      white-space: nowrap;
    }
    .btn-download-rect:hover {
      background: linear-gradient(135deg, #34d399 0%, #10b981 100%);
      transform: translateY(-1px);
    }

    .donate-tabs {
      display: flex;
      gap: 8px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 12px;
    }
    .donate-tab-btn {
      background: #1e293b;
      border: 1px solid var(--line-light);
      color: var(--dim);
      font-size: 13px;
      font-weight: 600;
      padding: 8px 16px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: all 0.2s;
    }
    .donate-tab-btn.active {
      background: #0284c7;
      border-color: #38bdf8;
      color: #fff;
    }
    .donate-tab-content {
      display: none;
      flex-direction: column;
      align-items: center;
      gap: 14px;
      text-align: center;
    }
    .donate-tab-content.active { display: flex; }
    .qr-img {
      width: 200px;
      height: 200px;
      border-radius: var(--radius-md);
      border: 1px solid rgba(255, 255, 255, 0.15);
      background: #fff;
      padding: 6px;
    }
    .copy-pill {
      background: #1e293b;
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 8px 16px;
      border-radius: var(--radius-sm);
      font-size: 13px;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      color: #93c5fd;
      transition: all 0.2s;
    }
    .copy-pill:hover {
      border-color: #38bdf8;
      color: #fff;
      background: rgba(56, 189, 248, 0.15);
    }

    /* Floating Discord Circle Button */
    .discord-float {
      position: fixed;
      bottom: 24px;
      right: 24px;
      width: 52px;
      height: 52px;
      border-radius: 50%;
      background: #5865F2;
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.35);
      border: 1px solid rgba(255, 255, 255, 0.25);
      z-index: 990;
      cursor: pointer;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      text-decoration: none;
    }
    .discord-float:hover {
      transform: scale(1.08);
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
    }
    .discord-tooltip {
      position: absolute;
      right: 64px;
      background: #1e1f22;
      color: #dbdee1;
      font-size: 12px;
      font-weight: 600;
      padding: 6px 12px;
      border-radius: 6px;
      white-space: nowrap;
      pointer-events: none;
      opacity: 0;
      transform: translateX(10px);
      transition: all 0.2s ease;
      box-shadow: 0 4px 12px rgba(0,0,0,0.4);
      border: 1px solid #2b2d31;
    }
    .discord-float:hover .discord-tooltip {
      opacity: 1;
      transform: translateX(0);
    }

    /* Footer */
    footer {
      margin-top: auto;
      border-top: 1px solid var(--line);
      padding: 16px 28px;
      font-size: 12px;
      color: var(--dimmer);
      text-align: center;
      background: rgba(6, 9, 14, 0.95);
      width: 100%;
    }
  </style>
</head>
<body>

  <!-- HEADER -->
  <header>
    <a href="#" class="brand">
      <img src="data:image/png;base64,__B64_ICON__" alt="DPS Logo" class="game-logo">
      <div class="brand-titles">
        <h1>DPS DESKTOP PENSION SQUAD</h1>
        <div class="brand-badge">⚡ AUTO HELPER</div>
      </div>
    </a>

    <!-- TOP CENTER HUD -->
    <div class="header-hud">
      <div class="hud-item hud-soul" title="Linh hồn nhân vật">
        <div class="hud-icon">
          <img src="data:image/png;base64,__SOUL_ICON_B64__" class="hud-img-icon" alt="Linh Hồn">
        </div>
        <div class="hud-info">
          <span class="hud-label">Linh Hồn</span>
          <span class="hud-val" id="hudSoul">--</span>
        </div>
      </div>
      <div class="hud-item hud-stone" title="Đá linh hồn nhân vật">
        <div class="hud-icon">
          <img src="data:image/png;base64,__GEM_ICON_B64__" class="hud-img-icon" alt="Đá Linh Hồn">
        </div>
        <div class="hud-info">
          <span class="hud-label">Đá Linh Hồn</span>
          <span class="hud-val" id="hudSoulStone">--</span>
        </div>
      </div>
      <div class="hud-item hud-cap" title="Dung lượng kho và túi">
        <div class="hud-icon">🎒</div>
        <div class="hud-info">
          <span class="hud-label">Dung Lượng Kho</span>
          <span class="hud-val" id="hudCap">-- / --</span>
        </div>
        <div class="hud-mini-bar">
          <div class="hud-mini-fill" id="hudCapBar" style="width: 0%"></div>
        </div>
      </div>
    </div>

    <div class="header-status">
      <button class="support-tab-btn" onclick="openPermissionModal()" style="border-color: rgba(56, 189, 248, 0.4); color: #38bdf8;" title="Hướng dẫn bật quyền trình duyệt để kết nối game">
        <span style="font-size:14px;">❓</span>
        <span>Hướng Dẫn Kết Nối</span>
      </button>
      <button class="support-tab-btn notranslate" id="supportMeBtn" translate="no" onclick="openDonateModal()" title="Ủng hộ tác giả / Support the Developer">
        <span style="font-size:15px;">☕</span>
        <span id="supportMeBtnText">Ủng Hộ Tác Giả</span>
      </button>
      <div class="chip" id="pidChip">
        <span class="dot"></span>
        <span>PID: <b id="pidVal">--</b></span>
      </div>
      <div class="chip status-dead" id="statusChip">
        <span class="dot"></span>
        <span id="statusText">Chưa kết nối game</span>
      </div>
    </div>
  </header>

  <!-- MAIN CONTAINER -->
  <main class="container">
    
    <!-- Top Alert Banner -->
    <div class="alert-banner" id="topAlert">
      <div class="alert-banner-content">
        <span style="font-size: 18px;">⚠️</span>
        <div><b>Lưu ý quan trọng:</b> Tool điều khiển trực tiếp thông qua game. Bạn cần tải gói cài đặt 1–Click để kích hoạt mod bên trong thư mục game Steam trước khi sử dụng.</div>
      </div>
      <button class="alert-banner-btn" onclick="openDownloadModal()">📥 Tải File 1-Click Ngay</button>
      <button class="alert-close-btn" onclick="dismissAlert()" title="Đóng thông báo">✕</button>
    </div>




    <!-- Download Strip -->
    <div class="download-strip">
      <div class="download-strip-info">
        <div class="download-strip-icon">📦</div>
        <div class="download-strip-text">
          <h3>GÓI CÀI ĐẶT TỰ ĐỘNG 1–CLICK (MOD HELPER RUNTIME)</h3>
          <p>Tự động phát hiện thư mục game Steam và cài đặt trong 2 giây • Không làm hỏng file gốc của game</p>
        </div>
      </div>
      <button class="btn-download-trigger" onclick="openDownloadModal()">
        📥 TẢI FILE 1-CLICK & HƯỚNG DẪN
      </button>
    </div>

    <!-- Top Mini Action Bar -->
    <div class="mini-actions-bar">
      <button class="btn-mini-action btn-mini-comb" onclick="triggerCombine()" title="Ghép đồ xưởng ngay lập tức">
        ⚡ GHÉP ĐỒ NGAY
      </button>
      <button class="btn-mini-action btn-mini-stash" onclick="triggerStash()" title="Cất đồ túi đồ vào kho ngay lập tức">
        📥 CẤT ĐỒ NGAY
      </button>
    </div>

    <!-- Split Layout -->
    <div class="split-layout">
      
      <!-- LEFT: CONTROLS COLUMN -->
      <div class="controls-column">
        
        <!-- MAIN NAVIGATION TABS -->
        <div class="nav-tabs-bar">
          <button class="nav-tab-btn active" id="btnTabHelper" onclick="switchMainTab('helper')">
            <span>⚡</span>
            <span>Trợ Thủ Tự Động</span>
          </button>
          <button class="nav-tab-btn nav-tab-vip" id="btnTabVip" onclick="switchMainTab('vip')">
            <span id="vipTabIcon">👑</span>
            <span id="vipTabText">Chức Năng VIP</span>
            <span class="vip-lock-badge" id="vipLockBadge">🔒 Khóa</span>
          </button>
        </div>

        <!-- TAB 1: HELPER MODULES -->
        <div id="tabContentHelper" style="display: flex; flex-direction: column; gap: 14px;">

        <!-- MODULE 1: COMBINE -->
        <section class="card card-cyan">
          <div class="card-header">
            <div class="card-title">
              <span class="card-icon">⚡</span>
              <span>Tự Động Hợp Thành (Lò Rèn / Xưởng)</span>
            </div>
            <span class="status-badge" id="badgeCombine">Đang Tắt</span>
          </div>

          <div class="form-row">
            <div>
              <div class="form-label">Bật Tự Động Hợp Thành Định Kỳ</div>
              <div class="form-sublabel">Tự động lặp lại công thức chế tạo trong Xưởng định kỳ theo số phút đã thiết lập</div>
            </div>
            <label class="switch">
              <input type="checkbox" id="toggleCombine" onchange="onToggleCombine(this)">
              <span class="slider"></span>
            </label>
          </div>

          <div class="config-row">
            <div class="config-group">
              <span class="config-label">Chu kỳ chạy mỗi:</span>
              <input type="number" id="combineInterval" class="num-input" value="5" min="1" max="120" onchange="updateCombineInterval()">
              <span class="config-unit">phút</span>
            </div>
            <span style="font-size: 11.5px; color: var(--dimmer); margin-left: auto;">(Khuyến dùng: 3 – 5 phút/lần)</span>
          </div>
        </section>

        <!-- MODULE 2: STASH -->
        <section class="card card-emerald">
          <div class="card-header">
            <div class="card-title">
              <span class="card-icon">📦</span>
              <span>Tự Động Cất Đồ Vào Kho</span>
            </div>
            <span class="status-badge" id="badgeStash">Đang Tắt</span>
          </div>

          <div class="form-row">
            <div>
              <div class="form-label">Bật Tự Động Cất Đồ Định Kỳ</div>
              <div class="form-sublabel">Cất đồ từ túi cá nhân tuần tự vào các ngăn kho đã chọn</div>
            </div>
            <label class="switch">
              <input type="checkbox" id="toggleStash" onchange="onToggleStash(this)">
              <span class="slider"></span>
            </label>
          </div>

          <div class="config-row">
            <div class="config-group">
              <span class="config-label">Chu kỳ chạy mỗi:</span>
              <input type="number" id="stashInterval" class="num-input" value="60" min="5" max="3600" onchange="updateStashInterval()">
              <span class="config-unit">giây</span>
            </div>
            <div class="config-group" style="margin-left: 12px;">
              <span class="config-label">Cất từ Kho:</span>
              <input type="number" id="stashStart" class="num-input" value="1" min="1" max="8" oninput="updateStashTabs()" onchange="updateStashTabs()">
              <span class="config-label">đến Kho:</span>
              <input type="number" id="stashEnd" class="num-input" value="5" min="1" max="8" oninput="updateStashTabs()" onchange="updateStashTabs()">
            </div>
          </div>

          <!-- Capacity Box (Only visible when connected) -->
          <div class="capacity-box" id="capacityBox" style="display: none;">
            <div class="cap-header">
              <span class="cap-title">🎒 Dung lượng kho & túi cá nhân</span>
              <span class="cap-stat" id="capStat">0 / 0 slot</span>
            </div>
            <div class="cap-progress-track">
              <div class="cap-progress-bar" id="capBar" style="width: 0%"></div>
            </div>
            <div class="cap-details">
              <span>Túi cá nhân: <b id="invStat">-- / --</b></span>
              <span>Hòm đồ phụ: <b id="storageStat">-- / --</b></span>
              <span>Tỷ lệ lấp đầy: <b id="capPercent">0%</b></span>
            </div>
          </div>
          <!-- Capacity Placeholder when disconnected -->
          <div class="capacity-placeholder" id="capacityPlaceholder">
            ⏳ Kết nối game để theo dõi dung lượng kho và túi đồ theo thời gian thực
          </div>
        </section>

        <!-- MODULE 3: CHEST OPENER -->
        <section class="card card-purple">
          <div class="card-header">
            <div class="card-title">
              <span class="card-icon">🎁</span>
              <span>Tự Động Mở Rương Báu (Chest Opener)</span>
            </div>
            <span class="status-badge" id="badgeAutoBox">Đang Tắt</span>
          </div>

          <div class="form-row">
            <div>
              <div class="form-label">Bật Tự Động Mở Rương Định Kỳ</div>
              <div class="form-sublabel">Tự động phát hiện và mở sạch tất cả rương rơi trên sàn đấu (Normal, Stage, Elite) ngầm</div>
            </div>
            <label class="switch">
              <input type="checkbox" id="toggleAutoBox" onchange="onToggleAutoBox(this)">
              <span class="slider"></span>
            </label>
          </div>

          <div class="config-row">
            <div class="config-group">
              <span class="config-label">Chu kỳ kiểm tra:</span>
              <input type="number" id="boxInterval" class="num-input" value="3" min="1" max="60" onchange="updateBoxInterval()">
              <span class="config-unit">giây</span>
            </div>
            <div style="margin-left: auto;">
              <span class="box-count-badge" id="boxCountBadge">Rương đang có: <b id="boxCountVal">0 Rương</b></span>
            </div>
          </div>
        </section>

        <!-- MODULE 4: DLC UNLOCK -->
        <section class="card card-amber">
          <div class="card-header">
            <div class="card-title">
              <span class="card-icon">🎁</span>
              <span>Mở Khóa DLC Lò Rèn & Xưởng (Phím F5)</span>
            </div>
            <label class="switch">
              <input type="checkbox" id="toggleDlc" onchange="onToggleDlc(this)">
              <span class="slider"></span>
            </label>
          </div>
          <div style="font-size: 12px; color: var(--dim); line-height: 1.5;">
            Kích hoạt mở khóa ngầm DLC Lò Rèn (Workshop) và các gói DLC trong game. Mặc định luôn <b>TẮT</b> khi vào web để bảo đảm an toàn trang bị. Phím tắt: <b>F5</b>.
          </div>
          <div style="margin-top: 10px; display: flex; align-items: center; justify-content: space-between;">
            <span class="status-badge" id="badgeDlc">Đang Tắt</span>
          </div>
        </section>

        <!-- MODULE 5: DETECTOR SHIELD -->
        <section class="card card-blue">
          <div class="card-header">
            <div class="card-title">
              <span class="card-icon">🔰</span>
              <span>Lá Chắn Chống Phát Hiện (Detector Shield — Phím F2)</span>
            </div>
            <label class="switch">
              <input type="checkbox" id="toggleShield" checked onchange="onToggleShield(this)">
              <span class="slider"></span>
            </label>
          </div>
          <div style="font-size: 12px; color: var(--dim); line-height: 1.5;">
            Vô hiệu hóa 3 bộ dò quét gian lận của game (Anti-Cheat Probes, Obscured Cheat, SpeedHack Handler). Luôn tự động <b>BẬT</b> khi mở để bảo vệ an toàn cho tài khoản. Phím tắt: <b>F2</b>.
          </div>
          <div style="margin-top: 10px;">
            <span class="status-badge live" id="badgeShield">Đang Bật (Bảo Vệ)</span>
          </div>
        </section>

        </div> <!-- END TAB 1: HELPER MODULES -->

        <!-- TAB 2: VIP MODULES (Hidden until authenticated) -->
        <div id="tabContentVip" style="display: none; flex-direction: column; gap: 14px;">
          
          <!-- VIP HEADER BANNER -->
          <div style="background: linear-gradient(135deg, rgba(210,153,34,0.18) 0%, rgba(245,158,11,0.08) 100%); border: 1px solid #d29922; border-radius: var(--radius-sm); padding: 12px 16px; display: flex; align-items: center; justify-content: space-between;">
            <div style="display: flex; align-items: center; gap: 10px;">
              <span style="font-size: 22px;">👑</span>
              <div>
                <b style="color: #fbbf24; font-size: 14px;">Khu Vực Can Thiệp VIP (Đã Xác Thực)</b>
                <div style="font-size: 12px; color: #d29922;">God Mode, Detector Shield, Tăng Sát Thương & Tốc Đánh</div>
              </div>
            </div>
            <button onclick="lockVip()" style="background: #21262d; border: 1px solid #f85149; color: #ff7b72; font-size: 11.5px; font-weight: 700; padding: 5px 12px; border-radius: 6px; cursor: pointer; transition: all 0.2s;" onmouseover="this.style.background='#da3633'; this.style.color='#fff';" onmouseout="this.style.background='#21262d'; this.style.color='#ff7b72';" title="Khóa lại ngay lập tức">
              🔒 Khóa Lại Tab
            </button>
          </div>

          <!-- VIP MODULE 1: COMBAT MULTIPLIERS -->
          <section class="card card-amber">
            <div class="card-header">
              <div class="card-title">
                <span class="card-icon">⚔️</span>
                <span>Chỉ Số Chiến Đấu (Combat Multipliers)</span>
              </div>
            </div>

            <!-- Damage Multiplier -->
            <div style="margin-bottom: 18px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="font-size: 13px; font-weight: 700; color: #f0f6fc;">Sát Thương Đầu Ra (Damage):</span>
                <span style="font-size: 14px; font-weight: 800; color: #fbbf24;" id="vipDmgVal">1.00x</span>
              </div>
              <div style="display: flex; align-items: center; gap: 12px;">
                <input type="range" id="vipDmgSlider" min="1" max="50" step="0.25" value="1" style="flex: 1; accent-color: #f59e0b;" oninput="onVipDmgSlider(this.value)" onchange="sendVipDmg(this.value)">
                <input type="number" id="vipDmgInput" class="num-input" value="1" min="1" max="1000" step="0.5" style="width: 70px;" onchange="sendVipDmg(this.value)">
              </div>
              <div style="display: flex; gap: 6px; margin-top: 8px; flex-wrap: wrap;">
                <button class="btn-preset" onclick="sendVipDmg(1)">1x (Chuẩn)</button>
                <button class="btn-preset" onclick="sendVipDmg(2)">2x</button>
                <button class="btn-preset" onclick="sendVipDmg(5)">5x</button>
                <button class="btn-preset" onclick="sendVipDmg(10)">10x</button>
                <button class="btn-preset" onclick="sendVipDmg(25)">25x</button>
                <button class="btn-preset" onclick="sendVipDmg(50)">50x</button>
              </div>
            </div>

            <!-- Attack Speed Multiplier -->
            <div>
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="font-size: 13px; font-weight: 700; color: #f0f6fc;">Tốc Độ Đánh (Attack Speed):</span>
                <span style="font-size: 14px; font-weight: 800; color: #38bdf8;" id="vipAspdVal">1.00x</span>
              </div>
              <div style="display: flex; align-items: center; gap: 12px;">
                <input type="range" id="vipAspdSlider" min="1" max="20" step="0.5" value="1" style="flex: 1; accent-color: #38bdf8;" oninput="onVipAspdSlider(this.value)" onchange="sendVipAspd(this.value)">
                <input type="number" id="vipAspdInput" class="num-input" value="1" min="1" max="20" step="0.5" style="width: 70px;" onchange="sendVipAspd(this.value)">
              </div>
              <div style="display: flex; gap: 6px; margin-top: 8px; flex-wrap: wrap;">
                <button class="btn-preset" onclick="sendVipAspd(1)">1x (Chuẩn)</button>
                <button class="btn-preset" onclick="sendVipAspd(1.5)">1.5x</button>
                <button class="btn-preset" onclick="sendVipAspd(2)">2x</button>
                <button class="btn-preset" onclick="sendVipAspd(3)">3x</button>
                <button class="btn-preset" onclick="sendVipAspd(5)">5x</button>
                <button class="btn-preset" onclick="sendVipAspd(10)">10x (Max)</button>
              </div>
            </div>
          </section>

          <!-- VIP MODULE 2: GOD MODE -->
          <section class="card card-emerald">
            <div class="card-header">
              <div class="card-title">
                <span class="card-icon">🛡️</span>
                <span>Bất Tử (God Mode — Phím F1)</span>
              </div>
              <label class="switch">
                <input type="checkbox" id="toggleGod" onchange="onToggleGod(this)">
                <span class="slider"></span>
              </label>
            </div>
            <div style="font-size: 12px; color: var(--dim); line-height: 1.5;">
              Miễn nhiễm hoàn toàn 100% mọi sát thương nhận vào từ quái vật và Boss. Có thể bật/tắt tức thì bằng phím <b>F1</b> trong game.
            </div>
            <div style="margin-top: 10px;">
              <span class="status-badge" id="badgeGod">Đang Tắt</span>
            </div>
          </section>

          <!-- VIP MODULE 3: EMERGENCY PANIC -->
          <section class="card card-purple">
            <div class="card-header">
              <div class="card-title">
                <span class="card-icon">🚨</span>
                <span>Khẩn Cấp & Đưa Về Chuẩn (Panic Reset)</span>
              </div>
            </div>
            <div style="display: flex; gap: 10px; flex-wrap: wrap;">
              <button class="btn-mini-action" style="background:#238636; border-color:#2ea043; color:#fff;" onclick="resetVipToNormal()">
                ⚡ Đưa Chỉ Số Về Chuẩn (1x Dmg / 1x Aspd)
              </button>
              <button class="btn-mini-action" style="background:#da3633; border-color:#f85149; color:#fff;" onclick="triggerPanic()">
                🚨 PANIC (F12) — Tắt Hết Mod Ngay
              </button>
            </div>
          </section>

        </div> <!-- END TAB 2: VIP MODULES -->

      </div>

      <!-- RIGHT: LOG COLUMN -->
      <div class="log-column">
        <div class="log-container">
          <div class="log-header">
            <div class="log-title">
              <span>📜</span>
              <span>Nhật Ký Hoạt Động Thời Gian Thực</span>
            </div>
            <button class="btn-clear-log" onclick="clearLog()">Xóa Log</button>
          </div>
          <div class="log-feed" id="logFeed">
            <div class="log-entry">
              <span class="log-time">[00:00:00]</span>
              <span class="log-tag tag-info">HỆ THỐNG</span>
              <span class="log-msg">Trình điều khiển DPS Auto Helper đã sẵn sàng. Đang kết nối tới game...</span>
            </div>
          </div>
        </div>
      </div>

    </div>
  </main>

  <!-- MODAL: VIP AUTHENTICATION -->
  <div class="modal-overlay" id="vipAuthModal" style="display:none;" onclick="if(event.target===this) closeVipModal()">
    <div class="modal-card" style="max-width: 440px;">
      <div class="modal-header" style="border-bottom: 1px solid rgba(245, 158, 11, 0.3);">
        <div class="modal-title" style="color: #fbbf24;">
          <span>👑</span>
          <span>Xác Thực Quyền Truy Cập VIP</span>
        </div>
        <button class="modal-close-btn" onclick="closeVipModal()">✕</button>
      </div>
      <div class="modal-body" style="text-align: center; padding: 24px 20px;">
        <div style="font-size: 40px; margin-bottom: 12px;">🔒</div>
        <div style="font-size: 15px; font-weight: 700; color: #f0f6fc; margin-bottom: 6px;">Khu Vực Tính Năng VIP</div>
        <div style="font-size: 13px; color: #8b949e; line-height: 1.5; margin-bottom: 20px;">
          Các tính năng can thiệp chuyên sâu (God Mode, Detector Shield, Tăng Sát Thương & Tốc Đánh) chỉ dành riêng cho VIP. Vui lòng nhập mã bảo vệ:
        </div>
        <div style="margin-bottom: 16px;">
          <input type="password" id="vipPinInput" placeholder="Nhập mã bí mật VIP..." style="width: 100%; padding: 12px 16px; background: #0d1117; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: 16px; text-align: center; letter-spacing: 2px; outline: none; transition: border-color 0.2s;" onkeydown="if(event.key==='Enter') submitVipPin()" onfocus="this.style.borderColor='#f59e0b'" onblur="this.style.borderColor='#30363d'">
        </div>
        <div id="vipAuthErr" style="display: none; color: #ff7b72; font-size: 13px; margin-bottom: 14px; font-weight: 600;">⚠️ Mã bảo mật không chính xác!</div>
        <div style="display: flex; gap: 10px; justify-content: center;">
          <button onclick="submitVipPin()" style="background: linear-gradient(180deg, #d29922 0%, #bb8009 100%); border: 1px solid #e3b341; color: #000; font-weight: 800; font-size: 13px; padding: 10px 24px; border-radius: 8px; cursor: pointer; box-shadow: 0 4px 14px rgba(210,153,34,0.3); transition: all 0.2s;" onmouseover="this.style.filter='brightness(1.15)'" onmouseout="this.style.filter=''">
            🔓 MỞ KHÓA VIP
          </button>
          <button onclick="closeVipModal()" style="background: #21262d; border: 1px solid #30363d; color: #c9d1d9; font-weight: 600; font-size: 13px; padding: 10px 18px; border-radius: 8px; cursor: pointer;">
            Đóng
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- MODAL: DOWNLOAD 1-CLICK -->
  <div class="modal-overlay" id="downloadModal" onclick="if(event.target===this) closeDownloadModal()">
    <div class="modal-card">
      <div class="modal-header">
        <div class="modal-title">
          <span>📦</span>
          <span>Tải Gói Tự Động 1–Click DPS Auto Helper</span>
        </div>
        <button class="modal-close-btn" onclick="closeDownloadModal()">✕</button>
      </div>
      <div class="modal-body">
        <div class="modal-dl-row">
          <div class="modal-dl-row-left">
            <div style="font-size: 32px;">📥</div>
            <div>
              <div style="font-weight: 700; font-size: 14px; color: #fff;">DPS_Auto_Helper_1Click.zip</div>
              <div style="font-size: 12px; color: var(--dim); margin-top: 3px;">Phiên bản mới nhất • Đầy đủ runtime • Kích thước: ~57 MB</div>
            </div>
          </div>
          <a href="https://github.com/titlee2111/dps-auto-helper/raw/main/DPS_Auto_Helper_1Click.zip" class="btn-download-rect" download>
            📥 TẢI FILE ZIP
          </a>
        </div>

        <div style="background: rgba(14, 165, 233, 0.08); border: 1px solid rgba(14, 165, 233, 0.25); border-radius: var(--radius-sm); padding: 14px 18px; font-size: 13px; line-height: 1.6; color: #bae6fd;">
          <div style="font-weight: 700; color: #38bdf8; margin-bottom: 6px;">📖 Hướng dẫn cài đặt siêu tốc:</div>
          <ol style="margin-left: 20px;">
            <li>Tải file ZIP về và giải nén ra bất kỳ đâu trên máy tính.</li>
            <li>Chạy file <b>Cai_Dat_1Click.bat</b> để công cụ tự nhận diện thư mục game Steam và cài đặt trong 2 giây.</li>
            <li>Khởi động game <b>DPS Desktop Pension Squad</b> trên Steam.</li>
            <li>Mở website bảng điều khiển: <a href="https://titlee2111.github.io/dps-auto-helper/" target="_blank" style="color:#38bdf8; text-decoration:underline; font-weight:bold;">https://titlee2111.github.io/dps-auto-helper/</a> để tự động kết nối và điều khiển game!</li>
          </ol>
        </div>
      </div>
    </div>
  </div>

  <!-- MODAL: BROWSER PERMISSION GUIDE -->
  <div id="permissionGuideModal" class="modal-overlay" style="display: none;" onclick="if(event.target === this) closePermissionModal()">
    <div class="modal-card" style="max-width: 660px; width: 95%; max-height: 92vh; overflow-y: auto;">
      <div class="modal-header">
        <div class="modal-title-wrap">
          <span class="modal-icon">⚡</span>
          <div class="modal-title">HƯỚNG DẪN KẾT NỐI: BẬT QUYỀN TRÌNH DUYỆT</div>
        </div>
        <button class="modal-close-btn" onclick="closePermissionModal()">✕</button>
      </div>
      <div class="modal-body" style="padding-top: 6px;">
        <p style="color: #94a3b8; font-size: 13px; line-height: 1.5; margin-bottom: 12px;">
          Nếu game đang chạy nhưng web báo <b style="color: #f87171;">"Chưa kết nối"</b> (do trình duyệt bảo mật khi web chạy trên HTTPS), bạn chỉ cần bật công tắc sau 1 lần duy nhất:
        </p>

        <div style="background: rgba(15, 23, 42, 0.75); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 10px; padding: 12px 16px; font-size: 13px; line-height: 1.7; color: #e2e8f0; margin-bottom: 14px;">
          <div style="margin-bottom: 6px;">
            <span style="display: inline-block; background: #2563eb; color: #fff; font-weight: bold; border-radius: 4px; padding: 1px 7px; font-size: 11px; margin-right: 6px;">BƯỚC 1</span>
            Nhấp vào biểu tượng <b>Cài đặt trang web</b> (icon nút gạt nhỏ ở đầu thanh địa chỉ web URL).
          </div>
          <div style="margin-bottom: 6px;">
            <span style="display: inline-block; background: #dc2626; color: #fff; font-weight: bold; border-radius: 4px; padding: 1px 7px; font-size: 11px; margin-right: 6px;">BƯỚC 2</span>
            Bật công tắc <b>"Ứng dụng trên thiết bị"</b> (hoặc <i>Insecure content / Local network</i>) sang màu <b>XANH (ON)</b>.
          </div>
          <div>
            <span style="display: inline-block; background: #10b981; color: #fff; font-weight: bold; border-radius: 4px; padding: 1px 7px; font-size: 11px; margin-right: 6px;">BƯỚC 3</span>
            Nhấn <b>F5 (Tải lại trang)</b>. Web sẽ tự động kết nối thành công tới game!
          </div>
        </div>

        <div style="text-align: center; margin-bottom: 14px;">
          <img src="data:image/png;base64,__GUIDE_IMG_B64__" alt="Hướng dẫn bật quyền trình duyệt" style="max-width: 100%; height: auto; border-radius: 8px; border: 1px solid rgba(255,255,255,0.2); box-shadow: 0 4px 20px rgba(0,0,0,0.5);">
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 14px; margin-top: 8px;">
          <label style="display: flex; align-items: center; gap: 8px; color: #cbd5e1; font-size: 13px; cursor: pointer; user-select: none;">
            <input type="checkbox" id="dontShowGuideAgain" style="width: 16px; height: 16px; accent-color: #38bdf8; cursor: pointer;">
            <span>Không hiển thị lại lần sau</span>
          </label>
          <button onclick="closePermissionModal()" style="background: #2563eb; color: #fff; border: none; border-radius: 8px; padding: 8px 18px; font-weight: 600; font-size: 13px; cursor: pointer;">
            Đã hiểu & Đóng
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- MODAL: DONATE / SUPPORT AUTHOR (Exact War of Genesis Structure) -->
  <div id="donateModal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.85); z-index:9999999; justify-content:center; align-items:center; padding:16px; backdrop-filter:blur(6px); -webkit-backdrop-filter:blur(6px);" onclick="if(event.target === this) closeDonateModal();">
    <div style="background:#161b22; border:1px solid #30363d; border-radius:14px; max-width:640px; width:100%; max-height:92vh; overflow-y:auto; box-shadow:0 20px 50px rgba(0,0,0,0.9); padding:24px; position:relative;">
      
      <!-- Modal Header -->
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #30363d; padding-bottom:14px; margin-bottom:16px;">
        <div style="display:flex; align-items:center; gap:10px;">
          <span style="font-size:26px;">☕</span>
          <div>
            <h3 style="margin:0; color:#e3b341; font-size:18px; display:flex; align-items:center; gap:8px;" id="donateModalTitle">
              Ủng Hộ Tác Giả / Support the Developer
            </h3>
            <div style="font-size:12px; color:#8b949e; margin-top:2px;" id="donateModalSubtitle">DPS Desktop Pension Squad Auto Helper — 100% Miễn Phí & Phi Lợi Nhuận</div>
          </div>
        </div>
        <button onclick="closeDonateModal()" style="background:transparent; border:none; color:#8b949e; font-size:22px; cursor:pointer; padding:4px 8px; border-radius:6px; line-height:1; transition:color 0.15s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#8b949e'">✕</button>
      </div>

      <!-- Heartfelt Message Box -->
      <div style="background:linear-gradient(135deg, rgba(227, 179, 65, 0.08) 0%, rgba(31, 111, 235, 0.08) 100%); border:1px solid rgba(227, 179, 65, 0.3); border-radius:10px; padding:14px 16px; margin-bottom:18px; font-size:13px; line-height:1.65; color:#c9d1d9;">
        <div style="font-weight:600; color:#f0f6fc; margin-bottom:6px; display:flex; align-items:center; gap:6px;">
          <span>💌</span> <span id="donateGreeting">Lời Nhắn Từ Tác Giả:</span>
        </div>
        <div id="donateLetterContent">
          Chào bạn! Cảm ơn bạn rất nhiều vì đã tin tưởng và đồng hành cùng <b>DPS Desktop Pension Squad Auto Helper</b>.<br>
          Dự án này được mình phát triển hoàn toàn tâm huyết và miễn phí nhằm mang lại những công cụ tiện ích nhất cho anh em cày game (tự động hợp thành đồ xưởng, tự động cất đồ vào kho, tự động mở rương báu và tối ưu hóa tài nguyên).<br>
          Nếu bạn cảm thấy Helper hữu ích và giúp bạn cắm máy rảnh tay hoặc săn được nhiều đồ giá trị, hãy ủng hộ mình một ly cà phê ☕ nhé! Mọi đóng góp dù lớn hay nhỏ đều là nguồn động lực to lớn giúp mình duy trì và hoàn thiện tool tốt hơn nữa. Cảm ơn bạn rất nhiều! ❤️
        </div>
      </div>

      <!-- Tab Switcher (Vietnam MB Bank vs Binance / International) -->
      <div style="display:flex; gap:8px; margin-bottom:16px; border-bottom:1px solid #30363d; padding-bottom:12px;">
        <button id="donateTabBtnMb" class="modal-tab-btn active" onclick="switchDonateTab('mb')">
          <span>🇻🇳</span> <span id="donateTabMbLabel">Ngân Hàng MB (Việt Nam)</span>
        </button>
        <button id="donateTabBtnBinance" class="modal-tab-btn" onclick="switchDonateTab('binance')">
          <span>🌐</span> <span id="donateTabBinanceLabel">Binance Pay</span>
        </button>
        <button id="donateTabBtnBmc" class="modal-tab-btn" onclick="switchDonateTab('bmc')">
          <span>☕</span> <span id="donateTabBmcLabel">Buy Me a Coffee</span>
        </button>
      </div>

      <!-- TAB 1: MB BANK (VIETQR) -->
      <div id="donateTabMb" style="display:block;">
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap:18px; align-items:center; background:#0d1117; border:1px solid #30363d; border-radius:12px; padding:16px;">
          <div style="text-align:center;">
            <img src="__MB_QR__" alt="MB Bank QR" style="width:190px; height:190px; object-fit:contain; background:#fff; padding:6px; border-radius:8px; box-shadow:0 4px 14px rgba(0,0,0,0.5); border:1px solid #30363d; display:inline-block;">
            <div id="donateMbQrSub" style="font-size:11px; color:#8b949e; margin-top:6px;">📲 Quét bằng ứng dụng Ngân hàng bất kỳ</div>
          </div>
          <div style="display:flex; flex-direction:column; gap:10px; font-size:13px;">
            <div>
              <div style="color:#8b949e; font-size:11.5px; margin-bottom:2px;">NGÂN HÀNG (BANK)</div>
              <div style="font-weight:bold; color:#f0f6fc; display:flex; align-items:center; justify-content:space-between; background:#161b22; padding:6px 10px; border-radius:6px; border:1px solid #30363d;">
                <span>MB Bank (Ngân Hàng Quân Đội)</span>
              </div>
            </div>
            <div>
              <div style="color:#8b949e; font-size:11.5px; margin-bottom:2px;">SỐ TÀI KHOẢN (ACCOUNT NUMBER)</div>
              <div style="font-weight:bold; color:#7ee787; font-size:15px; letter-spacing:0.5px; display:flex; align-items:center; justify-content:space-between; background:#161b22; padding:6px 10px; border-radius:6px; border:1px solid #30363d;">
                <span id="mbAccNum">0562462346</span>
                <button class="small-copy-btn" onclick="copyDonateText('0562462346', this)" style="background:#238636; color:#fff;">📋 Sao chép</button>
              </div>
            </div>
            <div>
              <div style="color:#8b949e; font-size:11.5px; margin-bottom:2px;">CHỦ TÀI KHOẢN (ACCOUNT HOLDER)</div>
              <div style="font-weight:bold; color:#58a6ff; display:flex; align-items:center; justify-content:space-between; background:#161b22; padding:6px 10px; border-radius:6px; border:1px solid #30363d;">
                <span>LY THAI SON</span>
                <button class="small-copy-btn" onclick="copyDonateText('LY THAI SON', this)" style="background:#30363d; color:#c9d1d9;">📋 Sao chép</button>
              </div>
            </div>
            <div>
              <div style="color:#8b949e; font-size:11.5px; margin-bottom:2px;">LỜI NHẮN (NOTE)</div>
              <div id="donateMbNoteText" style="color:#e3b341; font-style:italic; font-size:12px; background:#161b22; padding:6px 10px; border-radius:6px; border:1px solid #30363d; display:flex; align-items:center; justify-content:space-between;">
                <span>Ủng hộ DPS Helper</span>
                <button class="small-copy-btn" onclick="copyDonateText('Ung ho DPS Helper', this)" style="background:#30363d; color:#c9d1d9;">📋 Sao chép</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 2: BINANCE PAY (INTERNATIONAL) -->
      <div id="donateTabBinance" style="display:none;">
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap:18px; align-items:center; background:#0d1117; border:1px solid #30363d; border-radius:12px; padding:16px;">
          <div style="text-align:center;">
            <img src="__BINANCE_QR__" alt="Binance Pay QR" style="width:190px; height:190px; object-fit:contain; background:#fff; padding:6px; border-radius:8px; box-shadow:0 4px 14px rgba(0,0,0,0.5); border:1px solid #30363d; display:inline-block;">
            <div id="donateBinanceQrSub" style="font-size:11px; color:#8b949e; margin-top:6px;">📲 Quét bằng App Binance (Binance Pay)</div>
          </div>
          <div style="display:flex; flex-direction:column; gap:10px; font-size:13px;">
            <div>
              <div style="color:#8b949e; font-size:11.5px; margin-bottom:2px;">NỀN TẢNG (PLATFORM)</div>
              <div style="font-weight:bold; color:#f0f6fc; display:flex; align-items:center; justify-content:space-between; background:#161b22; padding:6px 10px; border-radius:6px; border:1px solid #30363d;">
                <span style="color:#f0b90b; font-weight:bold;">🔶 Binance Pay (Crypto)</span>
              </div>
            </div>
            <div>
              <div style="color:#8b949e; font-size:11.5px; margin-bottom:2px;">BINANCE PAY ID / USERNAME</div>
              <div style="font-weight:bold; color:#f0b90b; font-size:15px; letter-spacing:0.5px; display:flex; align-items:center; justify-content:space-between; background:#161b22; padding:6px 10px; border-radius:6px; border:1px solid #30363d;">
                <span id="binanceUser">User-9e11c</span>
                <button class="small-copy-btn" onclick="copyDonateText('User-9e11c', this)" style="background:#f0b90b; color:#0d1117; font-weight:bold;">📋 Sao chép</button>
              </div>
            </div>
            <div>
              <div style="color:#8b949e; font-size:11.5px; margin-bottom:2px;">TIỀN TỆ HỖ TRỢ (SUPPORTED COINS)</div>
              <div style="color:#c9d1d9; font-size:12px; background:#161b22; padding:6px 10px; border-radius:6px; border:1px solid #30363d;">
                USDT, BUSD, BNB, BTC, ETH... (0% phí nội bộ Binance)
              </div>
            </div>
            <div>
              <div style="color:#8b949e; font-size:11.5px; margin-bottom:2px;">HƯỚNG DẪN NHANH (HOW TO PAY)</div>
              <div id="donateBinanceGuide" style="color:#8b949e; font-size:11.5px; background:#161b22; padding:6px 10px; border-radius:6px; border:1px solid #30363d; line-height:1.5;">
                Mở App Binance ➔ Bấm biểu tượng <b>Pay</b> hoặc <b>Quét mã QR</b> góc trên màn hình ➔ Quét mã hoặc nhập Pay ID: <b>User-9e11c</b>.
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 3: BUY ME A COFFEE (GLOBAL) -->
      <div id="donateTabBmc" style="display:none;">
        <div style="background:#0d1117; border:1px solid #30363d; border-radius:12px; padding:28px 20px; text-align:center;">
          <div style="font-size:46px; margin-bottom:10px;">☕</div>
          <div id="donateBmcTitle" style="font-weight:bold; color:#f0f6fc; font-size:16px; margin-bottom:6px;">Buy Me a Coffee</div>
          <div id="donateBmcDesc" style="font-size:12.5px; color:#8b949e; margin-bottom:18px; line-height:1.5;">Ủng hộ tác giả qua Buy Me a Coffee — hỗ trợ thẻ quốc tế & PayPal, không cần tài khoản game.</div>
          <a id="donateBmcLink" href="https://buymeacoffee.com/titlee" target="_blank" rel="noopener noreferrer" style="display:inline-block; background:#FFDD00; color:#0d1117; font-weight:bold; padding:12px 30px; border-radius:26px; text-decoration:none; font-size:14.5px; letter-spacing:0.3px; box-shadow:0 4px 14px rgba(255,221,0,0.25); transition:transform 0.15s ease;" onmouseover="this.style.transform='scale(1.04)'" onmouseout="this.style.transform=''">☕ buymeacoffee.com/titlee</a>
          <div id="donateBmcGuide" style="font-size:11.5px; color:#8b949e; margin-top:14px; line-height:1.5;">Bấm nút phía trên để mở trang Buy Me a Coffee trong tab mới →</div>
        </div>
      </div>

      <!-- Modal Footer -->
      <div style="display:flex; justify-content:space-between; align-items:center; margin-top:20px; padding-top:14px; border-top:1px solid #30363d;">
        <div id="donateFooterWish" style="font-size:12px; color:#8b949e;">
          🌟 Chúc bạn chơi game vui vẻ & săn được nhiều đồ giá trị!
        </div>
        <button id="donateCloseBtn" onclick="closeDonateModal()" style="padding:8px 22px; background:#30363d; color:#f0f6fc; border-radius:6px; font-size:13px; cursor:pointer; font-weight:bold; border:none; transition:background 0.2s;" onmouseover="this.style.background='#444c56'" onmouseout="this.style.background='#30363d'">
          Đóng
        </button>
      </div>

    </div>
  </div>

  <!-- FLOATING DISCORD CIRCLE BUTTON -->
  <a href="https://discord.gg/RuHaQU22K" target="_blank" rel="noopener noreferrer" class="discord-float" title="Tham gia Discord Hỗ Trợ & Giao Lưu">
    <svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor">
      <path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028 14.09 14.09 0 0 0 1.226-1.994.076.076 0 0 0-.041-.106 13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.929 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.894.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/>
    </svg>
    <span class="discord-tooltip">Tham gia Discord Hỗ Trợ</span>
  </a>

  <!-- FOOTER -->
  <footer>
    DPS Desktop Pension Squad Auto Helper
  </footer>

  <!-- JAVASCRIPT LOGIC -->
  <script>
    let API_BASE = (window.location.protocol.startsWith('http') && window.location.port) ? '' : 'http://127.0.0.1:47900';
    const PROBE_PORTS = [47900, 47901, 47902, 47903, 47904, 47905];
    let isConnected = false;
    let initialSyncDone = false;
    let lastBoxCount = 0;
    let lastStashStep = 0;
    let lastStashCurr = 0;

    // Default settings (Detector Shield always ON by default for safety, DLC OFF, Multipliers 1x)
    const defaultSettings = {
      auto_comb: 0,
      auto_stash: 0,
      auto_box: 1,
      dlc: 0,
      god: 0,
      shield: 1,
      vip_dmg: 1,
      vip_aspd: 1,
      comb_min: 5,
      stash_sec: 60,
      stash_start: 1,
      stash_end: 5,
      box_interval: 1.5
    };

    // Load persisted settings from localStorage
    function loadSavedSettings() {
      const saved = localStorage.getItem('dps_settings');
      if (!saved) {
        return { ...defaultSettings };
      }
      try {
        const parsed = JSON.parse(saved);
        parsed.stash_start = Math.max(1, Math.min(8, parseInt(parsed.stash_start) || 1));
        parsed.stash_end = Math.max(parsed.stash_start, Math.min(8, parseInt(parsed.stash_end) || 5));
        parsed.vip_dmg = Math.max(1, Math.min(1000, parseFloat(parsed.vip_dmg) || 1));
        parsed.vip_aspd = Math.max(1, Math.min(20, parseFloat(parsed.vip_aspd) || 1));
        parsed.shield = parsed.shield !== undefined ? (parsed.shield ? 1 : 0) : 1;
        parsed.dlc = parsed.dlc ? 1 : 0;
        parsed.god = parsed.god ? 1 : 0;
        const merged = { ...defaultSettings, ...parsed };
        return merged;
      } catch (e) {
        return { ...defaultSettings };
      }
    }

    function saveSettings(settings) {
      try {
        localStorage.setItem('dps_settings', JSON.stringify(settings));
      } catch (e) {}
    }

    let userSettings = loadSavedSettings();

    // VIP State & Auth
    let isVipUnlocked = (localStorage.getItem('dps_vip_unlocked') === '1');
    let currentMainTab = 'helper';

    function initVipState() {
      const lockBadge = document.getElementById('vipLockBadge');
      if (isVipUnlocked) {
        if (lockBadge) {
          lockBadge.innerText = '🔓 Đã mở';
          lockBadge.className = 'vip-lock-badge unlocked';
        }
      } else {
        if (lockBadge) {
          lockBadge.innerText = '🔒 Khóa';
          lockBadge.className = 'vip-lock-badge';
        }
      }
    }

    function switchMainTab(tab) {
      if (tab === 'vip' && !isVipUnlocked) {
        openVipModal();
        return;
      }
      currentMainTab = tab;
      const btnHelper = document.getElementById('btnTabHelper');
      const btnVip = document.getElementById('btnTabVip');
      const contentHelper = document.getElementById('tabContentHelper');
      const contentVip = document.getElementById('tabContentVip');

      if (tab === 'helper') {
        if (btnHelper) btnHelper.classList.add('active');
        if (btnVip) btnVip.classList.remove('active');
        if (contentHelper) contentHelper.style.display = 'flex';
        if (contentVip) contentVip.style.display = 'none';
      } else if (tab === 'vip') {
        if (btnHelper) btnHelper.classList.remove('active');
        if (btnVip) btnVip.classList.add('active');
        if (contentHelper) contentHelper.style.display = 'none';
        if (contentVip) contentVip.style.display = 'flex';
      }
    }

    function openVipModal() {
      const modal = document.getElementById('vipAuthModal');
      const input = document.getElementById('vipPinInput');
      const err = document.getElementById('vipAuthErr');
      if (err) err.style.display = 'none';
      if (input) input.value = '';
      if (modal) modal.style.display = 'flex';
      setTimeout(() => { if (input) input.focus(); }, 100);
    }

    function closeVipModal() {
      const modal = document.getElementById('vipAuthModal');
      if (modal) modal.style.display = 'none';
    }

    function submitVipPin() {
      const input = document.getElementById('vipPinInput');
      const err = document.getElementById('vipAuthErr');
      if (!input) return;
      const val = input.value.trim().toLowerCase();
      if (val === 'son' || val === '2111' || val === 'vip2111' || val === 'admin') {
        isVipUnlocked = true;
        localStorage.setItem('dps_vip_unlocked', '1');
        initVipState();
        closeVipModal();
        switchMainTab('vip');
        addLog('VIP ACCESS', 'Xác thực quyền VIP thành công! Đã mở khóa toàn bộ bảng can thiệp.', 'ok');
      } else {
        if (err) {
          err.innerText = '⚠️ Mật mã VIP không chính xác! Vui lòng thử lại.';
          err.style.display = 'block';
        }
      }
    }

    function lockVip() {
      isVipUnlocked = false;
      localStorage.removeItem('dps_vip_unlocked');
      initVipState();
      switchMainTab('helper');
      addLog('VIP ACCESS', 'Đã khóa lại Tab VIP an toàn.', 'warn');
    }

    // VIP Combat Multipliers
    function onVipDmgSlider(val) {
      document.getElementById('vipDmgVal').innerText = Number(val).toFixed(2) + 'x';
      document.getElementById('vipDmgInput').value = val;
    }

    async function sendVipDmg(val) {
      const num = Math.max(1, parseFloat(val) || 1);
      userSettings.vip_dmg = num;
      saveSettings(userSettings);
      document.getElementById('vipDmgVal').innerText = num.toFixed(2) + 'x';
      document.getElementById('vipDmgSlider').value = Math.min(50, num);
      document.getElementById('vipDmgInput').value = num;
      addLog('CHỈ SỐ VIP', `Đang thiết lập Sát thương x${num} (đã lưu)...`, 'info');
      try {
        const res = await fetch(`${API_BASE}/set?dmg=${num}`);
        if (res.ok) {
          addLog('CHỈ SỐ VIP', `Đã áp dụng Sát thương x${num} thành công!`, 'ok');
          updateStatus(await res.json());
        }
      } catch (e) {
        addLog('LỖI KẾT NỐI', 'Không thể áp dụng chỉ số sát thương.', 'err');
      }
    }

    function onVipAspdSlider(val) {
      document.getElementById('vipAspdVal').innerText = Number(val).toFixed(2) + 'x';
      document.getElementById('vipAspdInput').value = val;
    }

    async function sendVipAspd(val) {
      const num = Math.max(1, parseFloat(val) || 1);
      userSettings.vip_aspd = num;
      saveSettings(userSettings);
      document.getElementById('vipAspdVal').innerText = num.toFixed(2) + 'x';
      document.getElementById('vipAspdSlider').value = Math.min(20, num);
      document.getElementById('vipAspdInput').value = num;
      addLog('CHỈ SỐ VIP', `Đang thiết lập Tốc độ đánh x${num} (đã lưu)...`, 'info');
      try {
        const res = await fetch(`${API_BASE}/set?aspd=${num}`);
        if (res.ok) {
          addLog('CHỈ SỐ VIP', `Đã áp dụng Tốc đánh x${num} thành công!`, 'ok');
          updateStatus(await res.json());
        }
      } catch (e) {
        addLog('LỖI KẾT NỐI', 'Không thể áp dụng chỉ số tốc đánh.', 'err');
      }
    }

    async function onToggleGod(el) {
      const val = el.checked ? 1 : 0;
      userSettings.god = val;
      saveSettings(userSettings);
      updateBadge('badgeGod', val, 'ĐANG BẬT BẤT TỬ', 'Đang Tắt');
      addLog('GOD MODE (F1)', el.checked ? 'ĐÃ BẬT Bất tử (Miễn nhiễm sát thương 100% - đã lưu cho phiên sau)!' : 'Đã TẮT Bất tử.', el.checked ? 'ok' : 'warn');
      try {
        const res = await fetch(`${API_BASE}/set?god=${val}`);
        if (res.ok) updateStatus(await res.json());
      } catch (e) {
        addLog('LỖI KẾT NỐI', 'Không thể đổi trạng thái God Mode.', 'err');
      }
    }

    async function onToggleShield(el) {
      const val = el.checked ? 1 : 0;
      userSettings.shield = val;
      saveSettings(userSettings);
      updateBadge('badgeShield', val, 'ĐANG BẬT BẢO VỆ', 'Đang Tắt (Nguy hiểm)');
      addLog('LÁ CHẮN (F2)', el.checked ? 'ĐÃ BẬT Lá chắn chống phát hiện (đã lưu cho phiên sau)!' : 'ĐÃ TẮT Lá chắn (Cảnh báo: Anti-cheat game có thể quét)!', el.checked ? 'ok' : 'err');
      try {
        const res = await fetch(`${API_BASE}/set?shield=${val}`);
        if (res.ok) updateStatus(await res.json());
      } catch (e) {
        addLog('LỖI KẾT NỐI', 'Không thể đổi trạng thái Lá chắn.', 'err');
      }
    }

    async function resetVipToNormal() {
      addLog('CHỈ SỐ VIP', 'Đang đưa các chỉ số về chuẩn (1x Sát thương, 1x Tốc đánh)...', 'info');
      userSettings.vip_dmg = 1;
      userSettings.vip_aspd = 1;
      saveSettings(userSettings);
      await sendVipDmg(1);
      await sendVipAspd(1);
    }

    async function triggerPanic() {
      addLog('PANIC (F12)', 'Đang gửi lệnh khẩn cấp Panic (Tắt God Mode, reset chỉ số)...', 'warn');
      userSettings.god = 0;
      userSettings.vip_dmg = 1;
      userSettings.vip_aspd = 1;
      saveSettings(userSettings);
      applySettingsToUI();
      try {
        await fetch(`${API_BASE}/set?god=0`);
        await fetch(`${API_BASE}/set?dmg=1`);
        await fetch(`${API_BASE}/set?aspd=1`);
        addLog('PANIC', 'Đã vô hiệu hóa toàn bộ can thiệp chiến đấu khẩn cấp!', 'ok');
        fetchStatus();
      } catch (e) {}
    }

    // Apply loaded settings to UI immediately (all OFF by default unless user turned ON before)
    function applySettingsToUI() {
      document.getElementById('toggleCombine').checked = !!userSettings.auto_comb;
      updateBadge('badgeCombine', userSettings.auto_comb, `Đang Bật (${userSettings.comb_min}p)`, 'Đang Tắt');

      document.getElementById('toggleStash').checked = !!userSettings.auto_stash;
      updateBadge('badgeStash', userSettings.auto_stash, `Đang Bật (${userSettings.stash_sec}s)`, 'Đang Tắt');

      document.getElementById('toggleAutoBox').checked = !!userSettings.auto_box;
      updateBadge('badgeAutoBox', userSettings.auto_box, `Đang Bật (${userSettings.box_interval}s)`, 'Đang Tắt');

      document.getElementById('toggleDlc').checked = !!userSettings.dlc;
      updateBadge('badgeDlc', userSettings.dlc, 'ĐÃ KÍCH HOẠT', 'Đang Tắt');

      const tShield = document.getElementById('toggleShield');
      if (tShield) tShield.checked = !!userSettings.shield;
      updateBadge('badgeShield', userSettings.shield, 'ĐANG BẬT BẢO VỆ', 'Đang Tắt (Nguy hiểm)');

      const tGod = document.getElementById('toggleGod');
      if (tGod) tGod.checked = !!userSettings.god;
      updateBadge('badgeGod', userSettings.god, 'ĐANG BẬT BẤT TỬ', 'Đang Tắt');

      const dVal = userSettings.vip_dmg || 1;
      const dSlider = document.getElementById('vipDmgSlider');
      const dInput = document.getElementById('vipDmgInput');
      const dText = document.getElementById('vipDmgVal');
      if (dText) dText.innerText = Number(dVal).toFixed(2) + 'x';
      if (dSlider) dSlider.value = Math.min(50, dVal);
      if (dInput) dInput.value = dVal;

      const aVal = userSettings.vip_aspd || 1;
      const aSlider = document.getElementById('vipAspdSlider');
      const aInput = document.getElementById('vipAspdInput');
      const aText = document.getElementById('vipAspdVal');
      if (aText) aText.innerText = Number(aVal).toFixed(2) + 'x';
      if (aSlider) aSlider.value = Math.min(20, aVal);
      if (aInput) aInput.value = aVal;

      document.getElementById('combineInterval').value = userSettings.comb_min;
      document.getElementById('stashInterval').value = userSettings.stash_sec;
      document.getElementById('stashStart').value = userSettings.stash_start;
      document.getElementById('stashEnd').value = userSettings.stash_end;
      document.getElementById('boxInterval').value = userSettings.box_interval;
    }

    function updateBadge(id, isActive, onText, offText) {
      const el = document.getElementById(id);
      if (!el) return;
      if (!isConnected) {
        el.className = 'status-badge';
        el.innerText = 'Chưa kết nối';
        return;
      }
      el.className = isActive ? 'status-badge active' : 'status-badge';
      el.innerText = isActive ? onText : offText;
    }

    // Toast & Modals
    function openDownloadModal() {
      document.getElementById('downloadModal').style.display = 'flex';
    }
    function closeDownloadModal() {
      document.getElementById('downloadModal').style.display = 'none';
    }
    function openDonateModal() {
      document.getElementById('donateModal').style.display = 'flex';
    }
    function closeDonateModal() {
      document.getElementById('donateModal').style.display = 'none';
    }
    function dismissAlert() {
      const el = document.getElementById('topAlert');
      if (el) el.style.display = 'none';
    }

    function openPermissionModal() {
      const modal = document.getElementById('permissionGuideModal');
      const chk = document.getElementById('dontShowGuideAgain');
      if (chk) {
        chk.checked = (localStorage.getItem('dps_hide_permission_modal') === '1');
      }
      if (modal) modal.style.display = 'flex';
    }

    function closePermissionModal() {
      const modal = document.getElementById('permissionGuideModal');
      const chk = document.getElementById('dontShowGuideAgain');
      if (chk && chk.checked) {
        localStorage.setItem('dps_hide_permission_modal', '1');
      } else {
        localStorage.removeItem('dps_hide_permission_modal');
      }
      if (modal) modal.style.display = 'none';
    }

    function switchDonateTab(tab) {
      const tabMb = document.getElementById('donateTabMb');
      const tabBinance = document.getElementById('donateTabBinance');
      const tabBmc = document.getElementById('donateTabBmc');
      const btnMb = document.getElementById('donateTabBtnMb');
      const btnBinance = document.getElementById('donateTabBtnBinance');
      const btnBmc = document.getElementById('donateTabBtnBmc');

      if (tab === 'mb') {
        if (tabMb) tabMb.style.display = 'block';
        if (tabBinance) tabBinance.style.display = 'none';
        if (tabBmc) tabBmc.style.display = 'none';
        if (btnMb) btnMb.classList.add('active');
        if (btnBinance) btnBinance.classList.remove('active');
        if (btnBmc) btnBmc.classList.remove('active');
      } else if (tab === 'binance') {
        if (tabMb) tabMb.style.display = 'none';
        if (tabBinance) tabBinance.style.display = 'block';
        if (tabBmc) tabBmc.style.display = 'none';
        if (btnMb) btnMb.classList.remove('active');
        if (btnBinance) btnBinance.classList.add('active');
        if (btnBmc) btnBmc.classList.remove('active');
      } else if (tab === 'bmc') {
        if (tabMb) tabMb.style.display = 'none';
        if (tabBinance) tabBinance.style.display = 'none';
        if (tabBmc) tabBmc.style.display = 'block';
        if (btnMb) btnMb.classList.remove('active');
        if (btnBinance) btnBinance.classList.remove('active');
        if (btnBmc) btnBmc.classList.add('active');
      }
    }

    function copyDonateText(text, btn) {
      function showSuccess() {
        if (!btn) return;
        const oldHtml = btn.innerHTML;
        btn.innerHTML = '✅ Đã chép!';
        btn.style.filter = 'brightness(1.2)';
        setTimeout(function() {
          btn.innerHTML = oldHtml;
          btn.style.filter = '';
        }, 2000);
      }

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(showSuccess).catch(function() {
          fallbackCopyText(text, showSuccess);
        });
      } else {
        fallbackCopyText(text, showSuccess);
      }
    }

    function fallbackCopyText(text, cb) {
      const ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      try {
        document.execCommand('copy');
        if (cb) cb();
      } catch (e) {
        prompt('Copy thủ công tại đây:', text);
      }
      document.body.removeChild(ta);
    }

    // Logger
    function addLog(tag, msg, type = 'info') {
      const feed = document.getElementById('logFeed');
      if (!feed) return;
      const now = new Date();
      const timeStr = `[${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}:${String(now.getSeconds()).padStart(2, '0')}]`;
      
      const entry = document.createElement('div');
      entry.className = 'log-entry';
      entry.innerHTML = `
        <span class="log-time">${timeStr}</span>
        <span class="log-tag tag-${type}">${tag}</span>
        <span class="log-msg">${msg}</span>
      `;
      feed.appendChild(entry);
      feed.scrollTop = feed.scrollHeight;
    }

    function clearLog() {
      const feed = document.getElementById('logFeed');
      if (feed) feed.innerHTML = '';
      addLog('HỆ THỐNG', 'Đã xóa toàn bộ nhật ký.', 'info');
    }

    // Sync saved settings to game upon first connect
    async function syncSavedSettingsToGame() {
      addLog('ĐỒNG BỘ', 'Đang đồng bộ cấu hình đã lưu (mặc định tắt nếu chưa bật) vào game...', 'info');
      try {
        await fetch(`${API_BASE}/set?auto_comb=${userSettings.auto_comb}`);
        await fetch(`${API_BASE}/set?comb_min=${userSettings.comb_min}`);
        await fetch(`${API_BASE}/set?auto_stash=${userSettings.auto_stash}`);
        await fetch(`${API_BASE}/set?stash_sec=${userSettings.stash_sec}`);
        await fetch(`${API_BASE}/set?stash_start=${userSettings.stash_start}`);
        await fetch(`${API_BASE}/set?stash_end=${userSettings.stash_end}`);
        await fetch(`${API_BASE}/set?auto=${userSettings.auto_box}`);
        await fetch(`${API_BASE}/set?dlc=${userSettings.dlc !== undefined ? userSettings.dlc : 0}`);
        await fetch(`${API_BASE}/set?god=${userSettings.god !== undefined ? userSettings.god : 0}`);
        await fetch(`${API_BASE}/set?shield=${userSettings.shield !== undefined ? userSettings.shield : 1}`);
        await fetch(`${API_BASE}/set?dmg=${userSettings.vip_dmg || 1}`);
        await fetch(`${API_BASE}/set?aspd=${userSettings.vip_aspd || 1}`);
        addLog('ĐỒNG BỘ', 'Đồng bộ cấu hình phiên trước thành công!', 'ok');
      } catch (err) {
        addLog('ĐỒNG BỘ', 'Lỗi đồng bộ cấu hình vào game.', 'err');
      }
    }

    // UI Updates from Game Status
    function updateStatus(data) {
      const wasConnected = isConnected;
      isConnected = true;

      // First time connecting in this browser session
      if (!wasConnected) {
        addLog('KẾT NỐI', `Đã kết nối thành công tới game DPS (PID: ${data.pid || '--'})`, 'ok');
        if (!initialSyncDone) {
          initialSyncDone = true;
          syncSavedSettingsToGame();
        }
      }

      // Header Chips
      const statusChip = document.getElementById('statusChip');
      const statusText = document.getElementById('statusText');
      statusChip.className = 'chip status-live';
      statusText.innerText = 'Đã kết nối game';




      const pidVal = document.getElementById('pidVal');
      if (pidVal && data.pid) pidVal.innerText = data.pid;

      // Top Center HUD Updates
      if (data.soul !== undefined) {
        document.getElementById('hudSoul').innerText = Number(data.soul).toLocaleString();
      }
      if (data.soul_stone !== undefined) {
        document.getElementById('hudSoulStone').innerText = Number(data.soul_stone).toLocaleString();
      }

      // Capacity Calculations & Display
      const capBox = document.getElementById('capacityBox');
      const capPlaceholder = document.getElementById('capacityPlaceholder');
      if (capBox) capBox.style.display = 'flex';
      if (capPlaceholder) capPlaceholder.style.display = 'none';

      const invOcc = data.inv_occupied || 0;
      const invCap = data.inv_capacity || 0;
      const stoOcc = data.storage_occupied || 0;
      const stoCap = data.storage_capacity || 0;
      const totalOcc = data.total_occupied !== undefined ? data.total_occupied : (invOcc + stoOcc);
      const totalCap = data.total_capacity !== undefined ? data.total_capacity : (invCap + stoCap);
      const capPercent = totalCap > 0 ? Math.round((totalOcc / totalCap) * 100) : 0;

      // Update Top HUD Capacity & Module 2 Details
      if (totalCap > 0) {
        document.getElementById('hudCap').innerText = `${totalOcc} / ${totalCap}`;
        document.getElementById('hudCapBar').style.width = `${Math.min(100, capPercent)}%`;
        document.getElementById('capStat').innerText = `${totalOcc} / ${totalCap} slot (${capPercent}%)`;
        document.getElementById('capBar').style.width = `${Math.min(100, capPercent)}%`;
        document.getElementById('invStat').innerText = `${invOcc} / ${invCap}`;
        document.getElementById('storageStat').innerText = `${stoOcc} / ${stoCap}`;
        document.getElementById('capPercent').innerText = `${capPercent}%`;
      } else {
        document.getElementById('hudCap').innerText = `-- / --`;
        document.getElementById('hudCapBar').style.width = `0%`;
        document.getElementById('capStat').innerText = `Đang kết nối dữ liệu kho game...`;
        document.getElementById('capBar').style.width = `0%`;
        document.getElementById('invStat').innerText = `-- / --`;
        document.getElementById('storageStat').innerText = `-- / --`;
        document.getElementById('capPercent').innerText = `0%`;
      }

      // Color coding for capacity bar
      const bar = document.getElementById('capBar');
      if (bar) {
        if (capPercent >= 90) bar.style.background = '#ef4444';
        else if (capPercent >= 75) bar.style.background = '#f59e0b';
        else bar.style.background = '#10b981';
      }

      // Module 1: Combine
      if (data.auto_comb !== undefined) {
        document.getElementById('toggleCombine').checked = !!data.auto_comb;
        updateBadge('badgeCombine', data.auto_comb, `Đang Bật (${data.comb_min || userSettings.comb_min}p)`, 'Đang Tắt');
      }

      // Module 2: Stash
      if (data.auto_stash !== undefined) {
        document.getElementById('toggleStash').checked = !!data.auto_stash;
        updateBadge('badgeStash', data.auto_stash, `Đang Bật (${data.stash_sec || userSettings.stash_sec}s)`, 'Đang Tắt');
      }

      // Sync Stash range from game if inputs are not actively being edited
      const sInput = document.getElementById('stashStart');
      const eInput = document.getElementById('stashEnd');
      if (data.stash_start !== undefined && sInput && document.activeElement !== sInput) {
        if (parseInt(sInput.value) !== data.stash_start) {
          sInput.value = data.stash_start;
          userSettings.stash_start = data.stash_start;
        }
      }
      if (data.stash_end !== undefined && eInput && document.activeElement !== eInput) {
        if (parseInt(eInput.value) !== data.stash_end) {
          eInput.value = data.stash_end;
          userSettings.stash_end = data.stash_end;
          saveSettings(userSettings);
        }
      }

      // Realtime Stash progress logging in the web console
      if (data.stash_step !== undefined) {
        if (data.stash_step === 1) {
          if (data.stash_curr !== undefined && data.stash_curr !== lastStashCurr && data.stash_curr > 0) {
            addLog('CẤT ĐỒ', `Đang cất đồ vào Kho ${data.stash_curr} / ${data.stash_end || userSettings.stash_end}...`, 'info');
            lastStashCurr = data.stash_curr;
          }
        } else if (data.stash_step === 0 && lastStashStep === 1) {
          addLog('CẤT ĐỒ', `Đã cất đồ xong toàn bộ (Kho ${data.stash_start || userSettings.stash_start} đến Kho ${data.stash_end || userSettings.stash_end})!`, 'ok');
          lastStashCurr = 0;
        }
        lastStashStep = data.stash_step;
      }

      // Module 3: Auto Box
      if (data.auto !== undefined) {
        document.getElementById('toggleAutoBox').checked = !!data.auto;
        updateBadge('badgeAutoBox', data.auto, `Đang Bật (${userSettings.box_interval}s)`, 'Đang Tắt');
      }
      if (data.box_count !== undefined) {
        document.getElementById('boxCountVal').innerText = `${data.box_count} Rương`;
        if (data.box_count !== lastBoxCount && data.box_count > 0) {
          addLog('RƯƠNG BÁU', `Phát hiện ${data.box_count} rương báu trên sàn đấu.`, 'box');
        }
        lastBoxCount = data.box_count;
      }

      // Module 4: DLC Toggle
      if (data.dlc !== undefined) {
        document.getElementById('toggleDlc').checked = !!data.dlc;
        updateBadge('badgeDlc', data.dlc, 'ĐÃ KÍCH HOẠT', 'Đang Tắt');
      }

      // VIP Combat Stats
      if (data.dmg !== undefined) {
        document.getElementById('vipDmgVal').innerText = Number(data.dmg).toFixed(2) + 'x';
        const slider = document.getElementById('vipDmgSlider');
        const input = document.getElementById('vipDmgInput');
        if (slider && document.activeElement !== slider) slider.value = Math.min(50, Number(data.dmg));
        if (input && document.activeElement !== input) input.value = Number(data.dmg);
      }
      if (data.aspd !== undefined) {
        document.getElementById('vipAspdVal').innerText = Number(data.aspd).toFixed(2) + 'x';
        const slider = document.getElementById('vipAspdSlider');
        const input = document.getElementById('vipAspdInput');
        if (slider && document.activeElement !== slider) slider.value = Math.min(20, Number(data.aspd));
        if (input && document.activeElement !== input) input.value = Number(data.aspd);
      }
      if (data.god !== undefined) {
        document.getElementById('toggleGod').checked = !!data.god;
        updateBadge('badgeGod', data.god, 'ĐANG BẬT BẤT TỬ', 'Đang Tắt');
      }
      if (data.shield !== undefined) {
        document.getElementById('toggleShield').checked = !!data.shield;
        updateBadge('badgeShield', data.shield, 'ĐANG BẬT BẢO VỆ', 'Đang Tắt (Nguy hiểm)');
      }

      // Sync and persist any updates triggered directly in game via hotkeys
      let needSave = false;
      if (data.dlc !== undefined && userSettings.dlc !== data.dlc) {
        userSettings.dlc = data.dlc;
        needSave = true;
      }
      if (data.god !== undefined && userSettings.god !== data.god) {
        userSettings.god = data.god;
        needSave = true;
      }
      if (data.shield !== undefined && userSettings.shield !== data.shield) {
        userSettings.shield = data.shield;
        needSave = true;
      }
      if (data.dmg !== undefined && userSettings.vip_dmg !== data.dmg) {
        userSettings.vip_dmg = data.dmg;
        needSave = true;
      }
      if (data.aspd !== undefined && userSettings.vip_aspd !== data.aspd) {
        userSettings.vip_aspd = data.aspd;
        needSave = true;
      }
      if (needSave) {
        saveSettings(userSettings);
      }
    }

    function setDisconnected() {
      if (isConnected) {
        addLog('MẤT KẾT NỐI', 'Không thể kết nối tới game. Vui lòng kiểm tra game đã bật chưa.', 'err');
      }
      isConnected = false;
      const statusChip = document.getElementById('statusChip');
      const statusText = document.getElementById('statusText');
      if (statusChip) statusChip.className = 'chip status-dead';
      if (statusText) statusText.innerText = 'Chưa kết nối game';

      const pidVal = document.getElementById('pidVal');
      if (pidVal) pidVal.innerText = '--';

      // Reset Top HUD
      document.getElementById('hudSoul').innerText = '--';
      document.getElementById('hudSoulStone').innerText = '--';
      document.getElementById('hudCap').innerText = '-- / --';
      document.getElementById('hudCapBar').style.width = '0%';

      // Hide capacity box, show placeholder
      const capBox = document.getElementById('capacityBox');
      const capPlaceholder = document.getElementById('capacityPlaceholder');
      if (capBox) capBox.style.display = 'none';
      if (capPlaceholder) capPlaceholder.style.display = 'block';

      // Badges
      ['badgeCombine', 'badgeStash', 'badgeAutoBox', 'badgeDlc', 'badgeGod', 'badgeShield'].forEach(id => {
        const el = document.getElementById(id);
        if (el) {
          el.className = 'status-badge';
          el.innerText = 'Chưa kết nối';
        }
      });

      if (window.location.protocol === 'https:' && localStorage.getItem('dps_hide_permission_modal') !== '1' && !window._hasAutoPromptedGuide) {
        window._hasAutoPromptedGuide = true;
        setTimeout(openPermissionModal, 1500);
      }

    }

    // Polling API with multi-port probe
    async function fetchStatus() {
      try {
        const res = await fetch(`${API_BASE}/status`, { signal: AbortSignal.timeout(2000) });
        if (res.ok) {
          const data = await res.json();
          updateStatus(data);
          return;
        }
      } catch (e) {
        // Fallback auto-probe for port range
        if (API_BASE.startsWith('http://127.0.0.1')) {
          for (const p of PROBE_PORTS) {
            try {
              const probeUrl = `http://127.0.0.1:${p}`;
              const probeRes = await fetch(`${probeUrl}/status`, { signal: AbortSignal.timeout(600) });
              if (probeRes.ok) {
                API_BASE = probeUrl;
                const data = await probeRes.json();
                updateStatus(data);
                return;
              }
            } catch (err) {}
          }
        }
      }
      setDisconnected();
    }

    // User Interactive Actions & Toggles
    async function triggerCombine() {
      addLog('THỦ CÔNG', 'Đang gửi lệnh Ghép đồ xưởng ngay...', 'info');
      try {
        const res = await fetch(`${API_BASE}/set?combine=1`);
        if (res.ok) {
          addLog('THÀNH CÔNG', 'Đã kích hoạt ghép đồ xưởng thành công!', 'ok');
          const data = await res.json();
          updateStatus(data);
        } else {
          addLog('LỖI', 'Lệnh ghép đồ thất bại.', 'err');
        }
      } catch (e) {
        addLog('LỖI KẾT NỐI', 'Không thể gửi lệnh tới game.', 'err');
      }
    }

    async function triggerStash() {
      addLog('THỦ CÔNG', 'Đang gửi lệnh Cất đồ vào kho ngay...', 'info');
      try {
        const res = await fetch(`${API_BASE}/set?stash=1`);
        if (res.ok) {
          addLog('THÀNH CÔNG', 'Đã cất đồ vào kho thành công!', 'ok');
          const data = await res.json();
          updateStatus(data);
        } else {
          addLog('LỖI', 'Lệnh cất đồ thất bại.', 'err');
        }
      } catch (e) {
        addLog('LỖI KẾT NỐI', 'Không thể gửi lệnh tới game.', 'err');
      }
    }

    async function onToggleCombine(el) {
      const val = el.checked ? 1 : 0;
      userSettings.auto_comb = val;
      saveSettings(userSettings);
      updateBadge('badgeCombine', val, `Đang Bật (${userSettings.comb_min}p)`, 'Đang Tắt');
      addLog('HỢP THÀNH', el.checked ? 'Đã BẬT tự động ghép đồ (đã lưu cho phiên sau).' : 'Đã TẮT tự động ghép đồ.', el.checked ? 'ok' : 'warn');
      try {
        const res = await fetch(`${API_BASE}/set?auto_comb=${val}`);
        if (res.ok) updateStatus(await res.json());
      } catch (err) {}
    }

    async function updateCombineInterval() {
      const input = document.getElementById('combineInterval');
      if (!input) return;
      const val = Math.max(1, parseInt(input.value) || 5);
      userSettings.comb_min = val;
      saveSettings(userSettings);
      addLog('CẤU HÌNH', `Đã đổi chu kỳ ghép đồ thành ${val} phút (đã lưu).`, 'info');
      try {
        const res = await fetch(`${API_BASE}/set?comb_min=${val}`);
        if (res.ok) updateStatus(await res.json());
      } catch (err) {}
    }

    async function onToggleStash(el) {
      const val = el.checked ? 1 : 0;
      userSettings.auto_stash = val;
      saveSettings(userSettings);
      updateBadge('badgeStash', val, `Đang Bật (${userSettings.stash_sec}s)`, 'Đang Tắt');
      addLog('CẤT ĐỒ', el.checked ? 'Đã BẬT tự động cất đồ (đã lưu cho phiên sau).' : 'Đã TẮT tự động cất đồ.', el.checked ? 'ok' : 'warn');
      try {
        const res = await fetch(`${API_BASE}/set?auto_stash=${val}`);
        if (res.ok) updateStatus(await res.json());
      } catch (err) {}
    }

    async function updateStashInterval() {
      const input = document.getElementById('stashInterval');
      if (!input) return;
      const val = Math.max(5, parseInt(input.value) || 60);
      userSettings.stash_sec = val;
      saveSettings(userSettings);
      addLog('CẤU HÌNH', `Đã đổi chu kỳ cất đồ thành ${val} giây (đã lưu).`, 'info');
      try {
        const res = await fetch(`${API_BASE}/set?stash_sec=${val}`);
        if (res.ok) updateStatus(await res.json());
      } catch (err) {}
    }

    async function updateStashTabs() {
      const sInput = document.getElementById('stashStart');
      const eInput = document.getElementById('stashEnd');
      if (!sInput || !eInput) return;
      const start = Math.max(1, parseInt(sInput.value) || 1);
      const end = Math.min(8, Math.max(start, parseInt(eInput.value) || 5));
      eInput.value = end;
      userSettings.stash_start = start;
      userSettings.stash_end = end;
      saveSettings(userSettings);
      addLog('CẤU HÌNH', `Đã đổi phạm vi cất đồ: Kho ${start} đến Kho ${end} (đã lưu).`, 'info');
      if (end > 5) {
        addLog('CẢNH BÁO', 'Kho 6, 7, 8 là các kho từ gói DLC StoragePack. Nếu tài khoản chưa sở hữu DLC này trên Steam, máy chủ sẽ tự động xóa vật phẩm khi đồng bộ!', 'warn');
      }
      try {
        await fetch(`${API_BASE}/set?stash_start=${start}`);
        const res = await fetch(`${API_BASE}/set?stash_end=${end}`);
        if (res.ok) updateStatus(await res.json());
      } catch (err) {}
    }

    async function onToggleAutoBox(el) {
      const val = el.checked ? 1 : 0;
      userSettings.auto_box = val;
      saveSettings(userSettings);
      updateBadge('badgeAutoBox', val, `Đang Bật (${userSettings.box_interval}s)`, 'Đang Tắt');
      addLog('MỞ RƯƠNG', el.checked ? 'Đã BẬT tự động mở rương rơi (đã lưu cho phiên sau).' : 'Đã TẮT tự động mở rương.', el.checked ? 'box' : 'warn');
      try {
        const res = await fetch(`${API_BASE}/set?auto=${val}`);
        if (res.ok) updateStatus(await res.json());
      } catch (err) {}
    }

    async function updateBoxInterval() {
      const input = document.getElementById('boxInterval');
      if (!input) return;
      const val = Math.max(1, parseInt(input.value) || 3);
      userSettings.box_interval = val;
      saveSettings(userSettings);
      addLog('CẤU HÌNH', `Đã đổi chu kỳ kiểm tra rương thành ${val} giây (đã lưu).`, 'info');
    }

    async function onToggleDlc(el) {
      const val = el.checked ? 1 : 0;
      userSettings.dlc = val;
      saveSettings(userSettings);
      updateBadge('badgeDlc', val, 'ĐÃ KÍCH HOẠT', 'Đang Tắt');
      addLog('DLC UNLOCK', el.checked ? 'ĐÃ KÍCH HOẠT Mở Khóa DLC Lò Rèn ngầm (đã lưu).' : 'Đã TẮT Mở Khóa DLC (về nguyên bản).', el.checked ? 'warn' : 'info');
      try {
        const res = await fetch(`${API_BASE}/set?dlc=${val}`);
        if (res.ok) updateStatus(await res.json());
      } catch (err) {}
    }

    // Initialize UI from local storage
    applySettingsToUI();
    initVipState();

    // Start polling
    fetchStatus();
    setInterval(fetchStatus, 2000);
  </script>
</body>
</html>
"""

final_html = (html_template
  .replace("__B64_ICON__", b64_icon)
  .replace("__SOUL_ICON_B64__", b64_soul)
  .replace("__GEM_ICON_B64__", b64_gem)
  .replace("__GUIDE_IMG_B64__", b64_guide)
  .replace("__MB_QR__", mb_qr_src)
  .replace("__BINANCE_QR__", binance_qr_src))

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Generated {HTML_FILE} ({len(final_html)} bytes)")
