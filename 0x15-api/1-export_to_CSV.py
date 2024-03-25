#!/usr/bin/python3
"""
This module uses an API to export information about an employee's
todo list in csv format.
"""

if __name__ == '__main__':

    import csv
    import requests
    import sys

    employee_id = int(sys.argv[1])

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')

    employee_username = users.json()[employee_id - 1]['username']

    with open(f'{employee_id}.csv', 'w') as file:
        for todo in todos.json():
            if todo['userId'] == employee_id:
                task_status = todo['completed']
                task = todo['title']
                file.write(f'"{employee_id}","{employee_username}",'
                           f'"{task_status}","{task}"\n')
