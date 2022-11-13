from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from random import randint
#from bot_commands import  *

from token01 import  TOK
bot_token = TOK
print('Бот запущен!')

# привязка телефонной книги
import sqlite3

bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


# pip install python-telegram-bot==13.14
# Updater → Dispatсher → Handlers → start → wait_for_the_end
# Updater - взаимодействие между клиентом и сервером
# Dispatсher - отвечает за вызов обработчика сообщений
# Handlers - обработчики сообщений

def start(update, context):
    context.bot.send_message(update.effective_chat.id, f'Перед вами телефонный справочник\n'
    '/start - Запуск программы\n'
    '/list - Показать всех абонентов\n'
    '/stop - Выход\n')

# показать все контакты
def list(update, context):
    context.bot.send_message(update.effective_chat.id, 'Перед Вами полный список базы данных ')
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute("select * from phonebook")
    results = cursor.fetchall()
    print(results) # вывожу просто для контроля
    update.message.text = results
    update.message.reply_text(update.message.text)
    return

def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END

def list_output(update, context):
    context.bot.send_message(update.effective_chat.id, 'проверка: ')
    #update.message.reply_text(f'это будет {int(update.message.text) * 1000} грамм')
    return 1


list_handler = ConversationHandler(
         entry_points=[CommandHandler('list', list)],
         states={
            # Функция читает ответ на первый вопрос и задаёт второй.
              1: [MessageHandler(Filters.text & ~Filters.command, list_output)],
            # Функция читает ответ на второй вопрос и задаёт третий.
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )
