# Set up Flask Application

Before we can run the development server, we need to set up a Flask application. Create a new Python file called `app.py` and add the following code:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == "__main__":
    app.run(debug=True)
```

In this code, we create a Flask application and define a route that returns a simple "Hello, Flask!" message. The `if __name__ == "__main__":` block ensures that the Flask application is only run when the script is executed directly, not when it is imported as a module.


