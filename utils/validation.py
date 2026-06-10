from datetime import datetime
import re 

def validate_due_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")

def validate_email(value):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Za-z]{2,}$"
    if not re.match(pattern, value):
        raise ValueError("Invalid Format")
    return value
def validate_name(name):
    if not name:
        raise ValueError( "Name cannot be empty")
    return name
def validate_status(status):
    valid_status = ("completed", "pending")
    if status not in valid_status:
        raise ValueError("Invalid Status")
    return status
