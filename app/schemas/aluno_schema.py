from pydantic import BaseModel

class AlunoBase(BaseModel):
    nome: str
    email: str
    matricula: str
    turma: str

class AlunoCreate(AlunoBase):
    pass

class AlunoResponse(AlunoBase):
    id: int

    class Config:
        orm_mode = True
