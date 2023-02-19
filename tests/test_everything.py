"""Tests for the pylint_bug_mre package."""
import pylint_bug_mre

def test_goodbye():
    """Create a Goodbye instance and display it."""
    goodbye = pylint_bug_mre.goodbye.Goodbye("Noah")
    goodbye.display()

def test_hello():
    """Create a Hello instance and display it."""
    hello = pylint_bug_mre.hello.Hello("Noah")
    hello.display()
