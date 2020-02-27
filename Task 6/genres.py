from database import DataBase


class Genres(DataBase):
    def __init__(self, genre):
        super().__init__()
        self.genre = genre

    def add_genre(self):
        sql_statement = """INSERT INTO genres (genre)
                           VALUES (%s);"""
        self.query_database(sql_statement, (self.genre,))
        self.commit_query()

    def update_genre(self, id, new_genre):
        sql_statement = """UPDATE genres SET 
                           genre = %s WHERE genre_id = %s;"""
        self.query_database(sql_statement, (new_genre, id))
        self.commit_query()
        self.genre = new_genre

    def delete_genre(self, id):
        sql_statement = """DELETE FROM genres WHERE genre_id = %s;"""
        self.query_database(sql_statement, (id,))
        self.commit_query()

    def delete_all_genres(self):
        sql_statement = """DELETE FROM genres;"""
        self.query_database(sql_statement)
        self.commit_query()

    def __del__(self):
        self.conn.close()
        self.cursor.close()

    def __str__(self):
        return f'Genre: {self.genre}'
