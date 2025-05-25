from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from app.core.database import Base

class Nota(Base):
    __tablename__ = "notas"

    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"), nullable=False)
    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"), nullable=False)
    valor = Column(Float, nullable=False)
    tipo = Column(String(50), nullable=False)
    data = Column(DateTime, nullable=False)
