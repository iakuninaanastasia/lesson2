import logging
import ephem
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot,update):
    print(update)
    text_cmd='Вызван /start'
    print(text_cmd)

    text_greet="""Привет {}!
Я простой бот и понимаю только команду {}
""".format(update.message.chat.first_name, '/start')
    logging.info('Пользователь {} нажал /start'.format(update.message.chat.username))
    update.message.reply_text(text_greet)

def talk_to_me(bot, update):
    user_text = update.message.text
    logging.info(user_text)
    update.message.reply_text(user_text)

#Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском.
#При помощи условного оператора if и ephem.constellation научите бота отвечать, в каком созвездии сегодня находится планета.

def constellation_of_planet (bot,update):
    user_text = update.message.text.replace('/planet ','').capitalize()
    today_date = datetime.datetime.today().strftime('%Y/%m/%d')
    if user_text=='Mars':
        today_location_of_planet=ephem.Mars(datetime.date.today())
        update.message.reply_text(ephem.constellation(today_location_of_planet))
    elif user_text=='Mercury':
        today_location_of_planet=ephem.Mercury(datetime.date.today())
        update.message.reply_text(ephem.constellation(today_location_of_planet))
    elif user_text=='Venus':
        today_location_of_planet=ephem.Venus(datetime.date.today())
        update.message.reply_text(ephem.constellation(today_location_of_planet))
    elif user_text=='Jupiter':    
        today_location_of_planet=ephem.Jupiter(datetime.date.today())
        update.message.reply_text(ephem.constellation(today_location_of_planet))
    elif user_text=='Saturn':    
        today_location_of_planet=ephem.Saturn(datetime.date.today())
        update.message.reply_text(ephem.constellation(today_location_of_planet))
    elif user_text=='Uranus':    
        today_location_of_planet=ephem.Uranus(datetime.date.today())
        update.message.reply_text(ephem.constellation(today_location_of_planet))
    elif user_text=='Neptune':    
        today_location_of_planet=ephem.Neptune(datetime.date.today())
        update.message.reply_text(ephem.constellation(today_location_of_planet)) 
    elif user_text=='Pluto':    
        today_location_of_planet=ephem.Pluto(datetime.date.today())
        update.message.reply_text(ephem.constellation(today_location_of_planet))              
    else:
        update.message.reply_text('Ошибка! Введите название планеты на английском.')



def word_count(bot,update):
    user_text = update.message.text
    user_text = user_text.replace('/wordcount ','')
    if len(user_text) <= 0:
        text_error_empty_string = 'Вы ввели пустую строку!'
        update.message.reply_text(text_error_empty_string)
    else:
        if user_text.startswith("\"") == True and user_text.endswith("\"") == True:
            word_count_in_user_text = int(user_text.count(' ')) + int(user_text.count('\n')) + 1
            text_count_words="{} слов".format(word_count_in_user_text)
            update.message.reply_text(text_count_words)
        else:
            update.message.reply_text('Введите фразу в кавычках!')
        


def calc (bot,update):
    user_text = update.message.text
    user_text = user_text.replace('/calc ','')
    if "=" not in user_text:
        update.message.reply_text('Выражение должно заканчиваться знаком =')
    elif " " in user_text:
        update.message.reply_text('Ошибка! Нельзя использовать пробелы в выражении.')
    else:
        try:
            user_text = user_text.replace('=','')
            if "+" in user_text:
                numbers = user_text.split("+")
                numbers = [float(x) for x in numbers]
                result_calc=round(numbers[0]-numbers[1])
                update.message.reply_text(result_calc)
            elif "-" in user_text:
                numbers = user_text.split("-")
                numbers = [float(x) for x in numbers]
                result_calc=round(numbers[0]-numbers[1])
                update.message.reply_text(result_calc)
            elif "/" in user_text:
                numbers = user_text.split("/")
                numbers = [float(x) for x in numbers]
                if numbers[1] == 0:
                    update.message.reply_text("Ошибка! Делить на 0 нельзя.")  
                else:
                    result_calc=round(numbers[0]/numbers[1])
                    update.message.reply_text(result_calc)
            elif "*" in user_text:
                numbers = user_text.split("*")
                numbers = [float(x) for x in numbers]
                result_calc=round(numbers[0]*numbers[1])
                update.message.reply_text(result_calc)
            else:
                update.message.reply_text('Данная команда умеет выполнять только следующие арифметические операции: сложение, вычитание, умножение и деление. Попробуйте использвать одну из этих операций.')
        except (ValueError):
            update.message.reply_text('Ошибка! Неверный формат операндов, операции можно выполнять только с числами')



def main():
    updtr=Updater(settings.TELEGRAM_API_KEY)
    dp=updtr.dispatcher
    dp.add_handler(CommandHandler("start",greet_user))
    dp.add_handler(CommandHandler("wordcount",word_count))
    dp.add_handler(CommandHandler("calc",calc))
    dp.add_handler(CommandHandler("planet",constellation_of_planet))
    dp.add_handler(MessageHandler(Filters.text,talk_to_me))

    updtr.start_polling()
    updtr.idle()


if __name__=="__main__":
    logging.info('Bot started')
    main()
