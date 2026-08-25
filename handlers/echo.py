from aiogram import Router
from aiogram.types import Message

router_echo = Router()


@router_echo.message()
async def echo_handler(message: Message):
    await message.answer("Я не понимаю эту команду. Используйте /start или /books.")