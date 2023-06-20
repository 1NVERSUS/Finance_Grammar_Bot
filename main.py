import telebot
from telebot import types
token='6108360249:AAHC6BHyPpZtcEHLA7Lf4b3v3-WX8cqeP7g'
bot = telebot.TeleBot(token)
inc = []

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет! Я бот-помощник по финансовой граматности')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton('income')
    markup.add(bt1)

@bot.message_handler(commands=['income'])
def income_handler(message):
    bot.send_message(message.chat.id, 'Напиши сумму, которую ты заработал')
    bot.register_next_step_handler(message, income)
def income(message):
    print(message.json()['text'])
