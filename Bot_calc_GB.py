import random
import telebot#библиотека для работы телеграм(лучше через venv)
from math import sqrt
from telebot import types

token = "" #токен полученный от телеграм
bot = telebot.TeleBot(token)


# a = ""
# sig = ""
# b = ""
# result = ""
def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def pow(a, b):
    return a ** b


def div(a, b):
    return a / b


def rem_of_div(a, b):
    return a % b


def int_div(a, b):
    return a // b


HELP = """
/start - Приветствие
/help - вывести инфо
/sum - сложение
/pow - возведение в степень
/mult - умножение
/sub - разница
/div - деление
/rem - остаток от деления
/in_div - целочисленное деление
/root_num - квадратный корень
"""




@bot.message_handler(commands=["help"]) # регистрация команды и как она обработается(функциями)
def hello(message):
    if message.text == "/help":
        msg = bot.reply_to(message, "Привет " + message.from_user.first_name + " Рад помочь, для работы с калькулятором вводите команды из меню через" + "  '/'  " + "и через пробел вводите элементы и знаки операций. Для помощи введите /help повторно")
        bot.register_next_step_handler(msg, hel) #Вывод подсказки для пользователя и переход на следующий шаг в этом обработчикеы

def hel(message):
    bot.send_message(message.chat.id, HELP) # Вывод инфо через созданную переменную


@bot.message_handler(commands=["sum"])
def addition(message):
    mess = message.text.strip(' ')#удаление лишних пробелов в начале и конце
    command = mess.split()#сообщение от пользователя разбор на строковые элементы
    a = float(command[1])#значения в индексах превращаются в цифры
    b = float(command[3])
    sig = command[2]#знак операции в строковом виде
    if sig == "+":#если знак соответствует предполагаемой операции
        res = sum(a, b) # выполнение соответствующей функции
        result = str(res)# результат функции опять делаем строкой
    else:
        result = "error"#если пользователь ввел операцию от другой команды(не тот знак выражения)
    bot.send_message(message.chat.id, result)#вывод для пользователя результата или сообщения об  ошибке


@bot.message_handler(commands=["sub"])
def diff(message):
    mess = message.text.strip(' ')  # удаление лишних пробелов в начале и конце
    command = mess.split()  # сообщение от пользователя разбор на строковые элементы
    a = float(command[1])
    b = float(command[3])
    sig = command[2]
    if sig == "-":
        res = sub(a, b)
        result = str(res)
    else:
        result = "error"
    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=["mult"])
def work(message):
    mess = message.text.strip(' ')  # удаление лишних пробелов в начале и конце
    command = mess.split()  # сообщение от пользователя разбор на строковые элементы
    a = float(command[1])
    b = float(command[3])
    sig = command[2]
    if sig == "*":
        res = mult(a, b)
        result = str(res)
    else:
        result = "error"
    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=["pow"])
def degree(message):
    mess = message.text.strip(' ')  # удаление лишних пробелов в начале и конце
    command = mess.split()  # сообщение от пользователя разбор на строковые элементы
    a = float(command[1])
    b = float(command[3])
    sig = command[2]
    if sig == "**":
        res = pow(a, b)
        result = str(res)
    else:
        result = "error"
    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=["div"])
def division(message):
    mess = message.text.strip(' ')  # удаление лишних пробелов в начале и конце
    command = mess.split()  # сообщение от пользователя разбор на строковые элементы
    a = float(command[1])
    b = float(command[3])
    sig = command[2]
    if sig == "/" and b != 0:
        res = div(a, b)
        result = str(res)
    else:
        result = "error"
    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=["rem"])
def rem_division(message):
    mess = message.text.strip(' ')  # удаление лишних пробелов в начале и конце
    command = mess.split()  # сообщение от пользователя разбор на строковые элементы
    a = float(command[1])
    b = float(command[3])
    sig = command[2]
    if sig == "%" and b != 0:
        res = rem_of_div(a, b)
        result = str(res)
    else:
        result = "error"
    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=["in_div"])
def int_division(message):
    mess = message.text.strip(' ')  # удаление лишних пробелов в начале и конце
    command = mess.split()  # сообщение от пользователя разбор на строковые элементы
    a = float(command[1])
    b = float(command[3])
    sig = command[2]
    if sig == "//" and b != 0:
        res = int_div(a, b)
        result = str(res)
    else:
        result = "error"
    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=["root_num"])
def root_numbers(message):
    mess = message.text.strip(' ')  # удаление лишних пробелов в начале и конце
    command = mess.split()  # сообщение от пользователя разбор на строковые элементы
    a = float(command[1])
    res = sqrt(a)
    result = str(res)
    bot.send_message(message.chat.id, result)


bot.polling(none_stop=True)
