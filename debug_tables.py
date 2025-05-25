from sqlalchemy import create_engine, inspect

engine = create_engine("mysql+mysqlconnector://root:admin123@localhost:3306/gestao_alunos")

inspector = inspect(engine)
tables = inspector.get_table_names()
print("Tabelas detectadas via SQLAlchemy:", tables)
