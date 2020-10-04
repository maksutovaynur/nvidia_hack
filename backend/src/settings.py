from os.path import join, abspath, dirname
from environs import Env

SRC_DIR = dirname(abspath(__file__))
env = Env()
env.read_env(join(SRC_DIR, ".env"))

BOT_TOKEN = env.str("BOT_TOKEN")

PERSON_DF_PATH = join(SRC_DIR, "person.csv")
PERSON_SKILL_PATH = join(SRC_DIR, "person_skills.json")

PROJECT_DF_PATH = join(SRC_DIR, "projects.csv")
PROJECT_TAG_PATH = join(SRC_DIR, "project_tags.json")

IMG_DIR = join(SRC_DIR, "profile_avatars")

