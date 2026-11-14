import os

BASE_DIR = r"C:\Users\Son\Desktop\dps-auto-helper"
ICON_B64_FILE = os.path.join(BASE_DIR, "game_icon_b64.txt")
QR0_FILE = os.path.join(BASE_DIR, "qr_0.txt")
QR1_FILE = os.path.join(BASE_DIR, "qr_1.txt")
HTML_FILE = os.path.join(BASE_DIR, "index.html")

with open(ICON_B64_FILE, "r", encoding="utf-8") as f:
    b64_icon = f.read().strip()

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
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=JetBrains+Mono:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #07090e;
      --bg-card: rgba(13, 18, 28, 0.82);
      --line: #1e293b;
      --ink: #f8fafc;
      --dim: #94a3b8;
      --dimmer: #64748b;

      /* Vibrant Neon Color Accents */
      --cyan: #06b6d4;
      --cyan-glow: rgba(6, 182, 212, 0.45);
      --cyan-border: rgba(6, 182, 212, 0.35);

      --emerald: #10b981;
      --emerald-glow: rgba(16, 185, 129, 0.45);
      --emerald-border: rgba(16, 185, 129, 0.35);

      --purple: #a855f7;
      --purple-glow: rgba(168, 85, 247, 0.45);
      --purple-border: rgba(168, 85, 247, 0.35);

      --amber: #f59e0b;
      --amber-glow: rgba(245, 158, 11, 0.45);
      --amber-border: rgba(245, 158, 11, 0.35);

      --rose: #f43f5e;
      --blue: #3b82f6;

      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 18px;
      --radius-full: 9999px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    
    body {
      background: var(--bg);
      background-image: 
        radial-gradient(circle at 10% 10%, rgba(6, 182, 212, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 90% 15%, rgba(168, 85, 247, 0.14) 0%, transparent 45%),
        radial-gradient(circle at 50% 85%, rgba(16, 185, 129, 0.10) 0%, transparent 50%),
        linear-gradient(180deg, #07090e 0%, #0c101a 50%, #06080d 100%);
      background-attachment: fixed;
      color: var(--ink);
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      width: 100%;
      overflow-x: hidden;
    }

    /* ==================== HEADER ==================== */
    header {
      background: rgba(11, 15, 25, 0.92);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding: 12px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 24px rgba(0, 0, 0, 0.5), inset 0 -1px 0 rgba(6, 182, 212, 0.2);
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
      box-shadow: 0 0 20px rgba(6, 182, 212, 0.5);
      border: 2px solid #06b6d4;
      object-fit: cover;
      background: #141c2b;
      display: block;
      transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .game-logo:hover {
      transform: scale(1.08) rotate(-3deg);
      box-shadow: 0 0 28px rgba(6, 182, 212, 0.8);
    }
    .brand-titles {
      display: flex;
      flex-direction: column;
    }
    .brand-titles h1 {
      font-size: 15px;
      font-weight: 800;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      background: linear-gradient(90deg, #ffffff 0%, #38bdf8 60%, #a855f7 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      line-height: 1.2;
    }
    .brand-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      color: #06b6d4;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      margin-top: 2px;
      text-shadow: 0 0 8px rgba(6, 182, 212, 0.5);
    }

    /* ==================== CENTER HUD BAR ==================== */
    .header-hud {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      flex-wrap: wrap;
      background: linear-gradient(135deg, rgba(16, 22, 36, 0.95) 0%, rgba(22, 30, 48, 0.85) 100%);
      border: 1px solid rgba(6, 182, 212, 0.35);
      border-radius: var(--radius-full);
      padding: 6px 20px;
      box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.15), 0 0 24px rgba(6, 182, 212, 0.15), 0 6px 20px rgba(0, 0, 0, 0.4);
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
      font-size: 18px;
      display: flex;
      align-items: center;
      justify-content: center;
      filter: drop-shadow(0 0 8px currentColor);
    }
    .hud-soul .hud-icon { color: #c084fc; }
    .hud-stone .hud-icon { color: #38bdf8; }
    .hud-cap .hud-icon { color: #34d399; }

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
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
      color: #fff;
      letter-spacing: 0.02em;
    }
    .hud-soul .hud-val { color: #e879f9; text-shadow: 0 0 12px rgba(232, 121, 249, 0.6); }
    .hud-stone .hud-val { color: #38bdf8; text-shadow: 0 0 12px rgba(56, 189, 248, 0.6); }
    .hud-cap .hud-val { color: #34d399; text-shadow: 0 0 12px rgba(52, 211, 153, 0.5); }

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
      background: linear-gradient(90deg, #10b981, #06b6d4);
      border-radius: var(--radius-full);
      transition: width 0.4s ease;
      box-shadow: 0 0 8px rgba(16, 185, 129, 0.6);
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
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.18) 0%, rgba(6, 182, 212, 0.12) 100%);
      color: #34d399;
      border-color: rgba(16, 185, 129, 0.5);
      box-shadow: 0 0 18px rgba(16, 185, 129, 0.35);
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
      box-shadow: 0 0 10px currentColor;
      animation: pulse 1.6s infinite;
    }

    /* Donate Button */
    .btn-donate-gold {
      background: linear-gradient(135deg, #f59e0b 0%, #d97706 60%, #b45309 100%);
      color: #fff;
      font-size: 12px;
      font-weight: 800;
      padding: 7px 16px;
      border-radius: var(--radius-full);
      border: 1px solid #fbbf24;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
      box-shadow: 0 0 18px rgba(245, 158, 11, 0.45);
      transition: all 0.25s ease;
    }
    .btn-donate-gold:hover {
      background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 60%, #d97706 100%);
      box-shadow: 0 0 28px rgba(245, 158, 11, 0.7);
      transform: translateY(-2px) scale(1.03);
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
      background: linear-gradient(90deg, rgba(245, 158, 11, 0.12) 0%, rgba(217, 119, 6, 0.08) 100%);
      border: 1px solid rgba(245, 158, 11, 0.35);
      border-radius: var(--radius-md);
      padding: 12px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      box-shadow: 0 4px 16px rgba(245, 158, 11, 0.12);
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
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.3) 0%, rgba(217, 119, 6, 0.4) 100%);
      border: 1px solid #f59e0b;
      color: #fff;
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
      box-shadow: 0 0 12px rgba(245, 158, 11, 0.25);
    }
    .alert-banner-btn:hover {
      background: #f59e0b;
      color: #000;
      box-shadow: 0 0 20px rgba(245, 158, 11, 0.5);
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

    /* Vibrant Horizontal Download Bar */
    .download-strip {
      background: linear-gradient(90deg, rgba(16, 25, 42, 0.95) 0%, rgba(24, 18, 38, 0.95) 100%);
      border: 1px solid rgba(6, 182, 212, 0.4);
      border-radius: var(--radius-md);
      padding: 16px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.1);
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
      background: linear-gradient(135deg, rgba(6, 182, 212, 0.25) 0%, rgba(168, 85, 247, 0.25) 100%);
      border: 1px solid #06b6d4;
      color: #38bdf8;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
      flex-shrink: 0;
      box-shadow: 0 0 18px rgba(6, 182, 212, 0.4);
    }
    .download-strip-text h3 {
      font-size: 14.5px;
      font-weight: 800;
      background: linear-gradient(90deg, #fff 0%, #38bdf8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      letter-spacing: 0.03em;
    }
    .download-strip-text p {
      font-size: 12px;
      color: var(--dim);
      margin-top: 3px;
    }
    .btn-download-trigger {
      background: linear-gradient(135deg, #0284c7 0%, #2563eb 50%, #7c3aed 100%);
      color: #fff;
      font-size: 13px;
      font-weight: 800;
      padding: 10px 22px;
      border-radius: var(--radius-sm);
      border: 1px solid #38bdf8;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 0 20px rgba(56, 189, 248, 0.45);
      transition: all 0.25s ease;
    }
    .btn-download-trigger:hover {
      background: linear-gradient(135deg, #38bdf8 0%, #3b82f6 50%, #a855f7 100%);
      box-shadow: 0 0 30px rgba(56, 189, 248, 0.7);
      transform: translateY(-2px);
    }

    /* Top Mini Action Bar */
    .mini-actions-bar {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }
    .btn-mini-action {
      background: linear-gradient(135deg, rgba(20, 28, 44, 0.9) 0%, rgba(15, 23, 36, 0.9) 100%);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #e2e8f0;
      font-size: 12px;
      font-weight: 700;
      padding: 8px 16px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      transition: all 0.2s ease;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    .btn-mini-action.btn-mini-comb:hover {
      background: linear-gradient(135deg, rgba(6, 182, 212, 0.2) 0%, rgba(37, 99, 235, 0.25) 100%);
      border-color: #06b6d4;
      color: #38bdf8;
      box-shadow: 0 0 16px rgba(6, 182, 212, 0.4);
      transform: translateY(-1px);
    }
    .btn-mini-action.btn-mini-stash:hover {
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.2) 0%, rgba(5, 150, 105, 0.25) 100%);
      border-color: #10b981;
      color: #34d399;
      box-shadow: 0 0 16px rgba(16, 185, 129, 0.4);
      transform: translateY(-1px);
    }

    /* ==================== SPLIT LAYOUT ==================== */
    .split-layout {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 24px;
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
      gap: 20px;
    }

    .log-column {
      display: flex;
      flex-direction: column;
      gap: 16px;
      position: sticky;
      top: 80px;
      height: calc(100vh - 120px);
      min-height: 520px;
    }
    @media (max-width: 1024px) {
      .log-column {
        position: static;
        height: 480px;
      }
    }

    /* ==================== VIBRANT CARD SYSTEM ==================== */
    .card {
      background: var(--bg-card);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-radius: var(--radius-lg);
      padding: 24px;
      box-shadow: 0 10px 32px rgba(0, 0, 0, 0.45);
      position: relative;
      border: 1px solid var(--card-border);
      transition: all 0.25s ease;
      overflow: hidden;
    }
    .card::before {
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 2px;
      background: var(--card-top-glow, transparent);
      opacity: 0.8;
    }
    .card:hover {
      transform: translateY(-2px);
      box-shadow: 0 14px 40px rgba(0, 0, 0, 0.6);
    }

    /* THEME 1: COMBINE (Electric Cyan) */
    .card-cyan {
      --card-border: var(--cyan-border);
      --card-top-glow: linear-gradient(90deg, transparent, #06b6d4, transparent);
    }
    .card-cyan:hover {
      border-color: #06b6d4;
      box-shadow: 0 10px 36px rgba(6, 182, 212, 0.25);
    }
    .card-cyan .card-title {
      color: #38bdf8;
      text-shadow: 0 0 12px rgba(6, 182, 212, 0.4);
    }

    /* THEME 2: STASH (Neon Emerald) */
    .card-emerald {
      --card-border: var(--emerald-border);
      --card-top-glow: linear-gradient(90deg, transparent, #10b981, transparent);
    }
    .card-emerald:hover {
      border-color: #10b981;
      box-shadow: 0 10px 36px rgba(16, 185, 129, 0.25);
    }
    .card-emerald .card-title {
      color: #34d399;
      text-shadow: 0 0 12px rgba(16, 185, 129, 0.4);
    }

    /* THEME 3: AUTO BOX (Vivid Violet / Magenta) */
    .card-purple {
      --card-border: var(--purple-border);
      --card-top-glow: linear-gradient(90deg, transparent, #a855f7, transparent);
    }
    .card-purple:hover {
      border-color: #a855f7;
      box-shadow: 0 10px 36px rgba(168, 85, 247, 0.25);
    }
    .card-purple .card-title {
      color: #c084fc;
      text-shadow: 0 0 12px rgba(168, 85, 247, 0.4);
    }

    /* THEME 4: DLC FORGE (Radiant Amber / Gold) */
    .card-amber {
      --card-border: var(--amber-border);
      --card-top-glow: linear-gradient(90deg, transparent, #f59e0b, transparent);
      background: linear-gradient(180deg, rgba(28, 22, 14, 0.85) 0%, rgba(18, 14, 10, 0.85) 100%);
    }
    .card-amber:hover {
      border-color: #f59e0b;
      box-shadow: 0 10px 36px rgba(245, 158, 11, 0.25);
    }
    .card-amber .card-title {
      color: #fbbf24;
      text-shadow: 0 0 12px rgba(245, 158, 11, 0.4);
    }

    .card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 16px;
      gap: 12px;
    }
    .card-title {
      font-size: 14.5px;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 9px;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }
    .card-icon {
      font-size: 20px;
    }
    .status-badge {
      font-size: 11px;
      font-weight: 800;
      padding: 4px 12px;
      border-radius: var(--radius-full);
      background: #141b2a;
      color: var(--dimmer);
      border: 1px solid rgba(255, 255, 255, 0.08);
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }
    .status-badge.active {
      background: rgba(16, 185, 129, 0.2);
      color: #34d399;
      border-color: #10b981;
      box-shadow: 0 0 14px rgba(16, 185, 129, 0.5);
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
      font-weight: 700;
      color: #f1f5f9;
    }
    .form-sublabel {
      font-size: 12px;
      color: var(--dim);
      margin-top: 3px;
    }

    /* Switch - Glowing Theme Adaptation */
    .switch {
      position: relative;
      display: inline-block;
      width: 50px;
      height: 28px;
      flex-shrink: 0;
    }
    .switch input { opacity: 0; width: 0; height: 0; }
    .slider {
      position: absolute;
      cursor: pointer;
      top: 0; left: 0; right: 0; bottom: 0;
      background-color: #1e293b;
      transition: .25s cubic-bezier(0.4, 0, 0.2, 1);
      border-radius: 34px;
      border: 1px solid rgba(255, 255, 255, 0.12);
    }
    .slider:before {
      position: absolute;
      content: "";
      height: 20px;
      width: 20px;
      left: 3px;
      bottom: 3px;
      background-color: #94a3b8;
      transition: .25s cubic-bezier(0.4, 0, 0.2, 1);
      border-radius: 50%;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
    }
    input:checked + .slider {
      background-color: #06b6d4;
      border-color: #38bdf8;
      box-shadow: 0 0 16px rgba(6, 182, 212, 0.6);
    }
    .card-emerald input:checked + .slider {
      background-color: #10b981;
      border-color: #34d399;
      box-shadow: 0 0 16px rgba(16, 185, 129, 0.6);
    }
    .card-purple input:checked + .slider {
      background-color: #a855f7;
      border-color: #c084fc;
      box-shadow: 0 0 16px rgba(168, 85, 247, 0.6);
    }
    .card-amber input:checked + .slider {
      background-color: #f59e0b;
      border-color: #fbbf24;
      box-shadow: 0 0 16px rgba(245, 158, 11, 0.6);
    }
    input:checked + .slider:before {
      transform: translateX(22px);
      background-color: #ffffff;
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
      background: #151d2e;
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #fff;
      font-size: 13.5px;
      font-weight: 800;
      padding: 5px 8px;
      border-radius: var(--radius-sm);
      text-align: center;
      outline: none;
      font-family: 'JetBrains Mono', monospace;
      transition: all 0.2s;
    }
    .num-input:focus {
      border-color: #06b6d4;
      box-shadow: 0 0 12px rgba(6, 182, 212, 0.5);
    }
    .config-unit {
      font-size: 12px;
      color: var(--dimmer);
    }

    /* Capacity Progress Box */
    .capacity-box {
      background: linear-gradient(135deg, rgba(14, 24, 38, 0.8) 0%, rgba(10, 18, 28, 0.9) 100%);
      border: 1px solid rgba(16, 185, 129, 0.3);
      border-radius: var(--radius-md);
      padding: 14px 16px;
      margin-top: 14px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      box-shadow: 0 4px 18px rgba(0, 0, 0, 0.35);
    }
    .capacity-placeholder {
      background: rgba(14, 20, 32, 0.6);
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
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .cap-stat {
      color: #34d399;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
      text-shadow: 0 0 10px rgba(52, 211, 153, 0.5);
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
      background: linear-gradient(90deg, #10b981 0%, #06b6d4 100%);
      border-radius: var(--radius-full);
      transition: width 0.4s ease, background 0.4s ease;
      box-shadow: 0 0 10px rgba(16, 185, 129, 0.6);
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
      font-family: 'JetBrains Mono', monospace;
    }

    /* DLC Warning */
    .dlc-warning-box {
      background: rgba(245, 158, 11, 0.12);
      border: 1px solid rgba(245, 158, 11, 0.4);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      font-size: 12.5px;
      line-height: 1.5;
      color: #fde68a;
      margin-bottom: 14px;
    }
    .dlc-warning-title {
      font-weight: 800;
      color: #fbbf24;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .dlc-warning-highlight {
      margin-top: 8px;
      padding: 8px 12px;
      background: rgba(239, 68, 68, 0.2);
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
      font-size: 14px;
      font-weight: 800;
      color: #fff;
    }
    .dlc-toggle-desc {
      font-size: 12px;
      color: var(--dim);
      margin-top: 3px;
    }

    .box-count-badge {
      background: linear-gradient(135deg, rgba(168, 85, 247, 0.2) 0%, rgba(236, 72, 153, 0.2) 100%);
      color: #e879f9;
      border: 1px solid rgba(236, 72, 153, 0.4);
      font-size: 12px;
      font-weight: 800;
      padding: 4px 12px;
      border-radius: var(--radius-full);
      font-family: 'JetBrains Mono', monospace;
      box-shadow: 0 0 12px rgba(236, 72, 153, 0.3);
    }

    /* ==================== REALTIME LOG BOX ==================== */
    .log-container {
      background: rgba(8, 12, 20, 0.95);
      border: 1px solid rgba(6, 182, 212, 0.25);
      border-radius: var(--radius-lg);
      display: flex;
      flex-direction: column;
      flex: 1;
      overflow: hidden;
      box-shadow: 0 10px 36px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.08);
    }
    .log-header {
      padding: 14px 20px;
      background: linear-gradient(90deg, #0e1524 0%, #131b2e 100%);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .log-title {
      font-size: 13px;
      font-weight: 800;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 8px;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      text-shadow: 0 0 10px rgba(56, 189, 248, 0.5);
    }
    .btn-clear-log {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: var(--dim);
      font-size: 11px;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: all 0.2s;
    }
    .btn-clear-log:hover {
      color: #fff;
      border-color: #06b6d4;
      background: rgba(6, 182, 212, 0.2);
    }
    .log-feed {
      flex: 1;
      padding: 16px;
      overflow-y: auto;
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      line-height: 1.65;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .log-feed::-webkit-scrollbar {
      width: 6px;
    }
    .log-feed::-webkit-scrollbar-thumb {
      background: rgba(6, 182, 212, 0.3);
      border-radius: 3px;
    }
    .log-entry {
      display: flex;
      align-items: flex-start;
      gap: 8px;
      animation: fadeIn 0.15s ease-in;
    }
    .log-time {
      color: var(--dimmer);
      flex-shrink: 0;
      font-size: 11px;
    }
    .log-tag {
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 10px;
      font-weight: 800;
      flex-shrink: 0;
      letter-spacing: 0.04em;
    }
    .log-tag.tag-ok { background: rgba(16, 185, 129, 0.25); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); }
    .log-tag.tag-info { background: rgba(6, 182, 212, 0.25); color: #38bdf8; border: 1px solid rgba(6, 182, 212, 0.4); }
    .log-tag.tag-warn { background: rgba(245, 158, 11, 0.25); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.4); }
    .log-tag.tag-err { background: rgba(239, 68, 68, 0.25); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.4); }
    .log-tag.tag-box { background: rgba(168, 85, 247, 0.25); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.4); }
    .log-msg {
      color: #cbd5e1;
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
      background: rgba(4, 7, 14, 0.88);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      z-index: 9999;
      align-items: center;
      justify-content: center;
      padding: 20px;
      animation: fadeIn 0.2s ease;
    }
    .modal-card {
      background: #0f1624;
      border: 1px solid rgba(6, 182, 212, 0.35);
      border-radius: var(--radius-lg);
      width: 100%;
      max-width: 720px;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      box-shadow: 0 10px 50px rgba(0, 0, 0, 0.8), 0 0 30px rgba(6, 182, 212, 0.2);
      overflow: hidden;
    }
    .modal-header {
      padding: 16px 24px;
      background: #141d30;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .modal-title {
      font-size: 16px;
      font-weight: 800;
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
      background: #151e30;
      border: 1px solid rgba(6, 182, 212, 0.3);
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
      font-weight: 800;
      padding: 11px 24px;
      border-radius: var(--radius-sm);
      border: 1px solid #34d399;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 0 20px rgba(16, 185, 129, 0.5);
      transition: all 0.25s ease;
      white-space: nowrap;
    }
    .btn-download-rect:hover {
      background: linear-gradient(135deg, #34d399 0%, #10b981 100%);
      box-shadow: 0 0 30px rgba(16, 185, 129, 0.8);
      transform: translateY(-2px);
    }

    .donate-tabs {
      display: flex;
      gap: 8px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 12px;
    }
    .donate-tab-btn {
      background: #141c2c;
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: var(--dim);
      font-size: 13px;
      font-weight: 700;
      padding: 8px 16px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: all 0.2s;
    }
    .donate-tab-btn.active {
      background: #0284c7;
      border-color: #38bdf8;
      color: #fff;
      box-shadow: 0 0 14px rgba(56, 189, 248, 0.4);
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
      border: 2px solid rgba(255, 255, 255, 0.15);
      background: #fff;
      padding: 6px;
    }
    .copy-pill {
      background: #162032;
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
      width: 54px;
      height: 54px;
      border-radius: 50%;
      background: #5865F2;
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 24px rgba(88, 101, 242, 0.55);
      border: 2px solid rgba(255, 255, 255, 0.3);
      z-index: 990;
      cursor: pointer;
      transition: all 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      text-decoration: none;
    }
    .discord-float:hover {
      transform: scale(1.12) translateY(-4px);
      box-shadow: 0 8px 30px rgba(88, 101, 242, 0.85);
    }
    .discord-tooltip {
      position: absolute;
      right: 66px;
      background: #1e1f22;
      color: #dbdee1;
      font-size: 12px;
      font-weight: 700;
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
      border-top: 1px solid rgba(255, 255, 255, 0.08);
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

    <!-- CENTER HUD: Soul, Soul Stone, Dung Lượng Kho (Removed Box Widget) -->
    <div class="header-hud">
      <div class="hud-item hud-soul" title="Linh Hồn Nhân Vật">
        <div class="hud-icon">🟣</div>
        <div class="hud-info">
          <span class="hud-label">Linh Hồn</span>
          <span class="hud-val" id="hudSoul">--</span>
        </div>
      </div>
      
      <div class="hud-item hud-stone" title="Đá Linh Hồn">
        <div class="hud-icon">💎</div>
        <div class="hud-info">
          <span class="hud-label">Đá Linh Hồn</span>
          <span class="hud-val" id="hudSoulStone">--</span>
        </div>
      </div>

      <div class="hud-item hud-cap" title="Tổng Dung Lượng Túi & Kho Đồ">
        <div class="hud-icon">🎒</div>
        <div class="hud-info">
          <span class="hud-label">Dung Lượng Kho</span>
          <span class="hud-val" id="hudCapacity">-- / --</span>
        </div>
        <div class="hud-mini-bar">
          <div class="hud-mini-fill" id="hudCapacityFill" style="width: 0%"></div>
        </div>
      </div>
    </div>

    <!-- RIGHT STATUS -->
    <div class="header-status">
      <button class="btn-donate-gold" onclick="openDonateModal()">
        ☕ Ủng Hộ Tác Giả
      </button>
      <div class="chip" id="chipPid">
        <span class="dot"></span>
        <span>PID: <b id="valPid">--</b></span>
      </div>
      <div class="chip status-dead" id="chipStatus">
        <span class="dot pulse"></span>
        <span id="txtStatus">Chưa kết nối game</span>
      </div>
    </div>
  </header>

  <!-- MAIN CONTAINER -->
  <div class="container">

    <!-- Dismissible Alert Banner -->
    <div class="alert-banner" id="topAlert">
      <div class="alert-banner-content">
        <span style="font-size:20px;">⚠️</span>
        <span><b>Lưu ý quan trọng:</b> Tool điều khiển trực tiếp thông qua game. Bạn cần tải gói cài đặt 1-Click để kích hoạt mod bên trong thư mục game Steam trước khi sử dụng.</span>
      </div>
      <div style="display:flex; align-items:center; gap:8px;">
        <button class="alert-banner-btn" onclick="openDownloadModal()">
          📥 Tải File 1-Click Ngay
        </button>
        <button class="alert-close-btn" onclick="dismissAlert()" title="Tắt thông báo này">✕</button>
      </div>
    </div>

    <!-- Sleek Horizontal Download Bar -->
    <div class="download-strip">
      <div class="download-strip-info">
        <div class="download-strip-icon">📦</div>
        <div class="download-strip-text">
          <h3>GÓI CÀI ĐẶT TỰ ĐỘNG 1-CLICK (MOD HELPER RUNTIME)</h3>
          <p>Tự động phát hiện thư mục game Steam và cài đặt trong 2 giây • Không làm hỏng file gốc của game</p>
        </div>
      </div>
      <div class="download-strip-actions">
        <button class="btn-download-trigger" onclick="openDownloadModal()">
          📥 TẢI FILE 1-CLICK & HƯỚNG DẪN
        </button>
      </div>
    </div>

    <!-- Top Mini Action Bar (Ghép đồ & Cất đồ) -->
    <div class="mini-actions-bar">
      <button class="btn-mini-action btn-mini-comb" onclick="triggerCombine()"><span class="btn-icon">⚡</span> GHÉP ĐỒ NGAY</button>
      <button class="btn-mini-action btn-mini-stash" onclick="triggerStash()"><span class="btn-icon">📥</span> CẤT ĐỒ NGAY</button>
    </div>

    <!-- Split Layout -->
    <div class="split-layout">

      <!-- LEFT: Controls Column -->
      <div class="controls-column">

        <!-- MODULE 1: AUTO COMBINE (Cyan Glow) -->
        <div class="card card-cyan" id="cardCombine">
          <div class="card-header">
            <div class="card-title">
              <span class="card-icon">⚡</span> TỰ ĐỘNG HỢP THÀNH (LÒ RÈN / XƯỞNG)
            </div>
            <span class="status-badge" id="badgeCombine">CHƯA KẾT NỐI</span>
          </div>

          <div class="form-row">
            <div>
              <div class="form-label">Bật Tự Động Hợp Thành Định Kỳ</div>
              <div class="form-sublabel">Tự động lặp lại công thức chế tạo trong Xưởng định kỳ theo số phút đã thiết lập</div>
            </div>
            <label class="switch">
              <input type="checkbox" id="toggleAutoComb" onchange="toggleAutoComb(this.checked)">
              <span class="slider"></span>
            </label>
          </div>

          <div class="config-row">
            <span class="config-label">Chu kỳ chạy mỗi:</span>
            <input type="number" id="combMin" class="num-input" value="5" min="1" max="120" onchange="updateCombMin()">
            <span class="config-unit">phút</span>
            <span class="config-unit" style="margin-left:auto; color:var(--dimmer);">(Khuyên dùng: 3 - 5 phút/lần)</span>
          </div>
        </div>

        <!-- MODULE 2: AUTO STASH & CAPACITY (Emerald Glow) -->
        <div class="card card-emerald" id="cardStash">
          <div class="card-header">
            <div class="card-title">
              <span class="card-icon">📦</span> TỰ ĐỘNG CẤT ĐỒ VÀO KHO
            </div>
            <span class="status-badge" id="badgeStash">CHƯA KẾT NỐI</span>
          </div>

          <div class="form-row">
            <div>
              <div class="form-label">Bật Tự Động Cất Đồ Định Kỳ</div>
              <div class="form-sublabel">Cất đồ từ túi cá nhân tuần tự vào các ngăn kho đã chọn</div>
            </div>
            <label class="switch">
              <input type="checkbox" id="toggleAutoStash" onchange="toggleAutoStash(this.checked)">
              <span class="slider"></span>
            </label>
          </div>

          <div class="config-row">
            <span class="config-label">Chu kỳ chạy mỗi:</span>
            <input type="number" id="stashSec" class="num-input" value="60" min="5" max="600" onchange="updateStashSec()">
            <span class="config-unit">giây</span>
            <span class="config-label" style="margin-left:14px;">Cất từ Kho:</span>
            <input type="number" id="stashStart" class="num-input" value="1" min="1" max="10" onchange="updateStashTabs()">
            <span class="config-label">đến Kho:</span>
            <input type="number" id="stashEnd" class="num-input" value="5" min="1" max="10" onchange="updateStashTabs()">
          </div>

          <!-- Capacity Breakdown Box (Only shown when connected) -->
          <div class="capacity-box" id="capacityBox" style="display: none;">
            <div class="cap-header">
              <span class="cap-title">📊 Dung Lượng Kho Đồ Hiện Tại</span>
              <span class="cap-stat" id="capSummary">-- / -- Slot</span>
            </div>
            <div class="cap-progress-track">
              <div class="cap-progress-bar" id="capProgressBar" style="width: 0%"></div>
            </div>
            <div class="cap-details">
              <span id="capInvDetail">🎒 Túi đồ: <b>-- / --</b> slot</span>
              <span id="capStorDetail">📦 Kho tổng: <b>-- / --</b> slot</span>
              <span id="capAvailDetail">🟢 Còn trống: <b>--</b> slot</span>
            </div>
          </div>
          <div class="capacity-placeholder" id="capacityPlaceholder">
            <span>⏳ Kết nối game để theo dõi dung lượng kho và túi đồ theo thời gian thực</span>
          </div>
        </div>

        <!-- MODULE 3: AUTO OPEN CHEST (Purple Glow) - Removed Open All button -->
        <div class="card card-purple" id="cardBox">
          <div class="card-header">
            <div class="card-title">
              <span class="card-icon">🎁</span> TỰ ĐỘNG MỞ RƯƠNG BÁU (CHEST OPENER)
            </div>
            <span class="status-badge" id="badgeBox">CHƯA KẾT NỐI</span>
          </div>

          <div class="form-row">
            <div>
              <div class="form-label">Bật Tự Động Mở Rương Định Kỳ</div>
              <div class="form-sublabel">Tự động phát hiện và mở sạch tất cả rương rơi trên sàn đấu (Normal, Stage, Elite) ngầm</div>
            </div>
            <label class="switch">
              <input type="checkbox" id="toggleAutoBox" onchange="toggleAutoBox(this.checked)">
              <span class="slider"></span>
            </label>
          </div>

          <div class="config-row">
            <span class="config-label">Chu kỳ kiểm tra:</span>
            <input type="number" id="boxInterval" class="num-input" value="3" min="1" max="60" onchange="updateBoxInterval()">
            <span class="config-unit">giây</span>
            <div style="margin-left:auto; display:flex; align-items:center; gap:8px;">
              <span class="config-label">Rương đang có:</span>
              <span class="box-count-badge" id="boxBadge">0 Rương</span>
            </div>
          </div>
        </div>

        <!-- MODULE 4: UNLOCK DLC FORGE (Amber Glow - Toggle ON/OFF) -->
        <div class="card card-amber" id="cardDlc">
          <div class="card-header">
            <div class="card-title">
              <span class="card-icon">🔓</span> MỞ KHÓA DLC LÒ RÈN / XƯỞNG
            </div>
            <span class="status-badge" id="dlcStatusBadge">CHƯA KẾT NỐI</span>
          </div>

          <div class="dlc-warning-box">
            <div class="dlc-warning-title">⚠️ Lưu ý quan trọng:</div>
            <div>Chức năng Tự Động Hợp Thành yêu cầu game phải có <b>DLC Lò Rèn (Workshop)</b>. Công tắc bên dưới giúp kích hoạt mở khóa DLC miễn phí ngầm trong game để có thể sử dụng được auto.</div>
            <div class="dlc-warning-highlight">⛔ <b>Dành cho người CHƯA CÓ DLC Lò Rèn để dùng auto. Nếu tài khoản của bạn đã mua hoặc đã có DLC rồi thì ĐỪNG DÙNG nút này!</b></div>
          </div>

          <!-- Interactive Toggle ON / OFF -->
          <div class="dlc-toggle-row">
            <div>
              <div class="dlc-toggle-name" id="dlcToggleText">Công Tắc Mở Khóa DLC (ON / OFF)</div>
              <div class="dlc-toggle-desc">Gạt BẬT để kích hoạt DLC Lò Rèn ngầm. Gạt TẮT để trả game về trạng thái nguyên bản.</div>
            </div>
            <label class="switch">
              <input type="checkbox" id="toggleDlc" onchange="onToggleDlc(this.checked)">
              <span class="slider"></span>
            </label>
          </div>
        </div>

      </div>

      <!-- RIGHT: Realtime Log Feed Column -->
      <div class="log-column">
        <div class="log-container">
          <div class="log-header">
            <div class="log-title">
              <span>⚡</span> NHẬT KÝ HOẠT ĐỘNG THỜI GIAN THỰC
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

  </div>

  <!-- FLOATING DISCORD CIRCLE BUTTON -->
  <a href="https://discord.gg/RuHaQU22K" target="_blank" rel="noopener noreferrer" class="discord-float" title="Tham gia Discord cộng đồng">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
      <path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.929 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.894.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/>
    </svg>
    <span class="discord-tooltip">💬 Tham gia Discord</span>
  </a>

  <!-- MODAL: DOWNLOAD & GUIDE -->
  <div class="modal-overlay" id="downloadModal" onclick="closeModalOnBg(event, 'downloadModal')">
    <div class="modal-card">
      <div class="modal-header">
        <div class="modal-title">
          <span>📦</span> TẢI FILE 1-CLICK & HƯỚNG DẪN CÀI ĐẶT
        </div>
        <button class="modal-close-btn" onclick="closeDownloadModal()">✕</button>
      </div>
      <div class="modal-body">
        <div class="modal-dl-row">
          <div class="modal-dl-row-left">
            <div style="font-size:32px;">🗜️</div>
            <div>
              <div style="font-weight:800; color:#fff; font-size:14.5px;">DPS_Auto_Helper_1Click.zip</div>
              <div style="font-size:12px; color:var(--dim); margin-top:3px;">Bản cài đặt tự động 1-Click trọn gói • Tốc độ cao qua GitHub Release</div>
            </div>
          </div>
          <div style="display:flex; flex-direction:column; align-items:flex-end; gap:6px;">
            <a href="https://github.com/titlee2111/dps-auto-helper/releases/download/v1.0.0/DPS_Auto_Helper_1Click.zip" class="btn-download-rect">
              📥 BẮT ĐẦU TẢI (.ZIP)
            </a>
            <a href="./DPS_Auto_Helper_1Click.zip" style="color:var(--dimmer); font-size:11px; text-decoration:none;">
              hoặc tải link dự phòng nội bộ
            </a>
          </div>
        </div>

        <div style="background:rgba(12,18,30,0.9); border:1px solid rgba(6,182,212,0.25); border-radius:var(--radius-md); padding:20px;">
          <h4 style="color:#38bdf8; font-size:13px; text-transform:uppercase; margin-bottom:12px; display:flex; align-items:center; gap:8px;">
            <span>📖</span> CÁCH CÀI ĐẶT TRONG 2 BƯỚC:
          </h4>
          <ol style="padding-left:20px; font-size:13px; color:#cbd5e1; line-height:1.85;">
            <li>Tải file <code>DPS_Auto_Helper_1Click.zip</code> và giải nén ra bất kỳ thư mục nào trên máy tính.</li>
            <li>Chạy file <code>Cai_Dat_Tu_Dong.bat</code>. Script sẽ tự động phát hiện thư mục game Steam của bạn và cài đặt mod runtime trong 2 giây.</li>
            <li>Mở game <b>DPS Desktop Pension Squad</b> trên Steam.</li>
            <li>F5 lại trang web này là công cụ sẽ tự động kết nối và hiển thị trạng thái xanh rực rỡ!</li>
          </ol>
        </div>
      </div>
    </div>
  </div>

  <!-- MODAL: DONATE / SUPPORT DEVELOPER -->
  <div class="modal-overlay" id="donateModal" onclick="closeModalOnBg(event, 'donateModal')">
    <div class="modal-card" style="max-width:540px;">
      <div class="modal-header">
        <div class="modal-title" style="color:#fbbf24;">
          <span>☕</span> ỦNG HỘ TÁC GIẢ (DONATE)
        </div>
        <button class="modal-close-btn" onclick="closeDonateModal()">✕</button>
      </div>
      <div class="modal-body">
        <p style="font-size:13px; color:var(--dim); text-align:center; line-height:1.5;">
          DPS Auto Helper hoàn toàn miễn phí. Nếu công cụ giúp bạn cắm máy rảnh tay, hãy cân nhắc mời tác giả một ly cà phê nhé! ❤️
        </p>

        <div class="donate-tabs">
          <button class="donate-tab-btn active" onclick="switchDonateTab(event, 'tabMb')">🇻🇳 MB Bank</button>
          <button class="donate-tab-btn" onclick="switchDonateTab(event, 'tabBinance')">🌐 Binance Pay</button>
          <button class="donate-tab-btn" onclick="switchDonateTab(event, 'tabBmc')">☕ Buy Me a Coffee</button>
        </div>

        <!-- MB Bank Tab -->
        <div class="donate-tab-content active" id="tabMb">
          <img src="__MB_QR__" alt="VietQR MB Bank" class="qr-img">
          <div style="display:flex; flex-direction:column; gap:8px; width:100%; align-items:center;">
            <div class="copy-pill" onclick="copyText('0562462346', 'Đã copy STK MB Bank!')">
              <span>STK: <b style="color:#fff;">0562462346</b> (MB Bank)</span>
              <span style="font-size:11px; opacity:0.8;">📋 Copy</span>
            </div>
            <div style="font-size:12.5px; color:#cbd5e1;">Chủ TK: <b>LY THAI SON</b></div>
            <div class="copy-pill" onclick="copyText('Ung ho DPS Auto Helper', 'Đã copy nội dung chuyển khoản!')">
              <span>Lời nhắn: <b style="color:#fff;">Ung ho DPS Auto Helper</b></span>
              <span style="font-size:11px; opacity:0.8;">📋 Copy</span>
            </div>
          </div>
        </div>

        <!-- Binance Pay Tab -->
        <div class="donate-tab-content" id="tabBinance">
          <img src="__BINANCE_QR__" alt="Binance Pay" class="qr-img">
          <div class="copy-pill" onclick="copyText('User-9e11c', 'Đã copy Binance Pay ID!')">
            <span>Binance Pay ID: <b style="color:#fff;">User-9e11c</b></span>
            <span style="font-size:11px; opacity:0.8;">📋 Copy</span>
          </div>
        </div>

        <!-- Buy Me a Coffee Tab -->
        <div class="donate-tab-content" id="tabBmc">
          <div style="padding:30px 10px; display:flex; flex-direction:column; align-items:center; gap:16px;">
            <div style="font-size:46px;">☕</div>
            <p style="font-size:13.5px; color:#cbd5e1;">Ủng hộ nhanh qua nền tảng quốc tế Buy Me a Coffee:</p>
            <a href="https://buymeacoffee.com/titlee" target="_blank" rel="noopener noreferrer" class="btn-download-rect" style="background:linear-gradient(135deg, #FFDD00 0%, #FBBF24 100%); color:#000; border-color:#d97706; font-weight:800;">
              ☕ Mời Tác Giả 1 Ly Cà Phê
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <footer>
    DPS Auto Helper • Tự Động Hóa Kho & Xưởng • <a href="javascript:void(0)" onclick="openDonateModal()" style="color:#fbbf24; text-decoration:none; font-weight:700;">☕ Ủng Hộ Tác Giả</a> • <a href="https://discord.gg/RuHaQU22K" target="_blank" rel="noopener noreferrer" style="color:#818cf8; text-decoration:none; font-weight:700;">💬 Discord Cộng Đồng</a>
  </footer>

  <script>
    const API_BASE = "http://127.0.0.1:47900";
    let isConnected = false;
    let autoBoxTimer = null;
    let boxIntervalSec = 3;

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
      addLog('HỆ THỐNG', 'Đã làm sạch nhật ký.', 'info');
    }

    // Modal Handlers
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
    function closeModalOnBg(e, modalId) {
      if (e.target.id === modalId) {
        document.getElementById(modalId).style.display = 'none';
      }
    }
    function dismissAlert() {
      const b = document.getElementById('topAlert');
      if (b) b.style.display = 'none';
    }

    function switchDonateTab(e, tabId) {
      document.querySelectorAll('.donate-tab-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.donate-tab-content').forEach(tab => tab.classList.remove('active'));
      e.target.classList.add('active');
      const target = document.getElementById(tabId);
      if (target) target.classList.add('active');
    }

    function copyText(text, toastMsg) {
      navigator.clipboard.writeText(text).then(() => {
        addLog('DONATE', toastMsg, 'ok');
      }).catch(() => {
        addLog('DONATE', 'Mã: ' + text, 'info');
      });
    }

    // Status Polling
    async function fetchStatus() {
      try {
        const res = await fetch(`${API_BASE}/status`, { cache: 'no-store' });
        if (!res.ok) throw new Error('HTTP ' + res.status);
        const data = await res.json();
        if (!isConnected) {
          isConnected = true;
          addLog('KẾT NỐI', `Đã kết nối thành công tới game (PID: ${data.pid || '30976'})`, 'ok');
        }
        updateStatus(data);
      } catch (err) {
        if (isConnected) {
          isConnected = false;
          addLog('MẤT KẾT NỐI', 'Không thể kết nối đến game. Vui lòng kiểm tra game đã mở chưa.', 'err');
        }
        markDisconnected();
      }
    }

    function updateStatus(st) {
      const chipStatus = document.getElementById('chipStatus');
      const txtStatus = document.getElementById('txtStatus');
      const valPid = document.getElementById('valPid');

      if (chipStatus) {
        chipStatus.className = 'chip status-live';
        txtStatus.innerText = 'Đang kết nối game';
      }
      if (valPid) valPid.innerText = st.pid || '--';

      // 1. Center HUD: Soul, Soul Stone, Capacity (Only active when connected)
      const hudSoul = document.getElementById('hudSoul');
      const hudSoulStone = document.getElementById('hudSoulStone');
      if (hudSoul) {
        const val = st.soul !== undefined ? st.soul : 9436884;
        hudSoul.innerText = Number(val).toLocaleString('vi-VN');
      }
      if (hudSoulStone) {
        const val = st.soul_stone !== undefined ? st.soul_stone : 1;
        hudSoulStone.innerText = Number(val).toLocaleString('vi-VN');
      }

      // Capacity calculation
      const invCur = st.inv_cur !== undefined ? st.inv_cur : 1;
      const invMax = st.inv_max !== undefined ? st.inv_max : 32;
      const storCur = st.storage_cur !== undefined ? st.storage_cur : 64;
      const storMax = st.storage_max !== undefined ? st.storage_max : 96;
      const totalCur = invCur + storCur;
      const totalMax = invMax + storMax;
      const pct = totalMax > 0 ? Math.round((totalCur / totalMax) * 100) : 0;

      const hudCap = document.getElementById('hudCapacity');
      const hudCapFill = document.getElementById('hudCapacityFill');
      if (hudCap) hudCap.innerText = `${totalCur} / ${totalMax} Slot`;
      if (hudCapFill) hudCapFill.style.width = `${pct}%`;

      // Show capacity breakdown in Module 2 when connected
      const capBox = document.getElementById('capacityBox');
      const capPlaceholder = document.getElementById('capacityPlaceholder');
      if (capBox) capBox.style.display = 'flex';
      if (capPlaceholder) capPlaceholder.style.display = 'none';

      const capSummary = document.getElementById('capSummary');
      const capProgressBar = document.getElementById('capProgressBar');
      const capInvDetail = document.getElementById('capInvDetail');
      const capStorDetail = document.getElementById('capStorDetail');
      const capAvailDetail = document.getElementById('capAvailDetail');

      if (capSummary) capSummary.innerText = `${totalCur} / ${totalMax} Slot (${pct}%)`;
      if (capProgressBar) {
        capProgressBar.style.width = `${pct}%`;
        if (pct >= 90) capProgressBar.style.background = 'linear-gradient(90deg, #ef4444, #dc2626)';
        else if (pct >= 75) capProgressBar.style.background = 'linear-gradient(90deg, #f59e0b, #d97706)';
        else capProgressBar.style.background = 'linear-gradient(90deg, #10b981, #06b6d4)';
      }
      if (capInvDetail) capInvDetail.innerHTML = `🎒 Túi đồ: <b>${invCur} / ${invMax}</b> slot`;
      if (capStorDetail) capStorDetail.innerHTML = `📦 Kho tổng: <b>${storCur} / ${storMax}</b> slot`;
      if (capAvailDetail) capAvailDetail.innerHTML = `🟢 Còn trống: <b>${totalMax - totalCur}</b> slot`;

      // Chest count badge in Module 3
      const boxCount = st.box_count !== undefined ? st.box_count : 0;
      const boxBadge = document.getElementById('boxBadge');
      if (boxBadge) boxBadge.innerText = `${boxCount} Rương`;

      // 2. Auto Combine module
      const tComb = document.getElementById('toggleAutoComb');
      const bComb = document.getElementById('badgeCombine');
      if (tComb && document.activeElement !== tComb) tComb.checked = (st.auto_comb === 1);
      if (bComb) {
        bComb.innerText = (st.auto_comb === 1) ? 'ĐANG CHẠY' : 'ĐÃ TẮT';
        bComb.className = (st.auto_comb === 1) ? 'status-badge active' : 'status-badge';
      }
      const cMin = document.getElementById('combMin');
      if (cMin && document.activeElement !== cMin && st.comb_min !== undefined) cMin.value = st.comb_min;

      // 3. Auto Stash module
      const tStash = document.getElementById('toggleAutoStash');
      const bStash = document.getElementById('badgeStash');
      if (tStash && document.activeElement !== tStash) tStash.checked = (st.auto_stash === 1);
      if (bStash) {
        bStash.innerText = (st.auto_stash === 1) ? 'ĐANG CHẠY' : 'ĐÃ TẮT';
        bStash.className = (st.auto_stash === 1) ? 'status-badge active' : 'status-badge';
      }
      const sSec = document.getElementById('stashSec');
      if (sSec && document.activeElement !== sSec && st.stash_sec !== undefined) sSec.value = st.stash_sec;
      const sStart = document.getElementById('stashStart');
      if (sStart && document.activeElement !== sStart && st.stash_start !== undefined) sStart.value = st.stash_start;
      const sEnd = document.getElementById('stashEnd');
      if (sEnd && document.activeElement !== sEnd && st.stash_end !== undefined) sEnd.value = st.stash_end;

      // 4. Auto Box module
      const tBox = document.getElementById('toggleAutoBox');
      const bBox = document.getElementById('badgeBox');
      if (tBox && document.activeElement !== tBox) {
        const isBoxOn = (st.auto_box === 1) || (autoBoxTimer !== null);
        tBox.checked = isBoxOn;
        if (bBox) {
          bBox.innerText = isBoxOn ? 'ĐANG CHẠY' : 'ĐÃ TẮT';
          bBox.className = isBoxOn ? 'status-badge active' : 'status-badge';
        }
      }

      // 5. DLC Toggle Switch (ON / OFF)
      const tDlc = document.getElementById('toggleDlc');
      const dlcBadge = document.getElementById('dlcStatusBadge');
      const dlcText = document.getElementById('dlcToggleText');
      if (tDlc && document.activeElement !== tDlc) {
        const isDlcActive = (st.dlc === 1);
        tDlc.checked = isDlcActive;
        if (dlcBadge) {
          dlcBadge.innerText = isDlcActive ? 'ĐÃ BẬT (ON)' : 'ĐANG TẮT (OFF)';
          dlcBadge.className = isDlcActive ? 'status-badge active' : 'status-badge';
        }
        if (dlcText) {
          dlcText.innerHTML = isDlcActive 
            ? '<span style="color:#10b981; font-weight:800;">Đang Bật Mở Khóa DLC (ON)</span>'
            : '<span style="color:#94a3b8;">Đang Tắt Mở Khóa DLC (OFF)</span>';
        }
      }
    }

    function markDisconnected() {
      const chipStatus = document.getElementById('chipStatus');
      const txtStatus = document.getElementById('txtStatus');
      const valPid = document.getElementById('valPid');
      if (chipStatus) {
        chipStatus.className = 'chip status-dead';
        txtStatus.innerText = 'Chưa kết nối game';
      }
      if (valPid) valPid.innerText = '--';

      // Reset HUD
      const hudSoul = document.getElementById('hudSoul');
      const hudSoulStone = document.getElementById('hudSoulStone');
      const hudCap = document.getElementById('hudCapacity');
      const hudCapFill = document.getElementById('hudCapacityFill');
      if (hudSoul) hudSoul.innerText = '--';
      if (hudSoulStone) hudSoulStone.innerText = '--';
      if (hudCap) hudCap.innerText = '-- / --';
      if (hudCapFill) hudCapFill.style.width = '0%';

      // Hide capacity box when disconnected
      const capBox = document.getElementById('capacityBox');
      const capPlaceholder = document.getElementById('capacityPlaceholder');
      if (capBox) capBox.style.display = 'none';
      if (capPlaceholder) capPlaceholder.style.display = 'block';

      ['badgeCombine', 'badgeStash', 'badgeBox', 'dlcStatusBadge'].forEach(id => {
        const b = document.getElementById(id);
        if (b) { b.innerText = 'CHƯA KẾT NỐI'; b.className = 'status-badge'; }
      });
    }

    // ACTION DISPATCHERS
    async function triggerCombine() {
      addLog('HỢP THÀNH', '⚡ Đang thực hiện ghép đồ ngay lập tức...', 'info');
      try {
        const res = await fetch(`${API_BASE}/set?combine=1`);
        if (res.ok) {
          const data = await res.json();
          updateStatus(data);
          addLog('HỢP THÀNH', '✅ Lệnh ghép đồ đã được gửi và thực thi trong Xưởng!', 'ok');
        }
      } catch (err) {
        addLog('LỖI', 'Không thể kết nối đến game: ' + err.message, 'err');
      }
    }

    async function triggerStash() {
      addLog('CẤT ĐỒ', '📥 Đang thực hiện cất đồ ngay lập tức vào Kho...', 'info');
      try {
        const res = await fetch(`${API_BASE}/set?stash=1`);
        if (res.ok) {
          const data = await res.json();
          updateStatus(data);
          addLog('CẤT ĐỒ', '✅ Lệnh cất đồ vào Kho đã thực thi thành công!', 'ok');
        }
      } catch (err) {
        addLog('LỖI', 'Không thể kết nối đến game: ' + err.message, 'err');
      }
    }

    async function toggleAutoComb(checked) {
      const val = checked ? 1 : 0;
      addLog('TỰ ĐỘNG HỢP THÀNH', checked ? '▶️ Đã BẬT Tự Động Hợp Thành định kỳ.' : '⏹️ Đã TẮT Tự Động Hợp Thành.', checked ? 'ok' : 'warn');
      try {
        const res = await fetch(`${API_BASE}/set?auto_comb=${val}`);
        if (res.ok) {
          const data = await res.json();
          updateStatus(data);
        }
      } catch (err) {
        addLog('LỖI', 'Không thể gửi lệnh: ' + err.message, 'err');
      }
    }

    async function toggleAutoStash(checked) {
      const val = checked ? 1 : 0;
      addLog('TỰ ĐỘNG CẤT ĐỒ', checked ? '▶️ Đã BẬT Tự Động Cất Đồ định kỳ.' : '⏹️ Đã TẮT Tự Động Cất Đồ.', checked ? 'ok' : 'warn');
      try {
        const res = await fetch(`${API_BASE}/set?auto_stash=${val}`);
        if (res.ok) {
          const data = await res.json();
          updateStatus(data);
        }
      } catch (err) {
        addLog('LỖI', 'Không thể gửi lệnh: ' + err.message, 'err');
      }
    }

    function toggleAutoBox(checked) {
      const val = checked ? 1 : 0;
      addLog('TỰ ĐỘNG MỞ RƯƠNG', checked ? `▶️ Đã BẬT Tự Động Mở Rương (chu kỳ ${boxIntervalSec}s).` : '⏹️ Đã TẮT Tự Động Mở Rương.', checked ? 'box' : 'warn');
      
      // Send to game server if supported
      fetch(`${API_BASE}/set?auto_box=${val}`).catch(() => {});

      if (checked) {
        if (autoBoxTimer) clearInterval(autoBoxTimer);
        autoBoxTimer = setInterval(() => {
          fetch(`${API_BASE}/set?open_box=1`).then(r => r.json()).then(data => {
            updateStatus(data);
            addLog('MỞ RƯƠNG', '🎁 Đã tự động mở sạch rương rơi trên sàn đấu!', 'box');
          }).catch(() => {});
        }, boxIntervalSec * 1000);
      } else {
        if (autoBoxTimer) {
          clearInterval(autoBoxTimer);
          autoBoxTimer = null;
        }
      }
      const bBox = document.getElementById('badgeBox');
      if (bBox) {
        bBox.innerText = checked ? 'ĐANG CHẠY' : 'ĐÃ TẮT';
        bBox.className = checked ? 'status-badge active' : 'status-badge';
      }
    }

    function updateBoxInterval() {
      const input = document.getElementById('boxInterval');
      if (!input) return;
      boxIntervalSec = Math.max(1, parseInt(input.value) || 3);
      addLog('CẤU HÌNH RƯƠNG', `Đã cập nhật chu kỳ mở rương: ${boxIntervalSec} giây.`, 'info');
      if (autoBoxTimer) {
        clearInterval(autoBoxTimer);
        autoBoxTimer = setInterval(() => {
          fetch(`${API_BASE}/set?open_box=1`).catch(() => {});
        }, boxIntervalSec * 1000);
      }
    }

    async function onToggleDlc(checked) {
      const val = checked ? 1 : 0;
      addLog('DLC LÒ RÈN', checked ? 'Đang gửi lệnh BẬT Mở Khóa DLC Lò Rèn...' : 'Đang gửi lệnh TẮT Mở Khóa DLC Lò Rèn...', checked ? 'warn' : 'info');
      try {
        const res = await fetch(`${API_BASE}/set?dlc=${val}`);
        if (res.ok) {
          const data = await res.json();
          updateStatus(data);
          addLog('DLC LÒ RÈN', checked ? '✅ ĐÃ BẬT Mở Khóa DLC Lò Rèn thành công!' : '⏹️ Đã TẮT Mở Khóa DLC Lò Rèn.', 'ok');
        }
      } catch (err) {
        addLog('LỖI', 'Không thể kết nối đến game: ' + err.message, 'err');
      }
    }

    async function updateCombMin() {
      const input = document.getElementById('combMin');
      if (!input) return;
      const val = Math.max(1, parseInt(input.value) || 5);
      addLog('CẤU HÌNH', `Đã đổi chu kỳ hợp thành: ${val} phút.`, 'info');
      try {
        const res = await fetch(`${API_BASE}/set?comb_min=${val}`);
        if (res.ok) updateStatus(await res.json());
      } catch (err) {}
    }

    async function updateStashSec() {
      const input = document.getElementById('stashSec');
      if (!input) return;
      const val = Math.max(5, parseInt(input.value) || 60);
      addLog('CẤU HÌNH', `Đã đổi chu kỳ cất đồ: ${val} giây.`, 'info');
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
      const end = Math.max(start, parseInt(eInput.value) || 5);
      addLog('CẤU HÌNH', `Đã đổi phạm vi cất đồ: Kho ${start} đến Kho ${end}.`, 'info');
      try {
        await fetch(`${API_BASE}/set?stash_start=${start}`);
        const res = await fetch(`${API_BASE}/set?stash_end=${end}`);
        if (res.ok) updateStatus(await res.json());
      } catch (err) {}
    }

    // Initialize
    fetchStatus();
    setInterval(fetchStatus, 2000);
  </script>
</body>
</html>
"""

final_html = html_template.replace("__B64_ICON__", b64_icon).replace("__MB_QR__", mb_qr_src).replace("__BINANCE_QR__", binance_qr_src)

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Generated {HTML_FILE} ({len(final_html)} bytes)")
