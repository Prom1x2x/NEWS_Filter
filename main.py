
import telebot
import os
import shutil
import pickle

# black_list = []
# with open('./DB/block_list.pickle', 'wb') as f:
#     pickle.dump(black_list,f)
# with open('./DB/block_list.pickle', 'rb') as f:
#     black_list = pickle.load(f)

text_example = ['Футбол это круто', 'Привет, я банан']
fragments = []
TOKEN = '5198566227:AAGeVXLtPHBNEgl5A1JAQwyL3a85gKKCCtw'

bot = telebot.TeleBot(TOKEN)

def addtoblock(message):
    new_word = message.text
    print(new_word)
    with open('./DB/block_list.pickle', 'rb') as f:
        black_list = pickle.load(f)
    black_list.append(new_word)
    print(black_list)
    with open('./DB/block_list.pickle', 'wb') as f:
        pickle.dump(black_list,f)

def view_news(message):
    bot.send_message(message.from_user.id, 'Вот что я подобрал для Вас')
    with open('./DB/block_list.pickle', 'rb') as f:
        black_list = pickle.load(f)
    for ban_word in black_list:
        for item in text_example:
            item = item.lower().replace(" ","")
            for part in range(len(item)):
                fragment = item[part: part+len(ban_word)]
                fragments.append(fragment)
    print(fragments)
    for text in fragments:
        # print(text)
        # print(fragments)
        if text == ban_word:
            print(ban_word)
    #         bot.send_message(message.from_user.id, text_example)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Hello')
    bot.send_message(message.from_user.id, f'''Вот что я умею?
/help - посмотреть список команд
/block - посмотреть черный список
/addtoblock - добавить тему/слово в черный список
/viewnews - посмотреть новости''')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, f'''Вот что я умею?
/help - посмотреть список команд
/block - посмотреть черный список
/addtoblock - добавить тему/слово в черный список
/viewnews - посмотреть новости''')

@bot.message_handler(commands=['block'])
def blocklist(message):
    bot.send_message(message.from_user.id, f'''Слова/темы в черном списке''')
    with open('./DB/block_list.pickle', 'rb') as f:
        black_list = pickle.load(f)
    bot.send_message(message.from_user.id, '\n'.join(black_list))

@bot.message_handler(commands=['addtoblock'])
def add_to_blacklist(message):
    add_text = bot.send_message(message.from_user.id, 'Введите слово, которое хотите добавить в черный список')
    bot.register_next_step_handler(add_text, addtoblock)

@bot.message_handler(commands = ['viewnews'])
def news(message):
    view_news(message)
    

@bot.message_handler(content_types = ['text'])
def get_text(message):
    pass
        

if __name__ == '__main__':
    bot.polling(none_stop = True, interval = 0)