def taskMAnager():
    tasks = []
    print("----WELCOME TO THE TASK MANAGEMENT APP----")
    
    total_task = int(input("Enter how many task you want to add : "))
    
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} : ")
        tasks.append(task_name)

    print(f"Today's Tasks are : \n{tasks}")

    while True:
        operation = int(input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))
        if operation == 1:
            add = input("Enter task you want to add : ")
            tasks.append(add)
            print(f"Task {add} has been added successfully!")

        elif operation == 2:
            updatedVal = input("Enter the task name you want to update : ")
            if updatedVal in tasks:
                up = input("Enter new task : ")
                ind = tasks.index(updatedVal)
                tasks[ind] = up
                print(f"Updated task successfully!")

        elif operation == 3:
            deleteVal = input("Enter the task name you want to delete : ")
            if deleteVal in tasks:
                ind = tasks.index(deleteVal)
                del tasks[ind]
                print(f"Task {deleteVal} has been deleted successfully!")

        elif operation == 4:
            print(f"Total Tasks :{tasks}")

        elif operation == 5:
            print("Closing the Program......")
            break

        else:
            print("Invalid Input")

taskMAnager()