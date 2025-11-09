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

