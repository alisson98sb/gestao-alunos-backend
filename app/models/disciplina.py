from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Disciplina(Base):
    __tablename__ = "disciplinas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    codigo = Column(String(20), nullable=False, unique=True)
    professor = Column(String(100), nullable=False)
