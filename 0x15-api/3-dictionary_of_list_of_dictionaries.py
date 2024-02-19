#!/usr/bin/python3
"""fetch employees data from api"""
import json
import requests

if __name__ == "__main__":
    all_tasks = []
    num = 0
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()

    data = {}
    filename = 'todo_all_employees.json'
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    with open(filename, "w", encoding='utf-8') as file:
        pass
    for user in users:
        all_tasks = []
        json_tasks = []
        userid = user.get("id")
        for task in tasks:
            if task.get("userId") == userid:
                all_tasks.append(task)
        for task in all_tasks:
            username = user.get("username")
            status = task.get("completed")
            title = task.get("title")
            json_tasks.append(
                {"username": username, "task": title, "completed": status})
        data[f"{userid}"] = json_tasks

        with open(filename, "a", newline='') as f:
            json.dump(data, f)
