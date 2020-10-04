from ..functions import FakeFunctions


def cmd_get_random_person(bot, chat_id):
    bot.send_message(
        chat_id,
        text=FakeFunctions.get_random_person()
    )

