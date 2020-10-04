from os.path import join, abspath, dirname
from environs import Env

SRC_DIR = dirname(abspath(__file__))
env = Env()
env.read_env(join(SRC_DIR, ".env"))

BOT_TOKEN = env.str("BOT_TOKEN")

