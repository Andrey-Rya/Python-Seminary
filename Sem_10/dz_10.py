import logging
import random

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from token01 import  TOK
bot_token = TOK

reply_keyboard = [['/play', '/info', '/close']]
stop_keyboard = [['/stop']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
stop_markup = ReplyKeyboardMarkup(stop_keyboard, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

#TOKEN = ''
TOKEN = bot_token

print('Бот запущен!')

verify = 0
candy = 0
conf = 0
def start(update, context):
    update.message.reply_text(
        "Привет! Давайте поиграем со мной в одну простую игру. Называется она конфетки. "
        "Для запуска игры нажмите /PLAY.\n"
        "Для того чтобы ознакомиться с правилами игры нажмите /INFO.\n"
        "Для выхода из игры нажмите /CLOSE\n",
        reply_markup=markup
    )

def play(update, context):
    update.message.reply_text("Введите количество конфет, которое вы хотите положить в тарелку"
                              " на столе (но не менее 30 шт)", reply_markup=stop_markup)
    return 3

def play_verify(update, context):
    global verify
    global candy
    verify = int(update.message.text)
    if verify > 30:
        update.message.reply_text(f"Вы положили в тарелку {verify} конфет(ы)", reply_markup=stop_markup)
        candy = int(verify)
        update.message.reply_text("Какое количество конфет Вы возьмете? (вводите от 1 до 28шт)", reply_markup=stop_markup)
        return 2

    else:
        update.message.reply_text("Введите количество конфет больше 30!", reply_markup=stop_markup)
        return 3


def player_1(update, context):
    global candy
    global conf
    try:
        conf = int(update.message.text)
        if conf > 28 or conf < 1:
            update.message.reply_text("Вы должны брать от 1 до 28 конфет!", reply_markup=stop_markup)
            return 2
        else:
            update.message.reply_text(f'Вы взяли {update.message.text} конфет(ы)', reply_markup=stop_markup)
            candy -= int(update.message.text) # аналогично candy = candy - int(update...)
            update.message.reply_text(f'На столе осталось {candy} конфет(ы)', reply_markup=stop_markup)
            if candy > 28:
                temp = random.randint(1,28)
                candy -= temp
                update.message.reply_text(f'БОТ взял {temp} конфет(ы)', reply_markup=stop_markup) # вместо 5 - candy%29 - это чтобы бот всегда выигрывал
                candy -= 5
                update.message.reply_text(f'На столе осталось {candy} конфет(ы)', reply_markup=stop_markup)
                if candy > 28:
                    update.message.reply_text("Какое количество конфет Вы возьмете?", reply_markup=stop_markup)

                else:
                    update.message.reply_text("Ура! Вы победили хитрого БОТА!", reply_markup=markup)
                    #context.bot.send_photo(update.effective_chat.id, photo=open('win.gif', 'rb')) # используем ссылку на лок файл
                    context.bot.send_document(chat_id=update.effective_chat.id, document='https://i.gifer.com/1W9X.gif') # можно использовать ссылку на внешний файл
                    return ConversationHandler.END
                return 2
            else:
                update.message.reply_text("Увы! Вы проиграли. Победил БОТ.", reply_markup=markup)
                #context.bot.send_photo(update.effective_chat.id, photo=open('lost.gif', 'rb'))
                context.bot.send_document(chat_id=update.effective_chat.id, document='https://i.gifer.com/7Oac.gif')
                return ConversationHandler.END
    except ValueError:
        update.message.reply_text("Вы должны вводить только числа!")
        return 2

def stop(update, context):
    update.message.reply_text('Всего доброго!', reply_markup=markup)
    return ConversationHandler.END

def info(update, context):
    update.message.reply_text(
        "Правила игры очень простые. Сначала вы кладете в тарелку какое то количество конфет. От 30 до бесконечности. "
        "От этого будет зависеть длительность игры. Затем берёте оттуда любое количество (от 1 до 28)."
        "Далее БОТ берет какое-то количество конфет (от 1 до 28). Побеждает тот, кто возьмет из тарелки "
        "последние оставшиеся конфеты.")


def close(update, context):
    update.message.reply_text(
        "Спасибо за то, что поиграли со мной!",
    reply_markup = ReplyKeyboardRemove())


play_handler = ConversationHandler(
        entry_points=[CommandHandler('play', play)],

        # Состояние внутри диалога.
        states={
            #1: [MessageHandler(Filters.text & ~Filters.command, play_get_candy)],
            2: [MessageHandler(Filters.text & ~Filters.command, player_1)],
            3: [MessageHandler(Filters.text & ~Filters.command, play_verify)],
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(play_handler)
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("close", close))
    dp.add_handler(CommandHandler("stop", stop))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
    
