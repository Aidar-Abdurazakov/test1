import asyncio
import logging
from aiogram.types import BotCommand
from config import bot, dp, Admin
from db import main_db
from handlers import commands, fsm, fsm_delete


async def set_commands():
    commands_list = [
        BotCommand(command="start", description="Старт бота"),
        BotCommand(command="books", description="Все книги"),
        BotCommand(command="add_book", description="Добавить книгу"),
        BotCommand(command="delete_book", description="Удалить книгу"),
    ]
    await bot.set_my_commands(commands_list)

async def on_startup():
    await main_db.init_db()
    await set_commands()

    for admin_id in Admin:
        try:
            await bot.send_message(
                chat_id=admin_id,
                text="🤖 Бот успешно запущен!"
            )
        except Exception as e:
            logging.error(f"Не удалось отправить сообщение админу {admin_id}: {e}")


dp.include_router(commands.router)
dp.include_router(fsm.router)
dp.include_router(fsm_delete.router)

dp.startup.register(on_startup)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())