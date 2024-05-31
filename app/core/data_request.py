from pydantic import BaseModel


class DataRequest(BaseModel):
    id: int
    client_id: int
    area_id: int
    data: str
