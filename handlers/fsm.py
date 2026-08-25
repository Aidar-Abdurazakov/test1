from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from db import main_db

router = Router()


class AddBookState(StatesGroup):
    number = State()
    title = State()
    author = State()
    genre = State()


@router.message(Command("add_book"))
async def cmd_add_book(message: Message, state: FSMContext):
    await state.set_state(AddBookState.number)
    await message.answer("Шаг 1 из 4: Введите номер книги (только число):")


@router.message(AddBookState.number)
async def process_number(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Ошибка! Номер книги должен быть числом. Попробуйте еще раз:")
        return

    await state.update_data(number=int(message.text))
    await state.set_state(AddBookState.title)
    await message.answer("Шаг 2 из 4: Введите название книги:")


@router.message(AddBookState.title)
async def process_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(AddBookState.author)
    await message.answer("Шаг 3 из 4: Введите автора книги:")


@router.message(AddBookState.author)
async def process_author(message: Message, state: FSMContext):
    await state.update_data(author=message.text)
    await state.set_state(AddBookState.genre)
    await message.answer("Шаг 4 из 4: Введите жанр книги:")


@router.message(AddBookState.genre)
async def process_genre(message: Message, state: FSMContext):
    user_data = await state.get_data()
    book_id = user_data["number"]
    title = user_data["title"]
    author = user_data["author"]
    genre = message.text

    await main_db.add_book_db(title, author, book_id)
    await main_db.add_book_detail_db(book_id, genre)

    await message.answer(
        f"✅ Книга успешно добавлена!\n\n"
        f"📌 Номер: {book_id}\n"
        f"📖 Название: {title}\n"
        f"✍️ Автор: {author}\n"
        f"🏷 Жанр: {genre}"
    )
    await state.clear()