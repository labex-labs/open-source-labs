# Deploy Flask Application

## Introduction

In this lab, we will learn how to deploy a Flask application to a server. We will create a distribution file for our application and install it on the server. The lab assumes you have a basic understanding of Flask, Python's virtual environments, and the command line.

## Steps

### Step 1: Build the Application

First, we need to create a wheel file for our application. We will use the `build` tool for this. Install the `build` tool using pip if you haven't already:

```bash
# Install the build tool
pip install build
```

Now, use the `build` tool to create the wheel file:

```bash
# Build the wheel file
python -m build --wheel
```

The wheel file should be in the `dist` directory with a name like `flaskr-1.0.0-py3-none-any.whl`.

### Step 2: Install the Application on the Server

Copy the wheel file to your server. Once it's there, set up a new Python virtual environment and install the wheel file using pip:

```bash
# Install the wheel file
pip install flaskr-1.0.0-py3-none-any.whl
```

Since this is a new environment, you need to initialize the database again:

```bash
# Initialize the database
flask --app flaskr init-db
```

### Step 3: Configure the Secret Key

In a production environment, you should change the secret key to a random value. To generate a random secret key, run the following command:

```bash
# Generate a random secret key
python -c 'import secrets; print(secrets.token_hex())'
```

Create a `config.py` file in the instance folder and set `SECRET_KEY` to the generated value.

```python
# .venv/var/flaskr-instance/config.py

SECRET_KEY = 'your_generated_secret_key'
```

### Step 4: Run the Application with a Production Server

For a production environment, you should use a WSGI server instead of the built-in development server. We will use Waitress as our WSGI server.

First, install Waitress:

```bash
# Install Waitress
pip install waitress
```

Now, tell Waitress to serve your application:

```bash
# Run the application with Waitress
waitress-serve --call 'flaskr:create_app'
```

## Summary

In this lab, we learned how to deploy a Flask application to a production server. We built our application into a wheel file, installed it on the server, configured the secret key, and ran the application with a production WSGI server.
