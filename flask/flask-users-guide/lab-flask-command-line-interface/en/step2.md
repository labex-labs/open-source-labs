# Create a Flask Application

Create a new Python file named `app.py` and add the following code to create a basic Flask application:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
```

Save the file and execute it using the following command in your terminal:

```
python app.py
```
