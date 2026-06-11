import pytest
from models.user import User
from models.project import Project
from models.task import Task

# tasts for user
def test_user_id_increments():
    u1 = User("Kevin", "kevin@example.com")
    u2 = User("Alice", "alice@example.com")
    assert u2.id == u1.id + 1

def test_valid_email():
    u = User("Bob", "bob@example.com")
    assert u.email == "bob@example.com"

def test_invalid_email():
    with pytest.raises(ValueError):
        User("Charlie", "bademail")


#tests for project
def test_project_creation():
    p = Project("Website Redesign", "Update UI", "2026-07-01", 1)
    assert p.title == "Website Redesign"
    assert p.user_id == 1
    assert str(p.due_date) == "2026-07-01"

def test_invalid_due_date():
    with pytest.raises(ValueError):
        Project("Bad Project", "Desc", "07-01-2026", 1)

#test for task
def test_task_status_validation():
    t = Task("Design Homepage", "pending")
    assert t.status == "pending"

def test_invalid_status():
    with pytest.raises(ValueError):
        Task("Bug Fix", "in-progress")

def test_mark_complete():
    t = Task("Write Docs", "pending")
    t.mark_complete()
    assert t.status == "completed"

def test_assign_user():
    t = Task("Setup DB", "pending")
    t.assign_user("Kevin")
    assert t.assigned_to == "Kevin"
