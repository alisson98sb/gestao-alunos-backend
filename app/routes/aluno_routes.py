from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import SessionLocal
from app.models.aluno import Aluno
from app.schemas.aluno_schema import AlunoCreate, AlunoResponse

router = APIRouter(prefix="/alunos", tags=["Alunos"])

# Dependência de sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AlunoResponse)
def criar_aluno(aluno: AlunoCreate, db: Session = Depends(get_db)):
    novo_aluno = Aluno(**aluno.dict())
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)
    return novo_aluno

@router.get("/", response_model=List[AlunoResponse])
def listar_alunos(db: Session = Depends(get_db)):
    return db.query(Aluno).all()

@router.get("/{id}", response_model=AlunoResponse)
def buscar_aluno(id: int, db: Session = Depends(get_db)):
    aluno = db.query(Aluno).filter(Aluno.id == id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

@router.put("/{id}", response_model=AlunoResponse)
def atualizar_aluno(id: int, dados: AlunoCreate, db: Session = Depends(get_db)):
    aluno = db.query(Aluno).filter(Aluno.id == id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    for chave, valor in dados.dict().items():
        setattr(aluno, chave, valor)
    db.commit()
    db.refresh(aluno)
    return aluno

@router.delete("/{id}")
def deletar_aluno(id: int, db: Session = Depends(get_db)):
    aluno = db.query(Aluno).filter(Aluno.id == id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    db.delete(aluno)
    db.commit()
    return {"message": "Aluno deletado com sucesso"}
