from datetime import datetime

class Tasks:


    total_tasks = []
    i = 0

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __repr__(self):
        return f'Task [{self.name}] has status {'completed' if self.status else 'pending'}'

#Check if a task exists, if it exists it returns 1
    @staticmethod
    def check_task(name):
        a = 0
        for x in Tasks.total_tasks:
            if name == x.name:
                a = 1
        return a

    @staticmethod
    def add_task(name):
        if Tasks.check_task(name) == 0:
            task = Tasks(name, False)
            Tasks.total_tasks.append(task)
            Tasks.i += 1
        else:
            print(f"Task [{name}] already exsists!")

    @staticmethod
    def view_tasks():
        print(f"Number of tasks: {Tasks.i} ")        
        for x in Tasks.total_tasks:
            print(str(x))
    
    @staticmethod
    def complete_task(name):

        if Tasks.check_task(name):
            for x in Tasks.total_tasks:
                if name == x.name:
                    if x.status:
                        print(f"Task [{name}] already completed!")
                    else:
                        x.status = True
                        print(f"Good job! Task [{name}] completed!")
        else:
            print(f"Task [{name}] doesn't exist!")
        
    @staticmethod
    def delete_task(name):

        if Tasks.check_task(name):
            for x in Tasks.total_tasks:
                if name == x.name:
                    Tasks.total_tasks.remove(x)
                    print(f"Successfully removed task [{name}]")
                    Tasks.i -= 1
        else:
            print(f"Task [{name}] doesn't exist!")

    @staticmethod
    def save_to_file(file_name):

        with open(f"{file_name}.txt", "w") as f:
            f.write(f"Task for {datetime.today().strftime('%d-%m-%Y')} \n")
            for x in Tasks.total_tasks:
                f.write(f"{str(x)} \n")


user_in = 'm'


print("""

╔═══╦╗──╔══╗─╔╗────────╔╗
║╔═╗║║──╚╣╠╝╔╝╚╗───────║║
║║─╚╣║───║║─╚╗╔╬══╗──╔═╝╠══╗
║║─╔╣║─╔╗║║──║║║╔╗╠══╣╔╗║╔╗║
║╚═╝║╚═╝╠╣╠╗─║╚╣╚╝╠══╣╚╝║╚╝║
╚═══╩═══╩══╝─╚═╩══╝──╚══╩══╝
""")

print("Hi! Welcome to your CLI to-do application!")

while user_in != 'x':

    user_in = input("""
Please type the keyword for one of the following actions:
        v = view current tasks
        a = add a new task
        c = mark a task as completed
        d = delete a task
        s = save tasks to a file
        x = exit application
Action>> """)
    
    if user_in == 'v':
        Tasks.view_tasks()

    elif user_in == 'a':
        name = input("Specify a name for your task>> ")
        Tasks.add_task(name)

    elif user_in == 'c':
        name = input("Specify the task to be marked as complete>> ")
        Tasks.complete_task(name)

    elif user_in == 'd':
        name = input("Specify the task to be deleted>> ")
        Tasks.delete_task(name)

    elif user_in == 's':
        file_name = input("Enter a name for the file where your tasks will be exported>> ")
        Tasks.save_to_file(file_name)
        print("Export successful!")

    elif user_in == 'x':
        print("Great job completing your tasks today!")
        choice = input("""Do you want to export all the tasks before leaving? 
Please type y (YES) or any other character for NO 
>> """)
        if choice == 'y':
            Tasks.save_to_file("Tasks")
            print("Tasks exported successfully to file Tasks.txt!")
            print("Stay productive!")
        else:
            print("Ok, then. Stay productive!")


    else:
        print("Wrong choice! Pleasye type one of the valid keywords!")


'''

Tasks.add_task("do dishes")
Tasks.add_task("do laundry")
Tasks.add_task("read homework")
Tasks.complete_task("hello")
Tasks.complete_task("do laundry")
Tasks.complete_task("do laundry")
Tasks.delete_task("do laundry")
Tasks.view_tasks()
#Tasks.check_task("do dishes")
        
'''
