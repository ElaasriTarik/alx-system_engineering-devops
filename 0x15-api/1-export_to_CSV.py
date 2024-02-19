#!/usr/bin/python3
"""fetch employees data from api"""
import csv
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
    filename = str(userid) + ".csv"
    with open(filename, "w") as file:
        pass
    for task in all_tasks:
        with open(filename, "a", newline='') as f:
            writer = csv.writer(f)
            user = response.get("username")
            status = task.get("completed")
            title = task.get("title")
            writer.writerow([str(userid), str(user), str(status), str(title)])
