from telebot import TeleBot
from . import CommandNames


HelpMessages = {
    CommandNames.SEARCH_PERSON.value: "Найти подходящих вам людей",
    CommandNames.SEARCH_PROJECT.value: "Найти интересные проекты",
    CommandNames.RANDOM_MEET.value: "Побеседовать со случайным человеком",
    CommandNames.HELP.value: "Показать это сообщение",
}


def cmd_help(chat_id, bot: TeleBot):
    bot.send_message(
        chat_id,
        text="\n".join(
            f"{cmd.value} - {HelpMessages.get(cmd.value, '...')}"
            for cmd in CommandNames
            if not cmd.value.startswith("_")
        )
    )
