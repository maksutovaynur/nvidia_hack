import telebot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton

log = print

bot = telebot.TeleBot(S.BOT_TOKEN)


@bot.message_handler(content_types=["text"])
def root(message: Message):
    log("root handler")
    chat_id = message.from_user.id
    t = message.text
    if t == "/search_person":
        pass
    elif t == "/search_project":
        pass
    elif t == "/appoint_lunch":
        pass
    else:
        pass

