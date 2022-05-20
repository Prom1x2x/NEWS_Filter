
import telebot
import os
import shutil
import pickle

black_list = []
with open('./DB/block_list.pickle', 'wb') as f:
    pickle.dump(black_list,f)
with open('./DB/block_list.pickle', 'rb') as f:
    black_list = pickle.load(f)

text_example = ['В Санкт-Петербурге смягчат меры по COVID-19 с 21 февраля', 'Сборная России по хоккею сыграет с Данией в четвертьфинале Олимпиады в Пекине', 'Российский биатлонист Эдуард Латыпов назвал причину неудачной стрельбы в эстафете на Олимпиаде в Пекине.']
fragments = {}
TOKEN = '5198566227:AAGeVXLtPHBNEgl5A1JAQwyL3a85gKKCCtw'

bot = telebot.TeleBot(TOKEN)

def addtoblock(message):
    new_word = message.text
    # print(new_word)
    with open('./DB/block_list.pickle', 'rb') as f:
        black_list = pickle.load(f)
    black_list.append(new_word)
    # print(black_list)
    with open('./DB/block_list.pickle', 'wb') as f:
        pickle.dump(black_list,f)
    bot.send_message(message.from_user.id, 'Слово добавлено в черный список')

def delfromblock(message):
    del_word = message.text
    with open('./DB/block_list.pickle', 'rb') as f:
        black_list = pickle.load(f)
    black_list.remove(del_word)
    with open('./DB/block_list.pickle', 'wb') as f:
        pickle.dump(black_list,f)
    bot.send_message(message.from_user.id, 'Слово удалено из черный список')

def view_news(message):
    buffer = []
    bot.send_message(message.from_user.id, 'Вот что я подобрал для Вас')
    with open('./DB/block_list.pickle', 'rb') as f:
        black_list = pickle.load(f)
    for ban_word in black_list:
        for item in text_example:
            fragments[item] = []
            new_item = item.lower().replace(" ","")
            for part in range(len(new_item)):
                fragment = new_item[part: part+len(ban_word)]
                fragments[item].append(fragment)

        for text in fragments.values():
            print(text)
            for word in text:
                # print(word)
                if word == ban_word.lower().replace(" ",""):
                    print(ban_word)
                    key=list(fragments.keys())[list(fragments.values()).index(text)]
                    buffer.append(key)
    print(buffer)
    for item in buffer:
        fragments.pop(item)
    for keys in fragments.keys():
        bot.send_message(message.from_user.id, keys)
                    

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Привет, я новостной бот, который будет отправлять самые интересные для тебя новости')
    bot.send_message(message.from_user.id, f'''Вот что я умею?
/help - посмотреть список команд
/block - посмотреть черный список
/addtoblock - добавить тему/слово в черный список
/viewnews - посмотреть новости
/delfromblock - удалить из черного списка''')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, f'''Вот что я умею?
/help - посмотреть список команд
/block - посмотреть черный список
/addtoblock - добавить тему/слово в черный список
/viewnews - посмотреть новости
/delfromblock - удалить из черного списка''')

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

@bot.message_handler(commands=['delfromblock'])
def del_from_block(message):
    add_text = bot.send_message(message.from_user.id, 'Введить слово/тему которое хотите убрать из черного списка')
    bot.register_next_step_handler(add_text, delfromblock)

@bot.message_handler(commands = ['viewnews'])
def news(message):
    view_news(message)
    

@bot.message_handler(content_types = ['text'])
def get_text(message):
    pass
        

if __name__ == '__main__':
    bot.polling(none_stop = True, interval = 0)