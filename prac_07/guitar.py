class Guitar:
    """Represent a Guitar object."""
    def __init__(self, name='',year=0, cost=0):
        """Initialise a Guitar instance.
                name: name of guitar.
                year: when the guitar was made.
                cost: cost of guitar.
                """
        self.name = name
        self.year = year
        self.cost = cost
    def get_age(self):
        """Figure out how old the guitar is."""
        return 2025 - self.year
    def is_vintage(self):
        """Determine if the guitar is vintage."""
        if self.get_age() >= 50:
            return True
        else:
            return False
    def __lt__(self, other):
        return self.year < other.year
    def __str__(self):
        """returns a string of details."""
        return f"{self.name} ({self.year}): ${self.cost}"