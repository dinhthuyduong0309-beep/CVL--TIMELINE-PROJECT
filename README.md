# Tiến độ dự án Tái cấu trúc – Cửu Vân Long

Kho lưu trữ trang theo dõi tiến độ của Ban Tái cấu trúc (buffet hải sản Cửu Vân Long).

- **Trang làm việc hằng ngày:** <https://dinhthuyduong0309-beep.github.io/cvl-timeline/>. Cả nhóm sửa trực tiếp, dữ liệu tự lưu vào Google Sheets "Tiến độ TCT CVL – dữ liệu" (tab `Tasks`) và tự đồng bộ 30 giây/lần.
- Trang cũ trên Claude (<https://claude.ai/artifact/KGFFAaVqw318vQpT2jexoN>) không còn dùng để cập nhật.
- **Repo này** giữ mã nguồn trang cùng các bản chụp dữ liệu theo thời điểm. Mỗi commit là một mốc để đối chiếu xem tiến độ đã thay đổi thế nào.

## Nội dung

| File | Mô tả |
|---|---|
| `index.html` | Trang Gantt chạy trên GitHub Pages, đọc/ghi dữ liệu qua Google Sheets. |
| `tracker.html` | Bản trang dùng trên Claude (cũ). |
| `data/tien-do.csv` | Bản chụp tiến độ, mở được bằng Excel (UTF-8). |
| `data/tien-do.json` | Cùng dữ liệu đó ở dạng JSON, có ghi thời điểm chụp. |

## Xem lịch sử thay đổi

- Vào tab **Commits** để xem từng lần cập nhật.
- Mở `data/tien-do.csv` rồi bấm **History** để so sánh các bản chụp theo từng dòng công việc.

## Lưu mốc dữ liệu

Dữ liệu sống nằm trong Google Sheets. Muốn lưu một mốc vào repo, vào Google Sheets → File → Tải xuống → CSV rồi tải lên thư mục `data/`.
