
class ProgrammingLanguage:
    """Represents a ProgrammingLanguage object."""

    def __init__(self, name = "", typing = '', reflection = False, year = 0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
    def is_dynamic(self):
        """Determine if the typing is dynamic."""
        if self.typing == "Dynamic":
            return True
        else:
            return False
    def __str__(self):
        """Return a string of information."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"