"""Tạo data/tien-do.json và data/tien-do.csv từ thư mục JSON xuất từ trang tiến độ.
Cách dùng: python scripts/snapshot.py <thư_mục_chứa_các_file_task_json>
"""
import json, glob, csv, sys, os, datetime
src = sys.argv[1]
T = {}
for f in glob.glob(os.path.join(src, "*.json")):
    j = json.load(open(f, encoding="utf-8")); d = j.get("data", j); d["id"] = d.get("id") or j.get("id"); T[d["id"]] = d
ROMAN = ["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII"]
kids = lambda p: sorted([t for t in T.values() if (t.get("parentId") or "") == p], key=lambda t: t.get("order", 0))
out = []
def walk(p, depth, prefix):
    for i, t in enumerate(kids(p)):
        w = (ROMAN[i] if i < len(ROMAN) else str(i+1)) if depth == 0 else f"{prefix}.{i+1}"
        out.append(dict(wbs=w, cap=depth+1, **{k: t.get(k, "") for k in ["id","parentId","name","owner","start","due","dueNote","progress","status","weeklyResult","nextAction","note","updatedAt"]}))
        walk(t["id"], depth+1, w)
walk("", 0, "")
snap = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7))).strftime("%Y-%m-%d %H:%M")
os.makedirs("data", exist_ok=True)
json.dump({"snapshot": snap, "source": "https://claude.ai/artifact/KGFFAaVqw318vQpT2jexoN", "tasks": out}, open("data/tien-do.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
H = ["WBS","Cấp","Tên công việc","Phụ trách","Bắt đầu","Thời hạn","Hạn (ghi chú)","% Hoàn thành","Trạng thái","Kết quả tuần","Hành động tiếp theo","Ghi chú","Sửa lần cuối"]
with open("data/tien-do.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(H)
    for t in out:
        w.writerow([t["wbs"],t["cap"],t["name"],t["owner"],t["start"],t["due"],t["dueNote"],t["progress"],t["status"],t["weeklyResult"],t["nextAction"],t["note"],t["updatedAt"]])
print(len(out), "dòng · chụp lúc", snap)
