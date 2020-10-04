import telebot
from telebot.types import Message, InlineKeyboardButton

from . import settings as S
from .commands import CallbackNames, CommandNames
from .commands.common import cmd_help
from .commands.tags import resp_add_tag, resp_rm_tag, \
    cmd_create_search_tags, resp_search_projects, resp_search_people

log = print

bot = telebot.TeleBot(S.BOT_TOKEN)


@bot.message_handler(content_types=["text"])
def root(message: Message):
    log("root handler")
    chat_id = message.from_user.id
    t = message.text
    if t == CommandNames.SEARCH_PERSON.value:
        cmd_create_search_tags(
            bot,
            chat_id,
            selected_head="Search person with skills",
            all_head="Add skill",
            add_key=InlineKeyboardButton(
                text="👤🔎 Search people",
                callback_data=CallbackNames.SEARCH_PERSON.value
            )
        )
    elif t == CommandNames.SEARCH_PROJECT.value:
        cmd_create_search_tags(
            bot,
            chat_id,
            selected_head="Search project by tech",
            all_head="Add tag",
            add_key=InlineKeyboardButton(
                text="📂🔎 Search projects",
                callback_data=CallbackNames.SEARCH_PROJECT.value
            )
        )
    elif t == CommandNames.RANDOM_MEET.value:
        pass
    elif t == CommandNames.HELP.value:
        cmd_help(chat_id, bot)
    else:
        cmd_help(chat_id, bot)


bot.callback_query_handler(
    lambda query: query.data.startswith(CallbackNames.ADD_TAG.value),
)(resp_add_tag(bot))

bot.callback_query_handler(
    lambda query: query.data.startswith(CallbackNames.RM_TAG.value)
)(resp_rm_tag(bot))

bot.callback_query_handler(
    lambda query: query.data.startswith(CallbackNames.SEARCH_PERSON.value)
)(resp_search_people(bot))

bot.callback_query_handler(
    lambda query: query.data.startswith(CallbackNames.SEARCH_PROJECT.value)
)(resp_search_projects(bot))
