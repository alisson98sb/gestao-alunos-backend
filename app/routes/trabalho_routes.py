from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.trabalho_schema import TrabalhoCreate, TrabalhoUpdate, TrabalhoResponse
from app.services import trabalho_service
from app.core.database import SessionLocal

router = APIRouter(prefix="/trabalhos", tags=["Trabalhos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[TrabalhoResponse])
def listar(db: Session = Depends(get_db)):
    return trabalho_service.listar_trabalhos(db)

@router.get("/{trabalho_id}", response_model=TrabalhoResponse)
def buscar(trabalho_id: int, db: Session = Depends(get_db)):
    return trabalho_service.buscar_trabalho_por_id(db, trabalho_id)

@router.post("/", response_model=TrabalhoResponse)
def criar(dados: TrabalhoCreate, db: Session = Depends(get_db)):
    return trabalho_service.criar_trabalho(db, dados)

@router.put("/{trabalho_id}", response_model=TrabalhoResponse)
def atualizar(trabalho_id: int, dados: TrabalhoUpdate, db: Session = Depends(get_db)):
    return trabalho_service.atualizar_trabalho(db, trabalho_id, dados)

@router.delete("/{trabalho_id}")
def deletar(trabalho_id: int, db: Session = Depends(get_db)):
    trabalho_service.deletar_trabalho(db, trabalho_id)
    return {"message": "Trabalho deletado com sucesso"}
