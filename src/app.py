from flask import Flask, jsonify, request
from src.tasks import add_task, get_tasks, remove_task

app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
def tasks_route():
    return jsonify(get_tasks())

@app.route('/tasks', methods=['POST'])
def add_task_route():
    task = request.json.get('task')
    add_task(task)
    return jsonify({'task': task}), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def remove_task_route(task_id):
    remove_task(task_id)
    return '', 204


if __name__ == "__main__":
    app.run()