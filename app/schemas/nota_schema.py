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

class NotaUpdate(BaseModel):
    aluno_id: int | None = None
    disciplina_id: int | None = None
    valor: float | None = None
    tipo: str | None = None
    data: datetime | None = None

class NotaResponse(NotaBase):
    id: int

    class Config:
        orm_mode = True
