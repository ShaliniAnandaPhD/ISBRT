import sqlite3

class DataManager:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_tables()

    def create_tables(self):
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS tests (
            id INTEGER PRIMARY KEY,
            prompt TEXT,
            response TEXT,
            analysis TEXT
        );
        """
        self.conn.execute(create_table_sql)

    def insert_test_data(self, prompt, response, analysis):
        insert_sql = "INSERT INTO tests (prompt, response, analysis) VALUES (?, ?, ?)"
        self.conn.execute(insert_sql, (prompt, response, analysis))
        self.conn.commit()

    def get_test_data(self):
        select_sql = "SELECT * FROM tests"
        cur = self.conn.cursor()
        cur.execute(select_sql)
        return cur.fetchall()
