
import telebot
from Test_Config import keys, TOKEN
from Test_Class import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def Settings( message : telebot.types.Message):
    text = 'Приветствие, это бот конвертации валют \n' \
           'укажите поочередно две валюты и число для конвертации \n' \
           'Узнать список доступных валют /values'
    bot.reply_to(message, text )

@bot.message_handler(content_types=['sticker', 'photo'])
def handle_photo (message: telebot.types.Message):
    bot.reply_to(message, f'Тупые картинки')

@bot.message_handler(commands=['values'])
def values (message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text',])
def convert (message: telebot.types.Message):
    try:
        values = list(map(str.lower, message.text.split(' ')))

        if len(values) != 3:
            raise ConvertionException('Слишком много параметров')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя \n{e} ')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n {e}')
    else:
        text = f'Цена {amount}  {quote} в {base} - {int(total_base) * int(amount)}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)