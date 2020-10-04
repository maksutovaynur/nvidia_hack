import enum


class CommandNames(enum.Enum):
    SEARCH_PERSON = "/search_person"
    SEARCH_PROJECT = "/search_project"
    RANDOM_LUNCH = "/random_lunch"
    RANDOM_PROJECT = "/random_project"
    HELP = "/help"


class CallbackNames(enum.Enum):
    ADD_TAG = "/addtag"
    RM_TAG = "/rmtag"
    SEARCH_PERSON = "/search_person"
    SEARCH_PROJECT = "/search_project"
