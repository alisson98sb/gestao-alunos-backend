from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.core.database import Base

class Prova(Base):
    __tablename__ = "provas"

    id = Column(Integer, primary_key=True, index=True)
    conteudo = Column(String(255), nullable=False)
    data_prova = Column(DateTime, nullable=False)
    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"), nullable=False)
