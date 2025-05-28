# 📚 Projeto Backend - Gestão Acadêmica

Este é um projeto de backend para gestão de alunos, notas, disciplinas, provas e trabalhos. Desenvolvido com **FastAPI**, **MySQL**, **SQLAlchemy** e **Alembic**, com autenticação via **Firebase** e versionamento via Git.

---

## 🚀 Como rodar o projeto localmente

### 1. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 2. Configure o ambiente:
Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```env
DATABASE_URL=mysql+mysqlconnector://root:admin123@localhost:3306/gestao_alunos
```

### 3. Execute a aplicação:
```bash
uvicorn app.main:app --reload
```

### 4. Teste a API via Swagger:
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔐 Autenticação Firebase

A API usa autenticação JWT com tokens do Firebase. Para obter um token:

1. Crie uma conta no Firebase.
2. Ative a autenticação por e-mail/senha.
3. Gere um token com:
```http
POST https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=YOUR_API_KEY
```
Body:
```json
{
  "email": "seu@email.com",
  "password": "suasenha",
  "returnSecureToken": true
}
```
4. Copie o `idToken` e use no Postman:
- Aba Authorization
- Tipo: Bearer Token
- Cole o token no campo

> 💡 O Firebase é inicializado uma única vez. No `app/core/firebase.py`:
```python
if not firebase_admin._apps:
    firebase_app = firebase_admin.initialize_app(cred)
else:
    firebase_app = firebase_admin.get_app()
```

---

## 🔧 Alembic - Migrações

### Criar novas migrations:
```bash
alembic revision --autogenerate -m "sua mensagem aqui"
```

### Aplicar as migrations:
```bash
alembic upgrade head
```

### Verificar histórico de migrations:
```bash
alembic history
```

### Fazer downgrade:
```bash
alembic downgrade <revision_id>
```

---

## 🧠 Entidades e Camadas

### ✅ Camadas de serviço implementadas para:
- Aluno
- Disciplina
- Nota
- Trabalho
- Prova

Cada entidade possui:
- Modelo (`app/models/`)
- Esquema Pydantic (`app/schemas/`)
- Rota (`app/routes/`)
- Serviço (`app/services/`)

---

## 📁 Estrutura de Diretórios

```
app/
├── core/               # Configuração do banco de dados e Firebase
├── models/             # Modelos SQLAlchemy
├── schemas/            # Schemas Pydantic (Create, Update, Response)
├── services/           # Camada de serviço
├── routes/             # Rotas FastAPI
└── main.py             # Entry point
```

---

## 🗃️ Versionamento
Este projeto está versionado com Git e hospedado no GitHub em repositórios separados para backend e frontend.

---

## 🔄 Progresso do Projeto

✅ Models e Migrations
✅ Testes manuais no Postman
✅ Serviços organizados
✅ Firebase configurado
✅ CRUDs protegidos
✅ Rota de criação de usuario no firebase
⬜ Testes automatizados
⬜ Documentação Swagger
⬜ Frontend ReactJS
⬜ Docker
