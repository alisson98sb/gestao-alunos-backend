from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.disciplina_schema import DisciplinaCreate, DisciplinaUpdate, DisciplinaResponse
from app.services import disciplina_service
from app.core.database import SessionLocal

router = APIRouter(prefix="/disciplinas", tags=["Disciplinas"])

# Função para injetar o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[DisciplinaResponse])
def listar_disciplinas(db: Session = Depends(get_db)):
    return disciplina_service.listar_disciplinas(db)

@router.get("/{disciplina_id}", response_model=DisciplinaResponse)
def buscar_disciplina(disciplina_id: int, db: Session = Depends(get_db)):
    return disciplina_service.buscar_disciplina_por_id(db, disciplina_id)

@router.post("/", response_model=DisciplinaResponse)
def criar_disciplina(dados: DisciplinaCreate, db: Session = Depends(get_db)):
    return disciplina_service.criar_disciplina(db, dados)

@router.put("/{disciplina_id}", response_model=DisciplinaResponse)
def atualizar_disciplina(disciplina_id: int, dados: DisciplinaUpdate, db: Session = Depends(get_db)):
    return disciplina_service.atualizar_disciplina(db, disciplina_id, dados)

@router.delete("/{disciplina_id}")
def deletar_disciplina(disciplina_id: int, db: Session = Depends(get_db)):
    disciplina_service.deletar_disciplina(db, disciplina_id)
    return {"message": "Disciplina deletada com sucesso"}
