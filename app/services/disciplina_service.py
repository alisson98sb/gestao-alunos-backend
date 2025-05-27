from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.disciplina import Disciplina
from app.schemas.disciplina_schema import DisciplinaCreate, DisciplinaUpdate

def listar_disciplinas(db: Session):
    return db.query(Disciplina).all()

def buscar_disciplina_por_id(db: Session, disciplina_id: int):
    disciplina = db.query(Disciplina).filter(Disciplina.id == disciplina_id).first()
    if not disciplina:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    return disciplina

def criar_disciplina(db: Session, dados: DisciplinaCreate):
    nova = Disciplina(**dados.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

def atualizar_disciplina(db: Session, disciplina_id: int, dados: DisciplinaUpdate):
    disciplina = buscar_disciplina_por_id(db, disciplina_id)
    for campo, valor in dados.dict(exclude_unset=True).items():
        setattr(disciplina, campo, valor)
    db.commit()
    db.refresh(disciplina)
    return disciplina

def deletar_disciplina(db: Session, disciplina_id: int):
    disciplina = buscar_disciplina_por_id(db, disciplina_id)
    db.delete(disciplina)
    db.commit()
