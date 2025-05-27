from pydantic import BaseModel
from datetime import datetime

class TrabalhoBase(BaseModel):
    titulo: str
    descricao: str | None = None
    data_entrega: datetime
    disciplina_id: int

class TrabalhoCreate(TrabalhoBase):
    pass

class TrabalhoUpdate(BaseModel):
    titulo: str | None = None
    descricao: str | None = None
    data_entrega: datetime | None = None
    disciplina_id: int | None = None

class TrabalhoResponse(TrabalhoBase):
    id: int

    class Config:
        orm_mode = True
