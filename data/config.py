from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
ADMINS = env.list('ADMINS')
YANDEX_KEY = env.str('YANDEX_KEY')
BITLY_KEY = env.str('BITLY_KEY')
CUTTLY_KEY = env.str('CUTTLY_KEY')
