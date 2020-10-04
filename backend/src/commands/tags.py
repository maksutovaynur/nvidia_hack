from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

from src.commands import CallbackNames
from ..functions import FakeFunctions


def extract_head_tags(text):
    head, tags = text.split(":", 1)
    return head, clean_tags(tags.split(", "))


def clean_tag(tag):
    return tag.strip()


def clean_tags(tags):
    tags = set(map(clean_tag, tags))
    return sorted(t for t in tags if t)


def add_tag(tags, tag):
    return clean_tags(set(tags) | {clean_tag(tag)})


def rm_tag(tags, tag):
    return clean_tags(set(tags) - {clean_tag(tag)})


def put_text(head, tags):
    return f"{head}: {', '.join(tags)}"


def tags_reply_markup(tags, txt_f=lambda t: t, clb_f=lambda t: t):
    kb = InlineKeyboardMarkup()
    kb.add(*(InlineKeyboardButton(text=txt_f(tag), callback_data=clb_f(tag)) for tag in tags))
    return kb


def repair_tags(bot, msg: Message, head, tags):
    kb = tags_reply_markup(
            tags,
            txt_f=lambda t: f"{t} \u274C",
            clb_f=lambda t: f"{CallbackNames.RM_TAG.value} {t}"
    )
    bot.edit_message_text(
        chat_id=msg.chat.id,
        message_id=msg.message_id,
        text=put_text(head, tags),
        reply_markup=kb
    )


def resp_add_tag(bot):
    def f(query: CallbackQuery):
        msg: Message = query.message.reply_to_message
        head, initial_tags = extract_head_tags(msg.text)
        tags = add_tag(initial_tags, query.data.split(" ", 1)[-1])
        if len(tags) != len(initial_tags):
            repair_tags(bot, msg, head, tags)
    return f


def resp_rm_tag(bot):
    def f(query: CallbackQuery):
        msg: Message = query.message
        head, initial_tags = extract_head_tags(msg.text)
        tags = rm_tag(initial_tags, query.data.split(" ", 1)[-1])
        if len(tags) != len(initial_tags):
            repair_tags(bot, msg, head, tags)
    return f


def resp_search_people(bot):
    def f(query: CallbackQuery):
        msg: Message = query.message.reply_to_message
        head, initial_tags = extract_head_tags(msg.text)
        people = FakeFunctions.get_people_by_skills(initial_tags)
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


def cmd_create_search_tags(bot, chat_id, selected_head, all_head, add_key=None):
    msg = bot.send_message(chat_id, text=f"{selected_head}: ")
    tags = FakeFunctions.get_skill_tags()
    kb = tags_reply_markup(tags, clb_f=lambda t: f"{CallbackNames.ADD_TAG.value} {t}")
    if add_key is not None:
        kb.add(add_key)
    bot.send_message(
        chat_id,
        text=all_head,
        reply_markup=kb,
        reply_to_message_id=msg.message_id
    )



