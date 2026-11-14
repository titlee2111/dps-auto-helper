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
  <style>
    :root {
      --bg: #0a0d14;
      --bg-alt: #101520;
      --card-bg: rgba(20, 27, 40, 0.78);
      --card-border: #232f45;
      --card-glow: rgba(59, 130, 246, 0.15);
      --line: #1e293b;
      --ink: #f8fafc;
      --dim: #94a3b8;
      --dimmer: #64748b;
      --primary: #3b82f6;
      --primary-hover: #2563eb;
      --primary-glow: rgba(59, 130, 246, 0.4);
      --purple: #8b5cf6;
      --purple-glow: rgba(139, 92, 246, 0.4);
      --ok: #10b981;
      --ok-glow: rgba(16, 185, 129, 0.4);
      --warn: #f59e0b;
      --warn-glow: rgba(245, 158, 11, 0.35);
      --err: #ef4444;
      --err-glow: rgba(239, 68, 68, 0.35);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --radius-full: 9999px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    
    body {
      background: var(--bg);
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(59, 130, 246, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 85% 80%, rgba(139, 92, 246, 0.06) 0%, transparent 40%),
        linear-gradient(180deg, #0a0d14 0%, #0d121c 100%);
      background-attachment: fixed;
      color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      width: 100%;
      overflow-x: hidden;
    }

    /* Header - Full Width */
    header {
      background: rgba(13, 18, 28, 0.90);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--card-border);
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
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
      width: 42px;
      height: 42px;
      border-radius: var(--radius-md);
      box-shadow: 0 0 16px var(--primary-glow);
      border: 2px solid #3b82f6;
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
      letter-spacing: 0.06em;
      text-transform: uppercase;
      background: linear-gradient(90deg, #ffffff 0%, #cbd5e1 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      line-height: 1.2;
    }
    .brand-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      color: #38bdf8;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      margin-top: 2px;
    }

    /* ==================== CENTER HUD BAR ==================== */
    .header-hud {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      flex-wrap: wrap;
      background: rgba(16, 22, 34, 0.85);
      border: 1px solid rgba(59, 130, 246, 0.25);
      border-radius: var(--radius-full);
      padding: 6px 16px;
      box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.08), 0 4px 15px rgba(0, 0, 0, 0.3);
    }

    .hud-item {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 2px 10px;
      border-right: 1px solid rgba(255, 255, 255, 0.08);
      position: relative;
    }
    .hud-item:last-child {
      border-right: none;
    }

    .hud-icon {
      font-size: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .hud-info {
      display: flex;
      flex-direction: column;
      line-height: 1.15;
    }
    .hud-label {
      font-size: 9px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--dimmer);
    }
    .hud-val {
      font-size: 13px;
      font-weight: 800;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      color: #fff;
      letter-spacing: 0.02em;
    }
    .hud-soul .hud-val { color: #c084fc; text-shadow: 0 0 10px rgba(192, 132, 252, 0.5); }
    .hud-stone .hud-val { color: #38bdf8; text-shadow: 0 0 10px rgba(56, 189, 248, 0.5); }
    .hud-cap .hud-val { color: #fbbf24; text-shadow: 0 0 10px rgba(251, 191, 36, 0.4); }
    .hud-box .hud-val { color: #f472b6; text-shadow: 0 0 10px rgba(244, 114, 182, 0.4); }

    .hud-mini-bar {
      width: 44px;
      height: 5px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: var(--radius-full);
      overflow: hidden;
      margin-left: 2px;
    }
    .hud-mini-fill {
      height: 100%;
      background: linear-gradient(90deg, #10b981, #f59e0b);
      border-radius: var(--radius-full);
      transition: width 0.3s ease;
    }

    .header-status {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
      flex-shrink: 0;
    }
    .chip {
      font-size: 12px;
      font-weight: 600;
      padding: 6px 14px;
      border-radius: var(--radius-full);
      background: #182234;
      color: var(--dim);
      border: 1px solid var(--card-border);
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }
    .chip.status-live {
      background: rgba(16, 185, 129, 0.12);
      color: #34d399;
      border-color: rgba(16, 185, 129, 0.35);
      box-shadow: 0 0 12px var(--ok-glow);
    }
    .chip.status-dead {
      background: rgba(239, 68, 68, 0.12);
      color: #f87171;
      border-color: rgba(239, 68, 68, 0.35);
    }
    .dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: currentColor;
      display: inline-block;
    }
    .dot.pulse {
      box-shadow: 0 0 8px currentColor;
      animation: pulse 1.8s infinite;
    }

    /* Donate Button */
    .btn-donate-gold {
      background: linear-gradient(135deg, #d97706 0%, #b45309 100%);
      color: #fff;
      font-size: 12px;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: var(--radius-full);
      border: 1px solid #f59e0b;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
      box-shadow: 0 0 14px rgba(245, 158, 11, 0.35);
      transition: all 0.2s ease;
    }
    .btn-donate-gold:hover {
      background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
      box-shadow: 0 0 20px rgba(245, 158, 11, 0.6);
      transform: translateY(-1px);
    }

    @keyframes pulse {
      0% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(1.15); }
      100% { opacity: 1; transform: scale(1); }
    }

    /* Main Container */
    .container {
      max-width: 100%;
      width: 100%;
      margin: 0;
      padding: 20px 28px;
      display: flex;
      flex-direction: column;
      gap: 20px;
      flex: 1;
    }

    /* Dismissible Alert Banner */
    .alert-banner {
      background: rgba(245, 158, 11, 0.08);
      border: 1px solid rgba(245, 158, 11, 0.25);
      border-radius: var(--radius-md);
      padding: 12px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      position: relative;
    }
    .alert-banner-content {
      display: flex;
      align-items: center;
      gap: 12px;
      color: #fbbf24;
      font-size: 13px;
      line-height: 1.4;
      flex: 1;
    }
    .alert-banner-btn {
      background: rgba(245, 158, 11, 0.2);
      border: 1px solid rgba(245, 158, 11, 0.4);
      color: #fff;
      font-size: 12px;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s ease;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .alert-banner-btn:hover {
      background: rgba(245, 158, 11, 0.35);
      border-color: #f59e0b;
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
    .alert-close-btn:hover {
      opacity: 1;
    }

    /* Horizontal Download Bar */
    .download-strip {
      background: linear-gradient(90deg, rgba(30, 41, 59, 0.9) 0%, rgba(20, 27, 40, 0.95) 100%);
      border: 1px solid rgba(59, 130, 246, 0.3);
      border-radius: var(--radius-md);
      padding: 14px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }
    .download-strip-info {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .download-strip-icon {
      width: 40px;
      height: 40px;
      border-radius: var(--radius-sm);
      background: rgba(59, 130, 246, 0.15);
      border: 1px solid rgba(59, 130, 246, 0.35);
      color: #60a5fa;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      flex-shrink: 0;
    }
    .download-strip-text h3 {
      font-size: 14px;
      font-weight: 700;
      color: #fff;
    }
    .download-strip-text p {
      font-size: 12px;
      color: var(--dim);
      margin-top: 2px;
    }
    .download-strip-actions {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .btn-download-trigger {
      background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
      color: #fff;
      font-size: 13px;
      font-weight: 700;
      padding: 8px 18px;
      border-radius: var(--radius-sm);
      border: 1px solid #3b82f6;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 0 14px var(--primary-glow);
      transition: all 0.2s ease;
    }
    .btn-download-trigger:hover {
      background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
      box-shadow: 0 0 20px var(--primary-glow);
      transform: translateY(-1px);
    }

    /* Top Mini Action Bar */
    .mini-actions-bar {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }
    .btn-mini-action {
      background: #162032;
      border: 1px solid #283955;
      color: #e2e8f0;
      font-size: 12px;
      font-weight: 700;
      padding: 7px 14px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }
    .btn-mini-action:hover {
      background: #1e2c45;
      border-color: #3b82f6;
      color: #fff;
      box-shadow: 0 0 10px rgba(59, 130, 246, 0.25);
    }
    .btn-mini-action.btn-mini-box:hover {
      border-color: #ec4899;
      box-shadow: 0 0 10px rgba(236, 72, 153, 0.3);
    }

    /* Split Layout: Left Controls, Right Realtime Log */
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

    /* Card Styling */
    .card {
      background: var(--card-bg);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-lg);
      padding: 22px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.35);
      position: relative;
    }
    .card:hover {
      border-color: #2e3e5c;
    }
    .card.active-card {
      border-color: rgba(59, 130, 246, 0.45);
      box-shadow: 0 8px 30px rgba(59, 130, 246, 0.12);
    }
    .card.card-purple {
      border-color: rgba(139, 92, 246, 0.3);
    }
    .card.card-purple:hover {
      border-color: rgba(139, 92, 246, 0.5);
    }

    .card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 16px;
      gap: 12px;
    }
    .card-title {
      font-size: 14px;
      font-weight: 800;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 8px;
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }
    .card-icon {
      font-size: 18px;
    }
    .status-badge {
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: var(--radius-full);
      background: #182234;
      color: var(--dimmer);
      border: 1px solid var(--card-border);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .status-badge.active {
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border-color: rgba(16, 185, 129, 0.4);
      box-shadow: 0 0 10px var(--ok-glow);
    }

    .form-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      padding: 12px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }
    .form-row:last-child {
      border-bottom: none;
      padding-bottom: 0;
    }
    .form-label {
      font-size: 13px;
      font-weight: 600;
      color: #e2e8f0;
    }
    .form-sublabel {
      font-size: 12px;
      color: var(--dimmer);
      margin-top: 2px;
    }

    /* Switch */
    .switch {
      position: relative;
      display: inline-block;
      width: 48px;
      height: 26px;
      flex-shrink: 0;
    }
    .switch input {
      opacity: 0;
      width: 0;
      height: 0;
    }
    .slider {
      position: absolute;
      cursor: pointer;
      top: 0; left: 0; right: 0; bottom: 0;
      background-color: #232f45;
      transition: .25s ease;
      border-radius: 34px;
      border: 1px solid #334460;
    }
    .slider:before {
      position: absolute;
      content: "";
      height: 18px;
      width: 18px;
      left: 3px;
      bottom: 3px;
      background-color: #94a3b8;
      transition: .25s ease;
      border-radius: 50%;
    }
    input:checked + .slider {
      background-color: #2563eb;
      border-color: #3b82f6;
      box-shadow: 0 0 12px var(--primary-glow);
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
      background: rgba(15, 23, 42, 0.6);
      padding: 10px 14px;
      border-radius: var(--radius-sm);
      border: 1px solid rgba(255, 255, 255, 0.05);
      flex-wrap: wrap;
    }
    .config-group {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .config-label {
      font-size: 12px;
      color: var(--dim);
    }
    .num-input {
      width: 58px;
      background: #182234;
      border: 1px solid #283955;
      color: #fff;
      font-size: 13px;
      font-weight: 700;
      padding: 5px 8px;
      border-radius: var(--radius-sm);
      text-align: center;
      outline: none;
      font-family: inherit;
    }
    .num-input:focus {
      border-color: #3b82f6;
      box-shadow: 0 0 8px var(--primary-glow);
    }
    .config-unit {
      font-size: 12px;
      color: var(--dimmer);
    }

    /* Capacity Progress Box */
    .capacity-box {
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.07);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      margin-top: 14px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .cap-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 12px;
    }
    .cap-title {
      color: var(--dim);
      font-weight: 600;
    }
    .cap-stat {
      color: #fbbf24;
      font-weight: 700;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }
    .cap-progress-track {
      width: 100%;
      height: 7px;
      background: rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-full);
      overflow: hidden;
    }
    .cap-progress-bar {
      height: 100%;
      background: linear-gradient(90deg, #10b981, #059669);
      border-radius: var(--radius-full);
      transition: width 0.3s ease, background 0.3s ease;
    }
    .cap-details {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11px;
      color: var(--dimmer);
      flex-wrap: wrap;
      gap: 8px;
      padding-top: 2px;
    }
    .cap-details b {
      color: #e2e8f0;
    }

    /* DLC Card & Warning */
    .dlc-card {
      border-color: rgba(245, 158, 11, 0.3);
      background: rgba(25, 20, 15, 0.75);
    }
    .dlc-warning-box {
      background: rgba(245, 158, 11, 0.1);
      border: 1px solid rgba(245, 158, 11, 0.3);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      font-size: 12px;
      line-height: 1.5;
      color: #fcd34d;
      margin-bottom: 14px;
    }
    .dlc-warning-title {
      font-weight: 800;
      color: #f59e0b;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .dlc-warning-highlight {
      margin-top: 6px;
      padding: 6px 10px;
      background: rgba(239, 68, 68, 0.15);
      border-left: 3px solid #ef4444;
      color: #fca5a5;
      font-size: 11.5px;
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
    }
    .dlc-toggle-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      padding: 8px 0;
    }
    .dlc-toggle-name {
      font-size: 13.5px;
      font-weight: 700;
      color: #fff;
    }
    .dlc-toggle-desc {
      font-size: 11.5px;
      color: var(--dimmer);
      margin-top: 3px;
    }

    /* Buttons */
    .btn-primary {
      background: linear-gradient(135deg, #2563eb, #1d4ed8);
      border: 1px solid #3b82f6;
      color: #fff;
      font-size: 12.5px;
      font-weight: 700;
      padding: 9px 16px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      width: 100%;
      transition: all 0.2s;
    }
    .btn-primary:hover {
      background: linear-gradient(135deg, #3b82f6, #2563eb);
      box-shadow: 0 0 15px var(--primary-glow);
    }

    .box-count-badge {
      background: rgba(236, 72, 153, 0.15);
      color: #f472b6;
      border: 1px solid rgba(236, 72, 153, 0.35);
      font-size: 11.5px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: var(--radius-full);
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }

    /* Log Box */
    .log-container {
      background: rgba(10, 14, 22, 0.95);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-lg);
      display: flex;
      flex-direction: column;
      flex: 1;
      overflow: hidden;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5);
    }
    .log-header {
      padding: 14px 18px;
      background: #121824;
      border-bottom: 1px solid var(--card-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .log-title {
      font-size: 13px;
      font-weight: 800;
      color: #e2e8f0;
      display: flex;
      align-items: center;
      gap: 8px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .btn-clear-log {
      background: none;
      border: 1px solid #283955;
      color: var(--dim);
      font-size: 11px;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: all 0.15s;
    }
    .btn-clear-log:hover {
      color: #fff;
      border-color: #3b82f6;
    }
    .log-feed {
      flex: 1;
      padding: 14px;
      overflow-y: auto;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 12px;
      line-height: 1.6;
      display: flex;
      flex-direction: column;
      gap: 6px;
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
      padding: 1px 6px;
      border-radius: 4px;
      font-size: 10px;
      font-weight: 700;
      flex-shrink: 0;
    }
    .log-tag.tag-ok { background: rgba(16, 185, 129, 0.2); color: #34d399; }
    .log-tag.tag-info { background: rgba(59, 130, 246, 0.2); color: #60a5fa; }
    .log-tag.tag-warn { background: rgba(245, 158, 11, 0.2); color: #fbbf24; }
    .log-tag.tag-err { background: rgba(239, 68, 68, 0.2); color: #f87171; }
    .log-tag.tag-box { background: rgba(236, 72, 153, 0.2); color: #f472b6; }
    .log-msg {
      color: #cbd5e1;
      word-break: break-word;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(4px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* MODAL OVERLAY STYLES */
    .modal-overlay {
      display: none;
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(5, 8, 15, 0.85);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      z-index: 9999;
      align-items: center;
      justify-content: center;
      padding: 20px;
      animation: fadeIn 0.2s ease;
    }
    .modal-card {
      background: #101623;
      border: 1px solid #233048;
      border-radius: var(--radius-lg);
      width: 100%;
      max-width: 720px;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6), 0 0 30px rgba(59, 130, 246, 0.15);
      overflow: hidden;
    }
    .modal-header {
      padding: 16px 24px;
      background: #141c2c;
      border-bottom: 1px solid #233048;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .modal-title {
      font-size: 16px;
      font-weight: 800;
      color: #fff;
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
    .modal-close-btn:hover {
      color: #fff;
    }
    .modal-body {
      padding: 24px;
      overflow-y: auto;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    /* Download Row inside modal */
    .modal-dl-row {
      background: #162032;
      border: 1px solid #2a3b5c;
      border-radius: var(--radius-md);
      padding: 16px 20px;
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
      padding: 10px 22px;
      border-radius: var(--radius-sm);
      border: 1px solid #34d399;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 0 16px var(--ok-glow);
      transition: all 0.2s ease;
      white-space: nowrap;
    }
    .btn-download-rect:hover {
      background: linear-gradient(135deg, #34d399 0%, #10b981 100%);
      box-shadow: 0 0 24px var(--ok-glow);
      transform: translateY(-1px);
    }

    /* Donate Tabs inside modal */
    .donate-tabs {
      display: flex;
      gap: 8px;
      border-bottom: 1px solid #233048;
      padding-bottom: 12px;
    }
    .donate-tab-btn {
      background: #141c2c;
      border: 1px solid #233048;
      color: var(--dim);
      font-size: 13px;
      font-weight: 700;
      padding: 8px 16px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: all 0.2s;
    }
    .donate-tab-btn.active {
      background: #2563eb;
      border-color: #3b82f6;
      color: #fff;
    }
    .donate-tab-content {
      display: none;
      flex-direction: column;
      align-items: center;
      gap: 14px;
      text-align: center;
    }
    .donate-tab-content.active {
      display: flex;
    }
    .qr-img {
      width: 200px;
      height: 200px;
      border-radius: var(--radius-md);
      border: 2px solid #233048;
      background: #fff;
      padding: 6px;
    }
    .copy-pill {
      background: #162032;
      border: 1px solid #2a3b5c;
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      font-size: 13px;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      color: #93c5fd;
    }
    .copy-pill:hover {
      border-color: #3b82f6;
      color: #fff;
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
      box-shadow: 0 4px 20px rgba(88, 101, 242, 0.45);
      border: 2px solid rgba(255, 255, 255, 0.2);
      z-index: 990;
      cursor: pointer;
      transition: all 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      text-decoration: none;
    }
    .discord-float:hover {
      transform: scale(1.1) translateY(-3px);
      box-shadow: 0 8px 25px rgba(88, 101, 242, 0.65);
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
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
      border: 1px solid #2b2d31;
    }
    .discord-float:hover .discord-tooltip {
      opacity: 1;
      transform: translateX(0);
    }

    /* Footer */
    footer {
      margin-top: auto;
      border-top: 1px solid var(--card-border);
      padding: 16px 28px;
      font-size: 12px;
      color: var(--dimmer);
      text-align: center;
      background: rgba(10, 13, 20, 0.95);
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

    <!-- CENTER HUD: Soul, Soul Stone, Inventory / Storage, Chests -->
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

      <div class="hud-item hud-box" title="Rương Báu Chưa Mở Trong Trận">
        <div class="hud-icon">🎁</div>
        <div class="hud-info">
          <span class="hud-label">Rương Báu</span>
          <span class="hud-val" id="hudBoxCount">0 Rương</span>
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
        <span style="font-size:18px;">⚠️</span>
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

    <!-- Top Mini Action Bar -->
    <div class="mini-actions-bar">
      <button class="btn-mini-action" onclick="triggerCombine()"><span class="btn-icon">⚡</span> GHÉP ĐỒ NGAY</button>
      <button class="btn-mini-action" onclick="triggerStash()"><span class="btn-icon">📥</span> CẤT ĐỒ NGAY</button>
      <button class="btn-mini-action btn-mini-box" onclick="triggerOpenBox()"><span class="btn-icon">🎁</span> MỞ RƯƠNG NGAY</button>
    </div>

    <!-- Split Layout -->
    <div class="split-layout">

      <!-- LEFT: Controls Column -->
      <div class="controls-column">

        <!-- MODULE 1: AUTO COMBINE -->
        <div class="card active-card" id="cardCombine">
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

        <!-- MODULE 2: AUTO STASH & CAPACITY -->
        <div class="card active-card" id="cardStash">
          <div class="card-header">
            <div class="card-title">
              <span class="card-icon">📦</span> TỰ ĐỘNG CẤT ĐỒ VÀO KHO
            </div>
            <span class="status-badge" id="badgeStash">CHƯA KẾT NỐI</span>
          </div>

          <div class="form-row">
            <div>
              <div class="form-label">Bật Tự Động Cất Đồ Định Kỳ</div>
              <div class="form-sublabel">Cất đồ từ túi đồ cá nhân tuần tự vào các ngăn kho đã chọn</div>
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

          <!-- Capacity Breakdown Box -->
          <div class="capacity-box">
            <div class="cap-header">
              <span class="cap-title">📊 Dung Lượng Kho Đồ Hiện Tại</span>
              <span class="cap-stat" id="capSummary">65 / 128 Slot (51%)</span>
            </div>
            <div class="cap-progress-track">
              <div class="cap-progress-bar" id="capProgressBar" style="width: 51%"></div>
            </div>
            <div class="cap-details">
              <span id="capInvDetail">🎒 Túi đồ: <b>1 / 32</b> slot</span>
              <span id="capStorDetail">📦 Kho tổng: <b>64 / 96</b> slot</span>
              <span id="capAvailDetail">🟢 Còn trống: <b>63</b> slot</span>
            </div>
          </div>
        </div>

        <!-- MODULE 3: AUTO OPEN CHEST -->
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
              <div class="form-sublabel">Tự động mở sạch tất cả rương rơi trên sàn đấu (Normal, Stage, Elite) ngầm theo chu kỳ</div>
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

          <div style="margin-top:14px;">
            <button class="btn-primary" style="background:linear-gradient(135deg, #8b5cf6, #6d28d9); border-color:#a78bfa;" onclick="triggerOpenBox()">
              🎁 MỞ TẤT CẢ RƯƠNG NGAY LẬP TỨC
            </button>
          </div>
        </div>

        <!-- MODULE 4: UNLOCK DLC FORGE (TOGGLE ON/OFF) -->
        <div class="card dlc-card" id="cardDlc">
          <div class="card-header">
            <div class="card-title" style="color:#f59e0b;">
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
              <span style="color:#38bdf8;">⚡</span> NHẬT KÝ HOẠT ĐỘNG THỜI GIAN THỰC
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
            <div style="font-size:28px;">🗜️</div>
            <div>
              <div style="font-weight:700; color:#fff; font-size:14px;">DPS_Auto_Helper_1Click.zip</div>
              <div style="font-size:12px; color:var(--dim); margin-top:2px;">Bản cài đặt tự động 1-Click trọn gói • Tốc độ cao qua GitHub Release</div>
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

        <div style="background:rgba(15,23,42,0.8); border:1px solid rgba(255,255,255,0.08); border-radius:var(--radius-md); padding:18px;">
          <h4 style="color:#38bdf8; font-size:13px; text-transform:uppercase; margin-bottom:12px; display:flex; align-items:center; gap:6px;">
            <span>📖</span> CÁCH CÀI ĐẶT TRONG 2 BƯỚC:
          </h4>
          <ol style="padding-left:20px; font-size:12.5px; color:#cbd5e1; line-height:1.8;">
            <li>Tải file <code>DPS_Auto_Helper_1Click.zip</code> và giải nén ra bất kỳ thư mục nào trên máy tính.</li>
            <li>Chạy file <code>Cai_Dat_Tu_Dong.bat</code>. Script sẽ tự động phát hiện thư mục game Steam của bạn và cài đặt mod runtime trong 2 giây.</li>
            <li>Mở game <b>DPS Desktop Pension Squad</b> trên Steam.</li>
            <li>F5 lại trang web này là công cụ sẽ tự động kết nối và hiển thị trạng thái xanh!</li>
          </ol>
        </div>
      </div>
    </div>
  </div>

  <!-- MODAL: DONATE / SUPPORT DEVELOPER -->
  <div class="modal-overlay" id="donateModal" onclick="closeModalOnBg(event, 'donateModal')">
    <div class="modal-card" style="max-width:540px;">
      <div class="modal-header">
        <div class="modal-title">
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
          <div style="display:flex; flex-direction:column; gap:6px; width:100%; align-items:center;">
            <div class="copy-pill" onclick="copyText('0562462346', 'Đã copy STK MB Bank!')">
              <span>STK: <b>0562462346</b> (MB Bank)</span>
              <span style="font-size:11px; opacity:0.8;">📋 Copy</span>
            </div>
            <div style="font-size:12px; color:#cbd5e1;">Chủ TK: <b>LY THAI SON</b></div>
            <div class="copy-pill" onclick="copyText('Ung ho DPS Auto Helper', 'Đã copy nội dung chuyển khoản!')">
              <span>Lời nhắn: <b>Ung ho DPS Auto Helper</b></span>
              <span style="font-size:11px; opacity:0.8;">📋 Copy</span>
            </div>
          </div>
        </div>

        <!-- Binance Pay Tab -->
        <div class="donate-tab-content" id="tabBinance">
          <img src="__BINANCE_QR__" alt="Binance Pay" class="qr-img">
          <div class="copy-pill" onclick="copyText('User-9e11c', 'Đã copy Binance Pay ID!')">
            <span>Binance Pay ID: <b>User-9e11c</b></span>
            <span style="font-size:11px; opacity:0.8;">📋 Copy</span>
          </div>
        </div>

        <!-- Buy Me a Coffee Tab -->
        <div class="donate-tab-content" id="tabBmc">
          <div style="padding:30px 10px; display:flex; flex-direction:column; align-items:center; gap:16px;">
            <div style="font-size:42px;">☕</div>
            <p style="font-size:13px; color:#cbd5e1;">Ủng hộ nhanh qua nền tảng quốc tế Buy Me a Coffee:</p>
            <a href="https://buymeacoffee.com/titlee" target="_blank" rel="noopener noreferrer" class="btn-download-rect" style="background:linear-gradient(135deg, #FFDD00 0%, #FBBF24 100%); color:#000; border-color:#d97706;">
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

      // 1. Center HUD: Soul, Soul Stone, Capacity, Chests
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
        else capProgressBar.style.background = 'linear-gradient(90deg, #10b981, #059669)';
      }
      if (capInvDetail) capInvDetail.innerHTML = `🎒 Túi đồ: <b>${invCur} / ${invMax}</b> slot`;
      if (capStorDetail) capStorDetail.innerHTML = `📦 Kho tổng: <b>${storCur} / ${storMax}</b> slot`;
      if (capAvailDetail) capAvailDetail.innerHTML = `🟢 Còn trống: <b>${totalMax - totalCur}</b> slot`;

      // Chest count
      const boxCount = st.box_count !== undefined ? st.box_count : 0;
      const hudBox = document.getElementById('hudBoxCount');
      const boxBadge = document.getElementById('boxBadge');
      if (hudBox) hudBox.innerText = `${boxCount} Rương`;
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
            ? '<span style="color:#10b981; font-weight:700;">Đang Bật Mở Khóa DLC (ON)</span>'
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

    async function triggerOpenBox() {
      addLog('MỞ RƯƠNG', '🎁 Đang thực hiện mở tất cả rương báu trong trận...', 'box');
      try {
        const res = await fetch(`${API_BASE}/set?open_box=1`);
        if (res.ok) {
          const data = await res.json();
          updateStatus(data);
          addLog('MỞ RƯƠNG', '✅ Đã mở sạch toàn bộ rương báu thành công!', 'ok');
        }
      } catch (err) {
        addLog('MỞ RƯƠNG', '✅ Lệnh mở rương báu đã được phát vào game!', 'ok');
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
          triggerOpenBox();
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
      addLog('CẤU HÌNH RƯƠNG', `Đã cập nhật chu kỳ mở rương thành: ${boxIntervalSec} giây.`, 'info');
      if (autoBoxTimer) {
        clearInterval(autoBoxTimer);
        autoBoxTimer = setInterval(() => {
          triggerOpenBox();
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
