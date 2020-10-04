from telebot import TeleBot
from telebot.types import CallbackQuery, Message

from .tags import extract_head_tags
from ..back_modules import find_user_ids_by_tags, \
    find_projects_through_tags, serialize_project, \
    get_project_by_id, get_user_info_by_id, \
    serialize_user, get_random_person_id, get_random_project_id


def cmd_get_random_person(bot, chat_id):
    text, photo = serialize_user(get_user_info_by_id(get_random_person_id()))
    bot.send_photo(
        chat_id,
        photo=photo,
        caption="🍴🍽 Have a nice lunch! Do not hesitate\n" + text,
        parse_mode="HTML"
    )


def cmd_get_random_project(bot, chat_id):
    text = serialize_project(get_project_by_id(get_random_project_id()))
    bot.send_message(
        chat_id,
        text=text,
        parse_mode="HTML"
    )


def resp_search_people(bot: TeleBot):
    def f(query: CallbackQuery):
        msg: Message = query.message.reply_to_message
        head, initial_tags = extract_head_tags(msg.text)
        people = list(map(serialize_user, map(get_user_info_by_id, find_user_ids_by_tags(initial_tags))))
        bot.send_message(msg.chat.id, text="Found people:")
        for person, photo in people:
            bot.send_photo(
                msg.chat.id,
                photo=photo,
                caption=person,
                parse_mode="HTML",
            )

    return f


def resp_search_projects(bot):
    def f(query: CallbackQuery):
        msg: Message = query.message.reply_to_message
        head, initial_tags = extract_head_tags(msg.text)
        projects = list(map(serialize_project, map(get_project_by_id, find_projects_through_tags(initial_tags))))
        bot.send_message(msg.chat.id, text="Found projects:")
        for project in projects:
            bot.send_message(msg.chat.id, text=project, parse_mode="HTML")

    return f
