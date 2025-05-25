from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import SessionLocal
from app.models.prova import Prova
from app.schemas.prova_schema import ProvaCreate, ProvaResponse

router = APIRouter(prefix="/provas", tags=["Provas"])

# Dependência de sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProvaResponse)
def criar_prova(prova: ProvaCreate, db: Session = Depends(get_db)):
    nova_prova = Prova(**prova.dict())
    db.add(nova_prova)
    db.commit()
    db.refresh(nova_prova)
    return nova_prova

@router.get("/", response_model=List[ProvaResponse])
def listar_provas(db: Session = Depends(get_db)):
    return db.query(Prova).all()

@router.get("/{id}", response_model=ProvaResponse)
def buscar_prova(id: int, db: Session = Depends(get_db)):
    prova = db.query(Prova).filter(Prova.id == id).first()
    if not prova:
        raise HTTPException(status_code=404, detail="Prova não encontrada")
    return prova

@router.put("/{id}", response_model=ProvaResponse)
def atualizar_prova(id: int, dados: ProvaCreate, db: Session = Depends(get_db)):
    prova = db.query(Prova).filter(Prova.id == id).first()
    if not prova:
        raise HTTPException(status_code=404, detail="Prova não encontrada")
    for chave, valor in dados.dict().items():
        setattr(prova, chave, valor)
    db.commit()
    db.refresh(prova)
    return prova

@router.delete("/{id}")
def deletar_prova(id: int, db: Session = Depends(get_db)):
    prova = db.query(Prova).filter(Prova.id == id).first()
    if not prova:
        raise HTTPException(status_code=404, detail="Prova não encontrada")
    db.delete(prova)
    db.commit()
    return {"message": "Prova deletada com sucesso"}
