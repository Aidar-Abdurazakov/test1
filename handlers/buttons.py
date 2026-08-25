from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

main_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/add_book"), KeyboardButton(text="/books")],
        [KeyboardButton(text="/delete_book")]
    ],
    resize_keyboard=True
)

menu_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Добавить книгу", callback_data="add_book_action")],
        [InlineKeyboardButton(text="Каталог", callback_data="view_catalog")]
    ]
)

def main_builder():
    builder = InlineKeyboardBuilder()
    builder.button(text="Список книг", callback_data="list_books")
    builder.adjust(1)
    return builder.as_markup()


def product_action(book_id):
    builder = InlineKeyboardBuilder()
    builder.button(text="Удалить", callback_data=f"delete_{book_id}")
    return builder.as_markup()