from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from db import main_db

router = Router()


class DeleteBookState(StatesGroup):
    book_id = State()


@router.message(Command("delete_book"))
async def cmd_delete_book(message: Message, state: FSMContext):
    await state.set_state(DeleteBookState.book_id)
    await message.answer("Введите номер книги (book_id), которую хотите удалить:")


@router.message(DeleteBookState.book_id)
async def process_delete_number(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Ошибка! Номер книги должен быть числом. Попробуйте еще раз:")
        return

    book_id = int(message.text)
    await main_db.delete_book_db(book_id)

    await message.answer(f"🗑 Книга №{book_id} и её детали успешно удалены!")
    await state.clear()