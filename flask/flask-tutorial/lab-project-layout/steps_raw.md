# Project Layout

## Introduction

This lab will guide you through the process of creating a project layout for a Python Flask application. A well-organized project structure makes it easier to manage and scale your application as it grows. By the end of this lab, you will have a clear understanding of how to structure your Flask projects effectively.

## Steps

### Step 1: Create the Project Directory

Create a project directory for your Flask application and navigate into it using the following commands:

```shell
$ mkdir flask-tutorial
$ cd flask-tutorial
```

### Step 2: Set up a Python Virtual Environment

Set up a Python virtual environment to isolate your project dependencies. Follow the installation instructions to create a virtual environment and install Flask for your project.

```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install Flask
```

### Step 3: Create the Flask Application

Create a simple Flask application in a file named `hello.py` using the following code:

```python
# hello.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
```

### Step 4: Organize the Project Structure

As your project grows, it becomes necessary to organize the code into multiple files and directories. Create the following structure for your project:

```
flask-tutorial/
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── .venv/
├── pyproject.toml
└── MANIFEST.in
```

### Step 5: Set Up Version Control (Optional)

It is recommended to use version control for your projects. Initialize a Git repository and create a `.gitignore` file to exclude unnecessary files:

```shell
$ git init
$ touch .gitignore
```

Add the following content to the `.gitignore` file:

```
.venv/
*.pyc
__pycache__/
instance/
.pytest_cache/
.coverage
htmlcov/
dist/
build/
*.egg-info/
```

### Step 6: Summary

Congratulations! You have successfully created a well-structured project layout for your Flask application. This organization will make it easier to manage and scale your application as it grows. Remember to use version control and regularly commit your changes to keep track of your project's history.

## Summary

In this lab, you learned how to create a project layout for a Python Flask application. By organizing your code into packages and modules, you can keep your project structured and maintainable. With a clear project structure, it becomes easier to collaborate with others and manage the growth of your application.
