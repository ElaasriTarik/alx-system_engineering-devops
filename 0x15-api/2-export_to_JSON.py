#!/usr/bin/python3
"""fetch employees data from api"""
import json
import requests
import sys


if __name__ == "__main__":
    all_tasks = []
    num = 0
    userid = int(sys.argv[1])
    response = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(userid)).json()

    username = response.get('name', 'username')
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    for task in tasks:
        if task.get("userId") == userid:
            all_tasks.append(task)
            if task.get("completed") is True:
                num += 1
    filename = str(userid) + ".json"
    with open(filename, "w", encoding='utf-8') as file:
        pass
    json_tasks = []
    data = {}
    for task in all_tasks:
        user = response.get("username")
        status = task.get("completed")
        title = task.get("title")
        json_tasks.append(
            {"task": title, "completed": status, "username": user})
    with open(filename, "a", newline='') as f:
        data = {f"{userid}": json_tasks}
        json.dump(data, f)
