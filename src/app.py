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

    @app.get("/tasks")
    def list_tasks():
        """Lista todas as tarefas cadastradas."""
        tasks = [task.to_dict() for task in storage.list_all()]
        return jsonify(tasks), 200

    @app.get("/tasks/<task_id>")
    def get_task(task_id: str):
        """Retorna uma tarefa pelo id."""
        task = storage.get(task_id)
        if task is None:
            return jsonify({"erro": "Tarefa não encontrada."}), 404
        return jsonify(task.to_dict()), 200

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

    @app.put("/tasks/<task_id>")
    @app.post("/tasks/<task_id>/update")
    def update_task(task_id: str):
        """Atualiza título, descrição e/ou status de uma tarefa."""
        if storage.get(task_id) is None:
            return jsonify({"erro": "Tarefa não encontrada."}), 404

        payload = request.get_json(silent=True) or {}
        title = payload.get("title") if "title" in payload else request.form.get("title")
        description = (
            payload.get("description")
            if "description" in payload
            else request.form.get("description")
        )
        status_raw = (
            payload.get("status") if "status" in payload else request.form.get("status")
        )

        status = None
        if status_raw is not None:
            try:
                status = TaskStatus(status_raw)
            except ValueError:
                return jsonify({"erro": f"Status inválido: {status_raw}"}), 400

        try:
            updated = storage.update(
                task_id,
                title=title,
                description=description,
                status=status,
            )
        except ValueError as exc:
            return jsonify({"erro": str(exc)}), 400

        return jsonify(updated.to_dict()), 200

    @app.delete("/tasks/<task_id>")
    @app.post("/tasks/<task_id>/delete")
    def delete_task(task_id: str):
        """Remove uma tarefa pelo id."""
        deleted = storage.delete(task_id)
        if not deleted:
            return jsonify({"erro": "Tarefa não encontrada."}), 404
        return jsonify({"mensagem": "Tarefa removida com sucesso."}), 200

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
