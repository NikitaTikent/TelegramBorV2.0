import telebot
from telebot import types
from parsers import ParseAll

bot = telebot.TeleBot()

def babki(XRP, Dollar, My):
    # Убирает лишние символы, добавляет нужные, производит расчет имеющихся средств в рублях
    XRP = XRP.replace('$', '').replace(',', '')
    Dollar = Dollar.replace(',', '.')
    Result = round((float(XRP) * float(Dollar)*float(My)), 1)
    return Result

def ImageOut(XRP, Dollar, ResultBabki):
    text_def = """\
    Курс Криптовалюты: {}\n\nКурс USD: {}Р\n\nРезультат: {}Р
    """
    Out = text_def.format(XRP, Dollar, ResultBabki)
    return Out

def Osnova(My):
    XRP, Dollar = ParseAll()
    ResultBabki = babki(XRP, Dollar, My)
    a = ImageOut(XRP, Dollar, ResultBabki)
    return a

# Клавиатура
keyboard1 = types.InlineKeyboardMarkup(row_width=1)
item = types.InlineKeyboardButton('Как обычно', callback_data='One')
keyboard1.add(item)
#


@bot.message_handler(content_types=['text'])
def lalala(message):
    My = float(float(message.text))
    bot.send_message(message.chat.id, Osnova(My), reply_markup=keyboard1)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'One':
                bot.send_message(call.message.chat.id, Osnova(0.0414), reply_markup=keyboard1)
    except Exception as e:
        bot.send_message(call.message.chat.id, 'error'+str(e), reply_markup=keyboard1)

# RUN

bot.polling(none_stop=True)
