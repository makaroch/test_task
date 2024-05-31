from pydantic import BaseModel


class DBSettings(BaseModel):
    '''
        pydantic model to connect to the database
    '''
    HOST: str
    PORT: int
    USER: str
    PASSWD: str
    DB_NAME: str
