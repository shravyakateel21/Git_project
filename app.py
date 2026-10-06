from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect("study.db")
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/tasks", methods=["GET"])
def get_tasks():

    conn = get_db()

    tasks = conn.execute(
        "SELECT * FROM tasks ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return jsonify([dict(task) for task in tasks])


@app.route("/api/tasks", methods=["POST"])
def add_task():

    data = request.get_json()

    task = data.get("task", "").strip()

    if task == "":
        return jsonify({"error": "Task cannot be empty"}), 400

    conn = get_db()

    cursor = conn.execute(
        "INSERT INTO tasks (task) VALUES (?)",
        (task,)
    )

    conn.commit()

    task_id = cursor.lastrowid

    conn.close()

    return jsonify({
        "id": task_id,
        "task": task,
        "completed": 0
    })


@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):

    data = request.get_json()

    completed = data.get("completed", 0)

    conn = get_db()

    conn.execute(
        "UPDATE tasks SET completed = ? WHERE id = ?",
        (completed, task_id)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Task updated"})


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    conn = get_db()

    conn.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Task deleted"})


if __name__ == "__main__":
    create_table()
    app.run(debug=True)