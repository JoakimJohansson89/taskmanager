import csv

class Task:
    """A class that specifys the details of a task."""
    def __init__(self, name, descr, due, priority, status, category):
        self.name = name
        self.descr = descr
        self.due = due
        self.priority = priority
        self.status = status
        self.category = category
    
        


class TaskManager:
    """A class that handles tasks."""
    def __init__(self):
        
        self.tasks = []
        self.housework = []
        self.occupation = []
        self.personal_life = []
        self.load_tasks_from_csv() # Call the method to load tasks from CSV file

    def load_tasks_from_csv(self):
        # Method to read tasks from CSV file and populate the task list
        filename = "Tasks.csv"
        try:
            with open(filename, "r") as csvfile:
                csv_reader = csv.reader(csvfile)

                try:
                    # Skip the header row    
                    next(csv_reader)
                except StopIteration:
                    # Handle the case where there is no header row (file exists)
                    print("-------------------")
                    print(f"The file {filename} is empty. Starting with an empty tasks list") 

                for row in csv_reader:
                    name, descr, due, priority, status, category = row
                    task = Task(name.strip(), descr.strip(), due.strip(), priority.strip(), status.strip(), category.strip())
                    self.tasks.append(task)

                    # Sort the tasks into categories
                    if category.lower() == " housework":
                        self.housework.append(task)
                    elif category.lower() == " occupation":
                        self.occupation.append(task)
                    elif category.lower() == " personal life":
                        self.personal_life.append(task)
                    else:
                        print(f"Category not recognised: {category.lower()}")
        
        except FileNotFoundError:
            # Handle the case where the file doesn't exist
            print(f"The file {filename} does not exist. Starting with an empty task list.")
    
    def add_task(self):

        #Add a task to the task manager
        name = input("What name would you like for the task?: ")
        descr = input("Give a short description of the task: ")
        due = input("Due date: ")
        priority = None

        # Check if the prioroty is already used by another task
        while priority is None or any(prio.priority == priority for prio in self.tasks):
            if priority is not None:
                print("Error: Priority already in use. Please choose a different number.")
                print("")
            priority = input("Task priority Number: ")


        status = input("What's the status of the task?: ")
        category = input("What's the category of the task? Housework, Occupation or Personal life?: ")

        task = Task(name, descr, due, priority, status, category)

        self.tasks.append(task)
        
        check = False
        while not check:     
            # Sort the tasks into categories
            if category.lower() == "housework":
                self.housework.append(task)
                check = True
            elif category.lower() == "occupation":
                self.occupation.append(task)
                check = True
            elif category.lower() == "personal life":
                self.personal_life.append(task)
                check = True
            else: 
                category = input(f"Category not recognised: {category}, try again: ")
                

    def list_task(self):
        # Lists all tasks
        categories = {
            "All Tasks: ":self.tasks,
            "Housework Tasks: ": self.housework,
            "Occupation Tasks: ": self.occupation,
            "Personal life Tasks: ": self.personal_life
        }

        for category, task_list in categories.items():
            print(category)
            for task in task_list:
                print(task.name)
    
    def list_descr(self):
        # List descriptions of the tasks.
        for task in self.tasks:
            print(f"{task.name}'s descriptions is: {task.descr}")
    
    def list_prio(self):
        # List the priority of the tasks.
        for task in self.tasks:
            print(f"{task.name}'s priority is: {task.priority}")

    def list_due(self):
        # List the due date of the tasks.
        for task in self.tasks:
            print(f"{task.name}'s due date is: {task.due}")

    def list_status(self):
        # List the status of the tasks.
        for task in self.tasks:
            print(f"{task.name}'s status is: {task.status}")
        
    def handeling_tasks(self):
        # Method that notes a task is completed and deletes it
        while True:
            print("Loop for handeling tasks, press \"Q\" to quit")
            task_name = input("Give the name of the task you've completed: ")
            for task in self.tasks:
                if task.name == task_name:
                    print(f"{task.name} succesfully completed")
                    self.tasks.remove(task)
            if task_name == "q":
                break
    
    def list_details_of_task(self):
        # Method that lists all the attributes of a task
        task_name = input("What task would you like to see the details of: ")
        for task in self.tasks:
            if task_name == task.name:
                print(f"---{task.name}---")
                print()
                print(f"Description: {task.descr}")
                print(f"Priority: {task.priority}")
                print(f"Due date: {task.due}")
                print(f"Status: {task.status}")
                print(f"Category: {task.category}")
    
    def modify_task(self):
        # Modify the description of a task
        # Change this to modify all the different attributes of a task.
        task_name = input("What task would you like to modify?: ")
        for task in self.tasks:
            if task.name == task_name:
                print("What would you like to modify?: ")
                print("1. Name")
                print("2. Description")
                print("3. Priority ranking")
                print("4. Due date")
                print("5. Status")
                print("6. Change category")
                choice = input("Select from 1 - 6: ")
                if choice == "1":
                    task.name = input("New name: ")
                elif choice == "2":
                    task.descr = input("New description: ")
                elif choice == "3":
                    task.priority = input("New priority ranking: ")
                elif choice == "4":
                    task.due = input("New due date: ")
                elif choice == "5":
                    task.status == input("New Status: ")
                elif choice == "6":
                    task.category == input("New category, Housework, Occupation or Personal life?: ")

    def completed_task(self):
        # Marking tasks as completed and also gives the option to remove it.
        task_name = input("What task would you like to mark as completed?: ")
        for task in self.tasks:
            if task.name == task_name:
                choice = input("Would you like to mark it as complete or just remove it? 1 for marking, 2 for removal: ")
                if choice == "1":
                    task.name = (task.name + " completed")
                    print(task.name)
                    task.status = "Completed"
                elif choice == "2":
                    self.tasks.remove(task)
                else:
                    print("Wrong input.")

    def save_task(self):
        # Saves the information of any task, or all tasks, to a text file.
        print("You are given to option to save a task to a csv.file, or if you'd like, save all tasks.")
        print("Either give the name of the task you'd like to save or just press \"a\" to save all tasks")
        choice = input("What task would you like to save to a file?(or just type \"a\" for all): ")

        filename = "Tasks.csv"
        
        with open(filename, 'w', newline ="") as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            # Write column headers if the file is empty
            if csvfile.tell() == 0:
                csvwriter.writerow(["Name", " Description", " Due Date", " Priority", " Status", " Category"])

            if choice.lower() == "a":
                # Save all tasks
                    for task in self.tasks:
                        csvwriter.writerow([f"{task.name}", f" {task.descr}", f" {task.due}", f" {task.priority}", f" {task.status}", f" {task.category}"])
            else:
                # Save a specfik task
                for task in self.tasks:
                    for task in self.tasks:
                        csvwriter.writerow([f"{task.name}", f" {task.descr}",f" {task.due}",f" {task.priority}", f" {task.status}", f" {task.category}"])
        print("")
        print(f"Tasks saved to {filename}")
                    
        


    

