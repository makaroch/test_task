from fastapi import FastAPI
from app.db.database import DBWorker
from app.core.data_request import DataRequest
import uvicorn

app = FastAPI()


@app.get("/get_request")
async def get_request(filter_client: str | None = None, filter_area: str | None = None) -> list[DataRequest]:
    if filter_client is not None and filter_area is not None:
        return await DBWorker().select_request_filter_area_client(client_name=filter_client, area_name=filter_area)
    if filter_client is not None:
        return await DBWorker().select_request_filter_client(client_name=filter_client)
    if filter_area is not None:
        return await DBWorker().select_request_filter_area(area_name=filter_area)
    return []


if __name__ == "__main__":
    uvicorn.run(app=app,
                host='127.0.0.1',
                port=80
                )
