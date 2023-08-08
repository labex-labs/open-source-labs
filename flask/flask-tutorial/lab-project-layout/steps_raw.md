# Flask Project Setup

## Introduction

In this lab, we will learn how to create a directory layout for a Flask project. We will be setting up a Flask application with a structured directory, which will include various files and packages needed for a Flask project. This layout is beneficial for managing larger projects.

## Steps

### Step 1: Create Project Directory

Start by creating a new directory for your Flask project and navigate into it using the terminal.

```bash
mkdir flask-tutorial
cd flask-tutorial
```

### Step 2: Install Flask

Set up a Python virtual environment and install Flask for your project. Follow the installation instructions provided in the official Flask documentation.

### Step 3: Create a Basic Flask App

Create a simple Flask application in a file named `hello.py`.

```python
# hello.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # Defines a route that returns a string
    return 'Hello, World!'
```

### Step 4: Organize the Project

As your project grows, it is recommended to organize your code into packages. Set up your project directory to contain the following:

- `flaskr/`: a Python package containing your application code and files.
- `tests/`: a directory containing test modules.
- `.venv/`: a Python virtual environment where Flask and other dependencies are installed.

```bash
/home/user/Projects/flask-tutorial
├── flaskr/
│ ├── __init__.py
│ ├── db.py
│ ├── schema.sql
│ ├── auth.py
│ ├── blog.py
│ ├── templates/
│ │ ├── base.html
│ │ ├── auth/
│ │ │ ├── login.html
│ │ │ └── register.html
│ │ └── blog/
│ │ ├── create.html
│ │ ├── index.html
│ │ └── update.html
│ └── static/
│ └── style.css
├── tests/
│ ├── conftest.py
│ ├── data.sql
│ ├── test_factory.py
│ ├── test_db.py
│ ├── test_auth.py
│ └── test_blog.py
├── .venv/
├── pyproject.toml
└── MANIFEST.in
```

### Step 5: Set Up Version Control

It's a good practice to use version control systems like Git. Create a `.gitignore` file to exclude files that are not needed in the repository.

```bash
# .gitignore

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

## Summary

In this lab, we have learned how to set up a Flask project directory. We started by creating a new project directory, installing Flask, setting up a basic Flask app, organizing the project into packages, and finally, setting up a version control system. Now you are ready to continue developing your Flask application with a well-structured project directory.
