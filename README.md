# Panda HSK Studio — bản sửa PDF/audio (v3)

Ứng dụng luyện HSK độc lập. Giao diện gấu trúc, tre, núi và dấu son.

## Chạy và triển khai

- Giải nén toàn bộ, giữ nguyên thư mục assets và vendor.
- Chạy `python3 -m http.server 4173`, mở http://localhost:4173 . Không mở index.html bằng file:// vì trình đọc PDF dùng JavaScript modules.
- Vercel: Framework Preset Other, không cần install/build command, Output Directory để trống (gốc dự án). Upload/push toàn bộ nội dung, không chỉ index.html.
- Bản này chưa được triển khai lên tài khoản Vercel do kết nối trước đó chưa có quyền tạo dự án.

## Sửa lỗi

- PDF nguồn đặt X-Frame-Options: SAMEORIGIN, khiến iframe trên domain khác bị chặn. Thay iframe bằng PDF.js được đóng gói nội bộ, đọc PDF cùng origin.
- 6 PDF và 6 MP3 có sẵn trong assets/exams. Audio giải nén từ gói chính thức, chuyển mono MP3 48 kbps / 32 kHz để giảm dung lượng; không đổi tốc độ và không cắt nội dung.
- Audio phát trực tiếp, điều khiển tốc độ, lưu vị trí nghe, báo lỗi và tải lại.
- PDF có chuyển trang, phóng to/thu nhỏ, báo lỗi, tải lại; vẫn cho mở tab riêng/tải và chọn file cá nhân.
- Không phụ thuộc CDN cho PDF.js hoặc Google Fonts. CMap và font dự phòng của PDF.js được đóng gói cùng app.
- Giữ namespace hsk-studio-v2 để bảo toàn lịch sử và bài làm cũ.

## Tài liệu

Nguồn: https://old.chinesetest.cn/godownload.do
Các bản PDF: https://old.chinesetest.cn/userfiles/file/HSK/level{1..6}/{mã đề}.pdf
Gói audio tương ứng có đuôi .rar. Tải ngày 09/11/2026.
Các mã: H10901, H20901, H31001, H41001, H51001, H61001.
Nội dung đề thuộc đơn vị phát hành; ứng dụng không liên kết với Chinese Test. Giấy phép Apache 2.0 của PDF.js tại vendor/PDFJS-LICENSE.

## Giới hạn

- Bộ đề HSK hệ 2.0. Chỉ H31001 chấm tự động 70 câu khách quan; phần viết và các đề khác tự đối chiếu PDF.
- Đây là chế độ luyện đề giấy với đồng hồ tổng; chưa mô phỏng khóa từng phần kỳ thi máy.
- Bài làm chỉ lưu ở trình duyệt hiện tại. Có thể xuất JSON/CSV.
- Trình đọc PDF dùng canvas; có link PDF gốc để dùng trình đọc tài liệu phù hợp nhu cầu hỗ trợ tiếp cận.
- Đã kiểm tra file PDF, giải mã toàn bộ MP3, thời lượng, đường dẫn tài nguyên, logic dữ liệu và cú pháp JS. Kiểm thử tương tác trình duyệt bản v3 chưa hoàn thành do giới hạn truy cập của môi trường xem thử.
