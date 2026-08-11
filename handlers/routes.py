
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton


router = Router()

def get_main_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="О боте")],
            [KeyboardButton(text="Старт"), KeyboardButton(text="Помощь")]
        ],
        resize_keyboard=True
    )
    return keyboard

@router.message(Command("start"))
@router.message(F.text.lower == "Старт")
async def start(message: Message):
    await message.answer(
        "Привет! Я твой личный ассистент.\n\n"
        "Напиши /help для помощи"
    )


@router.message(Command("help"))
async def help(message: Message):
    await message.answer(
        "Команды:\n"
        "/start — запуск\n"
        "/help — список команд\n"
        "/about — про нас",
        reply_markup=get_main_reply_keyboard()
    )


@router.message(Command("about"))
async def about(message: Message):
    await message.answer(
        f"Дорогой {message.from_user.full_name}, "
        "меня зовут Айдар, и я твой личный ассистент."
    )

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Напиши что нибудь")
