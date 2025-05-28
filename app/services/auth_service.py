import requests
from firebase_admin import auth
from fastapi import HTTPException
import os

FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")  # guarde no .env

def criar_usuario_e_autenticar(email: str, senha: str):
    try:
        # Cria o usuário no Firebase
        user = auth.create_user(email=email, password=senha)
        
        # Faz login para obter o idToken
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
        payload = {
            "email": email,
            "password": senha,
            "returnSecureToken": True
        }
        response = requests.post(url, json=payload)
        
        if response.status_code != 200:
            raise Exception("Erro ao autenticar usuário")
        
        token_data = response.json()
        return {
            "uid": user.uid,
            "email": user.email,
            "idToken": token_data["idToken"],
            "refreshToken": token_data["refreshToken"],
            "expiresIn": token_data["expiresIn"]
        }

    except auth.EmailAlreadyExistsError:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {str(e)}")
