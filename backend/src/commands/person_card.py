from telebot.types import CallbackQuery, Message

from .tags import extract_head_tags
from ..functions import FakeFunctions
from ..back_modules import find_user_ids_by_tags, find_projects_through_tags


def cmd_get_random_person(bot, chat_id):
    bot.send_message(
        chat_id,
        text=FakeFunctions.get_random_person()
    )


def resp_search_people(bot):
    def f(query: CallbackQuery):
        msg: Message = query.message.reply_to_message
        head, initial_tags = extract_head_tags(msg.text)
        people = find_user_ids_by_tags(initial_tags)
        bot.send_message(msg.chat.id, text="Found people:")
        for person in people:
            bot.send_message(msg.chat.id, text=person)
    return f


def resp_search_projects(bot):
    def f(query: CallbackQuery):
        msg: Message = query.message.reply_to_message
        head, initial_tags = extract_head_tags(msg.text)
        projects = FakeFunctions.get_projects_by_tags(initial_tags)
        bot.send_message(msg.chat.id, text="Found projects:")
        for project in projects:
            bot.send_message(msg.chat.id, text=project)
    return f
