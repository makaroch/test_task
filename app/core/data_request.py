from pydantic import BaseModel


class DataRequest(BaseModel):
    '''
        pydantic model to return data
    '''
    id: int
    client_id: int
    area_id: int
    data: str
