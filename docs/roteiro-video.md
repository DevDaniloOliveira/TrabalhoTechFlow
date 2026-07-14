# Roteiro do Vídeo Pitch (até 4 minutos)

**Objetivo:** apresentar o TechFlow cobrindo metodologia, demo, testes, CI e mudança de escopo.

## Antes de gravar

1. Mergear o PR da prioridade (TF-11), se ainda aberto.
2. Mover todos os cards do Kanban para refletir o estado final (maioria em Concluído).
3. Subir a app: `PYTHONPATH=. python src/app.py`
4. Abrir abas: interface (`localhost:5000`), Projects, Actions, README.

---

## Roteiro com timestamps

### 0:00 – 0:30 | Apresentação
> “Olá, sou [Nome]. Este é o TechFlow, um gerenciador de tarefas criado para uma startup de logística, no contexto da disciplina de Engenharia de Software. O repositório público está no GitHub e segue um fluxo ágil com issues, pull requests e CI.”

Mostrar: README / página inicial do repo.

### 0:30 – 1:00 | Metodologia e Kanban
> “Usamos um híbrido Scrum + Kanban. Cada funcionalidade virou uma issue e foi entregue por uma branch `feature/TF-XX` com PR. No Projects, o quadro tem as colunas A Fazer, Em Progresso e Concluído, com mais de dez cards.”

Mostrar: GitHub Projects com cards.

### 1:00 – 2:00 | Demo do sistema
> “Aqui está o sistema rodando. Vou criar uma tarefa operacional, alterar o status e definir prioridade alta — recurso pedido pelo cliente para destacar entregas críticas. Em seguida edito e excluo para mostrar o CRUD completo.”

Mostrar: navegador em `http://127.0.0.1:5000` — criar (prioridade alta), editar, listar ordenado, excluir.

### 2:00 – 2:40 | Testes automatizados
> “Os testes usam Pytest. Cobrem criação, validação de título, atualização, exclusão e a feature de prioridade. Vou rodar a suíte rapidamente.”

Mostrar: terminal com `pytest -q` (11 passed).

### 2:40 – 3:20 | GitHub Actions
> “A cada pull request, o GitHub Actions roda flake8 e Pytest. Este é um workflow verde, evidência de integração contínua.”

Mostrar: aba Actions com run bem-sucedido.

### 3:20 – 3:45 | Mudança de escopo
> “No meio do projeto o cliente pediu priorização de tarefas críticas. Documentamos a justificativa no README, criamos o card no Kanban e implementamos o campo prioridade com testes novos — sem descartar o que já estava pronto.”

Mostrar: seção “Mudança de escopo” no README + issue #11.

### 3:45 – 4:00 | Reflexão final
> “Esse exercício mostra por que Engenharia de Software importa no mercado: organização do trabalho, rastreabilidade, qualidade automatizada e capacidade de adaptar o escopo com segurança. Obrigado.”

---

## Checklist pós-gravação

- [ ] Vídeo ≤ 4 minutos
- [ ] Link público (YouTube ou Drive)
- [ ] Link colado no PDF teórico e, se quiser, no README
