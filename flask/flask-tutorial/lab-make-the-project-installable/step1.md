# Describe the Project

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
