# ⚡ DPS Auto Helper - Web Controller & 1-Click Mod
> **Zero Coordinates Automation Tool for DPS Desktop Pension Squad**  
> *Hỗ trợ tự động hóa Xưởng & Kho hoàn toàn ngầm qua C# IL2CPP, không chiếm chuột, không sợ lệch màn hình.*

[ Tiếng Việt ](#-tiếng-việt) | [ English ](#-english)

---

## 🇻🇳 TIẾNG VIỆT

### 📖 Giới Thiệu
**DPS Auto Helper** là công cụ hỗ trợ tự động hóa được thiết kế riêng cho game **DPS Desktop Pension Squad**. Điểm khác biệt lớn nhất so với các auto clicker thông thường là công cụ này sử dụng kiến trúc **Zero Coordinates (Không dùng tọa độ màn hình)**:
- Gọi trực tiếp vào logic mã nguồn C# nội bộ của game thông qua BepInEx 6 IL2CPP.
- Tuyệt đối **không chiếm chuột**, bạn có thể vừa chơi game vừa lướt web, làm việc hoặc treo máy thoải mái.
- Không bị ảnh hưởng bởi độ phân giải màn hình, tỷ lệ thu phóng (DPI scale) hay khi di chuyển cửa sổ game.
- Đã loại bỏ hoàn toàn các chức năng can thiệp game (God mode, Dame, Aspd, DLC,...) nhằm đảm bảo tính an toàn, minh bạch và giải trí lành mạnh cho bạn bè.

---

### ✨ Tính Năng Nổi Bật
1. **📦 Tự Động Cất Đồ Vào Kho (F6):**
   - Tự động cất đồ từ túi đồ cá nhân tuần tự vào các ngăn kho đã chọn.
   - **Tùy chỉnh phạm vi kho:** Có thể chọn cất từ Kho nào đến Kho nào (Ví dụ: Kho 1 -> Kho 5, hoặc Kho 2 -> Kho 4).
   - **Tùy chỉnh chu kỳ chạy:** Cài đặt số giây giữa mỗi lần cất đồ (Mặc định 60 giây, tùy chỉnh từ 2s đến 600s).
   - Nút **📦 Cất Đồ Vào Kho Ngay** để kích hoạt thủ công lập tức bằng 1 click.

2. **🔨 Tự Động Hợp Thành Xưởng (F7):**
   - Tự động mở bảng Xưởng, tự động điền nguyên liệu và lặp lại công thức chế tạo đã thiết lập.
   - **Tùy chỉnh chu kỳ chạy:** Cài đặt số phút giữa mỗi lần ghép đồ (Mặc định 5 phút).
   - Nút **🔨 Hợp Thành Xưởng Ngay** để kích hoạt ghép đồ thủ công lập tức bằng 1 click.

3. **🌐 Điều Khiển Qua Web Độc Lập:**
   - Hoạt động trực tiếp trên trình duyệt thông qua GitHub Pages hoặc file HTML nội bộ.
   - Hiển thị trạng thái kết nối game thời gian thực (PID, Port 47900, trạng thái Bật/Tắt).
   - Mọi cấu hình thời gian và kho đều được tự động lưu vĩnh viễn vào game.

---

### 📥 Hướng Dẫn Cài Đặt (3 Bước 1-Click)

1. **Bước 1: Tải Gói Mod 1-Click**
   - Bấm vào nút **"📥 TẢI MOD HỖ TRỢ 1-CLICK (.ZIP)"** trên trang web hoặc tải file `DPS_Auto_Helper_1Click.zip` từ mục Releases.
2. **Bước 2: Cài Đặt Tự Động**
   - Giải nén file zip vừa tải về ra một thư mục.
   - Nhấp đúp chuột chạy file **`Cai_Dat_Tu_Dong.bat`**. Tool sẽ tự động dò tìm thư mục Steam cài game của bạn và sao chép các file cần thiết trong 2 giây.
3. **Bước 3: Mở Game & Điều Khiển**
   - Khởi động game **DPS Desktop Pension Squad** bình thường qua Steam.
   - Mở trang web điều khiển trên trình duyệt (trang GitHub Pages này) để bắt đầu sử dụng!

*Gỡ cài đặt:* Nếu không muốn dùng nữa, chỉ cần chạy file **`Go_Cai_Dat.bat`** để xóa sạch mod và đưa game về nguyên bản 100%.

---
---

## 🇬🇧 ENGLISH

### 📖 Introduction
**DPS Auto Helper** is an advanced automation assistant designed specifically for **DPS Desktop Pension Squad**. Unlike traditional screen-coordinate macro tools or auto clickers, this tool adopts a **Zero Coordinates** design:
- Interacts directly with internal C# IL2CPP game routines via BepInEx 6.
- **Never hijacks your mouse cursor** — you can seamlessly browse the web, work, or multitask while the game is automated in the background.
- Completely immune to screen resolution changes, multi-monitor setups, DPI scaling, and window repositioning.
- All cheat features (God mode, Damage multipliers, Aspd, DLC unlockers) have been completely removed, ensuring a clean, safe, and quality-of-life utility to share with friends.

---

### ✨ Key Features
1. **📦 Auto-Stash Items to Storage (F6):**
   - Automatically transfers inventory items into designated storage tabs sequentially.
   - **Customizable Tab Range:** Configure start and end tabs (e.g., Tab 1 to 5, or Tab 2 to 4).
   - **Customizable Interval:** Set interval in seconds (Default: 60s, configurable from 2s to 600s).
   - Quick Action button: **📦 Stash Now** for instantaneous 1-click execution.

2. **🔨 Auto-Combine Workshop Recipes (F7):**
   - Automatically activates workshop repeating synthesis based on your prepared recipe.
   - **Customizable Interval:** Set interval in minutes (Default: 5 minutes).
   - Quick Action button: **🔨 Combine Now** for instantaneous 1-click execution.

3. **🌐 Web-Based Realtime Controller:**
   - Fully accessible via any web browser on GitHub Pages or local HTML.
   - Real-time connection feedback (PID detection, IPC port 47900, sync status badges).
   - All settings and timers persist across game restarts.

---

### 📥 1-Click Quick Setup Guide

1. **Step 1: Download 1-Click Bundle**
   - Click the green button **"📥 TẢI MOD HỖ TRỢ 1-CLICK (.ZIP)"** on the web page or download `DPS_Auto_Helper_1Click.zip`.
2. **Step 2: Run Automatic Installer**
   - Extract the downloaded ZIP archive into any folder.
   - Double-click **`Cai_Dat_Tu_Dong.bat`**. The installer automatically discovers your Steam game directory and installs the mod files in 2 seconds.
3. **Step 3: Launch Game & Control**
   - Start **DPS Desktop Pension Squad** via Steam.
   - Return to the web page: it will display **🟢 ĐÃ KẾT NỐI GAME (Connected)** and you are ready to go!

*Uninstall:* Run **`Go_Cai_Dat.bat`** at any time to cleanly remove all mod files and restore the game to its pristine vanilla state.

---

### 🔒 Security & Privacy Notice
- The mod communicates strictly locally over `http://127.0.0.1:47900`.
- No external network connections, telemetry, or remote servers are involved.
- Zero risk of malware or account compromise.
