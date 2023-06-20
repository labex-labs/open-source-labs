# Describe the Project

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
