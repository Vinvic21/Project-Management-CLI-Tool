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
    Task.ID_counter = max([t["id"] for t in tasks], default=0) + 1 
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
def list_tasks(args):
    tasks = load_json("task.json")
    filtered = [task for task in tasks if str(task["project_id"]) == str(args.project_id)]

    if not filtered:
        console.print(f"[red] No task found for project")
        return
    
    table = Table(title= f"Tasks for Project {args.project_id}")
    table.add_column("ID", justify= "right")
    table.add_column("Title", style="green")
    table.add_column("Status", style="green")
    table.add_column("assigned_to", style="green")
    
    for task in filtered:
        status_color = "green" if task["status"] == "completed" else "red" 
        
        table.add_row(
            str(task["id"]),
            task["title"],
            f"[{status_color}]{task['status']}",
            str(task["assigned_to"] or "Unassigned")
        )
    console.print(table)

def list_projects(args):
    projects = load_json("project.json")
    if args.user_id:
        projects = [project for project in projects if str(project["user_id"]) == str(args.user_id)]

    if not projects:
        console.print("[red] No projects found")
        return
    
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
def edit_user(args):
    users = load_json("user.json")
    for user in users:
        if str(user["id"]) == str(args.id):
            if args.name:
                user["name"] = args.name
            if args.email:
                user["email"] = args.email
            save_data("user.json", users)
            console.print(f"[green]User {args.id} updated successfully.")
            return
    console.print(f"[red]User with ID {args.id} not found.")
def edit_project(args):
    projects = load_json("project.json")
    for project in projects:
        if str(project["id"]) == str(args.id):
            if args.title:
                project["title"] = args.title
            if args.description:
                project["description"] = args.description
            if args.due_date:
                project["due_date"] = args.due_date
            save_data("project.json", projects)
            console.print(f"[green]Project {args.id} updated successfully.")
            return
    console.print(f"[red]Project with ID {args.id} not found.")
def edit_task(args):    
    tasks = load_json("task.json")
    for task in tasks:
        if str(task["id"]) == str(args.id):
            if args.title:
                task["title"] = args.title
            if args.status:
                task["status"] = args.status
            if args.assigned_to:
                task["assigned_to"] = args.assigned_to
            if args.project_id:
                task["project_id"] = args.project_id
            save_data("task.json", tasks)
            console.print(f"[green]Task {args.id} updated successfully.")
            return
    console.print(f"[red]Task with ID {args.id} not found.")
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

    list_tasks_parser = subparsers.add_parser("list-tasks", help="List tasks for a project")
    list_tasks_parser.add_argument("project_id", help="Project ID to list tasks for")
    list_tasks_parser.set_defaults(func=list_tasks)

    edit_user_parser = subparsers.add_parser("edit-user", help="Edit user details")
    edit_user_parser.add_argument("id", help="User ID to edit")
    edit_user_parser.add_argument("--name", help="New name for the user")
    edit_user_parser.add_argument("--email", help="New email for the user")
    edit_user_parser.set_defaults(func=edit_user)

    edit_project_parser = subparsers.add_parser("edit-project", help="Edit project details")
    edit_project_parser.add_argument("id", help="Project ID to edit")
    edit_project_parser.add_argument("--title", help="New title for the project")
    edit_project_parser.add_argument("--description", help="New description for the project")
    edit_project_parser.add_argument("--due_date", help="New due date for the project")
    edit_project_parser.set_defaults(func=edit_project)

    edit_task_parser = subparsers.add_parser("edit-task", help="Edit task details")
    edit_task_parser.add_argument("id", help="Task ID to edit")
    edit_task_parser.add_argument("--title", help="New title for the task")
    edit_task_parser.add_argument("--status", help="New status for the task")
    edit_task_parser.add_argument("--assigned_to", help="New assignee for the task")
    edit_task_parser.add_argument("--project_id", help="New project ID for the task")
    edit_task_parser.set_defaults(func=edit_task)

    proj_parser = subparsers.add_parser("list-projects", help="List available projects")
    proj_parser.add_argument("--user_id", help="Filter projects by user ID", default=None)
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
