"""Testes automatizados do CRUD de tarefas."""

from __future__ import annotations

from pathlib import Path

import pytest

from src.app import create_app
from src import app as app_module
from src.models import Task
from src.storage import TaskStorage


@pytest.fixture()
def storage(tmp_path: Path) -> TaskStorage:
    return TaskStorage(tmp_path / "tasks.json")


@pytest.fixture()
def client(storage: TaskStorage):
    app_module.storage = storage
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_criar_tarefa_valida(client):
    resposta = client.post(
        "/tasks",
        json={"title": "Separar carga", "description": "Docas 3"},
    )
    assert resposta.status_code == 201
    dados = resposta.get_json()
    assert dados["title"] == "Separar carga"
    assert dados["status"] == "todo"
    assert "id" in dados


def test_rejeitar_titulo_vazio(client):
    resposta = client.post("/tasks", json={"title": "   "})
    assert resposta.status_code == 400
    assert "erro" in resposta.get_json()


def test_atualizar_status(client):
    criada = client.post("/tasks", json={"title": "Coleta"}).get_json()
    resposta = client.put(
        f"/tasks/{criada['id']}",
        json={"status": "in_progress"},
    )
    assert resposta.status_code == 200
    assert resposta.get_json()["status"] == "in_progress"


def test_excluir_tarefa(client):
    criada = client.post("/tasks", json={"title": "Remover"}).get_json()
    resposta = client.delete(f"/tasks/{criada['id']}")
    assert resposta.status_code == 200
    assert client.get(f"/tasks/{criada['id']}").status_code == 404


def test_listar_tarefas(client):
    client.post("/tasks", json={"title": "A"})
    client.post("/tasks", json={"title": "B"})
    resposta = client.get("/tasks")
    assert resposta.status_code == 200
    assert len(resposta.get_json()) == 2


def test_board_kanban_renderiza_colunas(client):
    client.post("/tasks", json={"title": "No board", "status": "todo"})
    pagina = client.get("/")
    assert pagina.status_code == 200
    html = pagina.data.decode("utf-8")
    assert "A fazer" in html
    assert "Em progresso" in html
    assert "Concluído" in html
    assert "Nova tarefa" in html
    assert "No board" in html
    assert 'id="modal-criar"' in html


def test_modelo_rejeita_titulo_vazio():
    with pytest.raises(ValueError):
        Task(title="")
