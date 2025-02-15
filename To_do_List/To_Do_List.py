import os
import json

file_name = "tasks.json"

"""Function to view all tasks"""
def view_tasks():
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            for task in data['tasks']:
                status = "Complete" if task['completed'] else "Incomplete"
                print(f"{task['id']}. {task['title']}: {status}")

    except FileNotFoundError:
        print("File does not exixts!\n\n")
    except json.JSONDecodeError:
        print("Error reading json file! \n\n")

"""Function to create new task"""
def create_new_task():
    try:
        with open(file_name) as file:
            data = json.load(file)
            
        last_task_id = data['tasks'][-1]['id'] if data["tasks"] else 0
        task_title = input("Enter task title: ")

        new_task = {"id": last_task_id + 1, "title": task_title, "completed": False}
        data['tasks'].append(new_task)
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
        
    except (FileNotFoundError, json.JSONDecodeError):
        with open(file_name, "w") as file:
            json.dump({"tasks": []}, file, indent=4)
        create_new_task()
            
"""Function to mark task as complete/incomplete"""
def edit_task():
    try:
        view_tasks()
        with open(file_name) as file:
            data = json.load(file)
        id = int(input("Enter the id number of the task to be edited: "))
        
        while True:
            edit = input("Mark it as complete(c)/incomplete(i): ").strip().lower()
            if edit in ("c", "i"):
                break
        
        data['tasks'][id - 1]['completed'] = True if edit == 'c' else False
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print("File does not exists!")
    except json.JSONDecodeError:
        print("Error occured while decoding json file!")

def delete_task():
    try:
        view_tasks()
        id = int(input("Enter id number of the task to be deleted: "))
        with open(file_name) as file:
            data = json.load(file)
        for task in data['tasks']:
            if task['id'] == id:
                data['tasks'].remove(task)
        id = 1
        for task in data['tasks']:
            task['id'] = id
            id += 1 


        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
    
        print("\nTask removed sucessfully\n\n")
    except FileNotFoundError:
        print("\nFile does not exixts!\n\n")
    
    except json.JSONDecodeError:
        print("\nError occured while reading json file!\n\n")


if __name__ == "__main__":
    app_run = True
    while app_run:
        choice = int(input("**************TODO APPLICATION********************\n"
                           "Select the operation you want to perform\n"
                           "1. List all the tasks.\n"
                           "2. Create a new task (assigned as Incomplete by default).\n"
                           "3. Edit a task (as complete/incomplete).\n"
                           "4. Delete a task.\n"
                           "5. Exit\n"
                           "Your choice: ").strip())

        # List tasks
        if choice == 1:
            view_tasks()
        
        # Create new task
        elif choice == 2:
            create_new_task()
        
        # Edit task
        elif choice == 3:
             edit_task()

        # Delete task
        elif choice == 4:
            delete_task()

        # Exit application        
        elif choice == 5:
            app_run = False

           