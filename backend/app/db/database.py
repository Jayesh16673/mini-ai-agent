import sqlite3


def get_connection():
    conn = sqlite3.connect("memory.db")
    create_table(conn)
    return conn


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE,
            value TEXT
        )
    """)
    conn.commit()
