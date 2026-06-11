from utils.validation import validate_email
class User:
    Id_counter = 1
    def __init__(self, name, email):
        self.id = User.Id_counter
        self.name = name
        self.email = email
        User.Id_counter += 1 
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        self._email = validate_email(value)
    def __str__(self):
        return f"User:{self.id} {self.name} {self.email}"