import os
import sqlite3
from contextlib import contextmanager

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    filename TEXT,
                    prediction TEXT,
                    confidence REAL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

    @contextmanager
    def _connect(self):
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
        finally:
            conn.close()

    def log_prediction(self, filename, prediction, confidence):
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO logs (filename, prediction, confidence) VALUES (?, ?, ?)",
                (filename, prediction, float(confidence))
            )
            conn.commit()
