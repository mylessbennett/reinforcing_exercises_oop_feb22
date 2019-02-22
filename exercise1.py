class Task:
    """ Creates a task and due date """

    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date

    def __str__(self):
        return "{}: {}".format(self.description, self.due_date)


# task1 = Task('Get groceries', 'Feb. 25')
# task2 = Task('Do laundry', 'Feb. 24')
# task3 = Task('Finish assignment', 'Feb. 22')
#
# print(task1)
# print(task2)
# print(task3)
