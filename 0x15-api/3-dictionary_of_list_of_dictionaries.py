#!/usr/bin/python3
"""
This module uses an API to export information about an employee's
todo list in json format.
"""

if __name__ == '__main__':

    import json
    import requests

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')

    data = {}

    for todo in todos.json():
        task_status = todo['completed']
        task_title = todo['title']
        employee_id = todo['userId']
        employee_username = users.json()[employee_id - 1]['username']
        task = {
                'username': employee_username,
                'task': task_title,
                'completed': task_status
                }
        if employee_id in data:
            data[employee_id].append(task)
        else:
            data[employee_id] = [task]

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
