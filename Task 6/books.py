from database import DataBase


class Books(DataBase):
    def __init__(self, title, year, total_pages, quantiy):
        super().__init__()
        self.title = title
        self.year = year
        self.total_pages = total_pages
        self.quantiy = quantiy

    def add_book(self):
        sql_statement = """INSERT INTO books (title, year, total_pages, quantity)
                           VALUES (%s, %s, %s, %s);"""
        self.query_database(sql_statement,
                            (self.title, self.year, self.total_pages, self.quantiy))
        self.commit_query()

    def update_book(self, id, new_title, new_year, new_pages, new_quantity):
        sql_statement = """UPDATE books SET 
                           (title, year, total_pages, quantity) = (%s, %s, %s, %s) WHERE book_id = %s;"""
        self.query_database(sql_statement, (new_title, new_year, new_pages, new_quantity, id))
        self.commit_query()
        self.title = new_title
        self.year = new_year
        self.total_pages = new_pages
        self.quantiy = new_quantity

    def delete_book(self, id):
        sql_statement = """DELETE FROM books WHERE book_id = %s;"""
        self.query_database(sql_statement, (id,))
        self.commit_query()

    def delete_all_books(self):
        sql_statement = """DELETE FROM books;"""
        self.query_database(sql_statement)
        self.commit_query()

    def __str__(self):
        return f'Book title: {self.title}, year of issue: {self.year}, number of pages in a book: {self.total_pages}, ' \
               f'number of books available: {self.quantiy}'
