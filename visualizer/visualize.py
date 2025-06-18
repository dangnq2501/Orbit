import os
import json
import psycopg2
from dotenv import load_dotenv
from collections import defaultdict
from core.utils import genLocation
from core.prepareGraph import prepareGraph

# Load biến môi trường
load_dotenv()

# Kết nối PostgreSQL
conn = psycopg2.connect(os.getenv("DB_URL"))
cur = conn.cursor()

# Lấy dữ liệu from, to, value_eth
cur.execute('SELECT "from", "to", value_eth FROM walletall WHERE "from" IS NOT NULL AND "to" IS NOT NULL')
rows = cur.fetchall()

# Xử lý dữ liệu
node_set = set()
edge_map = defaultdict(float)  # (from, to) -> tổng value_eth

for from_addr, to_addr, value_eth in rows:
    from_addr = from_addr.strip()
    to_addr = to_addr.strip()

    if not from_addr or not to_addr:
        continue

    node_set.add(from_addr)
    node_set.add(to_addr)
    edge_map[(from_addr, to_addr)] += value_eth if value_eth else 0

# Tạo dữ liệu cho JSON
jsoned = {"nodes": [], "edges": []}
done_nodes = set()
done_edges = set()
edge_id = 0

for node in node_set:
    x, y = genLocation()
    jsoned["nodes"].append({
        "label": node,
        "x": x,
        "y": y,
        "id": f"id={node}",
        "size": 10  # Có thể thay bằng số giao dịch nếu muốn
    })
    done_nodes.add(node)

for (from_addr, to_addr), value in edge_map.items():
    if from_addr not in done_nodes or to_addr not in done_nodes:
        continue
    key = f"{from_addr}:{to_addr}"
    if key in done_edges:
        continue
    size = min(value, 20)
    jsoned["edges"].append({
        "source": f"id={from_addr}",
        "target": f"id={to_addr}",
        "id": edge_id,
        "size": size / 3 if size > 3 else size
    })
    done_edges.add(key)
    edge_id += 1

# Ghi file JSON.js để quark.html load
output_path = os.path.join(os.path.dirname(__file__), "libs", "graph.json.js")
prepareGraph(output_path, json.dumps(jsoned))

print("✅ Đã tạo dữ liệu đồ thị.")
print("🌐 Mở visualizer/quark.html để xem mạng giao dịch.")
