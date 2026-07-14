# TechFlow — Gerenciador de Tarefas Ágil

Sistema web básico de gerenciamento de tarefas desenvolvido pela **TechFlow Solutions** para uma startup de logística. O projeto simula o ciclo completo de Engenharia de Software ágil no GitHub: planejamento (Kanban), desenvolvimento, testes automatizados e integração contínua.

## Objetivo

Permitir que a equipe acompanhe o fluxo de trabalho, registre tarefas e atualize status em tempo real — base para priorização e monitoramento no contexto de operações logísticas.

## Escopo inicial

- CRUD de tarefas (criar, listar, editar, excluir)
- Status: `a fazer` | `em progresso` | `concluído`
- Interface web simples
- Testes automatizados com Pytest
- Pipeline CI com GitHub Actions

> **Nota:** a feature de **prioridade** (baixa/média/alta) será introduzida como **mudança de escopo** ao longo do projeto, documentada nesta seção quando implementada.

## Metodologia

Híbrido **Scrum + Kanban**:

- Quadro Kanban no GitHub Projects (colunas A Fazer / Em Progresso / Concluído)
- Trabalho organizado em issues; cada entrega via branch + Pull Request
- Commits semânticos e frequentes
- Integração contínua para validar qualidade a cada mudança

## Estrutura do repositório

```text
/
├── README.md
├── requirements.txt
├── pytest.ini
├── .gitignore
├── src/
│   ├── app.py              # Rotas Flask + interface
│   ├── models.py           # Modelo Task
│   ├── storage.py          # Persistência JSON
│   ├── templates/          # HTML da interface
│   └── data/               # tasks.json (gerado em runtime)
├── tests/                  # Testes Pytest
├── docs/                   # Material de apoio
└── .github/workflows/ci.yml
```

## Como executar

Requisitos: Python 3.12+ e `pip`.

```bash
# 1. Clone o repositório
git clone https://github.com/DevDaniloOliveira/TrabalhoTechFlow.git
cd TrabalhoTechFlow

# 2. Crie e ative o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate          # Windows (PowerShell): .venv\Scripts\Activate.ps1

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Suba a aplicação
PYTHONPATH=. python src/app.py
# alternativa: PYTHONPATH=. flask --app src.app run --debug
```

Abra no navegador: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### Rodar os testes

```bash
source .venv/bin/activate
pytest -q
```

### API JSON (opcional)

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/tasks` | Lista tarefas |
| POST | `/tasks` | Cria tarefa (`{"title","description","status"}`) |
| GET | `/tasks/<id>` | Busca por id |
| PUT | `/tasks/<id>` | Atualiza tarefa |
| DELETE | `/tasks/<id>` | Remove tarefa |
| GET | `/health` | Health check |

## Mudança de escopo

*(Preenchida quando a feature de prioridade for implementada.)*

## Licença

Projeto acadêmico — Engenharia de Software.
