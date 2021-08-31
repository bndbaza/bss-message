from pydantic import BaseModel


class PostBase(BaseModel):
    RegNumber: str
    Organ: str

    class Config:
        orm_mode = True
