# 📚 Projeto Backend - Gestão Acadêmica

Este é um projeto de backend para gestão de alunos, notas, disciplinas, provas e trabalhos. Desenvolvido com **FastAPI**, **MySQL**, **SQLAlchemy** e **Alembic**, com autenticação planejada e versionamento via Git.

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
├── core/               # Configuração do banco de dados
├── models/             # Modelos SQLAlchemy
├── schemas/            # Schemas Pydantic (Create, Update, Response)
├── services/           # Camada de serviço
├── routes/             # Rotas FastAPI
└── main.py             # Entry point
```

---

## 🗃️ Versionamento
Este projeto está versionado com Git e hospedado no GitHub em repositórios separados para backend e frontend.
