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
res = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}/todos')
response = json.loads(res.text)

data = []
for todo in response:
    values = [id, nameusr, todo.get("completed"), todo.get("title")]
    data.append(values)

filename = f'{id}.csv'
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerows(data)
