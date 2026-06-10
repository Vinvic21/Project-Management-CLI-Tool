import argparse
from models.project import Project
from models.task import Task
from models.user import User
from utils.IO import save_data, load_json

def add_user(args):
    users = load_json("user.json")
    new_user = User(args.name, args.email)
    users.append({"id": new_user.id, "name": new_user.name, "email": new_user.email})
    save_data("user.json", users)
    print(f"{new_user.name} added to list")

def add_projects(args):
    projects = load_json("project.json")
    new_project = Project(args.title, args.description, args.due_date, args.user_id )
    projects.append({
        "id":new_project.id,
        "title":new_project.title,
        "description":new_project.description,
        "due_date":str(new_project.due_date),
        "user_id":new_project.user_id

    })
    save_data("project.json", projects)
    print(f"{new_project.title} added to projects")

def add_task(args):
    tasks = load_json("task.json")
    new_task = Task(args.title, args.status, args.assigned_to, args.project_id)
    tasks.append({
        "id":new_task.id,
        "title":new_task.title,
        "status":new_task.status,
        "assigned_to":new_task.assigned_to,
        "project_id":new_task.project_id

    })
    save_data("task.json", tasks)
    print(f"{new_task.title} added to list")


def list_projects(args):
    projects = load_json("project.json")
    for project in projects:
        print(f"{project['id']}: {project['title']} {project['description']}(Due {project['due_date']})")

def complete_task(args):
    tasks = load_json("task.json")
    for task in tasks:
        if task["id"] ==int(args.task_id):
            task["status"] = "completed"
            print(f"{task['title']} marked as complete")
    save_data("task.json", tasks)



def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser("add-user", help="Add a new user")
    add_parser.add_argument("name", help="Add name")
    add_parser.add_argument("email", help="Add email")
    add_parser.set_defaults(func = add_user)

    project_add_parser = subparsers.add_parser("add-project", help="Add a new project")
    project_add_parser.add_argument("title", help="Add project title")
    project_add_parser.add_argument("description", help="Add project description")
    project_add_parser.add_argument("due_date", help="Add project due date")
    project_add_parser.add_argument("user_id", help="Add project user_id")
    project_add_parser.set_defaults(func = add_projects)

    task_add_parser = subparsers.add_parser("add-task", help="Add a new task")
    task_add_parser.add_argument("title", help="Add task title")
    task_add_parser.add_argument("status", help="Add status description")
    task_add_parser.add_argument("assigned_to", help="Task assigned to")
    task_add_parser.add_argument("project_id", help="Add task project_id")
    task_add_parser.set_defaults(func = add_task)


    proj_parser = subparsers.add_parser("list-projects", help="List available projects")
   
    proj_parser.set_defaults(func=list_projects)

    task_parser = subparsers.add_parser("complete-task", help = "Completed projects")
    task_parser.add_argument("task_id", help="task ID")
    task_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
