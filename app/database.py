import sqlite3

DB_NAME = ("database.sqlite")

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Это позволяет получать данные в виде словаря
    return conn


cursor.execute("""
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    completed TEXT NOT NULL
)
""")

conn.commit()
conn.close()