# Tiến độ dự án Tái cấu trúc – Cửu Vân Long

Kho lưu trữ trang theo dõi tiến độ của Ban Tái cấu trúc (buffet hải sản Cửu Vân Long).

- **Trang làm việc hằng ngày:** <https://claude.ai/artifact/KGFFAaVqw318vQpT2jexoN>. Cả nhóm cập nhật tiến độ tại đây và dữ liệu tự lưu.
- **Repo này** giữ mã nguồn trang cùng các bản chụp dữ liệu theo thời điểm. Mỗi commit là một mốc để đối chiếu xem tiến độ đã thay đổi thế nào.

## Nội dung

| File | Mô tả |
|---|---|
| `tracker.html` | Mã nguồn trang tiến độ (Gantt, công việc nhiều cấp, cột ghi chú). Khi mở trực tiếp ngoài Claude, trang chỉ lưu trên trình duyệt của máy đang mở. |
| `data/tien-do.csv` | Bản chụp tiến độ, mở được bằng Excel (UTF-8). |
| `data/tien-do.json` | Cùng dữ liệu đó ở dạng JSON, có ghi thời điểm chụp. |

## Xem lịch sử thay đổi

- Vào tab **Commits** để xem từng lần chụp dữ liệu.
- Mở `data/tien-do.csv` rồi bấm **History** để so sánh các bản chụp theo từng dòng công việc.

## Cập nhật bản chụp

Nhờ Claude: *"cập nhật bản chụp tiến độ CVL lên GitHub"*. Claude sẽ đọc dữ liệu mới nhất trên trang, ghi đè `data/` và tạo commit mới.
