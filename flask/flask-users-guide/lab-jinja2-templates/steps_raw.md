# Flask Jinja2 Templates

## Introduction

In this lab, you will learn how to use Jinja2 templates in Flask. Jinja2 is a powerful template engine that allows you to generate dynamic HTML pages in your Flask application. Templates are a great way to separate the presentation logic from the business logic of your application.

## Steps

### Step 1: Install Flask and Jinja2

Before we begin, make sure you have Flask and Jinja2 installed in your Python environment. You can install them using pip:

```
pip install Flask
pip install Jinja2
```

### Step 2: Create a Flask Application

Create a new file called `app.py` and import the necessary modules:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

In this code, we create a new Flask application and define a route for the root URL ("/"). When a user visits the root URL, the `index()` function will be called and it will render the `index.html` template.

### Step 3: Create a Jinja2 Template

Create a new directory called `templates` in the same directory as your `app.py` file. Inside the `templates` directory, create a new file called `index.html`. This file will contain the HTML code for your template.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Flask Jinja2 Templates Lab</title>
  </head>
  <body>
    <h1>Welcome to Flask Jinja2 Templates Lab</h1>
    <p>This is a simple Flask application using Jinja2 templates.</p>
  </body>
</html>
```

In this template, we have a simple HTML structure with a heading and a paragraph. You can customize the content of the template to fit your needs.

### Step 4: Run the Flask Application

Save the `app.py` file and run it using the following command:

```
python app.py
```

Open your web browser and visit `http://localhost:5000`. You should see the content of the `index.html` template rendered in your browser.

## Summary

Congratulations! You have successfully created a Flask application that uses Jinja2 templates. Templates are a powerful tool for generating dynamic HTML pages in your Flask application. You can now use templates to separate the presentation logic from the business logic of your application and create more flexible and maintainable code.
