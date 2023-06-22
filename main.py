
import telebot
from telebot import types
import datetime
import time
import sche
from celery import Celery
from celery.schedules import crontab

from models import Person, Notifications
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
    bot.send_message(message.chat.id, f'Вам нужно оплачивать по {k[idt][0]/k[idt][1]} в месяц')

@bot.message_handler(commands=['reset'])
def reset(message):
    idt = message.from_user.id
    m[idt] = 0
    n[idt] = 0

@bot.message_handler(commands=['show'])
def show(message):
    idt = message.from_user.id
    bot.send_message(message.chat.id, f'''Ваши доходы: {m[idt]} ({m[idt]/m[idt]+n[idt]}%)
Ваши расходы: {n[idt]} ({n[idt]/m[idt]+n[idt]}%)
Ваша прибыль/убытки: {m[idt] - n[idt]}''')
    if ((m[idt] - n[idt])/m[idt])*100 <= 3:
        ________('''Я предлагаю вам несколько вариантов увеличения доходов:
        1.Мотивировать повышение зарплаты на текущем месте работы.
        2.Сменить работу на более высокооплачиваемую.
        3.Найти подработку, в том числе в качестве фрилансера.
        Также есть несколько вариантов уменьшения расходов:
        1.Экономия на жилищно-комунальных услугах.
        2.Экономия на мобильной связи. Сегодня мобильные операторы и интернет провайдеры предлагают выгодные тарифы - просто ознакомьтесь и выберите подходящий!
        3.Экономия на одежде и обуви. Даже дизайнерские вещи можно покупать дешево на распродажах.
        4.Экономия на досуге и развлечениях. Здесь все должно быть в пределах нормы: если отказ от хобби резко снижает качество вашей жизни, то экономия на нем может вызвать стресс. Этот вид расходов оптимизируйте обдуманно.''')
    if ((m[idt] - n[idt])/m[idt])*100 > 3 and ((m[idt] - n[idt])/m[idt])*100 <= 20:
        ________('''Ваши доходы превышают рассходы, так держать! Если вы желаете ещё больший доход, я советую вам преобрести акции или другие ценные бумаги. Для начала следует получить базовые знания об инвестициях из интернет-источников.
        Инвестиции это риск,поэтому вам решать, пробовать ли себя в этом направлении или нет. ''')
    if ((m[idt] - n[idt])/m[idt])*100 > 20:
        _____('''У вас весьма большой доход. Надеюсь вы сможете продолжать в том же духе и исполните свои мечты!

def send_message():
    for person in Person.select():
        last_sent_date = Notifications.select().where(
            Notifications.id == person.telegram_id).order_by(
            Notifications.last_notification.desc())[0].last_notification

        if last_sent_date:
            message = "Hello, it's time to send the monthly report!"
            Notifications.create(id=person.telegram_id, last_notification=datetime.datetime.now())
        print(bot.send_message(person.telegram_id, message))
        Notifications.create(id=person.telegram_id, last_notification=datetime.datetime.now())
if __name__ == '__main__':
    bot.infinity_polling()
  

'''
0 10 * * * /path/to/venv/bin/celery -A main send_message
'''



