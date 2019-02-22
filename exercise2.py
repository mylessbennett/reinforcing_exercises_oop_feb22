from exercise1 import Task


class TodoList:
    """ Creates a list of tasks """

    tasks = {}

    def __init__(self):
        pass

    @classmethod
    def add_task(cls, description, due_date):
        current_task = Task(description, due_date)
        cls.tasks[description] = due_date
        return current_task


TodoList.add_task('Finish assignment', 'Feb. 22')
TodoList.add_task('Get groceries', 'Feb. 24')
TodoList.add_task('Do laundry', 'Feb. 25')
print(TodoList.tasks)
