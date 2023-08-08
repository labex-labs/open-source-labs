# Firing Before/After Request Functions

By creating a request context, the code that is normally run before a request is not triggered. To simulate the before-request functionality, call the `preprocess_request()` method. This ensures that database connections and other resources are available.

```python
# File: shell.py
# Execution: python shell.py

from flask import Flask

app = Flask(__name__)

# Create a request context
ctx = app.test_request_context()
ctx.push()

# Simulate the before-request functionality
app.preprocess_request()

# Work with the request object

# Pop the request context
ctx.pop()
```

To simulate the after-request functionality, call the `process_response()` method with a dummy response object before popping the request context.

```python
# File: shell.py
# Execution: python shell.py

from flask import Flask

app = Flask(__name__)

# Create a request context
ctx = app.test_request_context()
ctx.push()

# Simulate the before-request functionality
app.preprocess_request()

# Work with the request object

# Simulate the after-request functionality
app.process_response(app.response_class())

# Pop the request context
ctx.pop()
```
