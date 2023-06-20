import telebot
from telebot import types
token='6108360249:AAHC6BHyPpZtcEHLA7Lf4b3v3-WX8cqeP7g'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет! Я бот-помощник по финансовой граматности')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton('income')
    markup.add(bt1)

@bot.message_handler(commands=['income'])
def income_handler(message):
    f = open('income.txt', 'w')
    f.write(message)


bot.infinity_polling()
