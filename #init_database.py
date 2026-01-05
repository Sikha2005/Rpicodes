import sqlite3

conn = sqlite3.connect("iot_data.db")
cursor = conn.cursor()

# Table for LIVE sensor data
cursor.execute("""
CREATE TABLE IF NOT EXISTS live_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    temperature REAL,
    humidity REAL,
    gas REAL
)
""")

# Table for PREDICTED data
cursor.execute("""
CREATE TABLE IF NOT EXISTS predicted_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    sensor_type TEXT,
    predicted_value REAL
)
""")
conn.commit()
conn.close()

print(" SQLite database initialized successfully")