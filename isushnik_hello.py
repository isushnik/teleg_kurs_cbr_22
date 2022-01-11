import telebot
#from keyboard import generate_inline_keyboard
from cbr_requests_BIC import cbr_requests_BIC
from cbr_requests_kurs import cbr_requests_kurs
from cbr_requests_kurs import data_install_kurs
from cbr_news import cbr_news
from telebot import types
from datetime import datetime

TOKEN = None

with open("tkn.oe") as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Добро пожаловать, вот что я могу: \n')
 #   keyboard = keyboard.generate_inline_keyboard(['Имя', 'change_name'], ['Телефон', 'change_phone'], ['Вернуться обратно', 'back'])
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Курсы ЦБ']])
    # keyboard.add(*[types.KeyboardButton(name) for name in ['BIC - банк', 'Курсы ЦБ']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Новости', 'Информация', 'BIC']])
    bot.send_message(message.chat.id, 'Меню:', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    sp_hello = ['hi', 'ghbdtn', 'привет', 'хай', 'здорово', 'pljhjdj']
    if message.text.lower() in sp_hello:
        bot.send_message(message.from_user.id, 'Привет, чем могу помочь? Введи: /start или /help.')
    elif message.text == '/help':
        #bot.send_message(message.from_user.id, 'Раздел: помощь')
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton('Message the developer', url='telegram.me/isushnik'))
        bot.send_message(message.chat.id, 'Вы в разделе: Помощь', reply_markup=keyboard)
    elif message.text == 'Курсы ЦБ':
        now = datetime.now()
        now_data= now.strftime("%d %B %Y (%A)")
        bot.send_message(message.chat.id,'Сегодня, '+ now_data )

        bot.send_message(message.chat.id, data_install_kurs()) #  Курсы ЦБ на дату: {}'.format(data_install_kurs))

        requests_kurs_to_tlg = cbr_requests_kurs(valuta='USD') # запрос на USD
        print(requests_kurs_to_tlg)
        bot.send_message(message.from_user.id, requests_kurs_to_tlg)

        requests_kurs_to_tlg = cbr_requests_kurs(valuta='EUR') # запрос на EUR
        print(requests_kurs_to_tlg)
        bot.send_message(message.from_user.id, requests_kurs_to_tlg)



    elif message.text == 'Информация':
        bot.send_message(message.chat.id, 'Данные Курсов получены с сайта www.cbr.ru \n'
                                          'используя XML '
                                          '\n'
                                          '\n'
                                          '\n https://www.cbr.ru/development/SXML/ \n '
                                           'https://www.cbr.ru/')
    elif message.text == 'BIC - банк':
        bot.send_message(message.chat.id, 'Введи BIC банка:')
        bic = message.text
        bot.send_message(message.from_user.id, 'bic = 043304728', bic)
        bic = '043304728'
        print(bic, message.text, type(bic))
        answer_cbr_requests_BIC = cbr_requests_BIC(bic)
        bot.send_message(message.chat.id, 'Банк ' + answer_cbr_requests_BIC[0])
        print(answer_cbr_requests_BIC)

    elif message.text == 'Новости':
        count_news = 3
        answer_cbr_news = cbr_news()
        bot.send_message(message.chat.id, 'Новости')
        for i in range(count_news):
            print(answer_cbr_news[i])
            bot.send_message(message.chat.id, answer_cbr_news[i])

    elif message.text == 'BIC':
        bot.send_message(message.chat.id, "BIC - банк // in progress")

    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. ')


#http://www.cbr.ru/scripts/XML_bic.asp?bic=043304728

#bic = '043304728'
#answer_cbr_requests_BIC = cbr_requests_BIC(bic)
#print(answer_cbr_requests_BIC)
#bic_input = '043304728'

bot.polling(none_stop=True, interval=0)
#bot.polling()
# git up 2021_03_31
