# Configuration Handling Lab

## Introduction

In this lab, you will learn how to handle configuration in a Flask application. Configuration allows you to change settings in your application based on different environments, such as toggling debug mode, setting secret keys, and other environment-specific variables.

## Steps

### Step 1: Create a Flask Application

First, let's create a basic Flask application. Create a file called `app.py` and add the following code:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'
```

To run the application, execute the following command in your terminal:

```shell
python app.py
```

Open your web browser and visit `http://localhost:5000` to see the "Hello, Flask!" message.

### Step 2: Basic Configuration

Now let's add some basic configuration to our Flask application. In the same `app.py` file, add the following code:

```python
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mysecretkey'
```

The `DEBUG` configuration enables debug mode, which provides helpful error messages during development. The `SECRET_KEY` configuration is used for securely signing session cookies and other security-related needs.

To access the configuration values, you can use the `app.config` dictionary. For example, to print the value of the `SECRET_KEY`, add the following code to the `hello` route:

```python
@app.route('/')
def hello():
    secret_key = app.config['SECRET_KEY']
    return f'Hello, Flask! Secret Key: {secret_key}'
```

Restart the Flask application and visit `http://localhost:5000` to see the updated message with the secret key.

### Step 3: Configuration from Files

Hardcoding the configuration values in the code is not ideal, especially for sensitive information. Flask provides a way to load configuration from separate files. Create a new file called `config.py` and add the following code:

```python
DEBUG = False
SECRET_KEY = 'myothersecretkey'
```

In the `app.py` file, replace the previous configuration code with the following:

```python
app.config.from_object('config')
```

The `from_object` method loads the configuration from the `config` module. Now, the `DEBUG` and `SECRET_KEY` values will be loaded from the `config.py` file.

Restart the Flask application and visit `http://localhost:5000` to see the updated message with the new configuration values.

### Step 4: Environment-based Configuration

It's common to have different configurations for different environments, such as development, production, and testing. Flask allows you to switch configurations based on environment variables. Create a new file called `config_dev.py` and add the following code:

```python
DEBUG = True
SECRET_KEY = 'devsecretkey'
```

Create another file called `config_prod.py` with the following code:

```python
DEBUG = False
SECRET_KEY = 'prodsecretkey'
```

In the `app.py` file, replace the previous configuration code with the following:

```python
import os

if os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object('config_prod')
else:
    app.config.from_object('config_dev')
```

The `FLASK_ENV` environment variable is used to determine the environment. If it is set to `'production'`, the production configuration will be loaded; otherwise, the development configuration will be loaded.

Set the `FLASK_ENV` environment variable to `'production'` and restart the Flask application. Visit `http://localhost:5000` to see the updated message with the production configuration values.

### Step 5: Instance Folder

Flask provides an instance folder for storing configuration files that are specific to a particular deployment. This allows you to separate deployment-specific configurations from the rest of your code. By default, Flask uses a folder named `instance` in the same directory as your application.

Create a new folder called `instance` in the same directory as your `app.py` file. In the `instance` folder, create a file called `config.cfg` and add the following code:

```
DEBUG = True
SECRET_KEY = 'instancekey'
```

In the `app.py` file, add the following code before the configuration code:

```python
app.instance_path = os.path.abspath(os.path.dirname(__file__))
app.config.from_pyfile('config.cfg')
```

The `instance_path` is set to the absolute path of the `instance` folder. The `from_pyfile` method loads the configuration from the `config.cfg` file in the instance folder.

Restart the Flask application and visit `http://localhost:5000` to see the updated message with the instance configuration values.

## Summary

In this lab, you learned how to handle configuration in a Flask application. You learned how to set basic configuration values, load configuration from files, switch configurations based on environment variables, and use an instance folder for deployment-specific configurations. Configuration is an important aspect of building robust and flexible Flask applications.
