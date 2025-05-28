from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.prova_schema import ProvaCreate, ProvaUpdate, ProvaResponse
from app.services import prova_service
from app.core.database import SessionLocal
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/provas", tags=["Provas"],dependencies=[Depends(get_current_user)])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[ProvaResponse])
def listar(db: Session = Depends(get_db)):
    return prova_service.listar_provas(db)

@router.get("/{prova_id}", response_model=ProvaResponse)
def buscar(prova_id: int, db: Session = Depends(get_db)):
    return prova_service.buscar_prova_por_id(db, prova_id)

@router.post("/", response_model=ProvaResponse)
def criar(dados: ProvaCreate, db: Session = Depends(get_db)):
    return prova_service.criar_prova(db, dados)

@router.put("/{prova_id}", response_model=ProvaResponse)
def atualizar(prova_id: int, dados: ProvaUpdate, db: Session = Depends(get_db)):
    return prova_service.atualizar_prova(db, prova_id, dados)

@router.delete("/{prova_id}")
def deletar(prova_id: int, db: Session = Depends(get_db)):
    prova_service.deletar_prova(db, prova_id)
    return {"message": "Prova deletada com sucesso"}
