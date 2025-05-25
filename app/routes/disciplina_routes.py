from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import SessionLocal
from app.models.disciplina import Disciplina
from app.schemas.disciplina_schema import DisciplinaCreate, DisciplinaResponse

router = APIRouter(prefix="/disciplinas", tags=["Disciplinas"])

# Dependência de sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DisciplinaResponse)
def criar_disciplina(disciplina: DisciplinaCreate, db: Session = Depends(get_db)):
    nova_disciplina = Disciplina(**disciplina.dict())
    db.add(nova_disciplina)
    db.commit()
    db.refresh(nova_disciplina)
    return nova_disciplina

@router.get("/", response_model=List[DisciplinaResponse])
def listar_disciplinas(db: Session = Depends(get_db)):
    return db.query(Disciplina).all()

@router.get("/{id}", response_model=DisciplinaResponse)
def buscar_disciplina(id: int, db: Session = Depends(get_db)):
    disciplina = db.query(Disciplina).filter(Disciplina.id == id).first()
    if not disciplina:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    return disciplina

@router.put("/{id}", response_model=DisciplinaResponse)
def atualizar_disciplina(id: int, dados: DisciplinaCreate, db: Session = Depends(get_db)):
    disciplina = db.query(Disciplina).filter(Disciplina.id == id).first()
    if not disciplina:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    for chave, valor in dados.dict().items():
        setattr(disciplina, chave, valor)
    db.commit()
    db.refresh(disciplina)
    return disciplina

@router.delete("/{id}")
def deletar_disciplina(id: int, db: Session = Depends(get_db)):
    disciplina = db.query(Disciplina).filter(Disciplina.id == id).first()
    if not disciplina:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    db.delete(disciplina)
    db.commit()
    return {"message": "Disciplina deletada com sucesso"}
