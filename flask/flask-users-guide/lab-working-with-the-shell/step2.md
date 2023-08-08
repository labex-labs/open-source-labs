# Creating a Request Context

To create a proper request context in the shell, use the `test_request_context()` method, which creates a `RequestContext` object. In the shell, manually push and pop the request context using the `push()` and `pop()` methods.

```python
# File: shell.py
# Execution: python shell.py

from flask import Flask

app = Flask(__name__)

# Create a request context
ctx = app.test_request_context()

# Push the request context
ctx.push()

# Work with the request object

# Pop the request context
ctx.pop()
```
