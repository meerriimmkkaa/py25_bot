import telebot
import random
from env import TOKEN 

bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup()              #клавиатура
button1 = telebot.types.KeyboardButton('yes')
button2 = telebot.types.KeyboardButton('No')
keyboard.add(button1, button2)


@bot.message_handler(commands=['start', 'hello'])       #2

def start_function(message):
    msg = bot.send_message(message.chat.id,f'Вы запустили бот {message.chat.first_name} начнем игру?', reply_markup=keyboard) #3
    bot.register_next_step_handler(msg, answer_check)       #4
    # bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAJKn2OhQ3oGJhOfnEHguEno9QteFPUlAAIHAAPNjaUsHiteYSbeo0osBA')                #№№№выдает стикер , фото
    # bot.send_photo(message.chat.id,'https://avatars.mds.yandex.net/get-kinopoisk-image/1898899/957490ea-36aa-402e-90af-5257e5ff7797/1920x')

# @bot.message_handler()
# def echo_all(message):        ####выдает только сообщение
#     bot.send_message(message.chat.id, message.text)

def answer_check(msg):      #№5
    if msg.text == 'yes':
        bot.send_message(msg.chat.id, 'у тебя есть 3 попытки угадать число от 1 до 10! ;)')  #правило игры
        random_number = random.randint(1, 10)       #рандом число
        tryse = 3
        start_game(msg, random_number, tryse)


    else:
        bot.send_message(msg.chat.id, 'если не хочешь не надо :(')




def start_game(msg, random_number, tryse):
    msg = bot.send_message(msg.chat.id, 'Введите число от 1 до 10: ')               #ответ пользоватеою
    bot.register_next_step_handler(msg, check_func, random_number, tryse=tryse-1)                   

def check_func(msg, random_number, tryse):
    if msg.text == str(random_number):
        bot.send_message(msg.chat.id, 'Вы правильно ввели ! ')
    elif tryse == 0:
        bot.send_message(msg.chat.id, f'Вы не правильно ввели ! Число было - {random_number}')
    else:
        bot.send_message(msg.chat.id, f'Попробуй ещё разок, у тебя есталось {tryse} попыток!')
        start_game(msg, random_number, tryse)





bot.polling()       ##1











# git init
# git add .
# git commit - m  'names commit'
# git remote add origin hhtp
# git push origin master