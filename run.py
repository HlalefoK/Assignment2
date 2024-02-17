import tkinter as tk

# Create Tkinter window
window = tk.Tk()
window.title("Project Management System")

# Dictionary to store projects
projects = {}

# Dictionary to store project deadlines
project_deadlines = {}

# Dictionary to store tasks with dependencies
tasks = {}

# Dictionary to store assigned team members
assigned_team_members = {}

# Dictionary to store task deadlines
task_deadlines = {}

# Dictionary to store task progress
task_progress = {}

# Dictionary to store comments on tasks
task_comments = {}

# Dictionary to store user credentials
users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
    "user4": "password4",
    "user5": "password5",
    "user6": "password6",
    "user7": "password7",
}

current_user = ""


# Function to authenticate user
def authenticate_user():
    username = username_entry.get()
    password = password_entry.get()
    if users.get(username) == password:
        return True
    else:
        feedback_label.config(text="Authentication failed. Please try again.", fg="red")
        return False


# Function to create a project
def create_project():
    project_id = project_id_entry.get()
    project_name = project_name_entry.get()
    project_description = project_description_entry.get()
    projects[project_id] = {"name": project_name, "description": project_description}
    project_deadlines[project_id] = project_deadline_entry.get()
    feedback_label.config(text="Project created successfully.", fg="green")


# Function to assign a task
def assign_task():
    project_id = task_project_id_entry.get()
    task_id = task_id_entry.get()
    task_name = task_name_entry.get()
    team_member = task_team_member_entry.get()
    dependencies = task_dependencies_entry.get().split(',')
    assign_task_dependencies = [dependency.strip() for dependency in dependencies if dependency.strip()]
    tasks[task_id] = {"name": task_name, "dependencies": assign_task_dependencies}
    assigned_team_members[task_id] = team_member
    task_deadlines[task_id] = task_deadline_entry.get()
    task_progress[task_id] = 0
    task_comments[task_id] = []
    feedback_label.config(text="Task assigned successfully.", fg="green")


# Function to update progress
def update_progress():
    task_id = update_progress_task_id_entry.get()
    progress_update = int(update_progress_entry.get())
    task_progress[task_id] = progress_update
    feedback_label.config(text="Progress updated successfully.", fg="green")


# Function to add comment
def add_comment():
    task_id = add_comment_task_id_entry.get()
    comment = add_comment_entry.get()
    task_comments[task_id].append(comment)
    feedback_label.config(text="Comment added successfully.", fg="green")


# Function to view project status
def view_project_status():
    project_id = project_id_to_view_entry.get()
    status_text = f"Project: {projects[project_id]['name']} - {projects[project_id]['description']}\n"
    status_text += f"Deadline: {project_deadlines[project_id]}\n\nTasks:\n"
    for task_id, task_info in tasks.items():
        if task_id in assigned_team_members and assigned_team_members[task_id] == current_user:
            status_text += f"{task_info['name']} - Deadline: {task_deadlines[task_id]}, Progress: {task_progress[task_id]}%\n"
            if task_comments[task_id]:
                status_text += "Comments:\n"
                for comment in task_comments[task_id]:
                    status_text += f"  - {comment}\n"
    status_label.config(text=status_text)


# Create widgets for user authentication
username_label = tk.Label(window, text="Username:")
username_label.grid(row=0, column=0)
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1)

password_label = tk.Label(window, text="Password:")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=1, column=1)

authenticate_button = tk.Button(window, text="Authenticate", command=authenticate_user)
authenticate_button.grid(row=2, column=0, columnspan=2)

feedback_label = tk.Label(window, text="", fg="red")
feedback_label.grid(row=3, column=0, columnspan=2)


# Create widgets for creating a project
project_id_label = tk.Label(window, text="Project ID:")
project_id_label.grid(row=4, column=0)
project_id_entry = tk.Entry(window)
project_id_entry.grid(row=4, column=1)

