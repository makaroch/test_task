from fastapi import FastAPI
from app.db.database import DBWorker
from app.core.data_request import DataRequest
import uvicorn

app = FastAPI()


@app.get("/get_request")
async def get_request(filter_client: str | None = None, filter_area: str | None = None) -> list[DataRequest]:
    '''
    :param filter_client: the full name of the client to filter the request
    :param filter_area: the full name of the area to filter the request
    :return:
    '''
    if filter_client is not None and filter_area is not None:
        return await DBWorker().select_request_filter_area_client(client_name=filter_client, area_name=filter_area)
    if filter_client is not None:
        return await DBWorker().select_request_filter_client(client_name=filter_client)
    if filter_area is not None:
        return await DBWorker().select_request_filter_area(area_name=filter_area)
    return await DBWorker().select_request()


if __name__ == "__main__":
    uvicorn.run(app=app,
                host='127.0.0.1',
                port=80
                )
