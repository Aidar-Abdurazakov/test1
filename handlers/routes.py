from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton


router = Router()


def get_main_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="О боте")],
            [KeyboardButton(text="Старт"), KeyboardButton(text="/menu")]
        ],
        resize_keyboard=True
    )

    return keyboard


@router.message(Command("start"))
@router.message(F.text.lower() == "старт")
async def start(message: Message):

    await message.answer(
        "Добро пожаловать в наше кафе!\n\n"
        "Напиши /menu для помощи",
        reply_markup=get_main_reply_keyboard()
    )


@router.message(Command("menu"))
async def help(message: Message):

    await message.answer(
        "Команды:\n"
        "/start — запуск\n"
        "/menu — список команд\n"
        "/about — про нас",
        reply_markup=get_main_reply_keyboard()
    )


@router.message(Command("about"))
async def about(message: Message):

    await message.answer(
        f"Дорогой {message.from_user.full_name}, "
        "добро пожаловать в наше кафе 'Geeks'."
    )


@router.message(F.text.lower() == "пока")
async def goodbye(message: Message):

    await message.answer("До встречи!")