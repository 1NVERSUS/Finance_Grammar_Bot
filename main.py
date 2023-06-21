import telebot
from telebot import types
import datetime
import time
import sche
token='6108360249:AAHC6BHyPpZtcEHLA7Lf4b3v3-WX8cqeP7g'
bot = telebot.TeleBot(token)
a = []
m = {}
n = {}
k = {}
incom = 0
consum = 0
print('a')
if int(datetime.date.today().day) == 21:
    print('b')
    for id in m.keys():
        bot.send_message(id,'asda')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет! Я бот-помощник по финансовой грамотности')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton('income')
    markup.add(bt1)
    print(message)
    global m
    global n
    idt = message.from_user.id
    if idt not in m:
        incom = 0
        consum = 0
        m[idt] = incom
        n[idt] = consum
    bot.send_message(message.chat.id, f'''Добрый день.
На данный момент вы заработали - {m[idt]} евро,
а потратили - {n[idt]} тугриков
Ваша прибыль {m[idt] - n[idt]} копеек''')
    if m[idt]-n[idt] < 0:
        bot.send_message(message.chat.id, 'Мы советуем вам меньше тратить денег и не писать мне')

@bot.message_handler(commands=['income'])
def income_handler(message):
    bot.send_message(message.chat.id, 'Напиши сумму, которую ты заработал')
    bot.register_next_step_handler(message, income)


def income(message):
    global m
    idt = message.from_user.id
    incom = int(message.text)
    m[idt] = m[idt] + incom
    print(m)

@bot.message_handler(commands=['consumption'])
def consumption(message):
    bot.send_message(message.chat.id, 'Напиши сумму, которую ты потратил')
    bot.register_next_step_handler(message, consumption)


def consumption(message):
    global n
    idt = message.from_user.id
    consum = int(message.text)
    n[idt] = n[idt] + consum

def send_message():
    message = ''


@bot.message_handler(commands=['dream'])
def dream(message):
    bot.send_message(message.chat.id, 'Какую сумму вы хотите накопить?')
    bot.register_next_step_handler(message,dream2)
    sum = int(message.text)
    global sum
    idt = message.from_user.id
    if idt not in m:
        
        k[idt] = [sum, tme]
        consum = 0
        m[idt] = incom
        n[idt] = consum
    
def dream2(message):
    bot.send_message(message.chat.id, 'За какой срок вы хотите накопить сумму?')
    bot.register_next_step_handler(message.chat.id, dream3)
    tme = int(message.text)
    idt = message.from_user.id
     if idt not in k:
        global k
        k[idt] = [sum, tme]
        print(k)
    

def dream3(message):
    bot.send_message(message.chat.id, f'Вам нужно оплачивать {sum/time}')




bot.infinity_polling()
