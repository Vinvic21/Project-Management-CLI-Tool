import argparse
from models.project import Project
from models.task import Task
from models.user import User
from utils.IO import save_data, load_json
from rich.console import Console
from rich.table import Table

console = Console()
def add_user(args):
    users = load_json("user.json")
    User.Id_counter = max([u["id"] for u in users], default=0) + 1
    new_user = User(args.name, args.email)
    users.append({"id": new_user.id, "name": new_user.name, "email": new_user.email})
    save_data("user.json", users)
    console.print(f"[green]{new_user.name} added to list")

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
    console.print(f"[green]{new_project.title} added to projects")

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
def list_users(args):
    users = load_json("user.json")
    if not users:
        console.print("[red] No user Found")
    
    table = Table(title= "Users")
    table.add_column("ID", justify= "right")
    table.add_column("Name", style= "green")
    table.add_column("Email", style="green")

    for user in users:
        table.add_row(
            str(user["id"]),
            user["name"],
            user["email"]
        
        )
    
    console.print(table)

def list_projects(args):
    projects = load_json("project.json")
    if not projects:
        console.print("[red] No projects found")
    
    table = Table(title = "Projects")
    table.add_column("id", justify="right")
    table.add_column("title", style="green")
    table.add_column("description", style="green")
    table.add_column("due_date", style="green")
    table.add_column("user_id", style= "green")

    for project in projects:
        table.add_row(
            str(project["id"]),
            project["title"],
            project["description"],
            project["due_date"],
            str(project["user_id"])
        )
    
    console.print(table)
    
def complete_task(args):
    tasks = load_json("task.json")
    for task in tasks:
        if task["id"] ==int(args.task_id):
            task["status"] = "completed"
            console.print(f"[green]{task['title']} marked as complete")
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


    user_parser = subparsers.add_parser("list-users", help="List available users")
    user_parser.set_defaults(func=list_users)


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
