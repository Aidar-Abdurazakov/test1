from aiogram.filters import Command
from aiogram import Router, F
from aiogram.types import Message, FSInputFile, CallbackQuery
from config import bot
from handlers.buttons import main_buttons, main_builder, menu_inline
from db import main_db
from handlers.buttons import product_action

router_commands = Router()

@router_commands.message(Command('start'))
async def start_command(message:Message,bot):
    await message.answer('Привет!Напиши свое имя:', reply_markup=menu_inline)
    await bot.send_message(chat_id=message.chat.id, text=f'Привет. Твой ID - {message.from_user.id}')

@router_commands.message(Command('help'))
async def help_command(message:Message,bot):
    await message.answer("Команды:\n/start - старт бота\n/help - все команды\n/about - о нас\nallproducts - все товары")

@router_commands.message(F.text == 'привет')
async def hello_command(message: Message):
    await message.answer('Hello! Do you have a question?')

@router_commands.message(Command('about'))
async def about_command(message:Message,bot):
    await message.answer('Привет! Меня зовут Айдар, и я помогу хранить название твоих товаров в БД.')

@router_commands.message(Command('allproducts'))
async def products_command(message:Message):
    products = await main_db.get_product_db()

    if not products:
        await message.answer('В базе товаров нет!')
        return
    else:
        for name, price, category, description, product_id, photo_id  in products:
            await message.answer_photo(photo=photo_id,
                caption=(f'Название - {name}\nЦена - {price}\nОписание - {description}\nКатегория - {category}\nАртикул - {product_id}'))    