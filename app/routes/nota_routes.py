from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.nota_schema import NotaCreate, NotaUpdate, NotaResponse
from app.services import nota_service
from app.core.database import SessionLocal

router = APIRouter(prefix="/notas", tags=["Notas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[NotaResponse])
def listar(db: Session = Depends(get_db)):
    return nota_service.listar_notas(db)

@router.get("/{nota_id}", response_model=NotaResponse)
def buscar(nota_id: int, db: Session = Depends(get_db)):
    return nota_service.buscar_nota_por_id(db, nota_id)

@router.post("/", response_model=NotaResponse)
def criar(dados: NotaCreate, db: Session = Depends(get_db)):
    return nota_service.criar_nota(db, dados)

@router.put("/{nota_id}", response_model=NotaResponse)
def atualizar(nota_id: int, dados: NotaUpdate, db: Session = Depends(get_db)):
    return nota_service.atualizar_nota(db, nota_id, dados)

@router.delete("/{nota_id}")
def deletar(nota_id: int, db: Session = Depends(get_db)):
    nota_service.deletar_nota(db, nota_id)
    return {"message": "Nota deletada com sucesso"}
