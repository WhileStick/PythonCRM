from environs import Env

env = Env()
env.read_env()

DB_USER = env.str("DB_USER")
DB_HOST = env.str("DB_HOST")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")