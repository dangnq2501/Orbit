import os
import time
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

# Đọc biến môi trường
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

CSV_FILENAME = os.getenv("CSV_FILENAME")
CSV_DIR = os.getenv("CSV_DIR", "/app/data")
TABLE_NAME = os.getenv("TABLE_NAME")

# Tạo chuỗi kết nối
engine_url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

print("⏳ Waiting for PostgreSQL to be ready...")
time.sleep(10)

# Đọc file CSV
csv_path = os.path.join(CSV_DIR, CSV_FILENAME)
df = pd.read_csv(csv_path)

# Ghi dữ liệu vào PostgreSQL
engine = create_engine(engine_url)
df.to_sql(TABLE_NAME, engine, index=False, if_exists="replace")

print(f"✅ Data loaded to table '{TABLE_NAME}' successfully!")