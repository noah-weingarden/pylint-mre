"""A module for the Goodbye class."""

class Goodbye:
    """A class that can print goodbye."""
    def __init__(self, name: str):
        self.name = name

    def display(self):
        """Print out the name."""
        print(f"Goodbye {self.name}")

    def __repr__(self) -> str:
        return self.name
