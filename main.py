import telebot

TOKEN = '5198566227:AAGeVXLtPHBNEgl5A1JAQwyL3a85gKKCCtw'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Hello')
    bot.send_message(message.from_user.id, f'''Вот что я умею?
/help - посмотреть список команд
/black - посмотреть черный список
/addtoblok - добавить тему/слово в черный список''')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, f'''Вот что я умею?
/help - посмотреть список команд
/black - посмотреть черный список
/addtoblok - добавить тему/слово в черный список''')

@bot.message_handler(commands=['black'])
def blacklist(message):
    bot.send_message(message.from_user.id, f'''Слова/темы в черном списке''')

@bot.message_handler(commands=['addtoblok'])
def add_to_blacklist(message):
    bot.send_message(message.from_user.id, 'Введите слово, которое хотите добавить в черный список')

if __name__ == '__main__':
    bot.polling(none_stop = True, interval = 0)