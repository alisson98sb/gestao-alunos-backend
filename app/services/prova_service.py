from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.prova import Prova
from app.schemas.prova_schema import ProvaCreate, ProvaUpdate

def listar_provas(db: Session):
    return db.query(Prova).all()

def buscar_prova_por_id(db: Session, prova_id: int):
    prova = db.query(Prova).filter(Prova.id == prova_id).first()
    if not prova:
        raise HTTPException(status_code=404, detail="Prova não encontrada")
    return prova

def criar_prova(db: Session, dados: ProvaCreate):
    nova = Prova(**dados.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

def atualizar_prova(db: Session, prova_id: int, dados: ProvaUpdate):
    prova = buscar_prova_por_id(db, prova_id)
    for campo, valor in dados.dict(exclude_unset=True).items():
        setattr(prova, campo, valor)
    db.commit()
    db.refresh(prova)
    return prova

def deletar_prova(db: Session, prova_id: int):
    prova = buscar_prova_por_id(db, prova_id)
    db.delete(prova)
    db.commit()
