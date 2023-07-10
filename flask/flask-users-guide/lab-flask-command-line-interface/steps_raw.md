# Flask Command Line Interface

## Introduction

In this lab, you will learn how to use the Flask Command Line Interface (CLI) to manage your Flask application. The Flask CLI provides a set of commands that can help you run the development server, create custom commands, and more.

## Steps

### Step 1: Install Flask

Before getting started, make sure you have Flask installed in your Python environment. You can install Flask using pip:

```
pip install flask
```

### Step 2: Create a Flask Application

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

### Step 3: Run the Development Server

Instead of manually running the Flask application using `python app.py`, you can use the Flask CLI to start the development server. Stop the currently running application (if any) and execute the following command:

```
flask run
```

You should see the Flask development server start and display the URL where your application is running (usually `http://127.0.0.1:5000/`). Open that URL in your browser and you should see the "Hello, Flask!" message.

### Step 4: Create a Custom Command

The Flask CLI allows you to create custom commands that can be executed from the command line. Let's create a custom command named `greet` that takes a name as an argument and prints a greeting message.

Create a new Python file named `commands.py` and add the following code:

```python
import click

@click.command()
@click.argument('name')
def greet(name):
    click.echo(f'Hello, {name}!')

if __name__ == '__main__':
    greet()
```

Save the file and execute it using the following command:

```
python commands.py John
```

You should see the message "Hello, John!" printed in the terminal.

### Step 5: Register Commands with the Flask Application

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

## Summary

In this lab, you learned how to use the Flask Command Line Interface (CLI) to manage your Flask application. You learned how to run the development server, create custom commands, and register commands with your Flask application. The Flask CLI provides a convenient way to interact with your Flask application from the command line, making it easier to manage and test your application.
