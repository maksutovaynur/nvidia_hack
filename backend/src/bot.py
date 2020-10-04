import telebot
from telebot.types import Message, InlineKeyboardButton

from . import settings as S
from .commands import CallbackNames, CommandNames
from .commands.common import cmd_help
from .commands.tags import resp_add_tag, resp_rm_tag, \
    cmd_create_search_tags
from .commands.person_card import cmd_get_random_person, resp_search_people, resp_search_projects

from .back_modules import get_all_users_tags, get_all_projects_tags
log = print

bot = telebot.TeleBot(S.BOT_TOKEN)


@bot.message_handler(content_types=["text"])
def root(message: Message):
    log("root handler")
    chat_id = message.from_user.id
    t = message.text
    if t == "/start":
        bot.send_message(
            chat_id,
            text="Welcome to Nvidia Tinder"
        )
        cmd_help(bot, chat_id)
    elif t == CommandNames.SEARCH_PERSON.value:
        cmd_create_search_tags(
            bot,
            chat_id,
            selected_head="Search person with skills",
            all_head="Add skill",
            tags=get_all_users_tags(),
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
            tags=get_all_projects_tags(),
            add_key=InlineKeyboardButton(
                text="📂🔎 Search projects",
                callback_data=CallbackNames.SEARCH_PROJECT.value
            )
        )
    elif t == CommandNames.RANDOM_LUNCH.value:
        cmd_get_random_person(bot, chat_id)
    elif t == CommandNames.HELP.value:
        cmd_help(bot, chat_id)
    else:
        cmd_help(bot, chat_id)


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
