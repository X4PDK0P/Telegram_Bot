from config import TOKEN, admin_id
import telebot , plata
from telebot import types

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item_pd = types.KeyboardButton('Проверка подписки')
	item_opl = types.KeyboardButton('Купить подписку')
	item_adm = types.KeyboardButton('Связь с администратором')
	markup.add(item_opl, item_pd, item_adm)
	bot.send_message(message.chat.id, "{0.first_name}, используй кнопки".format(message.from_user), reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def bot_message(message):
	if message.chat.type == 'private':
		if message.text == 'Купить подписку':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item_back = types.KeyboardButton('Назад')
			markup.add(item_back)
			print(message)
			bot.send_message(message.chat.id, 'Описание подписки')
			plata.pay(message)



bot.polling(none_stop=True)


'''import config
import telebot
from telebot import types


TOKEN = ''

bot = telebot.TeleBot(TOKEN)
admin_id = ''


@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id, 'Hello. Write /help fro help.')


@bot.message_handler(commands=["help"])
def start(message):
	bot.send_message(message.chat.id, 'Help message😈')


@bot.message_handler(content_types=["text"])
def messages(message):
    if int(message.chat.id) == int(admin_id):
        try:
            chatId = message.text.split(': ')[0]
            text = message.text.split(': ')[1]
            bot.send_message(chatId, text)
        except:
            pass
    else:
        bot.send_message(admin_id, str(message.chat.id) + ': ' + message.text)
        bot.send_message(message.chat.id, '%s, wait please 👍'%message.chat.username)


bot.polling(none_stop=True)'''
