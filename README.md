# Minimal reproducible example

See [this comment]().

Steps to reproduce:

```console
$ python -m venv env
$ source env/bin/activate
$ pip install -e .
$ pip install -r requirements.txt
$ pytest tests
************* Module test_everything
tests/test_everything.py:6:14: E1101: Module 'pylint_bug_mre' has no 'goodbye' member; maybe 'Goodbye'? (no-member)
tests/test_everything.py:11:12: E1101: Module 'pylint_bug_mre' has no 'hello' member; maybe 'Hello'? (no-member)
```
