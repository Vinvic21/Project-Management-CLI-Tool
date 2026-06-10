from utils.validation import validate_status
class Task:
    ID_counter = 1
    def __init__(self, title, status= "pending", assigned_to= None, project_id= None):
        self.id = self.ID_counter
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
        self.project_id = project_id
        Task.ID_counter += 1
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        self._status = validate_status(value)
    def mark_complete(self):
        self.status = "completed"
    def assign_user(self,user_name):
        self.assigned_to =user_name
    def __str__(self):
        return f"Task {self.title} [{self.status}] (Assigned to: {self.assigned_to})"
    @classmethod
    def reset_counter(cls):
        cls.ID_counter = 1