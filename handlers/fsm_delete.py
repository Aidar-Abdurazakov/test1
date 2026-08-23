from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from db import main_db
from handlers.buttons import delete_confirm


router_delete = Router()


class DeleteProduct(StatesGroup):
    confirmation = State()


# Нажали кнопку "Удалить"
@router_delete.callback_query(F.data.startswith('delete:'))
async def delete_product(
    call: CallbackQuery,
    state: FSMContext
):
    product_id = call.data.split(':')[1]

    await state.update_data(product_id=product_id)

    await state.set_state(DeleteProduct.confirmation)

    await call.message.answer(
        'Вы точно хотите удалить этот товар?',
        reply_markup=delete_confirm
    )

    await call.answer()


# Нажали "Да, удалить"
@router_delete.callback_query(
    DeleteProduct.confirmation,
    F.data == 'confirm_delete'
)
async def confirm_delete(
    call: CallbackQuery,
    state: FSMContext
):
    data = await state.get_data()
    product_id = data['product_id']

    await main_db.delete_product_db(product_id)

    await call.message.answer(
        f'✅ Товар с артикулом {product_id} удалён!'
    )

    await state.clear()
    await call.answer()


# Нажали "Отмена"
@router_delete.callback_query(
    DeleteProduct.confirmation,
    F.data == 'cancel_delete'
)
async def cancel_delete(
    call: CallbackQuery,
    state: FSMContext
):
    await call.message.answer(
        '❌ Удаление отменено.'
    )

    await state.clear()
    await call.answer()