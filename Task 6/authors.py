from database import DataBase


class Author(DataBase):
    def __init__(self, name, surname):
        super().__init__()
        self.name = name
        self.surname = surname

    def add_author(self):
        sql_statement = """INSERT INTO authors (name, surname)
                           VALUES (%s, %s);"""
        self.query_database(sql_statement, (self.name, self.surname))
        self.commit_query()

    def update_author(self, id, new_name, new_surname):
        sql_statement = """UPDATE authors SET 
                           name = %s, surname = %s WHERE author_id = %s;"""
        self.query_database(sql_statement, (new_name, new_surname, id))
        self.commit_query()
        self.name = new_name
        self.surname = new_surname

    def delete_author(self, id):
        sql_statement = """DELETE FROM authors WHERE author_id = %s;"""
        self.query_database(sql_statement, (id,))
        self.commit_query()

    def delete_all_authors(self):
        sql_statement = """DELETE FROM authors;"""
        self.query_database(sql_statement)
        self.commit_query()

    def __str__(self):
        return f'Author name: {self.name}, author surname: {self.surname}'
