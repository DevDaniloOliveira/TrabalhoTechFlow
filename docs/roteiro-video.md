# Roteiro do Vídeo Pitch (até 4 minutos)

**Projeto:** TechFlow — Gerenciador de Tarefas Ágil  
**Repositório:** https://github.com/DevDaniloOliveira/TrabalhoTechFlow  

## Antes de gravar

1. Confirme que `main` está atualizada (board Kanban + prioridade + CI).
2. Suba a app: `PYTHONPATH=. python src/app.py`
3. Abra abas prontas:
   - App (`http://127.0.0.1:5000`)
   - GitHub Projects (Kanban)
   - Actions (último run verde)
   - README (seção Mudança de escopo)
4. Tenha 2–3 tarefas de exemplo no board para demonstrar drag-and-drop.

---

## Roteiro com timestamps

### 0:00 – 0:30 | Apresentação do projeto
> “Olá, sou [Nome]. Este é o TechFlow, um gerenciador de tarefas desenvolvido pela TechFlow Solutions para uma startup de logística, no contexto da disciplina de Engenharia de Software. O repositório é público no GitHub e segue um fluxo ágil com issues, pull requests e integração contínua.”

**Mostrar:** página do repositório / README.

### 0:30 – 1:00 | Metodologia ágil e Kanban
> “Usamos um híbrido Scrum + Kanban. Cada funcionalidade virou uma issue entregue por branch `feature/TF-XX` e Pull Request. No GitHub Projects, o quadro organiza mais de dez cards no fluxo do projeto.”

**Mostrar:** GitHub Projects com os cards.

### 1:00 – 2:10 | Demonstração do sistema
> “Aqui está o sistema rodando. O board da aplicação segue o padrão de ferramentas de gestão: colunas A fazer, Em progresso e Concluído. Vou criar uma tarefa pelo modal, abrir os detalhes, alterar a prioridade e arrastar o card para outra coluna para mudar o status.”

**Mostrar:**  
1. Nova tarefa (modal)  
2. Abrir card (detalhes / salvar)  
3. Arrastar entre colunas  

### 2:10 – 2:40 | Testes automatizados
> “Os testes usam Pytest e cobrem o CRUD, validações, prioridade e a renderização do board. Vou executar a suíte.”

**Mostrar:** terminal com `pytest -q` (todos passando).

### 2:40 – 3:15 | GitHub Actions
> “A cada pull request, o GitHub Actions roda flake8 e Pytest. Este é um workflow verde, evidência de integração contínua e controle de qualidade.”

**Mostrar:** aba Actions com run bem-sucedido.

### 3:15 – 3:40 | Mudança de escopo
> “No meio do projeto o cliente pediu priorização de tarefas críticas. Criamos o card no Kanban, implementamos o campo prioridade, adicionamos testes e documentamos a justificativa no README — sem descartar o que já estava pronto.”

**Mostrar:** seção “Mudança de escopo” no README + card correspondente no Project.

### 3:40 – 4:00 | Reflexão final
> “Esse exercício mostra a importância da Engenharia de Software no mercado: organização do trabalho, rastreabilidade, qualidade automatizada e capacidade de adaptar o escopo com segurança. Obrigado.”

---

## Checklist pós-gravação

- [ ] Vídeo com até 4 minutos
- [ ] Publicado com **link público** (YouTube ou Drive)
- [ ] Link colado na seção 9 de `parte-teorica.md` (e no PDF final)
- [ ] Opcional: link no README do repositório
