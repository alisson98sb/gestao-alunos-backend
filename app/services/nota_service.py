from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.nota import Nota
from app.schemas.nota_schema import NotaCreate, NotaUpdate

def listar_notas(db: Session):
    return db.query(Nota).all()

def buscar_nota_por_id(db: Session, nota_id: int):
    nota = db.query(Nota).filter(Nota.id == nota_id).first()
    if not nota:
        raise HTTPException(status_code=404, detail="Nota não encontrada")
    return nota

def criar_nota(db: Session, dados: NotaCreate):
    nova = Nota(**dados.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

def atualizar_nota(db: Session, nota_id: int, dados: NotaUpdate):
    nota = buscar_nota_por_id(db, nota_id)
    for campo, valor in dados.dict(exclude_unset=True).items():
        setattr(nota, campo, valor)
    db.commit()
    db.refresh(nota)
    return nota

def deletar_nota(db: Session, nota_id: int):
    nota = buscar_nota_por_id(db, nota_id)
    db.delete(nota)
    db.commit()
