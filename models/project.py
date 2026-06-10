from utils.validation import validate_due_date
class Project:
    ID_counter = 1
    def __init__(self, title, description,due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        Project.ID_counter += 1
        self.tasks= []
    
    @property
    def due_date(self):
        return self._due_date
    @due_date.setter
    def due_date(self, value):
        self._due_date = validate_due_date(value)

    def add_task(self, task):
        self.tasks.append(task)

    def __str__(self):
        return f"Project {self.title} (Due: {self.due_date})"