class DBException(Exception):
    pass


class EnvError(DBException):
    def __init__(self):
        super().__init__("Ошибка в переменных окружения")
