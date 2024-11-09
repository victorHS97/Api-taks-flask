import requests
import pytest

baseURL = 'http://127.0.0.1:5000'
tasks = []


def test_create_task():
    new_task = {
        "title": "Estudar Laravel",
        "description": "testando o create"
    }
    response = requests.post(f'{baseURL}/tasks', json=new_task)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])


def test_get_tasks():
    response = requests.get(f'{baseURL}/tasks')
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json


def test_get_task():
    if tasks:
        task_id = tasks[0]
    response = requests.get(f'{baseURL}/tasks/{task_id}')
    response_json = response.json()
    assert task_id == response_json['id']


def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "completed": True,
            "description": "Estudado",
            "title": "Estudar Laravel"
        }
    response = requests.put(f'{baseURL}/tasks/{task_id}', json=payload)
    response.status_code = 200
    response_json = response.json()
    assert "message" in response_json

    # nova requisição para validar o PUT
    response = requests.get(f'{baseURL}/tasks/{task_id}')
    response_json = response.json()
    assert response_json['title'] == payload['title']
    assert response_json['description'] == payload['description']
    assert response_json['completed'] == payload['completed']


def test_delete_task():
    if tasks:
        task_id = tasks[0]
    response = requests.delete(f'{baseURL}/tasks/{task_id}')
    response.status_code == 200

    # verificando a exclusão
    response = requests.get(f'{baseURL}/tasks/{task_id}')
    response.status_code == 400
