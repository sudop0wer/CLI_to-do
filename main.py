from datetime import datetime
import logging


logger = logging.getLogger("to-do")
logger.setLevel(logging.INFO)

log_path = "/home/ctuglea/python/CLI_to-do/log/"
handler = logging.FileHandler(f"{log_path}to-do_{datetime.today().strftime('%d-%m-%Y')}.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s: %(asctime)s: %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

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
    def add_task(name, user_name):
        if Tasks.check_task(name) == 0:
            task = Tasks(name, False)
            Tasks.total_tasks.append(task)
            Tasks.i += 1
            print(f"Added task [{name}].")
            logger.info(f"User {user_name} added task [{name}.]")
        else:
            print(f"Task [{name}] already exsists!")
            logger.warning(f"User {user_name} failed to add task [{name}]. Already existent!")

    @staticmethod
    def view_tasks(user_name):
        print(f"Number of tasks: {Tasks.i} ")        
        for x in Tasks.total_tasks:
            print(str(x))
        logger.info(f"User {user_name} viewed all tasks.")
    
    @staticmethod
    def complete_task(name, user_name):

        if Tasks.check_task(name):
            for x in Tasks.total_tasks:
                if name == x.name:
                    if x.status:
                        print(f"Task [{name}] already completed!")
                        logger.warning(f"User {user_name} failed to complete task [{name}]. Already completed!")
                    else:
                        x.status = True
                        print(f"Good job! Task [{name}] completed!")
                        logger.info(f"User {user_name} completed task [{name}].")
        else:
            print(f"Task [{name}] doesn't exist!")
            logger.warning(f"User {user_name} failed to complete task [{name}]. Task nonexistent!")
        
    @staticmethod
    def delete_task(name, user_name):

        if Tasks.check_task(name):
            for x in Tasks.total_tasks:
                if name == x.name:
                    Tasks.total_tasks.remove(x)
                    print(f"Successfully removed task [{name}]")
                    logger.info(f"User {user_name} removed task [{name}].")
                    Tasks.i -= 1
        else:
            print(f"Task [{name}] doesn't exist!")
            logger.info(f"User {user_name} failed to remove task [{name}]. Task nonexistent!")

    @staticmethod
    def save_to_file(file_name, user_name):

        with open(f"{file_name}.txt", "w") as f:
            f.write(f"Tasks for {datetime.today().strftime('%d-%m-%Y')} \n")
            for x in Tasks.total_tasks:
                f.write(f"{str(x)} \n")
        logger.info(f"User {user_name} exported all tasks to {file_name}.txt")


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
user_name = input("Please enter your username>> ")
logger.info(f"User {user_name} started the application.")

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
        Tasks.view_tasks(user_name)

    elif user_in == 'a':
        name = input("Specify a name for your task>> ")
        Tasks.add_task(name, user_name)

    elif user_in == 'c':
        name = input("Specify the task to be marked as complete>> ")
        Tasks.complete_task(name, user_name)

    elif user_in == 'd':
        name = input("Specify the task to be deleted>> ")
        Tasks.delete_task(name, user_name)

    elif user_in == 's':
        file_name = input("Enter a name for the file where your tasks will be exported>> ")
        Tasks.save_to_file(file_name, user_name)
        print("Export successful!")

    elif user_in == 'x':
        print("Great job completing your tasks today!")
        choice = input("""Do you want to export all the tasks before leaving? 
Please type y (YES) or any other character for NO 
>> """)
        if choice == 'y':
            Tasks.save_to_file("Tasks", user_name)
            print("Tasks exported successfully to file Tasks.txt!")
            print("Stay productive!")
        else:
            print("Ok, then. Stay productive!")


    else:
        print("Wrong choice! Pleasye type one of the valid keywords!")
        logging.warning(f"User {user_name} typed a wrong keyword!")



