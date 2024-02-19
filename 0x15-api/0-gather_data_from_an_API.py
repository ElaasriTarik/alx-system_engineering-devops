#!/usr/bin/python3
import requests
import json
import sys

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
print(f'Employee {username} is done with tasks({num}/{len(all_tasks)}):')
for task in all_tasks:
    if task.get("completed") is True:
        title = task.get("title")
        print(f"\t{title}")
