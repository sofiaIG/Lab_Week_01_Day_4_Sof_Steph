from modules.input import input_function
from modules.task_list import *
from modules.output import *
from data.task_list_py import *

display_of_created_tasks = input_function("Do you want load the tasks that have been already created? Y/N ")
empty_list = []

while display_of_created_tasks.lower != "y" and display_of_created_tasks.lower != "n":
    display_of_created_tasks = input_function("Invalid input. Only select between Y/N ")


if display_of_created_tasks.lower == "y":
    print(tasks)
else:
    print(empty_list)



while (True):
    print_menu()
    option = input_function("Select an option 1, 2, 3, 4, 5, display (m)enu or (q)uit: ")
    option = input("Select an option 1, 2, 3, 4, 5, display (m)enu or (q)uit: ")
    if (option.lower() == 'q'):
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif option == '4':
        description = input_function("Enter task description to search for: ")
        task = get_task_with_description(tasks, description)
        if task is not None:
            mark_task_complete(task)
            print("Task marked complete")
        else:
            print("Task not found")
    elif option == '5':
        time = int(input_function("Enter task duration: "))
        print_list(get_tasks_taking_at_least(tasks, time))
    elif option == '6':
        description = input_function("Enter task description to search for: ")
        print(get_task_with_description(tasks, description))
    elif option == '7':
        description = input_function("Enter description: ")
        time_taken = int(input_function("Enter time taken: "))
        task = create_task(description, time_taken)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")
