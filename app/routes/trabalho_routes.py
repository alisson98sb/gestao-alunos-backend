from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import SessionLocal
from app.models.trabalho import Trabalho
from app.schemas.trabalho_schema import TrabalhoCreate, TrabalhoResponse

router = APIRouter(prefix="/trabalhos", tags=["Trabalhos"])

# Dependência de sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TrabalhoResponse)
def criar_trabalho(trabalho: TrabalhoCreate, db: Session = Depends(get_db)):
    novo_trabalho = Trabalho(**trabalho.dict())
    db.add(novo_trabalho)
    db.commit()
    db.refresh(novo_trabalho)
    return novo_trabalho

@router.get("/", response_model=List[TrabalhoResponse])
def listar_trabalhos(db: Session = Depends(get_db)):
    return db.query(Trabalho).all()

@router.get("/{id}", response_model=TrabalhoResponse)
def buscar_trabalho(id: int, db: Session = Depends(get_db)):
    trabalho = db.query(Trabalho).filter(Trabalho.id == id).first()
    if not trabalho:
        raise HTTPException(status_code=404, detail="Trabalho não encontrado")
    return trabalho

@router.put("/{id}", response_model=TrabalhoResponse)
def atualizar_trabalho(id: int, dados: TrabalhoCreate, db: Session = Depends(get_db)):
    trabalho = db.query(Trabalho).filter(Trabalho.id == id).first()
    if not trabalho:
        raise HTTPException(status_code=404, detail="Trabalho não encontrado")
    for chave, valor in dados.dict().items():
        setattr(trabalho, chave, valor)
    db.commit()
    db.refresh(trabalho)
    return trabalho

@router.delete("/{id}")
def deletar_trabalho(id: int, db: Session = Depends(get_db)):
    trabalho = db.query(Trabalho).filter(Trabalho.id == id).first()
    if not trabalho:
        raise HTTPException(status_code=404, detail="Trabalho não encontrado")
    db.delete(trabalho)
    db.commit()
    return {"message": "Trabalho deletado com sucesso"}
