
import telebot
from telebot import types
import datetime
import time
import sche
from celery import Celery
from celery.schedules import crontab
token='6108360249:AAHC6BHyPpZtcEHLA7Lf4b3v3-WX8cqeP7g'
bot = telebot.TeleBot(token)

m = {}
n = {}
k = {}
sum = 0
incom = 0
consum = 0
celery_app = Celery('main',broker='pyamqp://guest@localhost//')
CHAT_ID = 1142880697

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет! Я бот-помощник по финансовой грамотности')
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
На данный момент доходы - {m[idt]},
а расходы - {n[idt]}
Ваша прибыль - {m[idt] - n[idt]}''')
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

#def send_message():
#    message = ''


@bot.message_handler(commands=['dream'])
def dream(message):
    bot.send_message(message.chat.id, 'Какую сумму вы хотите накопить?')
    bot.register_next_step_handler(message,dream2)





def dream2(message):
    bot.send_message(message.chat.id, 'За сколько месяцев вы хотите накопить сумму?')
    bot.register_next_step_handler(message, dream3)
    global sum
    sum = int(message.text)



def dream3(message):
    tme = int(message.text)
    idt = message.from_user.id
    global k
    if idt not in k:
        k[idt] = [sum, tme]
    print(k)
    bot.send_message(message.chat.id, f'Вам нужно оплачивать {k[idt][0]/k[idt][1]}')

@bot.message_handler(commands=['reset'])
def reset(message):
    idt = message.from_user.id
    m[idt] = 0
    n[idt] = 0

@bot.message_handler(commands=['show'])
def show(message):
    idt = message.from_user.id
    bot.send_message(message.chat.id, f'''Ваши доходы: {m[idt]}
Ваши расходы: {n[idt]}''')




@celery_app.task
def send_message():
    now = datetime.now()
    # Отправляем сообщение каждого 10-го числа месяца в 12:00
    if now.day == 22 and now.hour == 10:
        message = "Hello, it's time to send the monthly report!"
        bot.send_message(CHAT_ID, message)


if __name__ == '__main__':
    # Запускаем Celery
    celery_app.start()

'''
0 10 * * * /path/to/venv/bin/celery -A main send_message
'''


bot.infinity_polling()
