from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from . import CommandNames


HelpMessages = {
    CommandNames.SEARCH_PERSON.value: "🔎 Find suitable people 👤",
    CommandNames.SEARCH_PROJECT.value: "🔎 Find interesting projects 📂",
    CommandNames.RANDOM_LUNCH.value: "🤔 Have a lunch with random person?",
    CommandNames.RANDOM_PROJECT.value: "Investigate random project",
    CommandNames.HELP.value: "Show this help message again",
}


help_text = "\n".join(
    f"{cmd.value} - {HelpMessages.get(cmd.value, '...')}"
    for cmd in CommandNames
    if not cmd.value.startswith("_")
)


km = ReplyKeyboardMarkup(row_width=2)
km.add(*(KeyboardButton(cmd.value) for cmd in CommandNames))


def cmd_help(bot: TeleBot, chat_id):
    bot.send_message(
        chat_id,
        text=help_text,
        reply_markup=km
    )
