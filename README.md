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
├── .gitignore
├── src/                 # Aplicação Flask
├── tests/               # Testes Pytest
├── docs/                # Diagramas e material de apoio
└── .github/workflows/   # CI (GitHub Actions)
```

## Como executar

> Instruções completas serão refinadas na issue de documentação de execução. Preview:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/app.py
```

Acesse `http://127.0.0.1:5000` após a implementação da interface.

## Mudança de escopo

*(Preenchida quando a feature de prioridade for implementada.)*

## Licença

Projeto acadêmico — Engenharia de Software.
