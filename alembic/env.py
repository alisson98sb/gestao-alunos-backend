# from app.core.database import Base
# from app.models.aluno import Aluno
# from app.models.disciplina import Disciplina
# from app.models.nota import Nota
# from app.models.trabalho import Trabalho
# from app.models.prova import Prova

# target_metadata = Base.metadata

# _ = [Aluno, Disciplina, Nota, Trabalho, Prova]  # força a execução dos modelos

# print("Tabelas visíveis pelo Alembic:", list(Base.metadata.tables.keys()))

import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Permite importar o projeto (ajusta o path para src/app)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa Base e os modelos
from app.core.database import Base
from app.models import aluno, disciplina, nota, trabalho, prova

# Config do Alembic
config = context.config
fileConfig(config.config_file_name)

# Força avaliação dos modelos
target_metadata = Base.metadata

# Debug: imprime tabelas visíveis
print("✅ Tabelas no metadata:", list(Base.metadata.tables.keys()))

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True  # importante p/ detectar mudanças de tipo
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
