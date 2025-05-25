from pydantic import BaseModel
from datetime import datetime

class NotaBase(BaseModel):
    aluno_id: int
    disciplina_id: int
    valor: float
    tipo: str
    data: datetime

class NotaCreate(NotaBase):
    pass

class NotaResponse(NotaBase):
    id: int

    class Config:
        orm_mode = True
