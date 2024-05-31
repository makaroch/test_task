from pydantic import BaseModel


class DBSettings(BaseModel):
    HOST: str
    PORT: int
    USER: str
    PASSWD: str
    DB_NAME: str
