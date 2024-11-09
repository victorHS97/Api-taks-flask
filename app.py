from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)
tasks = []
task_control_id = 1


@app.route('/tasks', methods=['POST'])
def create_task():
    global task_control_id
    data = request.get_json()
    new_task = Task(id=task_control_id,
                    title=data['title'], description=data.get("description", ""))
    tasks.append(new_task)
    task_control_id += 1
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso", "id": new_task.id})


@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = []
    for task in tasks:
        task_list.append(task.to_dict())
    task_qtd = len(tasks)
    output = {
        "tasks": task_list,
        "total_tasks": task_qtd
    }
    return jsonify(output)


@app.route('/tasks/<int:Id>', methods=['GET'])
def get_task(Id):
    for task in tasks:
        if task.id == Id:
            return jsonify(task.to_dict())
    return jsonify({"message": "Atividade não cadastrada"}), 404


@app.route('/tasks/<int:Id>', methods=['PUT'])
def update_task(Id):
    task = None
    for t in tasks:
        if t.id == Id:
            task = t
    if task == None:
        return jsonify({"message": "Tarefa não encontrada"}), 404
    data = request.get_json()
    task.title = data["title"]
    task.description = data["description"]
    task.completed = data["completed"]

    return jsonify({"message": "Tarefa Atualizada com Sucesso"})


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    if not task:
        return jsonify({"message": "Tarefa não encontrada"}), 404
    tasks.remove(task)
    return jsonify({"message": "Tarefa Removida com Sucesso"})


if __name__ == '__main__':
    app.run(debug=True)
