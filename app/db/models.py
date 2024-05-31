from sqlalchemy import ForeignKey, String
from sqlalchemy.ext.asyncio import AsyncAttrs
from typing import Annotated
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

str_256 = Annotated[str, mapped_column(String(256))]


class Base(AsyncAttrs, DeclarativeBase):
    pass


class TRequest(Base):
    __tablename__ = "t_request"
    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("t_client.id", ondelete="CASCADE"))
    area_id: Mapped[int] = mapped_column(ForeignKey("t_area.id", ondelete="CASCADE"))
    data: Mapped[str_256]


class TClient(Base):
    __tablename__ = "t_client"
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname_client: Mapped[str_256]


class TArea(Base):
    __tablename__ = "t_area"
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname_area: Mapped[str_256]
