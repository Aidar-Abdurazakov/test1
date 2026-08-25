import aiosqlite
from db import queries
path_db = 'db/books.db'


async def init_db():
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.create_books_table)
        await conn.execute(queries.create_table_books_detail)
        await conn.commit()

    print('База данных подключена!')


async def add_book_db(name_books, author, book_id):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(
            queries.insert_book,
            (name_books, author, book_id)
        )
        await conn.commit()


async def add_book_detail_db(book_id, genre):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(
            queries.insert_book_detail,
            (book_id, genre)
        )
        await conn.commit()


async def get_books_db():
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.select_books)
        books = await cursor.fetchall()
    return books


async def delete_book_db(book_id):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(
            queries.delete_book,
            (book_id,)
        )

        await conn.execute(
            queries.delete_book_detail,
            (book_id,)
        )

        await conn.commit()