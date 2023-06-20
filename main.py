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
    f = open('income.txt', 'r+')
    for line in f:
        x = str(int(line) + int(message.text))
        f.seek(0)
        f.truncate()
        f.write(x)
    f.close()
@bot.message_handler(commands=['consumption'])
def consumption(message):
    bot.send_message(message.chat.id, 'Напиши сумму, которую ты потратил')
    bot.register_next_step_handler(message, consumption)

def consumption(message):
    d = open('consumption.txt', 'r+')
    for line in d:
        x = str(int(line) + int(message.text))
        d.seek(0)
        d.truncate()
        d.write(x)
    d.close()


bot.infinity_polling()
