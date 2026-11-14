# DPS Auto Helper (Web Controller & 1-Click Mod)

> Công cụ hỗ trợ tự động hóa dành riêng cho game **DPS Desktop Pension Squad** hoạt động ngầm thông qua logic C# nội bộ (Zero Coordinates), không chiếm chuột, không sợ lệch màn hình.

---

## 🌟 Tính Năng Trên Trang Web (Chỉ Dành Cho Tự Động Hóa)
1. **📦 Tự động Cất Đồ Vào Kho (F6):**
   - Bật / Tắt cất đồ định kỳ theo chu kỳ giây (Mặc định 60s, tùy chỉnh từ 2s đến 600s).
   - Tùy chỉnh phạm vi kho cất đồ (Kho bắt đầu -> Kho kết thúc, ví dụ Kho 1 -> Kho 5 hoặc Kho 1 -> Kho 4).
   - Nút cất đồ thủ công ngay lập tức bằng 1 chạm.
2. **🔨 Tự động Hợp Thành Xưởng (F7):**
   - Bật / Tắt lặp lại công thức chế tạo trong Xưởng định kỳ theo chu kỳ phút (Mặc định 5 phút).
   - Nút kích hoạt ghép đồ thủ công ngay lập tức.
3. **🛡️ An toàn & Độc lập:**
   - Đã loại bỏ hoàn toàn các chức năng can thiệp cheat (God mode, Dame, Tốc đánh, Mở hộp, Mở khóa DLC...).
   - Chỉ giữ lại 2 tính năng tự động tiện ích để chia sẻ cho bạn bè an toàn và minh bạch.

---

## 🚀 Hướng Dẫn Đưa Lên GitHub Pages (Dành Cho Chủ Sở Hữu)

1. **Tạo Repository mới trên GitHub:**
   - Vào [GitHub](https://github.com) -> New repository (ví dụ đặt tên là `dps-auto-helper`).
   - Đặt là **Public**.

2. **Đưa toàn bộ thư mục này lên GitHub:**
   - Các file cần có:
     - `index.html` (Giao diện web)
     - `DPS_Auto_Helper_1Click.zip` (Gói cài mod 1-click cho bạn bè)
     - `README.md`
   - Bạn có thể kéo thả trực tiếp các file này vào GitHub hoặc dùng lệnh git:
     ```bash
     git init
     git add .
     git commit -m "feat: initial dps auto helper with 1-click bundle"
     git branch -M main
     git remote add origin https://github.com/<tai-khoan-cua-ban>/dps-auto-helper.git
     git push -u origin main
     ```

3. **Bật GitHub Pages:**
   - Vào mục **Settings** của repository -> Chọn menu **Pages** ở cột trái.
   - Tại mục **Build and deployment** -> **Branch**: Chọn nhánh `main` và thư mục `/ (root)`.
   - Bấm **Save**. Chờ khoảng 1-2 phút, GitHub sẽ tạo đường link dạng:
     `https://<tai-khoan-cua-ban>.github.io/dps-auto-helper/`

---

## 🎮 Hướng Dẫn Dành Cho Bạn Bè Khi Sử Dụng

1. Bạn bè truy cập vào link GitHub Pages của bạn:
   `https://<tai-khoan-cua-ban>.github.io/dps-auto-helper/`
2. Bấm nút màu xanh to **"📥 TẢI MOD HỖ TRỢ 1-CLICK (.ZIP)"** trên web để tải gói cài đặt.
3. Giải nén file zip -> Chạy file `Cai_Dat_Tu_Dong.bat` (Tool sẽ tự động nhận diện thư mục cài game Steam và chép mod vào trong 2 giây).
4. Mở game **DPS Desktop Pension Squad** qua Steam.
5. Quay lại trang web điều khiển: Lúc này web sẽ hiển thị **🟢 ĐÃ KẾT NỐI GAME** và có thể bật/tắt F6, F7 tùy thích!
