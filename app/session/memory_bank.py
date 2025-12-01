import sqlite3
import os

DB_PATH = "data/memory_bank.db"
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

class MemoryBank:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self._create_table()

    def _create_table(self):
        c = self.conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT
        )
        """)
        self.conn.commit()

    def insert_fact(self, text):
        c = self.conn.cursor()
        c.execute("INSERT INTO memory (text) VALUES (?)", (text,))
        self.conn.commit()
        return c.lastrowid

    def list_all(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM memory ORDER BY id DESC")
        rows = c.fetchall()
        return [{'id': r[0], 'text': r[1]} for r in rows]
