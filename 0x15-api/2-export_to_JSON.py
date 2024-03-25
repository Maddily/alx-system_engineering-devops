#!/usr/bin/python3
"""
This module uses an API to export information about an employee's
todo list in json format.
"""

if __name__ == '__main__':

    import json
    import requests
    import sys

    employee_id = int(sys.argv[1])

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')

    employee_username = users.json()[employee_id - 1]['username']

    data = {employee_id: []}

    for todo in todos.json():
        if todo['userId'] == employee_id:
            task_status = todo['completed']
            task_title = todo['title']
            task = {
                    'task': task_title,
                    'completed': task_status,
                    'username': employee_username
                    }
            data[employee_id].append(task)

    with open(f'{employee_id}.json', 'w') as file:
        json.dump(data, file)
