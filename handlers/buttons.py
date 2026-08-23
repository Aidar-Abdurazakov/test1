from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.utils.keyboard import ReplyKeyboardBuilder

main_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/start'), KeyboardButton(text='/help'),
        KeyboardButton(text='/about'), KeyboardButton(text='/allproducts')
         ],
    ],
    resize_keyboard=True
)


main_buttons_builder = ReplyKeyboardBuilder()
main_buttons_builder.button(text='/start')
main_buttons_builder.button(text='/help')
main_buttons_builder.button(text='/about')
main_buttons_builder.button(text='/allproducts')
main_buttons_builder.adjust(2)

main_builder = main_buttons_builder.as_markup(
    resize_keyboard=True
)

menu_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='О нас', callback_data='about')],
        [InlineKeyboardButton(text='Помощь', callback_data='help')]
    ]
)

def product_action(product_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='✏️ Редактировать',
                    callback_data=f'edit:{product_id}'
                ),
                InlineKeyboardButton(
                    text='🗑 Удалить',
                    callback_data=f'delete:{product_id}'
                )
            ]
        ]
    )

delete_confirm = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='✅ Да, удалить',
                callback_data='confirm_delete'
            ),
            InlineKeyboardButton(
                text='❌ Отмена',
                callback_data='cancel_delete'
            )
        ]
    ]
)