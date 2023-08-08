# Development Server

## Introduction

In this tutorial, you will learn how to use the development server in Flask to run your Flask application during local development. The development server provides an interactive debugger and automatically reloads the code when changes are made. This tutorial will guide you through the steps to run the development server and handle common issues that may arise.

## Steps

### Step 1: Set up Flask Application

Before we can run the development server, we need to set up a Flask application. Create a new Python file called `app.py` and add the following code:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == "__main__":
    app.run(debug=True)
```

In this code, we create a Flask application and define a route that returns a simple "Hello, Flask!" message. The `if __name__ == "__main__":` block ensures that the Flask application is only run when the script is executed directly, not when it is imported as a module.

### Step 2: Run Development Server with Flask CLI

The easiest way to run the development server is to use the Flask CLI command `flask run`. Open a terminal or command prompt, navigate to the directory where your `app.py` file is located, and run the following command:

```bash
flask run
```

This will start the development server on `http://localhost:5000/`. You can access your Flask application by opening a web browser and entering this URL.

### Step 3: Enable Debug Mode

To enable debug mode, which provides an interactive debugger and automatically reloads the code when changes are made, add the `--debug` option to the `flask run` command:

```bash
flask run --debug
```

Now, any changes you make to your code will trigger an automatic reload of the development server.

### Step 4: Specify Application File

By default, Flask will look for a file named `app.py` to run as the Flask application. If your file has a different name or is located in a different directory, you can use the `--app` option to specify the application file:

```bash
flask run --app myapp.py
```

Replace `myapp.py` with the name of your application file.

### Step 5: Address Already in Use

If you see an `OSError` with the message "Address already in use" when trying to start the server, it means that another program is already using the port 5000, which is the default port for the development server. You can either identify and stop the other program or choose a different port.

To identify the process using port 5000, you can use the `netstat` or `lsof` command. Here are examples for Linux, macOS, and Windows:

- Linux:

```bash
netstat -nlp | grep 5000
```

- macOS / Linux:

```bash
lsof -P -i :5000
```

- Windows:

```bash
> netstat -ano | findstr 5000
```

Once you have identified the process, you can use other operating system tools to stop it. After stopping the process, you should be able to run the development server without any issues.

### Step 6: Running the Development Server from Python

In addition to using the Flask CLI command, you can also start the development server from Python code. Add the following code at the end of your `app.py` file:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Now, you can run the development server by executing the `app.py` file with Python:

```bash
python app.py
```

This will start the development server and you can access your Flask application in the same way as before.

## Summary

In this tutorial, you learned how to use the development server in Flask to run your Flask application during local development. You learned how to run the development server with the Flask CLI command, enable debug mode, specify the application file, and handle common issues such as "Address already in use". You also learned how to start the development server from Python code. With the development server, you can easily test and debug your Flask application before deploying it to production.
