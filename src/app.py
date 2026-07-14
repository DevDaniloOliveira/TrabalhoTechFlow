"""Aplicação Flask do gerenciador de tarefas TechFlow."""

from __future__ import annotations

from flask import Flask, jsonify, request

from .models import TaskStatus
from .storage import TaskStorage

storage = TaskStorage()


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.post("/tasks")
    def create_task():
        """Cria uma nova tarefa (JSON ou formulário)."""
        payload = request.get_json(silent=True) or {}
        title = payload.get("title") or request.form.get("title", "")
        description = payload.get("description") or request.form.get("description", "")
        status_raw = payload.get("status") or request.form.get("status", TaskStatus.TODO.value)

        try:
            status = TaskStatus(status_raw)
        except ValueError:
            return jsonify({"erro": f"Status inválido: {status_raw}"}), 400

        try:
            task = storage.create(title=title, description=description, status=status)
        except ValueError as exc:
            return jsonify({"erro": str(exc)}), 400

        return jsonify(task.to_dict()), 201

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
