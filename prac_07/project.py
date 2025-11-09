import datetime

from project_management import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
>>>"""
def main():
    """Display menu and take user input to make decisions."""
    print("Welcome to Pythonic Project Management")
    projects = []
    load_file("projects.txt",projects)
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "D":
            display_projects(projects)
        elif choice == "L":
            filename = input("Filename: ")
            load_file(filename, projects)
        elif choice == "U":
            update_project(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "S":
            filename = input("filename to save projects: ")
            save_project(projects)
            save_project(projects)
        choice = input(MENU).upper()
        save_choice = input("Would you like to save to projects.txt?").upper()
        if save_choice[1] == "Y":
            save_project(projects, "projects.txt")
        else:
            print("Thank you for using custom-built project management software.")


def load_file(filename,projects):
    """Load a file into a list called projects."""
    infile = open(filename,"r")
    infile.readline()
    for line in infile:
        row = [row.strip() for row in line.split("\t")]
        name = row[0]
        start_date = datetime.datetime.strptime(row[1], "%d/%m/%Y").date()
        priority = int(row[2])
        cost_estimate = float(row[-2])
        completion_percentage = int(row[-1])
        projects.append(Project(name,start_date,priority,cost_estimate,completion_percentage))
    infile.close()
    print(f"Loaded {len(projects)} projects from {filename}")



# display project
def display_projects(projects):
    """Display a list of projects."""
    projects.sort()
    print("Incomplete projects:")
    for project in projects:
        if project.completion_percentage != 100:
            print(project)
    print("Complete projects:")
    for project in projects:
        if project.completion_percentage == 100:
            print(project)

def add_project(projects):
    """Add a project to the list of projects."""
    name = input("Name: ")
    start_date = get_valid_date(prompt = "Start date (d/m/yyyy): ")
    priority = get_valid_input_value(prompt="Priority: ",min_value = 1, max_value = 10)
    while priority == "":
        print("Invalid input, enter a number.")
        priority = get_valid_input_value(prompt="Priority: ", min_value=1, max_value=10)
    cost_estimate = get_valid_cost()
    completion_percentage = get_valid_input_value(prompt = "Completion percentage: ", min_value = 0, max_value = 100)
    while completion_percentage == "":
        print("Invalid input, enter a number.")
        completion_percentage = get_valid_input_value(prompt = "Completion percentage: ", min_value = 0, max_value = 100)
    projects.append(Project(name,start_date,priority,cost_estimate,completion_percentage))
    print(projects[-1])



def filter_projects_by_date(projects):
    """Filter a list of projects by date."""
    date = get_valid_date(prompt = "Show projects that start after date (dd/mm/yy): ")
    print(f"That day is/was {date.strftime('%A')}")
    print(date.strftime("%d/%m/%Y"))
    for project in projects:
        if date <= project.start_date:
            print(project)

def update_project(projects):
    """Update the completion_percentage and priority of a project inside projects."""
    n = 0
    for project in projects:
        print(n, project)
        n+=1
    choice = get_valid_project_number(projects)
    new_percentage = get_valid_input_value(prompt = "New percentage: ", min_value = 0, max_value = 100)
    if new_percentage == "":
        projects[choice].completion_percentage = projects[choice].completion_percentage
    else:
        projects[choice].completion_percentage = new_percentage
    new_priority = get_valid_input_value(prompt="New priority: ",min_value = 1, max_value = 10)
    if new_priority == "":
        projects[choice].priority = projects[choice].priority
    else:
        projects[choice].priority = new_priority
    print(projects[choice])

def save_project(projects, filename = ""):
    """Save a list of projects to a file."""
    out_file = open(filename,"w")
    out_file.write((f"Name\tstart_date\tpriority\tcost_estimate\tcompletion_percentage\n"))
    for project in projects:
        out_file.write((f"{project.name}\t{project.start_date.strftime("%d/%m/%Y")}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n"))
    out_file.close()


# error checkers
def get_valid_project_number(projects):
    """Get a valid project number for update_project function."""
    while True:
        try:
            choice = int(input("Project choice: "))
            if 0 <= choice < len(projects):
                return choice
            else:
                print("Invalid choice, out of range.")
        except ValueError:
            print("Invalid input, enter a number.")

def get_valid_input_value(prompt = "", min_value = 0, max_value = 100):
    """Get a valid input value from user."""
    while True:
        choice = input(prompt)
        if choice == "":
            return choice
        elif choice.isdigit():
            int_choice = int(choice)
            if int_choice > max_value or int_choice < min_value:
                print("Invalid choice")
            else:
                return int_choice
        else:
            print("Invalid input, enter a number.")


def get_valid_cost():
    """Get a valid value for cost from user."""
    cost = ""
    while cost == "":
        try:
            cost = float(input("Cost: "))
        except ValueError:
            print("Invalid input, enter a number.")
    return cost


def get_valid_date(prompt = ""):
    """Get a valid date from user."""
    while True:
        try:
            date_string = input(prompt)
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            return date
        except ValueError:
            print("doesn't match formatting(dd/mm/yyyy).")
