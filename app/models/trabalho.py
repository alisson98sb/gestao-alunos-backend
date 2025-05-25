from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.core.database import Base

class Trabalho(Base):
    __tablename__ = "trabalhos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(String(255))
    data_entrega = Column(DateTime, nullable=False)
    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"), nullable=False)
