# Project Management CLI Tool

A simple command-line application for managing users, projects, and tasks.

## Features

- Add and list users
- Create projects with due dates and assigned user IDs
- Add tasks to projects with status and assignee
- List tasks for a specific project
- Mark tasks as complete

## Requirements

- Python 3.11+
- Dependencies listed in `requirements.txt`

## Installation

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the CLI from the project root:

```bash
python main.py <command> [arguments]
```

### Commands

- `add-user <name> <email>`
  - Add a new user
- `add-project <title> <description> <due_date> <user_id>`
  - Create a new project with `YYYY-MM-DD` due date
- `add-task <title> <status> <assigned_to> <project_id>`
  - Add a task to a project
- `list-users`
  - Show all users
- `list-projects [--user_id USER_ID]`
  - Show all projects, optionally filtered by user
- `list-tasks <project_id>`
  - Show tasks for a specific project
- `complete-task <task_id>`
  - Mark a task as completed

## Data Storage

Data is stored in JSON files under the `data/` folder:

- `data/user.json`
- `data/project.json`
- `data/task.json`

## Testing

Run tests with pytest:

```bash
pytest
```
