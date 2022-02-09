import telebot

TOKEN = '5198566227:AAGeVXLtPHBNEgl5A1JAQwyL3a85gKKCCtw'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Hello')
    bot.send_message(message.from_user.id, '''Что я умею?
                                            /help - посмотреть список команд
                                            /black - посмотреть черный список''')

@bot.message_handler(commands=['help'])
def help(message):
    pass


if __name__ == '__main__':
    bot.polling(none_stop = True, interval = 0)