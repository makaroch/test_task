import os

from dotenv import load_dotenv
from app.core.db_settings import DBSettings


def __get_env() -> DBSettings:
    load_dotenv()
    return DBSettings(
        HOST=os.getenv("HOST"),
        PORT=os.getenv("PORT"),
        USER=os.getenv("USER"),
        PASSWD=os.getenv("PASSWD"),
        DB_NAME=os.getenv("DB_NAME")
    )


def database_url_aiomysql() -> str:
    db_set = __get_env()
    return f"mysql+aiomysql://{db_set.USER}:{db_set.PASSWD}@{db_set.HOST}:{db_set.PORT}/{db_set.DB_NAME}"
