import telebot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from . import settings as S
from .functions import FakeFunctions
from .commands import Callbacks, Commands

log = print

bot = telebot.TeleBot(S.BOT_TOKEN)


@bot.message_handler(content_types=["text"])
def root(message: Message):
    log("root handler")
    chat_id = message.from_user.id
    t = message.text
    if t == Commands.SEARCH_PERSON:
        kb = InlineKeyboardMarkup(row_width=5)
        tags = FakeFunctions.get_skill_tags()
        for tag in tags:
            kb.add(InlineKeyboardButton(text=tag, callback_data=f"/addtag {tag}"))
        bot.send_message(chat_id, text="Add skill:", reply_markup=kb)

    elif t == Commands.SEARCH_PROJECT:
        pass
    elif t == Commands.APPOINT_LUNCH:
        pass
    elif t == Commands.HELP:
        bot.send_message(
            text="\n".join(f"{cmd}" for cmd in Commands.__dict__().values())
        )
    else:
        pass


@bot.callback_query_handler(lambda query: query.data.startswith(Callbacks.ADD_TAG))
def process_add_tag(query: CallbackQuery):
    print(query.message.id)



