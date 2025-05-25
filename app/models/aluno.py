# from sqlalchemy import Column, Integer, String
# from app.core.database import Base  # <- TEM que ser esse Base

# class Aluno(Base):
#     __tablename__ = "alunos"

#     id = Column(Integer, primary_key=True, index=True)
#     nome = Column(String(100), nullable=False)
#     email = Column(String(100), nullable=False, unique=True)
#     matricula = Column(String(20), nullable=False, unique=True)
#     turma = Column(String(50))
from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    matricula = Column(String(20), nullable=False, unique=True)
    turma = Column(String(50), nullable=True)
