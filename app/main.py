from fastapi import FastAPI

from app.routes.aluno_routes import router as aluno_router
from app.routes.disciplina_routes import router as disciplina_router
from app.routes.nota_routes import router as nota_router
from app.routes.trabalho_routes import router as trabalho_router
from app.routes.prova_routes import router as prova_router
from app.routes.auth_routes import router as auth_router

app = FastAPI(title="Gestão Acadêmica")

# Registro das rotas
app.include_router(aluno_router)
app.include_router(disciplina_router)
app.include_router(nota_router)
app.include_router(trabalho_router)
app.include_router(prova_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "API de Gestão de Alunos funcionando!"}
