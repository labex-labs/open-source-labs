# Make the Project Installable

## Introduction

In this lab, you will learn how to make your Python Flask project installable. Making your project installable allows you to build a wheel file, which can then be installed in any other environment. This makes it easier to deploy your project and use standard Python tools for managing dependencies.

## Steps

### Step 1: Describe the Project

The first step is to create a `pyproject.toml` file that describes your project and its dependencies. This file is used by the setuptools build backend to build your project.

```toml
# pyproject.toml

[project]
name = "flaskr"
version = "1.0.0"
dependencies = [
    "flask",
]

[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
```

You also need to create a `MANIFEST.in` file to specify non-Python files to include in the build.

```
# MANIFEST.in

include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global-exclude *.pyc
```

### Step 2: Install the Project

To install your project, use `pip` in your virtual environment.

```bash
$ pip install -e .
```

This command tells `pip` to find the `pyproject.toml` file in the current directory and install the project in editable mode. This means that any changes you make to your local code will only require re-installation if you change the project's metadata, such as its dependencies.

You can verify that the project is installed by running `pip list`.

```bash
$ pip list

Package Version Location
-------------- --------- ----------------------------------
click 6.7
Flask 1.0
flaskr 1.0.0 /home/user/Projects/flask-tutorial
itsdangerous 0.24
Jinja2 2.10
MarkupSafe 1.0
pip 9.0.3
setuptools 39.0.1
Werkzeug 0.14.1
wheel 0.30.0
```

### Step 3: Test the Project

Once the project is installed, you can continue running it as before. The `--app` flag is still set to `flaskr`, and `flask run` will still start the application. The only difference now is that you can run the application from anywhere, not just the project directory.

## Summary

By making your Python Flask project installable, you can easily deploy it in different environments using standard Python tools. This allows you to manage dependencies, isolate test environments, and use your project as a library in other projects.
