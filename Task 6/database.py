import psycopg2


class DataBase:
    def __init__(self):
        self.conn = psycopg2.connect(host='localhost', dbname='db', user='usr', password='pass')
        self.cursor = self.conn.cursor()

    def query_database(self, sql_statement, *args):
        self.cursor.execute(sql_statement, *args)
        return self.cursor

    def commit_query(self):
        return self.conn.commit()

    def fetch_one(self, sql_statement, *args):
        cursor = self.query_database(sql_statement, *args)
        return cursor.fetchone()

    def fetch_all(self, sql_statement, *args):
        cursor = self.query_database(sql_statement, *args)
        return cursor.fetchall()

    def __del__(self):
        self.conn.close()
        self.cursor.close()
