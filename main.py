import argparse

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
    args.func(args)

if __name__ == "__main__":
    main()
