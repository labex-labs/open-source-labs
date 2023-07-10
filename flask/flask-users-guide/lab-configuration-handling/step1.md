# Create a Flask Application

First, let's create a basic Flask application. Create a file called `app.py` and add the following code:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'
```

To run the application, execute the following command in your terminal:

```shell
python app.py
```

Open your web browser and visit `http://localhost:5000` to see the "Hello, Flask!" message.


