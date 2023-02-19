"""A module for the Hello class."""

class Hello:
    """A class that can print hello."""
    def __init__(self, name: str):
        self.name = name

    def display(self):
        """Print out the name."""
        print(f"Hello {self.name}")

    def __repr__(self) -> str:
        return self.name
