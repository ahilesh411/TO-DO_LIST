tasks = []
while True:
    print("\n--- TO-DO LIST ---")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Remove Task")
    print("4.Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        task=input("Enter a task: ")
        tasks.append(task)
        print("Task added!")
    elif choice=="2":
        if len(tasks)==0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])
    elif choice=="3":
        if len(tasks)==0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])
            num = int(input("Enter task number to remove: "))
            tasks.pop(num - 1)
            print("Task removed!")
    elif choice=="4":
        print("Thank you for using To-Do List!")
        break
    else:
        print("Invalid choice.")
