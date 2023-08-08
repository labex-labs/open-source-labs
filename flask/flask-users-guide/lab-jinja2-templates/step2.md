# Create a Flask Application

Create a new file called `app.py` and import the necessary modules:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

In this code, we create a new Flask application and define a route for the root URL ("/"). When a user visits the root URL, the `index()` function will be called and it will render the `index.html` template.
