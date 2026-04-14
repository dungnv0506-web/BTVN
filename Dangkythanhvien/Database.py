import sqlite3

def connect_db():
    return sqlite3.connect("users.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ho TEXT,
        ten TEXT,
        ngaysinh TEXT,
        sdt TEXT,
        matkhau TEXT,
        gioitinh TEXT
    )
    """)
    conn.commit()
    conn.close()