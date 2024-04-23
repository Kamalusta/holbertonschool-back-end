#!/usr/bin/python3
"""doc"""

import requests
import json
import sys
import csv


id = sys.argv[1]
res1 = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
response1 = json.loads(res1.text)
nameusr = response1.get('name')
username = response1.get('username')
res = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}/todos')
response = json.loads(res.text)

data = []

for todo in response:
    dic = {}
    dic['task'] = todo.get('title')
    dic['completed'] = todo.get('completed')
    dic['username'] = username
    data.append(dic)

user = {}
user[f'{id}'] = data

filename = f'{id}.json'
with open(filename, 'w') as file:
    json.dump(user, file)
