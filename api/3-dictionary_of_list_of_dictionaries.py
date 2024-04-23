#!/usr/bin/python3
"""doc"""

import json
import requests


if __name__ == "__main__":
    users = requests.get(f'https://jsonplaceholder.typicode.com/users')
    userres = json.loads(users.text)
    userdic = {}
    for user in userres:
        id = user.get('id')
        todo = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{id}/todos')
        todores = json.loads(todo.text)
        todolist = []
        for todo in todores:
            dic = {'username': user.get('username'),
                   'task': todo.get('title'),
                   'completed': todo.get('completed')
                   }
            todolist.append(dic)
        userdic[id] = todolist

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as file:
        json.dump(userdic, file)
