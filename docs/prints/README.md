# Pasta de prints (capturas de tela)

Salve aqui as imagens que serão inseridas no PDF teórico (`parte-teorica.md`).

## Nomes sugeridos

| Arquivo | Conteúdo | Obrigatório? |
|---------|----------|--------------|
| `01-kanban-github.png` | GitHub Projects com ≥ 10 cards | Sim |
| `02-commits.png` | Histórico de commits ou lista de PRs | Sim |
| `03-github-actions.png` | Workflow CI verde (flake8 + Pytest) | Sim |
| `04-uml-casos-de-uso.png` | Diagrama de casos de uso (se não usar só Mermaid) | Recomendado |
| `05-uml-classes.png` | Diagrama de classes | Recomendado |
| `06-app-board.png` | App rodando (`localhost:5000`) | Opcional |

## Dicas de captura

- Resolução legível (texto dos cards e commits visível)
- Evite dados sensíveis na tela
- No PDF, mantenha o **comentário** de cada print (já escrito em `parte-teorica.md`)

Após salvar as imagens com esses nomes, as referências `![...](prints/...)` no Markdown passam a exibir as prints automaticamente na exportação.
