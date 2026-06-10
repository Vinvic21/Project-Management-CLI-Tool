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


def list_projects(args):
    projects = load_json("projects.json")
    for project in projects:
        print(f"{project['id']}: {project['title']} (Due {project['due_date']})")

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
