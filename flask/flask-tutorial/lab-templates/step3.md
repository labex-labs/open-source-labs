# Create the Flask application

Create a new Python file called `app.py` and add the following code:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)
```

Run the Flask application using the following command:

```shell
python app.py
```

Open your web browser and navigate to `http://127.0.0.1:5000`. You should see the message "Hello, Flask!" displayed in your browser.
