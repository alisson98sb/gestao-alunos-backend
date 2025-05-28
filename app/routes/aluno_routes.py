from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.aluno_schema import AlunoCreate, AlunoUpdate, AlunoResponse
from app.services import aluno_service
from app.core.database import SessionLocal
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/alunos", tags=["Alunos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[AlunoResponse])
def listar_alunos(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return aluno_service.listar_alunos(db)

@router.get("/{aluno_id}", response_model=AlunoResponse)
def buscar_aluno(aluno_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return aluno_service.buscar_aluno_por_id(db, aluno_id)

@router.post("/", response_model=AlunoResponse)
def criar_aluno(dados: AlunoCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return aluno_service.criar_aluno(db, dados)

@router.put("/{aluno_id}", response_model=AlunoResponse)
def atualizar_aluno(aluno_id: int, dados: AlunoUpdate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return aluno_service.atualizar_aluno(db, aluno_id, dados)

@router.delete("/{aluno_id}")
def deletar_aluno(aluno_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    aluno_service.deletar_aluno(db, aluno_id)
    return {"message": "Aluno deletado com sucesso"}
