from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.trabalho import Trabalho
from app.schemas.trabalho_schema import TrabalhoCreate, TrabalhoUpdate

def listar_trabalhos(db: Session):
    return db.query(Trabalho).all()

def buscar_trabalho_por_id(db: Session, trabalho_id: int):
    trabalho = db.query(Trabalho).filter(Trabalho.id == trabalho_id).first()
    if not trabalho:
        raise HTTPException(status_code=404, detail="Trabalho não encontrado")
    return trabalho

def criar_trabalho(db: Session, dados: TrabalhoCreate):
    novo = Trabalho(**dados.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def atualizar_trabalho(db: Session, trabalho_id: int, dados: TrabalhoUpdate):
    trabalho = buscar_trabalho_por_id(db, trabalho_id)
    for campo, valor in dados.dict(exclude_unset=True).items():
        setattr(trabalho, campo, valor)
    db.commit()
    db.refresh(trabalho)
    return trabalho

def deletar_trabalho(db: Session, trabalho_id: int):
    trabalho = buscar_trabalho_por_id(db, trabalho_id)
    db.delete(trabalho)
    db.commit()
