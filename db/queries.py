create_books_table = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_books TEXT NOT NULL,
        author TEXT NOT NULL,
        book_id INTEGER NOT NULL
    )
"""

create_table_books_detail = """
    CREATE TABLE IF NOT EXISTS books_detail (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER NOT NULL,
        genre TEXT NOT NULL
    )
"""

insert_book = """
    INSERT INTO books
        (name_books, author, book_id)
    VALUES (?, ?, ?)
"""


insert_book_detail = """
    INSERT INTO books_detail
        (book_id, genre)
    VALUES (?, ?)
"""

select_books = """
    SELECT
        books.book_id,
        books.name_books,
        books.author,
        books_detail.genre
    FROM books
    INNER JOIN books_detail
        ON books.book_id = books_detail.book_id
"""


delete_book = """
    DELETE FROM books
    WHERE book_id = ?
"""


delete_book_detail = """
    DELETE FROM books_detail
    WHERE book_id = ?
"""