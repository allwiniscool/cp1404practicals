class Project:
    def __init__(self,name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage
    def __lt__(self, other):
        # Incomplete tasks (completion < 100) come before completed ones
        if self.completion_percentage == 100 and other.completion_percentage != 100:
            return  self.completion_percentage<other.completion_percentage
        elif self.completion_percentage != 100 and other.completion_percentage == 100:
            return other.completion_percentage<self.completion_percentage
        return self.priority < other.priority
    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"

