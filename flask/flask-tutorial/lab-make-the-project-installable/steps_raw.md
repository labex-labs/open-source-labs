# Make Project Installable

## Introduction

In this lab, we will learn how to make a Python Flask project installable. This will make the project deployable and manageable using standard Python tools. This process is beneficial as it allows the project to be installed in different environments, manage dependencies, and isolate test environments.

## Steps

### Step 1: Describe the Project

First, we need to create a `pyproject.toml` file to describe our project and how to build it.

The `pyproject.toml` file should look like this:

```toml
# pyproject.toml

[project]
name = "flaskr" # name of the project
version = "1.0.0" # version of the project
dependencies = [
    "flask", # dependencies of the project
]

[build-system]
requires = ["setuptools"] # required build system
build-backend = "setuptools.build_meta" # backend build system
```

### Step 2: Include Necessary Files

The setuptools build backend needs another file named `MANIFEST.in` to include non-Python files in the project.

Create a `MANIFEST.in` with the following content:

```none
# MANIFEST.in

include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global-exclude *.pyc
```

This tells the build to copy everything in the `static` and `templates` directories, and the `schema.sql` file, while excluding all bytecode files.

### Step 3: Install the Project

Next, we will use `pip` to install the project in the virtual environment.

Run the following command in your terminal:

```none
pip install -e .
```

This tells pip to find `pyproject.toml` in the current directory and install the project in editable or development mode. Editable mode means that as you make changes to your local code, you'll only need to re-install if you change the project's metadata.

To verify the installation, use the `pip list` command:

```none
pip list
```

The output should show the installed project and its dependencies.

## Summary

In this lab, we learned how to make a Python Flask project installable. We started by describing the project and including necessary files. We then installed the project in a virtual environment. Now, the project can be run from any location, not just the project directory.
