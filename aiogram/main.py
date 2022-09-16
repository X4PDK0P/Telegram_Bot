import asyncio
from config import TOKEN, U_TOKEN, admin_id
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.message import ContentType


bot = Bot(token=TOKEN, parse_mode=types.ParseMode.MARKDOWN)
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, loop=loop)


inline_btn_1 = InlineKeyboardButton('Подписка', callback_data='btn1')
inline_kb_menu = InlineKeyboardMarkup(row_width=2).add(inline_btn_1)


@dp.message_handler(commands='start')
async def send_welcome(msg: types.Message):
    await msg.answer(f'Я бот. Приятно познакомиться, {msg.from_user.first_name}!', reply_markup=inline_kb_menu)


@dp.message_handler(commands=['menu', 'help'])
async def menu(msg: types.Message):
    await msg.answer('Используй интересующие тебя кнопки', reply_markup=inline_kb_menu)


@dp.callback_query_handler(text = 'btn1')
async def menu_callback(callback_query: types.CallbackQuery):
    #await bot.answer_callback_query(callback_query.from_user.id, callback_query.inline_message_id)
    await bot.send_invoice(chat_id=callback_query.from_user.id,
                           title='Оформление подписки',
                           description='Описание',
                           payload='month_sub',
                           provider_token=U_TOKEN,
                           currency= 'RUB',
                           start_parameter='test_bot',
                           prices=[{'label': 'Rub',
                                    'amount': 19900}])


@dp.pre_checkout_query_handler()
async def pre_ch(pre_checkout_query = types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: types.Message):
    if message.successful_payment.invoice_payload == 'month_sub':
        #подписываем пользователя
        SUB = True
        await bot.send_message(message.from_user.id, 'Вам выдана подписка: \n' + str(SUB))
        user_id = message.from_user.id
        await bot.send_message(admin_id, 'Пользователь с ID:\n' + str(user_id))








if __name__ == '__main__':
   executor.start_polling(dp)

