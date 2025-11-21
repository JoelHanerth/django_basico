# Django Básico — Projeto de Exemplo

Projeto Django simples criado para demonstrar conceitos básicos: modelos, views, templates e rotas para um app chamado `produtos`.

**Visão Geral**
- **Nome:** django_basico
- **App principal:** `produtos` (CRUD básico com templates em `produtos/templates`)
- **Banco de dados:** `sqlite3` (arquivo `db.sqlite3` na raiz)

**Estrutura importante**
- `manage.py` — script de gerenciamento Django.
- `core/` — configurações do projeto (`settings.py`, `urls.py`, etc.).
- `produtos/` — app com `models.py`, `views.py`, `urls.py` e templates.
- `templates/` — templates globais do projeto.
- `static/` — CSS, JS e imagens (ex.: `static/produtos/css/estilo_global.css`).

Requisitos
- Python 3.8+ (recomendado 3.10/3.11)
- Django (a versão usada no projeto deve estar no ambiente — instale conforme necessário)

Instalação e execução (Windows PowerShell)

1. Criar e ativar ambiente virtual
```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

2. Instalar dependências (se houver `requirements.txt`)
```powershell
pip install -r requirements.txt
```

3. Aplicar migrações
```powershell
python manage.py migrate
```

4. (Opcional) Criar superuser
```powershell
python manage.py createsuperuser
```

5. Rodar o servidor de desenvolvimento
```powershell
python manage.py runserver
```

6. Acessar a aplicação
- Abra `http://127.0.0.1:8000/` no navegador. Rotas do app `produtos` estão configuradas em `produtos/urls.py`.

Observações sobre o app `produtos`
- Templates relevantes: `inserir_produto.html`, `listar_produtos.html`, `ver_produto.html`, `confirmar_exclusao.html` (localizados em `produtos/templates`).
- Se alterar arquivos estáticos em produção, execute `python manage.py collectstatic` e configure o servidor para servi-los.
