import requests
import pytest

baseURL = 'http://127.0.0.1:5000'
tasks = []


def test_create_task():
    new_task = {
        "title": "Tarefa Teste",
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
