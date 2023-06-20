# Install the Project

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
