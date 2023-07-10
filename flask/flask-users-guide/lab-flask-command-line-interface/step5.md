# Register Commands with the Flask Application

To make your custom commands available through the Flask CLI, you need to register them with your Flask application. Open the `app.py` file and modify it as follows:

```python
from flask import Flask
from commands import greet

app = Flask(__name__)
app.cli.add_command(greet)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
```

Save the file and restart the Flask development server using the `flask run` command. Now you can execute your custom command `greet` from the command line:

```
flask greet John
```

You should see the message "Hello, John!" printed in the terminal.
