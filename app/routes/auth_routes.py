from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from app.services.auth_service import criar_usuario_e_autenticar


router = APIRouter(prefix="/auth", tags=["Autenticação"])

class UsuarioCreate(BaseModel):
    email: EmailStr
    senha: str

@router.post("/registro")
def registrar_usuario(dados: UsuarioCreate):
    return criar_usuario_e_autenticar(dados.email, dados.senha)