class Menu:
    """Menu for using the tasktracker."""
    def __init__(self, taskmanager):
        self.taskmanager = taskmanager

    def display_menu(self):

        print()
        print("---TASK TRACKER MENU---")
        print()
        print("1. Add a task.")
        print("2. List your tasks by name.")
        print("3. List the discriptions of your tasks.")
        print("4. List the priority of your tasks.")
        print("5. List the due date of your tasks.")
        print("6. List the status of your tasks. ")
        print("7. List all details of a single task.")
        print("8. Modify a task.")
        print("9. Mark a task as complete and/or remove it. ")
        print("10. Save the information to a txt.file. ")
        print("Q to quit")
        print()
    
    def run_menu(self):
        #Loop for handeling the menu.
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            print()

            if choice == "1":
                self.taskmanager.add_task()
            elif choice == "2":
                self.taskmanager.list_task()
            elif choice == "3":
                self.taskmanager.list_descr()
            elif choice == "4":
                self.taskmanager.list_prio()
            elif choice == "5":
                self.taskmanager.list_due()
            elif choice == "6":
                self.taskmanager.list_status()
            elif choice == "7":
                self.taskmanager.list_details_of_task()
            elif choice == "8":
                self.taskmanager.modify_task()
            elif choice == "9":
                self.taskmanager.completed_task()
            elif choice == "10": 
                self.taskmanager.save_task()
            elif choice.lower() == "q":
                print("Good-Bye!")
                break
       

if __name__ == "__main__":
    taskmanager = TaskManager()
    menu = Menu(taskmanager)
    menu.run_menu()


