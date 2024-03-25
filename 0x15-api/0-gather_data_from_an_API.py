#!/usr/bin/python3
"""
This module uses an API to return information about an employee's
todo list progress.
"""

if __name__ == '__main__':

    import requests
    import sys

    employee_id = int(sys.argv[1])

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')

    employee_name = users.json()[employee_id - 1]['name']

    done_tasks_count = 0
    total_tasks_count = 0

    done_tasks = [todo['title'] for todo in todos.json()
                  if todo['userId'] == employee_id and todo['completed']]

    for todo in todos.json():
        if todo['userId'] == employee_id:
            total_tasks_count += 1
            if todo['completed']:
                done_tasks_count += 1

    print(f'Employee {employee_name} is done with tasks'
          f'({done_tasks_count}/{total_tasks_count}):')

    for task in done_tasks:
        print(f'\t {task}')
