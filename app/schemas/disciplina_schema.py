from pydantic import BaseModel

class DisciplinaBase(BaseModel):
    nome: str
    codigo: str
    professor: str

class DisciplinaCreate(DisciplinaBase):
    pass

class DisciplinaUpdate(BaseModel):
    nome: str | None = None
    codigo: str | None = None
    professor: str | None = None

class DisciplinaResponse(DisciplinaBase):
    id: int

    class Config:
        orm_mode = True
