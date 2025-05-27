from pydantic import BaseModel
from datetime import datetime

class ProvaBase(BaseModel):
    conteudo: str
    data_prova: datetime
    disciplina_id: int

class ProvaCreate(ProvaBase):
    pass

class ProvaUpdate(BaseModel):
    conteudo: str | None = None
    data_prova: datetime | None = None
    disciplina_id: int | None = None

class ProvaResponse(ProvaBase):
    id: int

    class Config:
        orm_mode = True
