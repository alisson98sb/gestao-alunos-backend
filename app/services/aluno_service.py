from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.aluno import Aluno
from app.schemas.aluno_schema import AlunoCreate, AlunoUpdate

def listar_alunos(db: Session):
    return db.query(Aluno).all()

def buscar_aluno_por_id(db: Session, aluno_id: int):
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

def criar_aluno(db: Session, dados: AlunoCreate):
    aluno = Aluno(**dados.dict())
    db.add(aluno)
    db.commit()
    db.refresh(aluno)
    return aluno

def atualizar_aluno(db: Session, aluno_id: int, dados: AlunoUpdate):
    aluno = buscar_aluno_por_id(db, aluno_id)
    for campo, valor in dados.dict(exclude_unset=True).items():
        setattr(aluno, campo, valor)
    db.commit()
    db.refresh(aluno)
    return aluno

def deletar_aluno(db: Session, aluno_id: int):
    aluno = buscar_aluno_por_id(db, aluno_id)
    db.delete(aluno)
    db.commit()
