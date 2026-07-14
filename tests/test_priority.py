"""Testes da feature de prioridade (mudança de escopo)."""

from __future__ import annotations

from pathlib import Path

import pytest

from src import app as app_module
from src.app import create_app
from src.models import TaskPriority
from src.storage import TaskStorage


@pytest.fixture()
def client(tmp_path: Path):
    app_module.storage = TaskStorage(tmp_path / "tasks.json")
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_criar_com_prioridade_alta(client):
    resposta = client.post(
        "/tasks",
        json={"title": "Atraso crítico", "priority": "alta"},
    )
    assert resposta.status_code == 201
    assert resposta.get_json()["priority"] == "alta"


def test_prioridade_invalida(client):
    resposta = client.post(
        "/tasks",
        json={"title": "X", "priority": "urgente"},
    )
    assert resposta.status_code == 400


def test_atualiza_prioridade(client):
    criada = client.post("/tasks", json={"title": "Rota"}).get_json()
    assert criada["priority"] == "media"
    resposta = client.put(
        f"/tasks/{criada['id']}",
        json={"priority": "baixa"},
    )
    assert resposta.status_code == 200
    assert resposta.get_json()["priority"] == "baixa"


def test_lista_ordena_por_prioridade(client):
    client.post("/tasks", json={"title": "Baixa", "priority": "baixa"})
    client.post("/tasks", json={"title": "Alta", "priority": "alta"})
    client.post("/tasks", json={"title": "Media", "priority": "media"})
    titulos = [t["title"] for t in client.get("/tasks").get_json()]
    assert titulos[0] == "Alta"
    assert titulos[-1] == "Baixa"


def test_rank_prioridade():
    assert TaskPriority.ALTA.rank > TaskPriority.MEDIA.rank > TaskPriority.BAIXA.rank
