# Application Setup

## Introduction

This lab will guide you through the process of setting up a Flask application step by step. You will learn how to create a Flask instance, configure the application, and run it.

## Steps

### Step 1: Create the Flask Application

Create a directory named "flaskr" and add the "**init**.py" file inside it. This file will serve as the application factory.

```python
# flaskr/__init__.py

import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```

### Step 2: Configure the Application

In the "create_app" function, configure the Flask application by setting the secret key and database path.

```python
# flaskr/__init__.py

# ...

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # ...
```

### Step 3: Load Configuration from File

Add code to load configuration from a file named "config.py" in the instance folder, if it exists.

```python
# flaskr/__init__.py

# ...

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ...
```

### Step 4: Create the Instance Folder

Ensure that the instance folder exists by creating it if it doesn't already exist.

```python
# flaskr/__init__.py

# ...

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # ...
```

### Step 5: Add a Route

Create a simple route that displays a "Hello, World!" message when accessed.

```python
# flaskr/__init__.py

# ...

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ...

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```

### Step 6: Run the Application

Run the Flask application using the "flask" command. Make sure you are in the top-level directory.

```bash
$ flask --app flaskr run --debug
```

### Summary

In this lab, you learned how to set up a Flask application by creating a Flask instance, configuring the application, and running it. You also added a simple route to display a "Hello, World!" message.
