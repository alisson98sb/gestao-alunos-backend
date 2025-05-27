from pydantic import BaseModel

class AlunoBase(BaseModel):
    nome: str
    email: str
    matricula: str
    turma: str

class AlunoCreate(AlunoBase):
    pass

class AlunoUpdate(BaseModel):
    nome: str | None = None
    email: str | None = None
    matricula: str | None = None
    turma: str | None = None

class AlunoResponse(AlunoBase):
    id: int

    class Config:
        orm_mode = True
