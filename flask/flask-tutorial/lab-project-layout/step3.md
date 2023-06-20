# Create a Basic Flask App

Create a simple Flask application in a file named `hello.py`.

```python
# hello.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # Defines a route that returns a string
    return 'Hello, World!'
```
