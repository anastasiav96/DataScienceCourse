from database import DataBase


class CreateTables(DataBase):
    def books_table(self):
        sql_statement = '''CREATE TABLE IF NOT EXISTS books
                (book_id        SERIAL          PRIMARY KEY,
                 title          VARCHAR(100)    NOT NULL,
                 year           INTEGER         NOT NULL,       
                 total_pages    INTEGER         NOT NULL,
                 quantity       INTEGER         NOT NULL);'''
        self.cursor.execute(sql_statement)
        self.conn.commit()

    def authors_table(self):
        sql_statement = '''CREATE TABLE IF NOT EXISTS authors
                (author_id     SERIAL          PRIMARY KEY,
                 name          VARCHAR(100)    NOT NULL,
                 surname       VARCHAR(100)    NOT NULL);'''
        self.cursor.execute(sql_statement)
        self.conn.commit()

    def book_authors_table(self):
        sql_statement = '''CREATE TABLE IF NOT EXISTS book_authors
                (book_id       SERIAL   REFERENCES books (book_id) ON DELETE CASCADE,
                 author_id     SERIAL   REFERENCES authors (author_id) ON DELETE CASCADE,
                 PRIMARY KEY(book_id, author_id));'''
        self.cursor.execute(sql_statement)
        self.conn.commit()

    def genres_table(self):
        sql_statement = '''CREATE TABLE IF NOT EXISTS genres
                (genre_id       SERIAL           PRIMARY KEY,
                 genre          VARCHAR(100)    UNIQUE NOT NULL);'''
        self.cursor.execute(sql_statement)
        self.conn.commit()

    def book_genres_table(self):
        sql_statement = '''CREATE TABLE IF NOT EXISTS book_genres
                (book_id    SERIAL     REFERENCES books (book_id) ON DELETE CASCADE,
                 genre_id   SERIAL     REFERENCES genres (genre_id) ON DELETE CASCADE,
                 PRIMARY KEY(book_id, genre_id));'''
        self.cursor.execute(sql_statement)
        self.conn.commit()
