#!/usr/bin/python3
"""doc"""

import requests
import json
import sys


def main(id):

    res1 = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    response1 = json.loads(res1.text)
    nameusr = response1.get('name')
    res = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}/todos')
    response = json.loads(res.text)
    done = 0
    ndone = 0

    for res in response:
        if res.get('completed'):
            done += 1
        else:
            ndone += 1

    print(f"Employee {nameusr} is done with tasks({done}/{ndone + done}):")
    for res in response:
        if res.get('completed'):
            print(f"\t {res.get('title')}")


if __name__ == "__main__":
    id = sys.argv[1]
    main(id)
