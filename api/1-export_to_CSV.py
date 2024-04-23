#!/usr/bin/python3
"""doc"""


import csv
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    res1 = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    response1 = json.loads(res1.text)
    nameusr = response1.get('name')
    res = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}/todos')
    response = json.loads(res.text)

    string = ""
    for todo in response:
        string += (
            f'"{id}",'
            f'"{nameusr}",'
            f'"{todo.get("completed")}",'
            f'"{todo.get("title")}"\n'
            )
    filename = f'{id}.csv'
    with open(filename, 'w', newline="") as file:
        file.write(string)
