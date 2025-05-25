from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import SessionLocal
from app.models.nota import Nota
from app.schemas.nota_schema import NotaCreate, NotaResponse

router = APIRouter(prefix="/notas", tags=["Notas"])

# Dependência de sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=NotaResponse)
def criar_nota(nota: NotaCreate, db: Session = Depends(get_db)):
    nova_nota = Nota(**nota.dict())
    db.add(nova_nota)
    db.commit()
    db.refresh(nova_nota)
    return nova_nota

@router.get("/", response_model=List[NotaResponse])
def listar_notas(db: Session = Depends(get_db)):
    return db.query(Nota).all()

@router.get("/{id}", response_model=NotaResponse)
def buscar_nota(id: int, db: Session = Depends(get_db)):
    nota = db.query(Nota).filter(Nota.id == id).first()
    if not nota:
        raise HTTPException(status_code=404, detail="Nota não encontrada")
    return nota

@router.put("/{id}", response_model=NotaResponse)
def atualizar_nota(id: int, dados: NotaCreate, db: Session = Depends(get_db)):
    nota = db.query(Nota).filter(Nota.id == id).first()
    if not nota:
        raise HTTPException(status_code=404, detail="Nota não encontrada")
    for chave, valor in dados.dict().items():
        setattr(nota, chave, valor)
    db.commit()
    db.refresh(nota)
    return nota

@router.delete("/{id}")
def deletar_nota(id: int, db: Session = Depends(get_db)):
    nota = db.query(Nota).filter(Nota.id == id).first()
    if not nota:
        raise HTTPException(status_code=404, detail="Nota não encontrada")
    db.delete(nota)
    db.commit()
    return {"message": "Nota deletada com sucesso"}
