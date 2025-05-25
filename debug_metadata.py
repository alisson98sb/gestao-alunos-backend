from app.core.database import Base, engine
from app.models.aluno import Aluno
from app.models.disciplina import Disciplina
from app.models.nota import Nota
from app.models.trabalho import Trabalho
from app.models.prova import Prova

print("Tabelas no metadata:")
print(list(Base.metadata.tables.keys()))

Base.metadata.create_all(bind=engine)
print("Tabelas criadas manualmente.")
