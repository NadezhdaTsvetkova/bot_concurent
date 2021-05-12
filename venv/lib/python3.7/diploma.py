import types
import telebot
from telebot import types
import requests
import xml.dom.minidom
import sqlite3

TOKEN1 = "1719712583:AAEDBRcfbnPckLc08RIM9LgfLgeShkUodpA"
bot = telebot.TeleBot(TOKEN1)

conn = sqlite3.connect('dbDiplom.db', check_same_thread=False)
cursor = conn.cursor()
cursor1 = conn.cursor()


def menu(k):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Описание']])
    keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Методы']])
    keyboard.row(
        *[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Техническое обеспечение']])
    keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Литература']])
    keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ["Назад"]])
    msg = bot.send_message(k.message.chat.id, 'Меню', reply_markup=keyboard)

def menu1(k):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Описание метода']])
    keyboard.row(
        *[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Технические помощники']])
    keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Литература по методу']])
    keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ["К меню ->"]])
    msg = bot.send_message(k.message.chat.id, 'Выберети информацию по этому методу:', reply_markup=keyboard)


def count_copy(x):
    request = f"SELECT name FROM technics WHERE n_of_grp=?"
    result1 = [i[0] for i in cursor.execute(request, (x,))]
    return len(result1)

def count_copy1(x):
    request = f"SELECT name FROM library WHERE type=?"
    result1 = [i[0] for i in cursor.execute(request, (x,))]
    return len(result1)
def count_copy2(x):
    request = f"SELECT name FROM methods WHERE type=?"
    result1 = [i[0] for i in cursor.execute(request, (x,))]
    return len(result1)

def count_copy4(x):
    request = f"SELECT name FROM library WHERE typeM=?"
    result1 = [i[0] for i in cursor.execute(request, (x,))]
    return len(result1)

def db_table_val(num: str, user_id: int):
    request = 'INSERT INTO numbers (num, user_id) VALUES (?, ?)'
    cursor.execute(request, (num, user_id))
    conn.commit()

def del_id(user_id):
    request = "DELETE FROM numbers WHERE user_id=?"
    cursor.execute(request, (user_id,))
    conn.commit()


def del_idM(user_id):
    request = "DELETE FROM numbersM WHERE user_id=?"
    cursor.execute(request, (user_id,))
    conn.commit()

def db_table_val1(num: str, user_id: int):
    request = 'INSERT INTO numbersM (num, user_id) VALUES (?, ?)'
    cursor.execute(request, (num, user_id))
    conn.commit()

def db_table_val4(x):
    request = f"SELECT name FROM methods WHERE type=?"
    result1 = [i[0] for i in cursor.execute(request, (x,))]
    return result1

def db_table_val2(x):
    request = f"SELECT name FROM technics WHERE n_of_grp=?"
    result1 = [i[0] for i in cursor.execute(request, (x,))]
    return result1

def db_table_val3(x):
    request = f"SELECT name FROM library WHERE type=?"
    result1 = [i[0] for i in cursor.execute(request, (x,))]
    return result1

def db_table_val5(x):
    request = f"SELECT name FROM library WHERE typeM=?"
    result1 = [i[0] for i in cursor.execute(request, (x,))]
    return result1

def get(user_id):
    request = f"SELECT num FROM numbers WHERE user_id=?"
    result = cursor.execute(request, (user_id,)).fetchone()
    return result[0]

def get1(user_id):
    request = f"SELECT num FROM numbersM WHERE user_id=?"
    result = cursor.execute(request, (user_id,)).fetchone()
    return result[0]