project_name_label = tk.Label(window, text="Project Name:")
project_name_label.grid(row=5, column=0)
project_name_entry = tk.Entry(window)
project_name_entry.grid(row=5, column=1)

project_description_label = tk.Label(window, text="Project Description:")
project_description_label.grid(row=6, column=0)
project_description_entry = tk.Entry(window)
project_description_entry.grid(row=6, column=1)

project_deadline_label = tk.Label(window, text="Project Deadline:")
project_deadline_label.grid(row=7, column=0)
project_deadline_entry = tk.Entry(window)
project_deadline_entry.grid(row=7, column=1)

create_project_button = tk.Button(window, text="Create Project", command=create_project)
create_project_button.grid(row=8, column=0, columnspan=2)


# Create widgets for assigning a task
task_project_id_label = tk.Label(window, text="Project ID:")
task_project_id_label.grid(row=9, column=0)
task_project_id_entry = tk.Entry(window)
task_project_id_entry.grid(row=9, column=1)

task_id_label = tk.Label(window, text="Task ID:")
task_id_label.grid(row=10, column=0)
task_id_entry = tk.Entry(window)
task_id_entry.grid(row=10, column=1)

task_name_label = tk.Label(window, text="Task Name:")
task_name_label.grid(row=11, column=0)
task_name_entry = tk.Entry(window)
task_name_entry.grid(row=11, column=1)

task_team_member_label = tk.Label(window, text="Assigned Team Member:")
task_team_member_label.grid(row=12, column=0)
task_team_member_entry = tk.Entry(window)
task_team_member_entry.grid(row=12, column=1)

task_dependencies_label = tk.Label(window, text="Task Dependencies:")
task_dependencies_label.grid(row=13, column=0)
task_dependencies_entry = tk.Entry(window)
task_dependencies_entry.grid(row=13, column=1)

task_deadline_label = tk.Label(window, text="Task Deadline:")
task_deadline_label.grid(row=14, column=0)
task_deadline_entry = tk.Entry(window)
task_deadline_entry.grid(row=14, column=1)

assign_task_button = tk.Button(window, text="Assign Task", command=assign_task)
assign_task_button.grid(row=15, column=0, columnspan=2)


# Create widgets for updating progress
update_progress_task_id_label = tk.Label(window, text="Task ID:")
update_progress_task_id_label.grid(row=16, column=0)
update_progress_task_id_entry = tk.Entry(window)
update_progress_task_id_entry.grid(row=16, column=1)

update_progress_label = tk.Label(window, text="Progress:")
update_progress_label.grid(row=17, column=0)
update_progress_entry = tk.Entry(window)
update_progress_entry.grid(row=17, column=1)

update_progress_button = tk.Button(window, text="Update Progress", command=update_progress)
update_progress_button.grid(row=18, column=0, columnspan=2)


# Create widgets for adding comment
add_comment_task_id_label = tk.Label(window, text="Task ID:")
add_comment_task_id_label.grid(row=19, column=0)
add_comment_task_id_entry = tk.Entry(window)
add_comment_task_id_entry.grid(row=19, column=1)

add_comment_label = tk.Label(window, text="Comment:")
add_comment_label.grid(row=20, column=0)
add_comment_entry = tk.Entry(window)
add_comment_entry.grid(row=20, column=1)

add_comment_button = tk.Button(window, text="Add Comment", command=add_comment)
add_comment_button.grid(row=21, column=0, columnspan=2)


# Create widgets for viewing project status
project_id_to_view_label = tk.Label(window, text="Project ID to View:")
project_id_to_view_label.grid(row=22, column=0)
project_id_to_view_entry = tk.Entry(window)
project_id_to_view_entry.grid(row=22, column=1)

view_status_button = tk.Button(window, text="View Project Status", command=view_project_status)
view_status_button.grid(row=22, column=2)

status_label = tk.Label(window, text="", justify="left")
status_label.grid(row=23, column=0, columnspan=3)

window.mainloop()
