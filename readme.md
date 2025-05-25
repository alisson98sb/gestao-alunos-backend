## Rodar o projeto

```bash
uvicorn app.main:app --reload
```

Senha de acesso: `Hn28H67.!E-6EAp`

---

## 🔄 A partir de agora, sempre que precisar...

### ➕ Adicionar/alterar colunas:

1. Modifique os modelos Python.
2. Gere e aplique uma nova migration:

```bash
alembic revision --autogenerate -m "add campo x"
alembic upgrade head
```

### 🔎 Ver histórico de migrations:

```bash
alembic history
```

### ⬅️ Voltar para uma versão anterior:

```bash
alembic downgrade <revision_id>
```
