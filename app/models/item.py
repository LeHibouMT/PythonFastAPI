from sqlalchemy import Column, Integer, String
from app.database import Base
from pydantic import BaseModel
from typing import Optional

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True, nullable=True)

class ItemModel(BaseModel):
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True