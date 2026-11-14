import os

BASE_DIR = r"C:\Users\Son\Desktop\dps-auto-helper"
ICON_B64_FILE = os.path.join(BASE_DIR, "game_icon_b64.txt")
HTML_FILE = os.path.join(BASE_DIR, "index.html")

with open(ICON_B64_FILE, "r", encoding="utf-8") as f:
    b64_icon = f.read().strip()

html_content = f"""<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>DPS Auto Helper - Tự Động Hóa Kho & Xưởng (Zero Coordinates)</title>
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
    }}

    /* Header */
    header {{
      background: rgba(13, 18, 28, 0.85);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--card-border);
      padding: 14px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 14px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
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

    /* Main Container */
    main {{
      max-width: 760px;
      width: 100%;
      margin: 0 auto;
      padding: 24px 16px 64px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}

    /* Offline Alert Navigation Banner */
    .offline-banner {{
      background: linear-gradient(135deg, rgba(239, 68, 68, 0.18) 0%, rgba(185, 28, 28, 0.08) 100%);
      border: 1px solid rgba(239, 68, 68, 0.4);
      border-radius: var(--radius-md);
      padding: 14px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      cursor: pointer;
      box-shadow: 0 4px 16px rgba(239, 68, 68, 0.12);
      transition: all 0.2s ease;
      user-select: none;
    }}
    .offline-banner:hover {{
      transform: translateY(-2px);
      border-color: rgba(239, 68, 68, 0.8);
      box-shadow: 0 6px 20px rgba(239, 68, 68, 0.22);
      background: linear-gradient(135deg, rgba(239, 68, 68, 0.24) 0%, rgba(185, 28, 28, 0.14) 100%);
    }}
    .offline-info {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .offline-icon {{
      font-size: 22px;
      animation: bounce 1.8s infinite;
    }}
    @keyframes bounce {{
      0%, 100% {{ transform: translateY(0); }}
      50% {{ transform: translateY(-4px); }}
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
    .btn-pill-action {{
      background: #ef4444;
      color: #fff;
      font-size: 11px;
      font-weight: 700;
      padding: 6px 12px;
      border-radius: var(--radius-full);
      white-space: nowrap;
      box-shadow: 0 0 10px rgba(239, 68, 68, 0.4);
      text-transform: uppercase;
      letter-spacing: 0.03em;
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
    }}
    .card:hover {{
      border-color: rgba(59, 130, 246, 0.35);
    }}

    /* Top Hero Card */
    .hero-card {{
      background: linear-gradient(145deg, rgba(24, 34, 52, 0.85) 0%, rgba(16, 22, 34, 0.95) 100%);
      border: 1px solid #334768;
      position: relative;
      overflow: hidden;
    }}
    .hero-card::before {{
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; height: 3px;
      background: linear-gradient(90deg, #3b82f6, #60a5fa, #10b981);
    }}
    .hero-header {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 16px;
    }}
    .hero-title h2 {{
      font-size: 17px;
      font-weight: 800;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .hero-title p {{
      font-size: 12px;
      color: var(--dim);
      margin-top: 4px;
      line-height: 1.45;
    }}
    .hero-features {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 18px;
    }}
    .feature-tag {{
      background: rgba(59, 130, 246, 0.12);
      border: 1px solid rgba(59, 130, 246, 0.3);
      color: #93c5fd;
      font-size: 11px;
      font-weight: 600;
      padding: 3px 10px;
      border-radius: var(--radius-full);
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    /* Horizontal Download Bar */
    .download-bar {{
      background: linear-gradient(135deg, rgba(20, 29, 44, 0.9) 0%, rgba(14, 20, 32, 0.95) 100%);
      border: 1px solid #384e72;
      border-radius: var(--radius-md);
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25);
      transition: all 0.2s ease;
    }}
    .download-bar:hover {{
      border-color: #3b82f6;
      box-shadow: 0 6px 20px rgba(59, 130, 246, 0.25);
    }}
    .file-info-group {{
      display: flex;
      align-items: center;
      gap: 14px;
      min-width: 0;
    }}
    .file-icon {{
      font-size: 26px;
      background: rgba(59, 130, 246, 0.15);
      border: 1px solid rgba(59, 130, 246, 0.35);
      border-radius: 12px;
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
      gap: 4px;
      min-width: 0;
    }}
    .file-name {{
      font-size: 14px;
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
      font-size: 11px;
    }}
    
    .btn-download-bar {{
      background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
      color: #ffffff;
      font-size: 14px;
      font-weight: 800;
      letter-spacing: 0.02em;
      padding: 12px 22px;
      border-radius: var(--radius-sm);
      border: 1px solid #60a5fa;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      text-decoration: none;
      box-shadow: 0 4px 16px rgba(37, 99, 235, 0.45);
      white-space: nowrap;
      flex-shrink: 0;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .btn-download-bar:hover {{
      background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
      transform: translateY(-2px);
      box-shadow: 0 6px 22px rgba(37, 99, 235, 0.65);
      border-color: #93c5fd;
    }}
    .btn-download-bar svg {{
      width: 18px;
      height: 18px;
      fill: currentColor;
    }}

    /* Full Modal Dialog Overlay */
    .modal-overlay {{
      position: fixed;
      inset: 0;
      z-index: 9999;
      background: rgba(4, 7, 13, 0.88);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 16px;
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
      max-width: 720px;
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
      padding: 16px 22px;
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
      padding: 22px;
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
      padding: 14px 16px;
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

    /* Automation Modules (F7 & F6) */
    .module-card {{
      position: relative;
    }}
    .module-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 18px;
      padding-bottom: 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }}
    .module-title {{
      font-size: 15px;
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
      padding: 5px 12px;
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
      padding: 16px 18px;
      margin-bottom: 18px;
      transition: border-color 0.2s ease;
    }}
    .switch-box:hover {{
      border-color: #3b82f6;
    }}
    .switch-desc h4 {{
      font-size: 14px;
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

    /* Config Form Rows */
    .config-row {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 16px;
      flex-wrap: wrap;
      background: rgba(13, 18, 27, 0.5);
      padding: 12px 16px;
      border-radius: var(--radius-sm);
      border: 1px solid #1c2738;
    }}
    .config-row label {{
      color: var(--dim);
      font-size: 13px;
      font-weight: 600;
    }}
    input[type=number] {{
      background: #090d14;
      border: 1px solid #2d3b50;
      color: #ffffff;
      padding: 8px 12px;
      border-radius: var(--radius-sm);
      font-weight: 700;
      font-size: 14px;
      text-align: center;
      transition: border-color 0.2s, box-shadow 0.2s;
    }}
    input[type=number]:focus {{
      outline: none;
      border-color: var(--primary);
      box-shadow: 0 0 10px var(--primary-glow);
    }}

    /* Action Buttons */
    .btn {{
      font-family: inherit;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.03em;
      padding: 12px 20px;
      border-radius: var(--radius-sm);
      border: 1px solid transparent;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.2s ease;
      text-decoration: none;
    }}
    .btn-action-f7 {{
      background: linear-gradient(135deg, #1e3a5f 0%, #172a44 100%);
      color: #60a5fa;
      border-color: #2b4c77;
      width: 100%;
    }}
    .btn-action-f7:hover {{
      background: linear-gradient(135deg, #254a78 0%, #1d3556 100%);
      border-color: #3b82f6;
      box-shadow: 0 4px 16px var(--primary-glow);
      color: #ffffff;
      transform: translateY(-1px);
    }}
    .btn-action-f6 {{
      background: linear-gradient(135deg, #133e29 0%, #0d281a 100%);
      color: #34d399;
      border-color: #1c583b;
      width: 100%;
    }}
    .btn-action-f6:hover {{
      background: linear-gradient(135deg, #195237 0%, #123725 100%);
      border-color: #10b981;
      box-shadow: 0 4px 16px var(--ok-glow);
      color: #ffffff;
      transform: translateY(-1px);
    }}

    /* Realtime Activity Notification */
    .activity-bar {{
      background: rgba(15, 23, 38, 0.9);
      backdrop-filter: blur(8px);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-md);
      padding: 12px 18px;
      font-size: 13px;
      color: var(--dim);
      display: flex;
      align-items: center;
      gap: 10px;
      min-height: 46px;
      transition: all 0.25s ease;
    }}
    .activity-bar.active {{
      background: rgba(16, 185, 129, 0.1);
      border-color: rgba(16, 185, 129, 0.35);
      color: #6ee7b7;
      font-weight: 600;
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
    }}

    /* Responsive */
    @media (max-width: 640px) {{
      header {{ padding: 12px 16px; }}
      .brand-titles h1 {{ font-size: 14px; }}
      main {{ padding: 16px 12px 48px; gap: 16px; }}
      .card {{ padding: 16px; }}
      .download-bar {{ flex-direction: column; align-items: stretch; gap: 12px; }}
      .config-row {{ flex-direction: column; align-items: flex-start; gap: 8px; }}
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
        <div class="brand-badge">⚡ Auto Helper • Zero Coordinates</div>
      </div>
    </a>
    <div class="header-status">
      <span id="pidBadge" class="chip">PID: -</span>
      <span id="connBadge" class="chip off">
        <span class="pulse-dot"></span>
        <span id="connText">Chưa kết nối game</span>
      </span>
    </div>
  </header>

  <main>

    <!-- Interactive Offline Navigation Banner (Opens Modal) -->
    <div id="offlineNotice" class="offline-banner" onclick="openDownloadModal()">
      <div class="offline-info">
        <span class="offline-icon">⚠️</span>
        <div class="offline-text">
          <h4>Chưa phát hiện game DPS đang chạy!</h4>
          <p>Bấm vào đây để mở bảng tải tool 1-Click &amp; xem hướng dẫn cài đặt ⬇️</p>
        </div>
      </div>
      <span class="btn-pill-action">Tải Tool &amp; Hướng Dẫn ⬇</span>
    </div>

    <!-- Activity Notification Bar -->
    <div id="actBar" class="activity-bar">
      <span>💬</span>
      <span id="actMsg">Sẵn sàng nhận lệnh điều khiển.</span>
    </div>

    <!-- TOP HERO SECTION: DOWNLOAD TOOL & MODAL TRIGGER -->
    <div id="heroDownloadCard" class="card hero-card">
      <div class="hero-header">
        <div class="hero-title">
          <h2><span>🚀</span> Gói Cài Đặt Tự Động Hóa 1-Click</h2>
          <p>Chuẩn Zero Coordinates: Điều khiển thông qua logic C# IL2CPP ngầm bên trong game. Tuyệt đối không chiếm chuột, không dùng macro giả lập, chạy ổn định bất kể độ phân giải màn hình.</p>
        </div>
      </div>

      <div class="hero-features">
        <span class="feature-tag">🛡️ Không chiếm chuột</span>
        <span class="feature-tag">🎯 Zero Coordinates</span>
        <span class="feature-tag">⚡ 1-Click Auto Install</span>
        <span class="feature-tag">💾 Tự lưu vĩnh viễn</span>
      </div>

      <!-- Hàng ngang thông tin file & nút bấm mở modal tải -->
      <div class="download-bar">
        <div class="file-info-group">
          <div class="file-icon">📦</div>
          <div class="file-details">
            <div class="file-name">DPS_Auto_Helper_1Click.zip</div>
            <div class="file-meta">
              <span class="meta-tag">57.19 MB</span>
              <span class="meta-tag">v1.0.0</span>
              <span class="meta-desc">Tự động nhận diện Steam &amp; Cài đặt trong 2 giây</span>
            </div>
          </div>
        </div>
        <button class="btn-download-bar" onclick="openDownloadModal()">
          <svg viewBox="0 0 24 24"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM17 13l-5 5-5-5h3V9h4v4h3z"/></svg>
          <span>TẢI MOD &amp; HƯỚNG DẪN</span>
        </button>
      </div>
    </div>

    <!-- MODULE 1: AUTO COMBINE F7 -->
    <div class="card module-card" style="border-top: 3px solid #3b82f6;">
      <div class="module-header">
        <div class="module-title" style="color: #60a5fa;">
          <span>🔨</span> Tự Động Hợp Thành Xưởng (F7)
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

      <button id="btnCombineNow" class="btn btn-action-f7">
        🔨 HỢP THÀNH XƯỞNG NGAY LẬP TỨC (F7)
      </button>
    </div>

    <!-- MODULE 2: AUTO STASH F6 -->
    <div class="card module-card" style="border-top: 3px solid #10b981;">
      <div class="module-header">
        <div class="module-title" style="color: #34d399;">
          <span>📦</span> Tự Động Cất Đồ Vào Kho (F6)
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

      <button id="btnStashNow" class="btn btn-action-f6">
        📦 CẤT ĐỒ VÀO KHO 1 -> 5 NGAY LẬP TỨC (F6)
      </button>
    </div>

  </main>

  <!-- FULL SCREEN MODAL DIALOG: DOWNLOAD & STEP-BY-STEP GUIDE -->
  <div id="modalDownload" class="modal-overlay" onclick="handleOverlayClick(event)">
    <div class="modal-dialog">
      <div class="modal-header">
        <h3><span>📦</span> Cài Đặt &amp; Tải Mod Tự Động Hóa 1-Click</h3>
        <button class="modal-close" onclick="closeDownloadModal()">✕</button>
      </div>
      <div class="modal-body">
        
        <!-- Hàng ngang tải file nổi bật -->
        <div class="download-bar" style="background:#141d2c; border-color:#38527a;">
          <div class="file-info-group">
            <div class="file-icon">📦</div>
            <div class="file-details">
              <div class="file-name">DPS_Auto_Helper_1Click.zip</div>
              <div class="file-meta">
                <span class="meta-tag">57.19 MB</span>
                <span class="meta-tag">v1.0.0</span>
                <span class="meta-desc">Trọn gói BepInEx 6 + Mod F6/F7</span>
              </div>
            </div>
          </div>
          <div style="display:flex; flex-direction:column; gap:6px; align-items:flex-end;">
            <a href="https://github.com/titlee2111/dps-auto-helper/releases/download/v1.0.0/DPS_Auto_Helper_1Click.zip" class="btn-download-bar">
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
              <p>Khởi động game <code>DPS Desktop Pension Squad</code> bình thường qua Steam. Sau đó quay lại trang web này, góc phải trên cùng sẽ chuyển sang <b>🟢 ĐÃ KẾT NỐI GAME</b> và bạn có thể bật/tắt F6, F7 tùy ý!</p>
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
          <button class="btn" style="background:#1e293b; color:#94a3b8; border:1px solid #334155;" onclick="closeDownloadModal()">
            Đã Hiểu, Đóng Lại
          </button>
        </div>

      </div>
    </div>
  </div>

  <footer>
    DPS Auto Helper • Zero Coordinates (Native C# IL2CPP) • Hoàn toàn không chiếm chuột • Tự động lưu cấu hình vĩnh viễn
  </footer>

  <script>
    const $ = id => document.getElementById(id);
    const API_BASE = 'http://127.0.0.1:47900';

    let isOnline = false;

    // Modal Control Functions
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

    document.addEventListener('keydown', e => {{
      if (e.key === 'Escape' && $('modalDownload').classList.contains('active')) {{
        closeDownloadModal();
      }}
    }});

    function notify(text, isActive = false) {{
      $('actMsg').textContent = text;
      $('actBar').className = isActive ? 'activity-bar active' : 'activity-bar';
    }}

    function updateStashBtnLabel() {{
      const s = $('stashStart').value || 1;
      const e = $('stashEnd').value || 5;
      $('btnStashNow').textContent = `📦 CẤT ĐỒ VÀO KHO ${{s}} -> ${{e}} NGAY LẬP TỨC (F6)`;
    }}

    // Realtime Game Sync
    function render(st) {{
      isOnline = true;
      $('offlineNotice').style.display = 'none';
      $('connBadge').className = 'chip on';
      $('connText').textContent = 'Đã kết nối game';
      $('pidBadge').textContent = 'PID: ' + (st.pid || '-');

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

      if (st.stash_step && st.stash_step > 0) {{
        notify(`⏳ Đang cất đồ vào Kho ${{st.stash_curr || 1}} (Kho ${{st.stash_start || 1}} -> ${{st.stash_end || 5}})...`, true);
      }}
    }}

    async function poll() {{
      try {{
        const res = await fetch(`${{API_BASE}}/status`, {{ cache: 'no-store' }});
        if (!res.ok) throw new Error('Game status not ok');
        const data = await res.json();
        render(data);
      }} catch (err) {{
        isOnline = false;
        $('offlineNotice').style.display = 'flex';
        $('connBadge').className = 'chip off';
        $('connText').textContent = 'Chưa kết nối game';
        $('pidBadge').textContent = 'PID: -';
        $('badgeCombine').className = 'badge-status';
        $('badgeCombine').textContent = 'Chưa kết nối';
        $('badgeStash').className = 'badge-status';
        $('badgeStash').textContent = 'Chưa kết nối';
      }}
    }}

    async function sendCommand(key, val) {{
      if (!isOnline) {{
        notify('⚠️ Game chưa mở hoặc chưa cài mod!', false);
        return;
      }}
      try {{
        const res = await fetch(`${{API_BASE}}/set?${{encodeURIComponent(key)}}=${{encodeURIComponent(val)}}`, {{ cache: 'no-store' }});
        if (res.ok) {{
          const data = await res.json();
          render(data);
        }}
      }} catch (err) {{
        notify('⚠️ Lỗi gửi lệnh đến game: ' + err.message, false);
      }}
    }}

    // Handlers: Combine
    $('toggleCombine').onchange = async (e) => {{
      const on = e.target.checked;
      const m = $('combineMin').value || 5;
      $('badgeCombine').className = on ? 'badge-status active' : 'badge-status';
      $('badgeCombine').textContent = on ? `ĐANG BẬT (mỗi ${{m}}p)` : 'Đã tắt';
      notify(on ? `ĐÃ BẬT Tự động Hợp Thành (mỗi ${{m}} phút khi mở xưởng)!` : 'ĐÃ TẮT Tự động Hợp Thành!', true);
      await sendCommand('auto_comb', on ? '1' : '0');
    }};

    $('combineMin').onchange = async (e) => {{
      const m = Math.max(1, parseInt(e.target.value) || 5);
      e.target.value = m;
      await sendCommand('comb_min', m.toString());
      notify(`Đã cập nhật chu kỳ Hợp Thành: ${{m}} phút.`, true);
    }};

    $('btnCombineNow').onclick = async () => {{
      notify('Đang kiểm tra bảng Xưởng & kích hoạt ghép đồ lặp lại...', true);
      try {{
        await sendCommand('combine', '1');
        notify('ĐÃ KÍCH HOẠT HỢP THÀNH XƯỞNG THÀNH CÔNG (F7)!', true);
      }} catch (err) {{
        notify('Lỗi gửi lệnh ghép đồ.', false);
      }}
    }};

    // Handlers: Stash
    $('toggleStash').onchange = async (e) => {{
      const on = e.target.checked;
      const s = $('stashSec').value || 60;
      $('badgeStash').className = on ? 'badge-status active' : 'badge-status';
      $('badgeStash').textContent = on ? `ĐANG BẬT (mỗi ${{s}}s)` : 'Đã tắt';
      notify(on ? `ĐÃ BẬT Tự động Cất Đồ (mỗi ${{s}} giây)!` : 'ĐÃ TẮT Tự động Cất Đồ!', true);
      await sendCommand('auto_stash', on ? '1' : '0');
    }};

    $('stashSec').onchange = async (e) => {{
      const s = Math.max(2, parseInt(e.target.value) || 60);
      e.target.value = s;
      await sendCommand('stash_sec', s.toString());
      notify(`Đã cập nhật chu kỳ Cất Đồ: ${{s}} giây.`, true);
    }};

    $('stashStart').onchange = async (e) => {{
      const start = Math.max(1, parseInt(e.target.value) || 1);
      e.target.value = start;
      updateStashBtnLabel();
      await sendCommand('stash_start', start.toString());
      notify(`Đã cập nhật cất từ Kho: ${{start}}`, true);
    }};

    $('stashEnd').onchange = async (e) => {{
      const end = Math.max(1, parseInt(e.target.value) || 5);
      e.target.value = end;
      updateStashBtnLabel();
      await sendCommand('stash_end', end.toString());
      notify(`Đã cập nhật cất đến Kho: ${{end}}`, true);
    }};

    $('btnStashNow').onclick = async () => {{
      const s = $('stashStart').value || 1;
      const e = $('stashEnd').value || 5;
      notify(`Đang kích hoạt cất đồ tuần tự Kho ${{s}} -> Kho ${{e}}...`, true);
      try {{
        await sendCommand('stash', '1');
        notify(`ĐÃ KÍCH HOẠT CẤT ĐỒ KHO ${{s}} -> ${{e}} THÀNH CÔNG (F6)!`, true);
      }} catch (err) {{
        notify('Lỗi gửi lệnh cất đồ.', false);
      }}
    }};

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
