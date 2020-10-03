import os
from environs import Env

env = Env()
env.read_env(os.path.join(__file__, os.path.pardir, ".env"))

BOT_TOKEN = env.str("BOT_TOKEN")