@bot.message_handler(commands=['start'])
def start(m):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        *[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Анализ конкурентных преимуществ']])
    keyboard.row(
        *[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Выделение основных конкурентов']])
    keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Сравнение по критериям']])
    keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Определение стратегии']])
    keyboard.row(
        *[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Анализ технических параметров']])
    msg = bot.send_message(m.chat.id, '‼Здравствуйте‼ \n✏Анализ конкуренции проекта - важнейший этап '
                                      'в битве за лидерство на рынке и удержания проекта "на плаву"‼\n'
                                      '✏EstimationComp_bot предлает разработанный алгоритм проверки '
                                      'конкурентоспособности\n'
                                      '✏Выберите нужный этап процесса диагностки, и мы предоставим всю необходимую информацию‼\n\n'
                                      'Остались вопросы по работе с ботом? Отправь любой ответ  на это сообщение'
                                      'и мы поможем тебе разобраться!', reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def text1(t):
    if t.text == "Как пользоваться ботом?":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ["Как пользоваться ботом?", "Вернуться к анализу", "Связаться с разработчиком"]])
        msg = bot.send_message(t.chat.id,
                               '✏EstimationComp_bot оперирует широкой базой данных, включающей различные методы,'
                               'алгоритмы и инструменты для диагности конкурентоспособности проекта!\n\n'
                               'Чтобы провести анализ -> выберите один из пунктов '
                               'алгоритма оценки\n -> получите всю необходимую информацию по инструментарию'
                               ' каждого из этапов✏\n\n'
                               'Остались вопросы? Свяжитесь с разработчиком!️', reply_markup=keyboard)

    elif (t.text == "Вернуться к анализу"):
        start(t)

    elif t.text == "Связаться с разработчиком":
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text='Чат', url='https://t.me/tsvetkova_fit')
        keyboard.add(url_button)
        bot.send_message(t.chat.id, 'Свяжитесь с разработчкиом в приватном чате', reply_markup=keyboard)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ["Как пользоваться ботом?", "Связаться с разработчиком", "Вернуться к анализу"]])
        msg = bot.send_message(t.chat.id, 'Если у Вас есть вопросы по работе '
                                          '️✏EstimationComp_bot, изучите процесс пользования или '
                                          'свяжитесь с разработчиком!', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda k: k.data)
def name(k):

    if (k.data == 'Удобство навигации') or (k.data == 'Выделение основных конкурентов') or (
            k.data == 'Определение уровня конкуренции') or (k.data == 'Анализ дизайна') or (
            k.data == 'Определение скорости работы') or (k.data == 'Система оплаты') or (
            k.data == 'Обратная связь') or (k.data == 'Сравнение по критериям') or (k.data == 'SEO анализ') or (
            k.data == 'Определение ссылочного профиля') or (k.data == 'Обзор контента') or (
            k.data == 'Диагностика рекламы') or (k.data == 'Ценовая политика') or (k.data == 'Email-рассылка') or (
            k.data == 'Оценка соц. сетей') or (k.data == 'Поведение пользователей') or (
            k.data == 'Исследование рынка') or (k.data == 'Анализ конкурентных преимуществ'):
        menu(k)
        us_id = k.from_user.id
        del_id(us_id)
        db_table_val(num=k.data, user_id=us_id)
    elif (k.data == 'К меню ->'):
        menu(k)

    elif (k.data == 'Методы'):
        a: str
        a = get(k.from_user.id)
        if (a == 'Удобство навигации') or (a == 'Выделение основных конкурентов') or (a == 'Анализ дизайна') or (
                a == 'Система оплаты') or (a == 'Обратная связь') or (a == 'Сравнение по критериям') or (
                a == 'SEO анализ') or (a == 'Определение ссылочного профиля') or (a == 'Обзор контента') or (
                a == 'Диагностика рекламы') or (a == 'Ценовая политика') or (a == 'Email-рассылка') or (
                a == 'Оценка соц. сетей') or (a == 'Поведение пользователей') or (a == 'Анализ состояния товара') or (
                a == 'Анализ конкурентных преимуществ'):
            keyboard = types.InlineKeyboardMarkup()
            sql = "SELECT methods FROM concurent WHERE name=?"
            cursor.execute(sql, (a,))
            result = cursor.fetchall()
            o = result[0]
            b = list(o)
            if (b[0]==0):
                sql = "SELECT technics FROM concurent WHERE name=?"
                cursor.execute(sql, (a,))
                result = cursor.fetchall()
                o = result[0]
                b = list(o)
                lng = count_copy(b[0])
                m = db_table_val2(b[0])
                list(m)
                i = 0
                while i < (lng):
                    keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                                   [m[i]]])
                    i = i + 1
                keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['К меню ->']])
                bot.send_message(k.message.chat.id, 'Все методы для проверки этапа проводятся через автоматизированные платформы, выберите подходящую', reply_markup=keyboard)
            else:
                keyboard = types.InlineKeyboardMarkup()
                bot.send_message(k.message.chat.id, a)
                m = db_table_val4(int(b[0]))
                lng = count_copy2(b[0])
                print(m)
                list(m)
                i = 0
                while i < (lng):
                    keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                                   [m[i]]])
                    i = i + 1
                keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['К меню ->']])

                bot.send_message(k.message.chat.id, k.data)
                bot.send_message(k.message.chat.id, 'Выберите нужный метод для рассмотрения:', reply_markup=keyboard)
    elif (k.data =='Экспертные оценки') or (k.data =='Модель Портера') or (k.data =='Классификация на группы')or(k.data =='Матрица BCG')or(k.data =='Бенчмаркинг')or(k.data =='Матрица Игоря Ансоффа')or(k.data =='Матрица Д.Абеля')or(k.data =='Матрица McKinsey'):
        menu1(k)
        us_id = k.from_user.id
        del_idM(us_id)
        db_table_val1(num=k.data, user_id=us_id)
    elif (k.data == 'Описание'):

        a = get(k.from_user.id)
        if (a == 'Удобство навигации') or (a == 'Выделение основных конкурентов') or (a == 'Анализ дизайна') or (
                a == 'Система оплаты') or (a == 'Обратная связь') or (a == 'Сравнение по критериям') or (
                a == 'SEO анализ') or (a == 'Определение ссылочного профиля') or (a == 'Обзор контента') or (
                a == 'Диагностика рекламы') or (a == 'Ценовая политика') or (a == 'Email-рассылка') or (
                a == 'Оценка соц. сетей') or (a == 'Поведение пользователей') or (a == 'Анализ состояния товара') or (
                a == 'Анализ конкурентных преимуществ'):
            bot.send_message(k.message.chat.id, k.data)
            bot.send_message(k.message.chat.id, a)
            keyboard = types.InlineKeyboardMarkup()
            keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['К меню ->']])
            sql = "SELECT description FROM concurent WHERE name=?"
            cursor.execute(sql, (a,))
            result = cursor.fetchall()
            for x in result:
                bot.send_message(k.message.chat.id, x, reply_markup=keyboard)
    elif (k.data == 'Литература по методу'):
        a = get1(k.from_user.id)
        if (a == 'Экспертные оценки') or (a == 'Модель Портера') or (a == 'Классификация на группы') or (
                a == 'Матрица BCG') or (a == 'Бенчмаркинг') or (a == 'Матрица Игоря Ансоффа') or (
                a == 'Матрица Д.Абеля') or (a == 'Матрица McKinsey'):
            bot.send_message(k.message.chat.id, k.data)
            bot.send_message(k.message.chat.id, a)
            keyboard = types.InlineKeyboardMarkup()
            sql = "SELECT library FROM methods WHERE name=?"
            cursor.execute(sql, (a,))
            result = cursor.fetchall()
            o = result[0]
            b = list(o)
            lng = count_copy4(b[0])
            m = db_table_val5(b[0])
            print(m)
            list(m)
            i = 0
            while i < (lng):
                bot.send_message(k.message.chat.id, m[i])
                i = i + 1
            keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['К меню ->']])
            bot.send_message(k.message.chat.id, '✏', reply_markup=keyboard)
    elif (k.data == 'Описание метода'):
        a = get1(k.from_user.id)
        if (a =='Экспертные оценки') or (a =='Модель Портера') or (a =='Классификация на группы')or(a =='Матрица BCG')or(a =='Бенчмаркинг')or(a =='Матрица Игоря Ансоффа')or(a=='Матрица Д.Абеля')or(a =='Матрица McKinsey'):
            keyboard = types.InlineKeyboardMarkup()
            keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['К меню ->']])
            sql = "SELECT description FROM methods WHERE name=?"
            cursor.execute(sql, (a,))
            result = cursor.fetchall()
            for x in result:
                bot.send_message(k.message.chat.id, x, reply_markup=keyboard)
    elif (k.data == 'Литература'):
        a: str
        a = get(k.from_user.id)
        if (a == 'Удобство навигации') or (a == 'Выделение основных конкурентов') or (a == 'Анализ дизайна') or (
                a == 'Система оплаты') or (a == 'Обратная связь') or (a == 'Сравнение по критериям') or (
                a == 'SEO анализ') or (a == 'Определение ссылочного профиля') or (a == 'Обзор контента') or (
                a == 'Диагностика рекламы') or (a == 'Ценовая политика') or (a == 'Email-рассылка') or (
                a == 'Оценка соц. сетей') or (a == 'Поведение пользователей') or (a == 'Анализ состояния товара') or (
                a == 'Анализ конкурентных преимуществ'):
            bot.send_message(k.message.chat.id, k.data)
            bot.send_message(k.message.chat.id, a)
            keyboard = types.InlineKeyboardMarkup()
            sql = "SELECT library FROM concurent WHERE name=?"
            cursor.execute(sql, (a,))
            result = cursor.fetchall()
            o = result[0]
            b = list(o)
            lng = count_copy1(b[0])
            m = db_table_val3(str(b[0]))
            print(m)
            list(m)
            i = 0

            while i < (lng):
                bot.send_message(k.message.chat.id, m[i])
                i = i + 1
            keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['К меню ->']])
            bot.send_message(k.message.chat.id, '✏', reply_markup=keyboard)
    elif (k.data == 'Технические помощники'):
        a = get1(k.from_user.id)
        if (a =='Экспертные оценки') or (a =='Модель Портера') or (a =='Классификация на группы')or(a =='Матрица BCG')or(a =='Бенчмаркинг')or(a =='Матрица Игоря Ансоффа')or(a=='Матрица Д.Абеля')or(a =='Матрица McKinsey'):
            bot.send_message(k.message.chat.id, k.data)
            keyboard = types.InlineKeyboardMarkup()
            bot.send_message(k.message.chat.id, a)
            sql = "SELECT technics FROM methods WHERE name=?"
            cursor.execute(sql, (a,))
            result = cursor.fetchall()
            o = result[0]
            b = list(o)
            lng = count_copy(b[0])
            m = db_table_val2(int(b[0]))
            print(m)
            list(m)
            i = 0
            while i < (lng):
                keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                               [m[i]]])
                i = i + 1
            keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['К меню ->']])
            bot.send_message(k.message.chat.id, 'Просмотрите подходящие сервисы:', reply_markup=keyboard)
    elif (k.data == 'Техническое обеспечение'):
        a: str
        a = get(k.from_user.id)
        if (a == 'Удобство навигации') or (a == 'Выделение основных конкурентов') or (a == 'Анализ дизайна') or (
                a == 'Система оплаты') or (a == 'Обратная связь') or (a == 'Сравнение по критериям') or (
                a == 'SEO анализ') or (a == 'Определение ссылочного профиля') or (a == 'Обзор контента') or (
                a == 'Диагностика рекламы') or (a == 'Ценовая политика') or (a == 'Email-рассылка') or (
                a == 'Оценка соц. сетей') or (a == 'Поведение пользователей') or (a == 'Анализ состояния товара') or (
                a == 'Анализ конкурентных преимуществ'):
            bot.send_message(k.message.chat.id,k.data)
            keyboard = types.InlineKeyboardMarkup()
            bot.send_message(k.message.chat.id, a)
            sql = "SELECT technics FROM concurent WHERE name=?"
            cursor.execute(sql, (a,))
            result = cursor.fetchall()
            o = result[0]
            b = list(o)
            lng = count_copy(b[0])
            m = db_table_val2(int(b[0]))
            print(m)
            list(m)
            i = 0
            while i < (lng):
                keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                               [m[i]]])
                i = i + 1
            keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['К меню ->']])
            bot.send_message(k.message.chat.id, 'Просмотрите подходящие сервисы:', reply_markup=keyboard)

    elif k.data == 'Анализ технических параметров':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Удобство навигации']])
        keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Анализ дизайна']])
        keyboard.row(
            *[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Система оплаты']])
        keyboard.row(
            *[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Обратная связь']])
        msg = bot.send_message(k.message.chat.id, 'Выберите параметр для рассмотрения:', reply_markup=keyboard)

    elif (k.data == 'Определение стратегии'):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(
            *[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Анализ состояния товара']])
        keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['SEO анализ']])
        keyboard.row(
            *[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Определение ссылочного профиля']])
        keyboard.row(
            *[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Поведение пользователей']])
        keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Обзор контента']])
        keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Оценка соц. сетей']])
        keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Диагностика рекламы']])
        keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Ценовая политика']])
        keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Email-рассылка']])
        msg = bot.send_message(k.message.chat.id, 'Выберите параметр для рассмотрения:', reply_markup=keyboard)

    elif (k.data == 'Назад'):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Анализ конкурентных преимуществ']])
        keyboard.row(
            *[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Выделение основных конкурентов']])
        keyboard.row(
            *[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Сравнение по критериям']])
        keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Определение стратегии']])
        keyboard.row(
            *[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Анализ технических параметров']])
        msg = bot.send_message(k.message.chat.id, '‼Здравствуйте‼ \n✏Анализ конкуренции проекта - важнейший этап '
                                                  'в битве за лидерство на рынке и удержания проекта "на плаву"‼\n'
                                                  '✏EstimationComp_bot предлает разработанный алгоритм проверки '
                                                  'конкурентоспособности\n'
                                                  '✏Выберите нужный этап процесса диагностки, и мы предоставим всю необходимую информацию‼\n\n'
                                                  'Остались вопросы по работе с ботом? Отправь любой ответ  на это сообщение, '
                                                  'и мы поможем тебе разобраться!', reply_markup=keyboard)
    else:
        us_id = k.from_user.id
        del_id(us_id)
        db_table_val(num=k.data, user_id=us_id)
        a: str
        a = get(k.from_user.id)
        keyboard = types.InlineKeyboardMarkup()
        bot.send_message(k.message.chat.id, a)
        sql = "SELECT description FROM technics WHERE name=?"
        cursor.execute(sql, (a,))
        result = cursor.fetchall()
        o = result[0]
        sql = "SELECT link FROM technics WHERE name=?"
        cursor.execute(sql, (a,))
        result = cursor.fetchall()
        lk = result[0]
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Назад']])
        bot.send_message(k.message.chat.id, o)
        bot.send_message(k.message.chat.id, lk, reply_markup=keyboard)

bot.polling(none_stop=True)
