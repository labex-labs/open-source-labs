# Create the Flask Application

Create a simple Flask application in a file named `hello.py` using the following code:

```python
# hello.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
```
