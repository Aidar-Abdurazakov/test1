from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db import main_db

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я бот для учета каталога книг.\n\n"
        "Доступные команды:\n"
        "/add_book — Добавить новую книгу\n"
        "/delete_book — Удалить книгу\n"
        "/books — Посмотреть каталог книг"
    )


@router.message(Command("books"))
async def cmd_books(message: Message):
    books = await main_db.get_books_db()

    if not books:
        await message.answer("База данных книг пока пуста.")
        return

    for book in books:
        book_id, title, author, genre = book
        text = (
            f"📖 **Книга №{book_id}**\n"
            f"**Название:** {title}\n"
            f"**Автор:** {author}\n"
            f"**Жанр:** {genre}"
        )
        await message.answer(text, parse_mode="Markdown")