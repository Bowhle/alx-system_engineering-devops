#!/usr/bin/python3
"""This script returns list info about the employee given an ID """
import json
import requests
""" The request module used to fetch the url response"""


def get_employee_tasks():
    """This function to get all employees to do"""
    try:
        """This script fetches user info """
        url = "https://jsonplaceholder.typicode.com/"
        user_response = requests.get(url + "users")
        user_data = user_response.json()

        """This script holds the employee data in a dictionary"""
        all_employee_task = {}

        for user in user_data:
            employee_id = user['id']
            employee_name = user['username']

            """This script gets the employee todo list for current employee"""
            todo_response = requests.get(url + f"todos?userId={employee_id}")
            todo_list = todo_response.json()

            """This script prepares json data"""
            tasks = [
                    {"username": employee_name,
                     "task": task["title"],
                     "completed": task["completed"]
                     }
                    for task in todo_list
                    ]
            all_employee_task[str(employee_id)] = tasks

        """ exports to json """
        json_filename = "todo_all_employees.json"
        with open(json_filename, mode="w") as json_file:
            json.dump(all_employee_task, json_file, indent=4)

    except Exception as e:
        print(f"an error occured: {e}")


if __name__ == "__main__":
    get_employee_tasks()
