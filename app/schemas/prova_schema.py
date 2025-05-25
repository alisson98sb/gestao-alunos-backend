from pydantic import BaseModel
from datetime import datetime

class ProvaBase(BaseModel):
    conteudo: str
    data_prova: datetime
    disciplina_id: int

class ProvaCreate(ProvaBase):
    pass

class ProvaResponse(ProvaBase):
    id: int

    class Config:
        orm_mode = True
