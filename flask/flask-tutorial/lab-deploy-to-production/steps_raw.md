# Deploy to Production

## Introduction

This lab provides a step-by-step guide on how to deploy a Python Flask application to a production server. It covers building and installing the application, configuring the secret key, and running the application with a production server.

## Steps

### Step 1: Build and Install

To deploy the Flask application, we need to create a distribution file called a wheel file. Follow the steps below to build and install the application:

1. Install the `build` tool by running the following command:

```bash
$ pip install build
```

2. Build the wheel file using the `build` tool:

```bash
$ python -m build --wheel
```

3. Locate the generated wheel file in the `dist` folder. The file name will be in the format of `{project name}-{version}-{python tag}-{abi tag}-{platform tag}`.

4. Copy the wheel file to the production server.

5. Set up a new virtual environment on the production server.

6. Install the wheel file using `pip`:

```bash
$ pip install flaskr-1.0.0-py3-none-any.whl
```

7. Run the `init-db` command to create the database in the instance folder:

```bash
$ flask --app flaskr init-db
```

Note: If Flask detects that it's installed (not in editable mode), it uses a different directory for the instance folder. You can find it at `.venv/var/flaskr-instance` instead.

### Step 2: Configure the Secret Key

It's important to change the default value of the `SECRET_KEY` in production to enhance security. Follow the steps below to configure the secret key:

1. Generate a random secret key by running the following command:

```bash
$ python -c 'import secrets; print(secrets.token_hex())'
```

Example output: `'192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'`

2. Create the `config.py` file in the instance folder and copy the generated secret key into it:

```python
# .venv/var/flaskr-instance/config.py

SECRET_KEY = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
```

You can also set any other necessary configuration in this file.

### Step 3: Run with a Production Server

Running the Flask application with the built-in development server is not recommended for production environments. Instead, use a production WSGI server like `Waitress`. Follow the steps below to run the application with Waitress:

1. Install Waitress in the virtual environment:

```bash
$ pip install waitress
```

2. Use the following command to start the Waitress server and specify the application to run:

```bash
$ waitress-serve --call 'flaskr:create_app'
```

The server will start running and listening on a specific address (e.g., `http://0.0.0.0:8080`).

## Summary

In this lab, you learned how to deploy a Python Flask application to a production server. You built and installed the application using a wheel file, configured the secret key for security, and ran the application with a production WSGI server like Waitress.
