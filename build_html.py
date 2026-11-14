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

html_content = f"""<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>DPS Auto Helper - Tự Động Hóa Kho & Xưởng</title>
  <link rel="icon" type="image/png" href="data:image/png;base64,{b64_icon}">
  <style>
    :root {{
      --bg: #0a0d14;
      --bg-alt: #101520;
      --card-bg: rgba(20, 27, 40, 0.75);
      --card-border: #232f45;
      --card-glow: rgba(59, 130, 246, 0.15);
      --line: #1e293b;
      --ink: #f8fafc;
      --dim: #94a3b8;
      --dimmer: #64748b;
      --primary: #3b82f6;
      --primary-hover: #2563eb;
      --primary-glow: rgba(59, 130, 246, 0.4);
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
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    
    body {{
      background: var(--bg);
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(59, 130, 246, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 85% 80%, rgba(16, 185, 129, 0.06) 0%, transparent 40%),
        linear-gradient(180deg, #0a0d14 0%, #0d121c 100%);
      background-attachment: fixed;
      color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Inter', sans-serif;
      line-height: 1.5;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      -webkit-font-smoothing: antialiased;
      width: 100%;
      overflow-x: hidden;
    }}

    /* Header - Full Width */
    header {{
      background: rgba(13, 18, 28, 0.85);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--card-border);
      padding: 14px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 14px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
      width: 100%;
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 14px;
      text-decoration: none;
    }}
    .game-logo {{
      width: 44px;
      height: 44px;
      border-radius: var(--radius-md);
      box-shadow: 0 0 16px var(--primary-glow);
      border: 2px solid #3b82f6;
      object-fit: cover;
      background: #141c2b;
      display: block;
      transition: transform 0.2s ease;
    }}
    .game-logo:hover {{
      transform: scale(1.05);
    }}
    .brand-titles {{
      display: flex;
      flex-direction: column;
    }}
    .brand-titles h1 {{
      font-size: 16px;
      font-weight: 800;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      background: linear-gradient(90deg, #ffffff 0%, #cbd5e1 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      line-height: 1.2;
    }}
    .brand-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      color: #38bdf8;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      margin-top: 2px;
    }}

    .header-status {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}
    .chip {{
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
      transition: all 0.25s ease;
    }}
    .chip.on {{
      color: #064e3b;
      background: #34d399;
      border-color: #10b981;
      box-shadow: 0 0 14px var(--ok-glow);
      font-weight: 700;
    }}
    .chip.off {{
      color: #fca5a5;
      background: rgba(239, 68, 68, 0.12);
      border-color: rgba(239, 68, 68, 0.35);
    }}
    .pulse-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: currentColor;
      box-shadow: 0 0 8px currentColor;
      animation: pulseAnim 2s infinite;
    }}
    @keyframes pulseAnim {{
      0% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.4; transform: scale(0.85); }}
      100% {{ opacity: 1; transform: scale(1); }}
    }}

    /* Support Button in Header */
    .btn-support-header {{
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.16) 0%, rgba(217, 119, 6, 0.28) 100%);
      color: #fbbf24;
      border: 1px solid #f59e0b;
      padding: 6px 14px;
      border-radius: var(--radius-full);
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 2px 10px rgba(245, 158, 11, 0.25);
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .btn-support-header:hover {{
      background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
      color: #ffffff;
      transform: translateY(-1px);
      box-shadow: 0 4px 16px rgba(245, 158, 11, 0.5);
    }}

    /* Main Container - FULL WIDTH WITH PADDING */
    main {{
      width: 100%;
      max-width: 100%;
      margin: 0;
      padding: 20px 28px 64px;
      display: flex;
      flex-direction: column;
      gap: 18px;
      flex: 1;
    }}

    /* Horizontal Download Rectangular Bar Across Top */
    .download-rect-bar {{
      width: 100%;
      background: linear-gradient(135deg, rgba(20, 28, 44, 0.95) 0%, rgba(13, 19, 30, 0.98) 100%);
      border: 1px solid #334768;
      border-radius: var(--radius-md);
      padding: 14px 22px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
      transition: all 0.2s ease;
    }}
    .download-rect-bar:hover {{
      border-color: #3b82f6;
      box-shadow: 0 6px 24px rgba(59, 130, 246, 0.2);
    }}
    .rect-left {{
      display: flex;
      align-items: center;
      gap: 14px;
      cursor: pointer;
      min-width: 0;
    }}
    .file-icon {{
      font-size: 26px;
      background: rgba(59, 130, 246, 0.15);
      border: 1px solid rgba(59, 130, 246, 0.35);
      border-radius: 10px;
      width: 48px;
      height: 48px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      box-shadow: 0 0 14px rgba(59, 130, 246, 0.25);
    }}
    .file-details {{
      display: flex;
      flex-direction: column;
      gap: 3px;
      min-width: 0;
    }}
    .file-name {{
      font-size: 14.5px;
      font-weight: 800;
      color: #ffffff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      letter-spacing: 0.02em;
    }}
    .file-meta {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      font-size: 12px;
      color: var(--dim);
    }}
    .meta-tag {{
      background: rgba(59, 130, 246, 0.14);
      border: 1px solid rgba(59, 130, 246, 0.35);
      color: #93c5fd;
      font-size: 11px;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: var(--radius-full);
    }}
    .meta-desc {{
      color: #94a3b8;
      font-size: 12px;
    }}
    
    .btn-download-rect {{
      background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
      color: #ffffff;
      font-size: 12.5px;
      font-weight: 800;
      letter-spacing: 0.03em;
      padding: 11px 20px;
      border-radius: var(--radius-sm);
      border: 1px solid #60a5fa;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 16px rgba(37, 99, 235, 0.45);
      white-space: nowrap;
      flex-shrink: 0;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      text-decoration: none;
    }}
    .btn-download-rect:hover {{
      background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(37, 99, 235, 0.65);
      border-color: #93c5fd;
    }}
    .btn-download-rect svg {{
      width: 17px;
      height: 17px;
      fill: currentColor;
    }}

    /* Offline Alert Navigation Banner with Close Button */
    .offline-banner {{
      width: 100%;
      background: linear-gradient(135deg, rgba(239, 68, 68, 0.18) 0%, rgba(185, 28, 28, 0.08) 100%);
      border: 1px solid rgba(239, 68, 68, 0.4);
      border-radius: var(--radius-md);
      padding: 12px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      box-shadow: 0 4px 16px rgba(239, 68, 68, 0.12);
      transition: all 0.2s ease;
      user-select: none;
    }}
    .offline-info {{
      display: flex;
      align-items: center;
      gap: 12px;
      cursor: pointer;
      flex: 1;
    }}
    .offline-icon {{
      font-size: 20px;
      animation: bounce 1.8s infinite;
    }}
    @keyframes bounce {{
      0%, 100% {{ transform: translateY(0); }}
      50% {{ transform: translateY(-3px); }}
    }}
    .offline-text h4 {{
      font-size: 13px;
      font-weight: 700;
      color: #fca5a5;
    }}
    .offline-text p {{
      font-size: 12px;
      color: #fecaca;
    }}
    .offline-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }}
    .btn-pill-action {{
      background: #ef4444;
      color: #fff;
      font-size: 11px;
      font-weight: 700;
      padding: 5px 12px;
      border-radius: var(--radius-full);
      white-space: nowrap;
      box-shadow: 0 0 10px rgba(239, 68, 68, 0.4);
      text-transform: uppercase;
      letter-spacing: 0.03em;
      cursor: pointer;
    }}
    .btn-dismiss-alert {{
      width: 26px;
      height: 26px;
      border-radius: 50%;
      border: 1px solid rgba(239, 68, 68, 0.4);
      background: rgba(239, 68, 68, 0.15);
      color: #fca5a5;
      font-size: 12px;
      font-weight: bold;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.15s ease;
    }}
    .btn-dismiss-alert:hover {{
      background: #ef4444;
      color: #fff;
      border-color: #ef4444;
    }}

    /* Card Base */
    .card {{
      background: var(--card-bg);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-lg);
      padding: 22px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.25);
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
      width: 100%;
    }}
    .card:hover {{
      border-color: rgba(59, 130, 246, 0.35);
    }}

    /* 2-COLUMN SPLIT LAYOUT: LEFT = CONTROLS, RIGHT = REALTIME LOG */
    .workspace-split {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      width: 100%;
      align-items: stretch;
    }}

    @media (max-width: 980px) {{
      .workspace-split {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Left Controls Column: Stack quick buttons on top, then cards */
    .controls-column {{
      display: flex;
      flex-direction: column;
      gap: 16px;
      width: 100%;
    }}

    /* Compact Quick Actions Panel at Top of Controls */
    .quick-actions-panel {{
      background: rgba(18, 25, 38, 0.85);
      border: 1px solid #283952;
      border-radius: var(--radius-md);
      padding: 12px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    }}
    .quick-title {{
      font-size: 12px;
      font-weight: 800;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .quick-btns-row {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}
    .btn-compact {{
      padding: 8px 16px;
      border-radius: var(--radius-sm);
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      letter-spacing: 0.02em;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      border: 1px solid transparent;
      outline: none;
      white-space: nowrap;
    }}
    .btn-compact:active {{
      transform: scale(0.96);
    }}
    .btn-compact-combine {{
      background: linear-gradient(135deg, rgba(37, 99, 235, 0.25) 0%, rgba(29, 78, 216, 0.35) 100%);
      color: #93c5fd;
      border-color: rgba(96, 165, 250, 0.45);
    }}
    .btn-compact-combine:hover {{
      background: #2563eb;
      color: #ffffff;
      border-color: #60a5fa;
      box-shadow: 0 0 14px rgba(37, 99, 235, 0.5);
      transform: translateY(-1px);
    }}
    .btn-compact-stash {{
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.25) 0%, rgba(5, 150, 105, 0.35) 100%);
      color: #6ee7b7;
      border-color: rgba(52, 211, 153, 0.45);
    }}
    .btn-compact-stash:hover {{
      background: #059669;
      color: #ffffff;
      border-color: #34d399;
      box-shadow: 0 0 14px rgba(16, 185, 129, 0.5);
      transform: translateY(-1px);
    }}

    .module-card {{
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      gap: 14px;
    }}
    .module-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-bottom: 12px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }}
    .module-title {{
      font-size: 14.5px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .badge-status {{
      font-size: 11px;
      font-weight: 700;
      padding: 4px 11px;
      border-radius: var(--radius-full);
      background: #1e293b;
      color: var(--dim);
      border: 1px solid #334155;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      transition: all 0.2s ease;
    }}
    .badge-status.active {{
      background: rgba(16, 185, 129, 0.16);
      color: #34d399;
      border-color: #10b981;
      box-shadow: 0 0 12px var(--ok-glow);
    }}

    /* Toggle Switch Row */
    .switch-box {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: rgba(13, 18, 27, 0.8);
      border: 1px solid #233044;
      border-radius: var(--radius-md);
      padding: 14px 18px;
      transition: border-color 0.2s ease;
    }}
    .switch-box:hover {{
      border-color: #3b82f6;
    }}
    .switch-desc h4 {{
      font-size: 13.5px;
      font-weight: 700;
      color: #ffffff;
    }}
    .switch-desc p {{
      font-size: 12px;
      color: var(--dim);
      margin-top: 3px;
    }}
    
    .switch {{
      position: relative;
      display: inline-block;
      width: 52px;
      height: 28px;
      flex-shrink: 0;
    }}
    .switch input {{
      opacity: 0;
      width: 0;
      height: 0;
    }}
    .slider {{
      position: absolute;
      cursor: pointer;
      top: 0; left: 0; right: 0; bottom: 0;
      background-color: #27354a;
      transition: 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      border-radius: 999px;
      border: 1px solid #3d4f6c;
    }}
    .slider:before {{
      position: absolute;
      content: "";
      height: 20px;
      width: 20px;
      left: 3px;
      bottom: 3px;
      background-color: #ffffff;
      transition: 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      border-radius: 50%;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
    }}
    input:checked + .slider {{
      background-color: #10b981;
      border-color: #34d399;
      box-shadow: 0 0 12px var(--ok-glow);
    }}
    input:checked + .slider:before {{
      transform: translateX(24px);
    }}

    /* Inputs Config Row */
    .config-row {{
      background: rgba(13, 18, 27, 0.5);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: var(--radius-md);
      padding: 12px 16px;
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }}
    .config-row label {{
      font-size: 13px;
      color: var(--dim);
      font-weight: 600;
    }}
    .config-row input[type="number"] {{
      background: #0f1623;
      border: 1px solid #2d3e58;
      border-radius: var(--radius-sm);
      color: #38bdf8;
      font-family: Consolas, monospace;
      font-size: 13.5px;
      font-weight: 700;
      padding: 6px 10px;
      outline: none;
      transition: all 0.2s ease;
      text-align: center;
    }}
    .config-row input[type="number"]:focus {{
      border-color: #38bdf8;
      box-shadow: 0 0 8px rgba(56, 189, 248, 0.35);
      background: #141d2e;
    }}

    /* DLC UNLOCK CARD STYLING */
    .dlc-card {{
      position: relative;
      display: flex;
      flex-direction: column;
      gap: 12px;
      background: rgba(22, 28, 42, 0.75);
    }}
    .dlc-warning-box {{
      background: rgba(245, 158, 11, 0.08);
      border: 1px solid rgba(245, 158, 11, 0.28);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      font-size: 12px;
      line-height: 1.55;
      color: #e2e8f0;
    }}
    .dlc-alert-tag {{
      background: rgba(239, 68, 68, 0.16);
      border: 1px solid rgba(239, 68, 68, 0.4);
      color: #fca5a5;
      font-size: 11.5px;
      font-weight: 800;
      padding: 6px 10px;
      border-radius: 6px;
      margin-top: 8px;
    }}
    .btn-action-dlc {{
      background: linear-gradient(135deg, #d97706 0%, #b45309 100%);
      color: #ffffff;
      box-shadow: 0 4px 16px rgba(217, 119, 6, 0.35);
      border: 1px solid #f59e0b;
      padding: 11px 18px;
      border-radius: var(--radius-sm);
      font-size: 12.5px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      letter-spacing: 0.03em;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      width: 100%;
    }}
    .btn-action-dlc:hover {{
      background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
      box-shadow: 0 6px 20px rgba(245, 158, 11, 0.55);
      transform: translateY(-2px);
    }}
    .btn-action-dlc.unlocked {{
      background: #182334;
      color: #6ee7b7;
      border-color: #059669;
      cursor: default;
      box-shadow: none;
      transform: none;
      pointer-events: none;
    }}

    /* RIGHT COLUMN: REALTIME ACTIVITY LOG CARD */
    .log-column {{
      display: flex;
      flex-direction: column;
      width: 100%;
    }}

    .log-card {{
      display: flex;
      flex-direction: column;
      height: 100%;
      border-top: 3px solid #8b5cf6;
      padding: 20px 22px;
      min-height: 520px;
    }}

    .log-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
      padding-bottom: 12px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      flex-wrap: wrap;
      gap: 10px;
    }}
    .log-title {{
      font-size: 14px;
      font-weight: 800;
      color: #c084fc;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .log-controls {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .btn-tool {{
      background: #182234;
      border: 1px solid #28374e;
      color: var(--dim);
      font-size: 11px;
      font-weight: 700;
      padding: 5px 10px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s ease;
    }}
    .btn-tool:hover {{
      background: #233148;
      color: #fff;
      border-color: #3b82f6;
    }}
    .btn-tool.active {{
      background: rgba(16, 185, 129, 0.16);
      color: #34d399;
      border-color: #10b981;
    }}

    /* Log Meta Stats Strip */
    .log-meta-strip {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: rgba(11, 15, 24, 0.7);
      border: 1px solid #1c273a;
      border-radius: var(--radius-sm);
      padding: 8px 14px;
      font-size: 11px;
      color: var(--dim);
      margin-bottom: 12px;
      font-family: Consolas, monospace;
    }}
    .log-meta-strip span b {{
      color: #38bdf8;
    }}

    /* Terminal Window Feed */
    .log-feed {{
      background: #080c14;
      border: 1px solid #1c2638;
      border-radius: var(--radius-md);
      padding: 14px 16px;
      flex: 1;
      min-height: 400px;
      max-height: 520px;
      overflow-y: auto;
      font-family: 'JetBrains Mono', Consolas, 'Courier New', monospace;
      font-size: 12px;
      line-height: 1.65;
      display: flex;
      flex-direction: column;
      gap: 6px;
      scrollbar-width: thin;
      scrollbar-color: #8b5cf6 #0e1420;
      box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.6);
    }}
    .log-feed::-webkit-scrollbar {{
      width: 6px;
    }}
    .log-feed::-webkit-scrollbar-track {{
      background: #0e1420;
      border-radius: 4px;
    }}
    .log-feed::-webkit-scrollbar-thumb {{
      background: #4c1d95;
      border-radius: 4px;
    }}
    .log-feed::-webkit-scrollbar-thumb:hover {{
      background: #8b5cf6;
    }}

    /* Log Entry Rows */
    .log-row {{
      display: flex;
      align-items: flex-start;
      gap: 8px;
      word-break: break-word;
      animation: logRowFade 0.2s ease-in;
    }}
    @keyframes logRowFade {{
      from {{ opacity: 0; transform: translateY(3px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
    .log-time {{
      color: #64748b;
      font-size: 11px;
      flex-shrink: 0;
      user-select: none;
    }}
    .log-tag {{
      font-size: 10px;
      font-weight: 800;
      padding: 1px 6px;
      border-radius: 4px;
      text-transform: uppercase;
      flex-shrink: 0;
      letter-spacing: 0.03em;
      user-select: none;
    }}
    .tag-sys {{ background: rgba(139, 92, 246, 0.18); color: #c084fc; border: 1px solid rgba(139, 92, 246, 0.35); }}
    .tag-conn {{ background: rgba(56, 189, 248, 0.18); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.35); }}
    .tag-stash {{ background: rgba(16, 185, 129, 0.18); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.35); }}
    .tag-comb {{ background: rgba(59, 130, 246, 0.18); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.35); }}
    .tag-cfg {{ background: rgba(245, 158, 11, 0.18); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.35); }}
    .tag-warn {{ background: rgba(239, 68, 68, 0.18); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.35); }}

    .log-msg {{
      color: #e2e8f0;
      flex: 1;
    }}
    .log-msg.highlight {{
      color: #ffffff;
      font-weight: 600;
    }}

    /* Modal Full Screen Popup */
    .modal-overlay {{
      display: none;
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(4, 6, 12, 0.84);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      z-index: 999;
      align-items: center;
      justify-content: center;
      padding: 20px;
      animation: fadeIn 0.2s ease-out;
    }}
    .modal-overlay.active {{
      display: flex;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; }}
      to {{ opacity: 1; }}
    }}
    .modal-dialog {{
      background: #111724;
      background-image: 
        radial-gradient(circle at 10% 10%, rgba(59, 130, 246, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 90% 90%, rgba(16, 185, 129, 0.08) 0%, transparent 40%);
      border: 1px solid #384e72;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8), 0 0 35px rgba(59, 130, 246, 0.25);
      border-radius: var(--radius-lg);
      max-width: 760px;
      width: 100%;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      animation: zoomIn 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    @keyframes zoomIn {{
      from {{ transform: scale(0.95); opacity: 0; }}
      to {{ transform: scale(1); opacity: 1; }}
    }}
    .modal-header {{
      background: #151f30;
      border-bottom: 1px solid #28374e;
      padding: 16px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-shrink: 0;
    }}
    .modal-header h3 {{
      font-size: 15px;
      font-weight: 800;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .modal-close {{
      width: 32px;
      height: 32px;
      border-radius: 50%;
      border: 1px solid #334768;
      background: rgba(255, 255, 255, 0.06);
      color: var(--dim);
      font-size: 16px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.15s ease;
    }}
    .modal-close:hover {{
      background: #ef4444;
      border-color: #ef4444;
      color: #fff;
    }}
    .modal-body {{
      padding: 24px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 18px;
      scrollbar-width: thin;
      scrollbar-color: #3b82f6 #111827;
    }}
    .modal-body::-webkit-scrollbar {{
      width: 6px;
    }}
    .modal-body::-webkit-scrollbar-track {{
      background: #111827;
    }}
    .modal-body::-webkit-scrollbar-thumb {{
      background: #3b82f6;
      border-radius: 999px;
    }}

    /* Guide Steps */
    .step-timeline {{
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}
    .step-card {{
      background: rgba(22, 30, 44, 0.7);
      border: 1px solid #233146;
      border-radius: var(--radius-sm);
      padding: 14px 18px;
      display: flex;
      gap: 14px;
      align-items: flex-start;
    }}
    .step-badge {{
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: var(--primary);
      color: #ffffff;
      font-size: 13px;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      box-shadow: 0 0 10px var(--primary-glow);
    }}
    .step-content h5 {{
      font-size: 13px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 4px;
    }}
    .step-content p {{
      font-size: 12px;
      color: var(--dim);
      line-height: 1.5;
    }}
    .step-content code {{
      background: #0d121c;
      border: 1px solid #243247;
      color: #38bdf8;
      padding: 2px 6px;
      border-radius: 4px;
      font-family: Consolas, monospace;
      font-size: 11px;
    }}
    .note-box {{
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid rgba(16, 185, 129, 0.25);
      border-radius: var(--radius-sm);
      padding: 10px 14px;
      font-size: 12px;
      color: #6ee7b7;
      margin-top: 10px;
      line-height: 1.45;
    }}

    /* DONATE MODAL SPECIFIC STYLES */
    .donate-dialog {{
      max-width: 650px;
      border: 1px solid #d97706;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.9), 0 0 35px rgba(245, 158, 11, 0.25);
      background: #111724;
      background-image: 
        radial-gradient(circle at 10% 10%, rgba(245, 158, 11, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 90% 90%, rgba(59, 130, 246, 0.08) 0%, transparent 40%);
    }}
    .donate-letter-box {{
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.08) 0%, rgba(59, 130, 246, 0.06) 100%);
      border: 1px solid rgba(245, 158, 11, 0.3);
      border-radius: var(--radius-sm);
      padding: 14px 18px;
      font-size: 12.5px;
      line-height: 1.65;
      color: #e2e8f0;
    }}
    .donate-tabs {{
      display: flex;
      gap: 8px;
      border-bottom: 1px solid #24334a;
      padding-bottom: 12px;
      margin-top: 4px;
    }}
    .donate-tab-btn {{
      flex: 1;
      padding: 9px 12px;
      font-size: 12.5px;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      background: #151d2d;
      color: var(--dim);
      border: 1px solid #28374e;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .donate-tab-btn:hover {{
      background: #1d273c;
      color: #ffffff;
      border-color: #3b82f6;
    }}
    .donate-tab-btn.active {{
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.18) 0%, rgba(217, 119, 6, 0.28) 100%);
      color: #fbbf24;
      border-color: #f59e0b;
      box-shadow: 0 0 12px rgba(245, 158, 11, 0.3);
    }}
    .donate-card {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 18px;
      align-items: center;
      background: #0c121e;
      border: 1px solid #24334a;
      border-radius: var(--radius-md);
      padding: 18px;
    }}
    .donate-qr-box {{
      text-align: center;
    }}
    .donate-qr-img {{
      width: 100%;
      max-width: 220px;
      border-radius: 10px;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.6);
      border: 1px solid #2e415d;
      display: inline-block;
      background: #ffffff;
      padding: 4px;
    }}
    .donate-info-list {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      font-size: 12.5px;
    }}
    .donate-field-label {{
      color: var(--dimmer);
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 3px;
    }}
    .donate-field-value {{
      font-weight: 700;
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: #131b2c;
      padding: 7px 12px;
      border-radius: 6px;
      border: 1px solid #233146;
    }}
    .btn-copy-small {{
      padding: 4px 10px;
      font-size: 11px;
      font-weight: 700;
      background: #1e293b;
      color: #38bdf8;
      border: 1px solid #334155;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.15s ease;
      white-space: nowrap;
    }}
    .btn-copy-small:hover {{
      background: #38bdf8;
      color: #0c121e;
      border-color: #38bdf8;
    }}

    /* FLOATING DISCORD CIRCLE BUTTON */
    .discord-float {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      width: 52px;
      height: 52px;
      border-radius: 50%;
      background: #5865F2;
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 18px rgba(88, 101, 242, 0.5), 0 0 10px rgba(88, 101, 242, 0.3);
      z-index: 990;
      transition: all 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      text-decoration: none;
      cursor: pointer;
    }}
    .discord-float:hover {{
      transform: scale(1.1) translateY(-3px);
      background: #4752c4;
      box-shadow: 0 8px 25px rgba(88, 101, 242, 0.7), 0 0 16px rgba(88, 101, 242, 0.5);
    }}
    .discord-float svg {{
      width: 28px;
      height: 28px;
      fill: currentColor;
    }}
    .discord-tooltip {{
      position: absolute;
      right: 64px;
      background: #171f30;
      color: #e2e8f0;
      font-size: 11.5px;
      font-weight: 700;
      padding: 6px 12px;
      border-radius: 6px;
      border: 1px solid #334768;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.5);
      white-space: nowrap;
      pointer-events: none;
      opacity: 0;
      transform: translateX(8px);
      transition: all 0.2s ease;
    }}
    .discord-float:hover .discord-tooltip {{
      opacity: 1;
      transform: translateX(0);
    }}

    /* Footer */
    footer {{
      margin-top: auto;
      text-align: center;
      padding: 24px;
      font-size: 12px;
      color: var(--dimmer);
      border-top: 1px solid var(--line);
      background: rgba(10, 13, 20, 0.8);
      width: 100%;
    }}

    /* Responsive */
    @media (max-width: 640px) {{
      header {{ padding: 12px 16px; }}
      .brand-titles h1 {{ font-size: 14px; }}
      main {{ padding: 16px 12px 48px; gap: 14px; }}
      .card {{ padding: 16px; }}
      .download-rect-bar {{ flex-direction: column; align-items: stretch; gap: 12px; padding: 14px; }}
      .quick-actions-panel {{ flex-direction: column; align-items: stretch; gap: 10px; }}
      .quick-btns-row {{ width: 100%; }}
      .quick-btns-row .btn-compact {{ flex: 1; justify-content: center; }}
      .config-row {{ flex-direction: column; align-items: flex-start; gap: 8px; }}
      .donate-tabs {{ flex-direction: column; }}
      .discord-float {{ bottom: 16px; right: 16px; width: 48px; height: 48px; }}
    }}
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <a href="#" class="brand">
      <img src="game-icon.png" onerror="this.src='data:image/png;base64,{b64_icon}'" alt="DPS Logo" class="game-logo">
      <div class="brand-titles">
        <h1>DPS Desktop Pension Squad</h1>
        <div class="brand-badge">⚡ Auto Helper</div>
      </div>
    </a>
    <div class="header-status">
      <button class="btn-support-header" onclick="openDonateModal()" title="Ủng hộ tác giả cốc cà phê">
        ☕ Ủng Hộ Tác Giả
      </button>
      <span id="pidBadge" class="chip">PID: -</span>
      <span id="connBadge" class="chip off">
        <span class="pulse-dot"></span>
        <span id="connText">Chưa kết nối game</span>
      </span>
    </div>
  </header>

  <main>

    <!-- Interactive Offline Navigation Banner with Close Button -->
    <div id="offlineNotice" class="offline-banner">
      <div class="offline-info" onclick="openDownloadModal()">
        <span class="offline-icon">⚠️</span>
        <div class="offline-text">
          <h4>Chưa phát hiện game DPS đang chạy!</h4>
          <p>Bấm vào đây để mở bảng tải tool 1-Click &amp; xem hướng dẫn cài đặt ⬇️</p>
        </div>
      </div>
      <div class="offline-actions">
        <span class="btn-pill-action" onclick="openDownloadModal()">Tải Tool ⬇</span>
        <button class="btn-dismiss-alert" onclick="dismissOfflineBanner(event)" title="Đóng thông báo">✕</button>
      </div>
    </div>

    <!-- TOP SECTION: FULL WIDTH RECTANGULAR BAR FOR 1-CLICK DOWNLOAD -->
    <div class="download-rect-bar">
      <div class="rect-left" onclick="openDownloadModal()">
        <div class="file-icon">📦</div>
        <div class="file-details">
          <div class="file-name">DPS_Auto_Helper_1Click.zip</div>
          <div class="file-meta">
            <span class="meta-tag">57.19 MB</span>
            <span class="meta-tag">v1.0.0</span>
            <span class="meta-desc">Gói cài đặt tự động 1-Click</span>
          </div>
        </div>
      </div>
      <button class="btn-download-rect" onclick="openDownloadModal()">
        <svg viewBox="0 0 24 24"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM17 13l-5 5-5-5h3V9h4v4h3z"/></svg>
        <span>TẢI MOD &amp; HƯỚNG DẪN</span>
      </button>
    </div>

    <!-- 2-COLUMN SPLIT WORKSPACE: LEFT CONTROLS, RIGHT REALTIME ACTION LOG -->
    <div class="workspace-split">

      <!-- LEFT COLUMN: MODULE CONTROLS -->
      <div class="controls-column">

        <!-- THAO TÁC NHANH (NHO NHỎ PHÍA TRÊN) -->
        <div class="quick-actions-panel">
          <div class="quick-title">
            <span>⚡</span> Thao Tác Nhanh:
          </div>
          <div class="quick-btns-row">
            <button id="btnCombineNow" class="btn-compact btn-compact-combine" title="Kích hoạt ghép đồ lặp lại trong Xưởng ngay lập tức">
              🔨 Ghép Đồ Ngay
            </button>
            <button id="btnStashNow" class="btn-compact btn-compact-stash" title="Kích hoạt cất toàn bộ đồ từ Balo vào các ngăn Kho đã chọn">
              📦 Cất Đồ Ngay
            </button>
          </div>
        </div>

        <!-- MODULE 1: TỰ ĐỘNG HỢP THÀNH XƯỞNG -->
        <div class="card module-card" style="border-top: 3px solid #3b82f6;">
          <div class="module-header">
            <div class="module-title" style="color: #60a5fa;">
              <span>🔨</span> Tự Động Hợp Thành Xưởng
            </div>
            <span id="badgeCombine" class="badge-status">Đã tắt</span>
          </div>

          <div class="switch-box">
            <div class="switch-desc">
              <h4>Bật Tự Động Ghép Đồ Định Kỳ</h4>
              <p>Tự động lặp lại công thức chế tạo trong Xưởng định kỳ theo số phút đã thiết lập</p>
            </div>
            <label class="switch">
              <input id="toggleCombine" type="checkbox">
              <span class="slider"></span>
            </label>
          </div>

          <div class="config-row">
            <label for="combineMin">Chu kỳ chạy mỗi:</label>
            <input id="combineMin" type="number" min="1" max="60" value="5" style="width: 75px;">
            <span style="color: var(--ink); font-size: 13px; font-weight: 600;">phút</span>
            <span style="color: var(--dimmer); font-size: 12px; margin-left: 10px;">(Khuyên dùng: 3 - 5 phút/lần)</span>
          </div>
        </div>

        <!-- MODULE 2: TỰ ĐỘNG CẤT ĐỒ VÀO KHO -->
        <div class="card module-card" style="border-top: 3px solid #10b981;">
          <div class="module-header">
            <div class="module-title" style="color: #34d399;">
              <span>📦</span> Tự Động Cất Đồ Vào Kho
            </div>
            <span id="badgeStash" class="badge-status">Đã tắt</span>
          </div>

          <div class="switch-box">
            <div class="switch-desc">
              <h4>Bật Tự Động Cất Đồ Định Kỳ</h4>
              <p>Cất đồ từ túi đồ cá nhân tuần tự vào các ngăn kho đã chọn</p>
            </div>
            <label class="switch">
              <input id="toggleStash" type="checkbox">
              <span class="slider"></span>
            </label>
          </div>

          <div class="config-row">
            <label for="stashSec">Chu kỳ chạy mỗi:</label>
            <input id="stashSec" type="number" min="2" max="600" value="60" style="width: 75px;">
            <span style="color: var(--ink); font-size: 13px; font-weight: 600;">giây</span>

            <span style="color: var(--line); margin: 0 6px;">|</span>

            <label for="stashStart">Cất từ Kho:</label>
            <input id="stashStart" type="number" min="1" max="10" value="1" style="width: 60px;">

            <label for="stashEnd">đến Kho:</label>
            <input id="stashEnd" type="number" min="1" max="10" value="5" style="width: 60px;">
          </div>
        </div>

        <!-- MODULE 3: MỞ KHÓA DLC LÒ RÈN (DÀNH CHO NGƯỜI CHƯA CÓ DLC) -->
        <div class="card dlc-card" style="border-top: 3px solid #f59e0b;">
          <div class="module-header">
            <div class="module-title" style="color: #fbbf24;">
              <span>🔓</span> Mở Khóa DLC Lò Rèn / Xưởng
            </div>
            <span id="badgeDlc" class="badge-status">Chưa mở khóa</span>
          </div>

          <div class="dlc-warning-box">
            <div style="font-weight: 700; color: #fbbf24; margin-bottom: 4px; display: flex; align-items: center; gap: 6px;">
              <span>⚠️</span> <span>Lưu ý quan trọng:</span>
            </div>
            <p>
              Chức năng Tự Động Hợp Thành yêu cầu game phải có <b>DLC Lò Rèn (Workshop)</b>. Nút bên dưới giúp kích hoạt mở khóa DLC miễn phí ngầm trong game để có thể sử dụng được auto.
            </p>
            <div class="dlc-alert-tag">
              ⛔ Dành cho người CHƯA CÓ DLC Lò Rèn để dùng auto. Nếu tài khoản của bạn đã mua hoặc đã có DLC rồi thì ĐỪNG DÙNG nút này!
            </div>
          </div>

          <button id="btnUnlockDlc" class="btn-action-dlc" onclick="triggerUnlockDlc()">
            🔓 MỞ KHÓA DLC LÒ RÈN (DÀNH CHO NGƯỜI CHƯA CÓ)
          </button>
        </div>

      </div>

      <!-- RIGHT COLUMN: REALTIME ACTIVITY & EXECUTION LOG -->
      <div class="log-column">
        <div class="card log-card">
          <div class="log-header">
            <div class="log-title">
              <span>📜</span> NHẬT KÝ HOẠT ĐỘNG THỜI GIAN THỰC
            </div>
            <div class="log-controls">
              <button id="btnAutoScroll" class="btn-tool active" onclick="toggleAutoScroll()">
                ⬇️ Tự Cuộn: BẬT
              </button>
              <button class="btn-tool" onclick="clearLogs()">
                🗑️ Xóa Log
              </button>
            </div>
          </div>

          <div class="log-meta-strip">
            <span>Tổng sự kiện: <b id="logCount">0</b></span>
            <span>Trạng thái: <b id="logStatusText" style="color:#34d399;">ĐANG ĐỒNG BỘ</b></span>
          </div>

          <!-- Scrollable Log Terminal -->
          <div id="logFeed" class="log-feed">
            <!-- Dynamic entries will be inserted here -->
          </div>
        </div>
      </div>

    </div>

  </main>

  <!-- FLOATING DISCORD CIRCLE BUTTON -->
  <a href="https://discord.gg/RuHaQU22K" target="_blank" rel="noopener noreferrer" class="discord-float" title="Tham gia Discord cộng đồng">
    <svg viewBox="0 0 127.14 96.36">
      <path fill="currentColor" d="M107.7,8.07A105.15,105.15,0,0,0,81.47,0a72.06,72.06,0,0,0-3.36,6.83A97.68,97.68,0,0,0,49,6.83,72.37,72.37,0,0,0,45.64,0,105.89,105.89,0,0,0,19.39,8.09C2.79,32.65-1.71,56.6.54,80.21h0A105.73,105.73,0,0,0,32.71,96.36,77.7,77.7,0,0,0,39.6,85.25a68.42,68.42,0,0,1-10.85-5.18c.91-.66,1.8-1.34,2.66-2a75.57,75.57,0,0,0,64.32,0c.87.71,1.76,1.39,2.66,2a68.68,68.68,0,0,1-10.87,5.19,77,77,0,0,0,6.89,11.1A105.25,105.25,0,0,0,126.6,80.22h0C129.24,52.84,122.09,29.11,107.7,8.07ZM42.45,65.69C36.18,65.69,31,60,31,53s5-12.74,11.43-12.74S54,45.91,53.89,53,48.84,65.69,42.45,65.69Zm42.24,0C78.41,65.69,73.25,60,73.25,53s5-12.74,11.44-12.74S96.23,45.91,96.12,53,91.08,65.69,84.69,65.69Z"/>
    </svg>
    <span class="discord-tooltip">💬 Tham gia Discord</span>
  </a>

  <!-- FULL SCREEN MODAL DIALOG: DOWNLOAD & STEP-BY-STEP GUIDE -->
  <div id="modalDownload" class="modal-overlay" onclick="handleOverlayClick(event)">
    <div class="modal-dialog">
      <div class="modal-header">
        <h3><span>📦</span> Cài Đặt &amp; Tải Mod Tự Động Hóa 1-Click</h3>
        <button class="modal-close" onclick="closeDownloadModal()">✕</button>
      </div>
      <div class="modal-body">
        
        <!-- Hàng ngang tải file nổi bật -->
        <div class="download-rect-bar" style="background:#141d2c; border-color:#38527a;">
          <div class="rect-left">
            <div class="file-icon">📦</div>
            <div class="file-details">
              <div class="file-name">DPS_Auto_Helper_1Click.zip</div>
              <div class="file-meta">
                <span class="meta-tag">57.19 MB</span>
                <span class="meta-tag">v1.0.0</span>
                <span class="meta-desc">Trọn gói BepInEx 6 + Mod Tự Động</span>
              </div>
            </div>
          </div>
          <div style="display:flex; flex-direction:column; gap:6px; align-items:flex-end;">
            <a href="https://github.com/titlee2111/dps-auto-helper/releases/download/v1.0.0/DPS_Auto_Helper_1Click.zip" class="btn-download-rect">
              <svg viewBox="0 0 24 24"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM17 13l-5 5-5-5h3V9h4v4h3z"/></svg>
              <span>BẮT ĐẦU TẢI (.ZIP)</span>
            </a>
            <a href="./DPS_Auto_Helper_1Click.zip" style="color:var(--dimmer); font-size:11px; text-decoration:none;">
              🔗 Link dự phòng (Local Mirror)
            </a>
          </div>
        </div>

        <!-- Bảng hướng dẫn chi tiết có thanh cuộn mượt mà -->
        <div class="step-timeline">

          <div class="step-card">
            <div class="step-badge">1</div>
            <div class="step-content">
              <h5>Tải File Cài Đặt 1-Click</h5>
              <p>Bấm nút <b>BẮT ĐẦU TẢI (.ZIP)</b> ở trên để tải về file <code>DPS_Auto_Helper_1Click.zip</code> (Dung lượng 57.19 MB đã bao gồm trọn gói runtime C# ngầm).</p>
            </div>
          </div>

          <div class="step-card">
            <div class="step-badge">2</div>
            <div class="step-content">
              <h5>Giải Nén &amp; Chạy File Cài Đặt Tự Động</h5>
              <p>Giải nén file zip ra một thư mục bất kỳ. Nhấp đúp chuột chạy file <code>Cai_Dat_Tu_Dong.bat</code>. Script thông minh sẽ tự động dò tìm thư mục Steam cài game và copy toàn bộ file mod vào trong đúng 2 giây!</p>
              <div class="note-box">
                💡 <b>Không cần kéo thả thủ công:</b> Script tự động kiểm tra Steam registry và thư viện game, bạn chỉ cần bấm chạy là xong.
              </div>
            </div>
          </div>

          <div class="step-card">
            <div class="step-badge">3</div>
            <div class="step-content">
              <h5>Mở Game &amp; Điều Khiển Qua Web</h5>
              <p>Khởi động game <code>DPS Desktop Pension Squad</code> bình thường qua Steam. Sau đó quay lại trang web này, góc phải trên cùng sẽ chuyển sang <b>🟢 ĐÃ KẾT NỐI GAME</b> và bạn có thể bật/tắt tự động tùy ý!</p>
            </div>
          </div>

          <div class="step-card">
            <div class="step-badge">4</div>
            <div class="step-content">
              <h5>Gỡ Cài Đặt Bất Cứ Lúc Nào</h5>
              <p>Nếu không muốn sử dụng nữa, chỉ việc chạy file <code>Go_Cai_Dat.bat</code> đi kèm trong file zip để xóa sạch toàn bộ file mod, đưa game về nguyên bản 100%.</p>
            </div>
          </div>

        </div>

        <div style="text-align: center; margin-top: 10px;">
          <button class="btn-compact" style="background:#1e293b; color:#94a3b8; border:1px solid #334155; padding:9px 20px;" onclick="closeDownloadModal()">
            Đã Hiểu, Đóng Lại
          </button>
        </div>

      </div>
    </div>
  </div>

  <!-- FULL SCREEN MODAL DIALOG: SUPPORT THE DEVELOPER / DONATE -->
  <div id="donateModal" class="modal-overlay" onclick="handleDonateOverlayClick(event)">
    <div class="modal-dialog donate-dialog">
      <div class="modal-header">
        <h3 style="color:#fbbf24;"><span>☕</span> Ủng Hộ Tác Giả / Support Developer</h3>
        <button class="modal-close" onclick="closeDonateModal()">✕</button>
      </div>
      <div class="modal-body">
        
        <!-- Heartfelt Message Box -->
        <div class="donate-letter-box">
          <div style="font-weight:700; color:#fbbf24; margin-bottom:6px; display:flex; align-items:center; gap:6px;">
            <span>💌</span> <span>Lời Nhắn Từ Tác Giả:</span>
          </div>
          <div>
            Chào bạn! Cảm ơn bạn rất nhiều vì đã tin tưởng và sử dụng <b>DPS Auto Helper</b>.<br>
            Dự án này được mình phát triển hoàn toàn tâm huyết và miễn phí nhằm hỗ trợ anh em cày cuốc tự động hóa tối đa trong game <b>DPS Desktop Pension Squad</b> (tự động hợp thành công thức xưởng định kỳ, tự động cất đồ tuần tự vào các ngăn kho thông minh, chạy logic ngầm IL2CPP không chiếm chuột, lưu cấu hình vĩnh viễn).<br>
            Nếu bạn cảm thấy Helper hữu ích và giúp bạn tiết kiệm thời gian hoặc cày game nhàn nhã hơn, hãy ủng hộ mình một ly cà phê ☕ nhé! Mọi đóng góp dù lớn hay nhỏ đều là nguồn động lực to lớn giúp mình duy trì và cập nhật tool tốt hơn nữa. Cảm ơn bạn rất nhiều! ❤️
          </div>
        </div>

        <!-- Tab Switcher -->
        <div class="donate-tabs">
          <button id="donateTabBtnMb" class="donate-tab-btn active" onclick="switchDonateTab('mb')">
            <span>🇻🇳</span> <span>Ngân Hàng MB (Việt Nam)</span>
          </button>
          <button id="donateTabBtnBinance" class="donate-tab-btn" onclick="switchDonateTab('binance')">
            <span>🌐</span> <span>Binance Pay (Crypto)</span>
          </button>
          <button id="donateTabBtnBmc" class="donate-tab-btn" onclick="switchDonateTab('bmc')">
            <span>☕</span> <span>Buy Me a Coffee</span>
          </button>
        </div>

        <!-- TAB 1: MB BANK (VIETQR) -->
        <div id="donateTabMb" class="donate-card" style="display:grid;">
          <div class="donate-qr-box">
            <img src="{mb_qr_src}" alt="MB Bank VietQR" class="donate-qr-img">
            <div style="font-size:11px; color:var(--dimmer); margin-top:8px;">📲 Quét bằng ứng dụng Ngân hàng bất kỳ</div>
          </div>
          <div class="donate-info-list">
            <div>
              <div class="donate-field-label">Ngân Hàng (Bank)</div>
              <div class="donate-field-value">
                <span>MB Bank (Ngân Hàng Quân Đội)</span>
              </div>
            </div>
            <div>
              <div class="donate-field-label">Số Tài Khoản (Account Number)</div>
              <div class="donate-field-value">
                <span id="mbAccNum" style="color:#34d399; font-size:14.5px;">0562462346</span>
                <button class="btn-copy-small" onclick="copyDonateText('0562462346', this)">📋 Sao chép</button>
              </div>
            </div>
            <div>
              <div class="donate-field-label">Chủ Tài Khoản (Account Holder)</div>
              <div class="donate-field-value">
                <span style="color:#60a5fa;">LY THAI SON</span>
                <button class="btn-copy-small" onclick="copyDonateText('LY THAI SON', this)">📋 Sao chép</button>
              </div>
            </div>
            <div>
              <div class="donate-field-label">Lời Nhắn Chuyển Khoản (Note)</div>
              <div class="donate-field-value" style="color:#fbbf24; font-style:italic;">
                <span>Ủng hộ DPS Auto Helper</span>
                <button class="btn-copy-small" onclick="copyDonateText('Ủng hộ DPS Auto Helper', this)">📋 Sao chép</button>
              </div>
            </div>
          </div>
        </div>

        <!-- TAB 2: BINANCE PAY (INTERNATIONAL) -->
        <div id="donateTabBinance" class="donate-card" style="display:none;">
          <div class="donate-qr-box">
            <img src="{binance_qr_src}" alt="Binance Pay QR" class="donate-qr-img">
            <div style="font-size:11px; color:var(--dimmer); margin-top:8px;">📲 Quét bằng App Binance (Binance Pay)</div>
          </div>
          <div class="donate-info-list">
            <div>
              <div class="donate-field-label">Nền Tảng (Platform)</div>
              <div class="donate-field-value">
                <span style="color:#f0b90b;">🔶 Binance Pay (Crypto)</span>
              </div>
            </div>
            <div>
              <div class="donate-field-label">Binance Pay ID / Username</div>
              <div class="donate-field-value">
                <span id="binanceUser" style="color:#f0b90b; font-size:14.5px;">User-9e11c</span>
                <button class="btn-copy-small" onclick="copyDonateText('User-9e11c', this)">📋 Sao chép</button>
              </div>
            </div>
            <div>
              <div class="donate-field-label">Tiền Tệ Hỗ Trợ (Supported Coins)</div>
              <div class="donate-field-value" style="color:var(--dim); font-size:12px;">
                <span>USDT, BUSD, BNB, BTC, ETH... (0% phí nội bộ Binance)</span>
              </div>
            </div>
            <div>
              <div class="donate-field-label">Hướng Dẫn Nhanh (How To Pay)</div>
              <div class="donate-field-value" style="color:var(--dimmer); font-size:11.5px; line-height:1.4;">
                Mở App Binance ➔ Bấm biểu tượng Pay hoặc Quét mã QR ➔ Quét mã hoặc nhập Pay ID: User-9e11c.
              </div>
            </div>
          </div>
        </div>

        <!-- TAB 3: BUY ME A COFFEE (GLOBAL) -->
        <div id="donateTabBmc" style="display:none;">
          <div style="background:#0c121e; border:1px solid #24334a; border-radius:var(--radius-md); padding:32px 20px; text-align:center;">
            <div style="font-size:46px; margin-bottom:12px;">☕</div>
            <div style="font-weight:800; color:#ffffff; font-size:16px; margin-bottom:6px;">Buy Me a Coffee</div>
            <div style="font-size:12.5px; color:var(--dim); margin-bottom:20px; line-height:1.5;">Ủng hộ tác giả qua Buy Me a Coffee — hỗ trợ thẻ quốc tế (Visa/Mastercard) &amp; PayPal tiện lợi.</div>
            <a href="https://buymeacoffee.com/titlee" target="_blank" rel="noopener noreferrer" style="display:inline-block; background:#FFDD00; color:#0d1117; font-weight:800; padding:12px 32px; border-radius:26px; text-decoration:none; font-size:14.5px; letter-spacing:0.3px; box-shadow:0 4px 16px rgba(255,221,0,0.3); transition:transform 0.15s ease;">☕ buymeacoffee.com/titlee</a>
            <div style="font-size:11.5px; color:var(--dimmer); margin-top:14px;">Bấm nút phía trên để mở trang Buy Me a Coffee trong tab mới →</div>
          </div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px; padding-top:14px; border-top:1px solid #24334a;">
          <div style="font-size:12px; color:var(--dimmer);">
            🌟 Chúc bạn chơi game DPS vui vẻ &amp; cày được nhiều loot ngon!
          </div>
          <button class="btn-compact" style="background:#1e293b; color:#94a3b8; border:1px solid #334155; padding:8px 18px;" onclick="closeDonateModal()">
            Đã Hiểu, Đóng Lại
          </button>
        </div>

      </div>
    </div>
  </div>

  <footer>
    DPS Auto Helper • Tự Động Hóa Kho &amp; Xưởng • <a href="javascript:void(0)" onclick="openDonateModal()" style="color:#fbbf24; text-decoration:none; font-weight:700;">☕ Ủng Hộ Tác Giả</a> • <a href="https://discord.gg/RuHaQU22K" target="_blank" rel="noopener noreferrer" style="color:#818cf8; text-decoration:none; font-weight:700;">💬 Discord Cộng Đồng</a>
  </footer>

  <script>
    const $ = id => document.getElementById(id);
    const API_BASE = 'http://127.0.0.1:47900';

    let isOnline = false;
    let offlineBannerDismissed = false;
    let autoScrollEnabled = true;
    let logCounter = 0;

    let prevStatus = null;
    let prevStashCurr = null;

    // Modal Control Functions: Download
    function openDownloadModal() {{
      $('modalDownload').classList.add('active');
      document.body.style.overflow = 'hidden';
    }}

    function closeDownloadModal() {{
      $('modalDownload').classList.remove('active');
      document.body.style.overflow = '';
    }}

    function handleOverlayClick(e) {{
      if (e.target === $('modalDownload')) {{
        closeDownloadModal();
      }}
    }}

    // Modal Control Functions: Donate / Support
    function openDonateModal() {{
      $('donateModal').classList.add('active');
      document.body.style.overflow = 'hidden';
    }}

    function closeDonateModal() {{
      $('donateModal').classList.remove('active');
      document.body.style.overflow = '';
    }}

    function handleDonateOverlayClick(e) {{
      if (e.target === $('donateModal')) {{
        closeDonateModal();
      }}
    }}

    function switchDonateTab(tab) {{
      const tabMb = $('donateTabMb');
      const tabBinance = $('donateTabBinance');
      const tabBmc = $('donateTabBmc');
      const btnMb = $('donateTabBtnMb');
      const btnBinance = $('donateTabBtnBinance');
      const btnBmc = $('donateTabBtnBmc');

      tabMb.style.display = (tab === 'mb') ? 'grid' : 'none';
      tabBinance.style.display = (tab === 'binance') ? 'grid' : 'none';
      tabBmc.style.display = (tab === 'bmc') ? 'block' : 'none';

      btnMb.className = (tab === 'mb') ? 'donate-tab-btn active' : 'donate-tab-btn';
      btnBinance.className = (tab === 'binance') ? 'donate-tab-btn active' : 'donate-tab-btn';
      btnBmc.className = (tab === 'bmc') ? 'donate-tab-btn active' : 'donate-tab-btn';
    }}

    function copyDonateText(text, btn) {{
      navigator.clipboard.writeText(text).then(() => {{
        const originalText = btn.innerHTML;
        btn.innerHTML = '✅ Đã chép!';
        btn.style.background = '#10b981';
        btn.style.color = '#ffffff';
        btn.style.borderColor = '#10b981';
        setTimeout(() => {{
          btn.innerHTML = originalText;
          btn.style.background = '';
          btn.style.color = '';
          btn.style.borderColor = '';
        }}, 2000);
      }}).catch(() => {{
        const input = document.createElement('input');
        input.value = text;
        document.body.appendChild(input);
        input.select();
        document.execCommand('copy');
        document.body.removeChild(input);
        btn.innerHTML = '✅ Đã chép!';
        setTimeout(() => {{ btn.innerHTML = '📋 Sao chép'; }}, 2000);
      }});
    }}

    function dismissOfflineBanner(e) {{
      if (e) e.stopPropagation();
      $('offlineNotice').style.display = 'none';
      offlineBannerDismissed = true;
    }}

    document.addEventListener('keydown', e => {{
      if (e.key === 'Escape') {{
        if ($('modalDownload').classList.contains('active')) closeDownloadModal();
        if ($('donateModal').classList.contains('active')) closeDonateModal();
      }}
    }});

    // Log Feed System
    function getTimeStr() {{
      const d = new Date();
      const pad = n => n.toString().padStart(2, '0');
      return `[${{pad(d.getHours())}}:${{pad(d.getMinutes())}}:${{pad(d.getSeconds())}}]`;
    }}

    function addLog(tagType, message, highlight = false) {{
      logCounter++;
      $('logCount').textContent = logCounter;

      const feed = $('logFeed');
      const row = document.createElement('div');
      row.className = 'log-row';

      let tagClass = 'tag-sys';
      let tagLabel = tagType.toUpperCase();

      switch (tagType.toLowerCase()) {{
        case 'conn':
        case 'kết nối':
          tagClass = 'tag-conn';
          tagLabel = 'KẾT NỐI';
          break;
        case 'cất đồ':
          tagClass = 'tag-stash';
          tagLabel = 'CẤT ĐỒ';
          break;
        case 'hợp thành':
          tagClass = 'tag-comb';
          tagLabel = 'HỢP THÀNH';
          break;
        case 'dlc':
        case 'mở khóa':
          tagClass = 'tag-cfg';
          tagLabel = 'DLC LÒ RÈN';
          break;
        case 'cfg':
        case 'cấu hình':
          tagClass = 'tag-cfg';
          tagLabel = 'CẤU HÌNH';
          break;
        case 'warn':
        case 'cảnh báo':
        case 'lỗi':
          tagClass = 'tag-warn';
          tagLabel = 'CẢNH BÁO';
          break;
      }}

      row.innerHTML = `
        <span class="log-time">${{getTimeStr()}}</span>
        <span class="log-tag ${{tagClass}}">${{tagLabel}}</span>
        <span class="log-msg ${{highlight ? 'highlight' : ''}}">${{message}}</span>
      `;

      feed.appendChild(row);

      // Keep maximum 300 entries to prevent memory bloat
      while (feed.children.length > 300) {{
        feed.removeChild(feed.firstChild);
      }}

      if (autoScrollEnabled) {{
        feed.scrollTop = feed.scrollHeight;
      }}
    }}

    function toggleAutoScroll() {{
      autoScrollEnabled = !autoScrollEnabled;
      const btn = $('btnAutoScroll');
      if (autoScrollEnabled) {{
        btn.className = 'btn-tool active';
        btn.innerHTML = '⬇️ Tự Cuộn: BẬT';
        $('logFeed').scrollTop = $('logFeed').scrollHeight;
      }} else {{
        btn.className = 'btn-tool';
        btn.innerHTML = '⏸️ Tự Cuộn: TẮT';
      }}
    }}

    function clearLogs() {{
      $('logFeed').innerHTML = '';
      logCounter = 0;
      $('logCount').textContent = '0';
      addLog('sys', 'Đã làm sạch màn hình nhật ký hoạt động.');
    }}

    function updateStashBtnLabel() {{
      const s = $('stashStart').value || 1;
      const e = $('stashEnd').value || 5;
      $('btnStashNow').textContent = `📦 Cất Đồ Ngay (Kho ${{s}} -> ${{e}})`;
    }}

    // Realtime Game Sync
    function render(st) {{
      const wasOnline = isOnline;
      isOnline = true;
      $('offlineNotice').style.display = 'none';
      $('connBadge').className = 'chip on';
      $('connText').textContent = 'Đã kết nối game';
      $('pidBadge').textContent = 'PID: ' + (st.pid || '-');
      $('logStatusText').textContent = 'ĐANG ĐỒNG BỘ';
      $('logStatusText').style.color = '#34d399';

      if (!wasOnline) {{
        addLog('conn', `Kết nối thành công tới DPS.exe (PID: ${{st.pid || '30976'}}, Cổng: ${{st.port || '47900'}})`, true);
      }}

      // 1. Dong bo Combine
      if (st.comb_min !== undefined && document.activeElement !== $('combineMin')) {{
        $('combineMin').value = st.comb_min;
      }}
      if (st.auto_comb !== undefined) {{
        const on = (st.auto_comb === 1 || st.auto_comb === true);
        $('toggleCombine').checked = on;
        $('badgeCombine').className = on ? 'badge-status active' : 'badge-status';
        $('badgeCombine').textContent = on ? `ĐANG BẬT (mỗi ${{st.comb_min || $('combineMin').value || 5}}p)` : 'Đã tắt';
      }}

      // 2. Dong bo Stash
      if (st.stash_sec !== undefined && document.activeElement !== $('stashSec')) {{
        $('stashSec').value = st.stash_sec;
      }}
      if (st.stash_start !== undefined && document.activeElement !== $('stashStart')) {{
        $('stashStart').value = st.stash_start;
      }}
      if (st.stash_end !== undefined && document.activeElement !== $('stashEnd')) {{
        $('stashEnd').value = st.stash_end;
      }}
      updateStashBtnLabel();

      if (st.auto_stash !== undefined) {{
        const on = (st.auto_stash === 1 || st.auto_stash === true);
        $('toggleStash').checked = on;
        $('badgeStash').className = on ? 'badge-status active' : 'badge-status';
        $('badgeStash').textContent = on ? `ĐANG BẬT (mỗi ${{st.stash_sec || $('stashSec').value || 60}}s)` : 'Đã tắt';
      }}

      // 3. Phat hien tien trinh cat do
      if (st.stash_step && st.stash_step > 0) {{
        if (st.stash_curr !== prevStashCurr) {{
          addLog('cất đồ', `⏳ Đang cất đồ vào Kho ${{st.stash_curr || 1}} (Lộ trình Kho ${{st.stash_start || 1}} -> ${{st.stash_end || 5}})...`);
          prevStashCurr = st.stash_curr;
        }}
      }} else if (prevStashCurr !== null) {{
        addLog('cất đồ', `✅ Đã hoàn tất chu kỳ cất đồ Kho ${{st.stash_start || 1}} -> ${{st.stash_end || 5}}!`, true);
        prevStashCurr = null;
      }}

      // 4. Dong bo DLC Lò Rèn
      if (st.dlc !== undefined) {{
        const isDlcUnlocked = (st.dlc === 1 || st.dlc === true);
        const badge = $('badgeDlc');
        const btn = $('btnUnlockDlc');
        if (isDlcUnlocked) {{
          badge.className = 'badge-status active';
          badge.textContent = 'ĐÃ MỞ KHÓA';
          btn.innerHTML = '✅ DLC LÒ RÈN ĐÃ ĐƯỢC MỞ KHÓA';
          btn.className = 'btn-action-dlc unlocked';
        }} else {{
          badge.className = 'badge-status';
          badge.textContent = 'Chưa mở khóa';
          btn.innerHTML = '🔓 MỞ KHÓA DLC LÒ RÈN (DÀNH CHO NGƯỜI CHƯA CÓ)';
          btn.className = 'btn-action-dlc';
        }}
      }}

      prevStatus = st;
    }}

    async function poll() {{
      try {{
        const res = await fetch(`${{API_BASE}}/status`, {{ cache: 'no-store' }});
        if (!res.ok) throw new Error('Game status not ok');
        const data = await res.json();
        render(data);
      }} catch (err) {{
        if (isOnline) {{
          addLog('warn', 'Mất kết nối với game DPS.exe. Đang thử kết nối lại...', true);
        }}
        isOnline = false;
        if (!offlineBannerDismissed) {{
          $('offlineNotice').style.display = 'flex';
        }}
        $('connBadge').className = 'chip off';
        $('connText').textContent = 'Chưa kết nối game';
        $('pidBadge').textContent = 'PID: -';
        $('badgeCombine').className = 'badge-status';
        $('badgeCombine').textContent = 'Chưa kết nối';
        $('badgeStash').className = 'badge-status';
        $('badgeStash').textContent = 'Chưa kết nối';
        $('badgeDlc').className = 'badge-status';
        $('badgeDlc').textContent = 'Chưa kết nối';
        $('logStatusText').textContent = 'CHƯA KẾT NỐI';
        $('logStatusText').style.color = '#ef4444';
      }}
    }}

    async function sendCommand(key, val) {{
      if (!isOnline) {{
        addLog('warn', 'Không thể gửi lệnh: Chưa kết nối tới game!');
        return;
      }}
      try {{
        const res = await fetch(`${{API_BASE}}/set?${{encodeURIComponent(key)}}=${{encodeURIComponent(val)}}`, {{ cache: 'no-store' }});
        if (res.ok) {{
          const data = await res.json();
          render(data);
        }}
      }} catch (err) {{
        addLog('warn', `Lỗi gửi lệnh đến game: ${{err.message}}`);
      }}
    }}

    // Handlers: Combine
    $('toggleCombine').onchange = async (e) => {{
      const on = e.target.checked;
      const m = $('combineMin').value || 5;
      $('badgeCombine').className = on ? 'badge-status active' : 'badge-status';
      $('badgeCombine').textContent = on ? `ĐANG BẬT (mỗi ${{m}}p)` : 'Đã tắt';
      addLog('hợp thành', on ? `ĐÃ BẬT Tự động Hợp Thành Xưởng (chu kỳ ${{m}} phút/lần)` : 'ĐÃ TẮT Tự động Hợp Thành Xưởng', true);
      await sendCommand('auto_comb', on ? '1' : '0');
    }};

    $('combineMin').onchange = async (e) => {{
      const m = Math.max(1, parseInt(e.target.value) || 5);
      e.target.value = m;
      addLog('cfg', `Cập nhật chu kỳ Hợp Thành Xưởng: ${{m}} phút`);
      await sendCommand('comb_min', m.toString());
    }};

    $('btnCombineNow').onclick = async () => {{
      addLog('hợp thành', 'Đang gửi lệnh kích hoạt Hợp Thành Xưởng...');
      try {{
        await sendCommand('combine', '1');
        addLog('hợp thành', '✅ ĐÃ KÍCH HOẠT HỢP THÀNH XƯỞNG THÀNH CÔNG!', true);
      }} catch (err) {{
        addLog('warn', 'Lỗi gửi lệnh hợp thành xưởng.');
      }}
    }};

    // Handlers: Stash
    $('toggleStash').onchange = async (e) => {{
      const on = e.target.checked;
      const s = $('stashSec').value || 60;
      const start = $('stashStart').value || 1;
      const end = $('stashEnd').value || 5;
      $('badgeStash').className = on ? 'badge-status active' : 'badge-status';
      $('badgeStash').textContent = on ? `ĐANG BẬT (mỗi ${{s}}s)` : 'Đã tắt';
      addLog('cất đồ', on ? `ĐÃ BẬT Tự động Cất Đồ (mỗi ${{s}} giây, Kho ${{start}} -> ${{end}})` : 'ĐÃ TẮT Tự động Cất Đồ', true);
      await sendCommand('auto_stash', on ? '1' : '0');
    }};

    $('stashSec').onchange = async (e) => {{
      const s = Math.max(2, parseInt(e.target.value) || 60);
      e.target.value = s;
      addLog('cfg', `Cập nhật chu kỳ cất đồ: ${{s}} giây`);
      await sendCommand('stash_sec', s.toString());
    }};

    $('stashStart').onchange = async (e) => {{
      const start = Math.max(1, parseInt(e.target.value) || 1);
      e.target.value = start;
      updateStashBtnLabel();
      addLog('cfg', `Cập nhật cấu hình: Bắt đầu cất từ Kho ${{start}}`);
      await sendCommand('stash_start', start.toString());
    }};

    $('stashEnd').onchange = async (e) => {{
      const end = Math.max(1, parseInt(e.target.value) || 5);
      e.target.value = end;
      updateStashBtnLabel();
      addLog('cfg', `Cập nhật cấu hình: Cất đến Kho ${{end}}`);
      await sendCommand('stash_end', end.toString());
    }};

    $('btnStashNow').onclick = async () => {{
      const s = $('stashStart').value || 1;
      const e = $('stashEnd').value || 5;
      addLog('cất đồ', `Đang gửi lệnh cất đồ tuần tự từ Kho ${{s}} đến Kho ${{e}}...`);
      try {{
        await sendCommand('stash', '1');
        addLog('cất đồ', `✅ ĐÃ KÍCH HOẠT CẤT ĐỒ KHO ${{s}} -> ${{e}} THÀNH CÔNG!`, true);
      }} catch (err) {{
        addLog('warn', 'Lỗi gửi lệnh cất đồ.');
      }}
    }};

    // Handler: Unlock DLC
    async function triggerUnlockDlc() {{
      if (!isOnline) {{
        addLog('warn', 'Không thể mở khóa DLC: Chưa kết nối tới game!');
        return;
      }}
      if (prevStatus && prevStatus.dlc === 1) {{
        addLog('dlc', 'DLC Lò Rèn đã được mở khóa trong game rồi.');
        return;
      }}
      addLog('dlc', 'Đang gửi lệnh mở khóa DLC Lò Rèn / Xưởng vào game...');
      try {{
        await sendCommand('dlc', '1');
        addLog('dlc', '✅ ĐÃ MỞ KHÓA DLC LÒ RÈN THÀNH CÔNG! Giờ bạn có thể mở Xưởng trong game để ghép đồ tự động.', true);
      }} catch (err) {{
        addLog('warn', 'Lỗi gửi lệnh mở khóa DLC.');
      }}
    }}

    // Initialization
    addLog('sys', 'Hệ thống DPS Auto Helper v1.0.0 đã sẵn sàng.');
    addLog('conn', 'Đang kết nối tới dịch vụ điều khiển ngầm...');
    updateStashBtnLabel();
    poll();
    setInterval(poll, 1000);
  </script>
</body>
</html>
"""

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {HTML_FILE} ({os.path.getsize(HTML_FILE)} bytes)")
