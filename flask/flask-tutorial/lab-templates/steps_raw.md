# Flask Templates Lab

## Introduction

In this lab, we will learn how to use templates in Flask to render dynamic HTML pages. Templates allow us to separate the presentation logic from the business logic in our Flask application, making our code more modular and maintainable.

## Steps

### Step 1: Set up the project

Create a new directory for your Flask project and navigate to it in your terminal.

### Step 2: Install Flask

Install Flask using the following command:

```python
pip install flask
```

### Step 3: Create the Flask application

Create a new Python file called `app.py` and add the following code:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)
```

Run the Flask application using the following command:

```shell
python app.py
```

Open your web browser and navigate to `http://127.0.0.1:5000`. You should see the message "Hello, Flask!" displayed in your browser.

### Step 4: Create the templates directory

Create a new directory called `templates` in your project directory. This is where we will store our HTML templates.

### Step 5: Create the base template

Create a new file called `base.html` inside the `templates` directory and add the following code:

```html+jinja
<!doctype html>
<html>
<head>
    <title>{% block title %}Flask App{% endblock %}</title>
</head>
<body>
    <header>
        {% block header %}
        <h1>Flask App</h1>
        {% endblock %}
    </header>
    <section class="content">
        {% block content %}
        <p>Welcome to my Flask App!</p>
        {% endblock %}
    </section>
</body>
</html>
```

### Step 6: Create a child template

Create a new file called `child.html` inside the `templates` directory and add the following code:

```html+jinja
{% extends 'base.html' %}

{% block header %}
    <h1>Child Template</h1>
{% endblock %}

{% block content %}
    <p>This is the content of the child template.</p>
{% endblock %}
```

### Step 7: Update the Flask application

Update the `app.py` file to render the child template. Replace the `index` function with the following code:

```python
from flask import render_template

@app.route('/')
def index():
    return render_template('child.html')
```

### Step 8: Test the application

Restart the Flask application using the following command:

```shell
python app.py
```

Open your web browser and navigate to `http://127.0.0.1:5000`. You should see the header "Child Template" and the content "This is the content of the child template."

## Summary

In this lab, we learned how to use templates in Flask to render dynamic HTML pages. We created a base template and a child template, and used the `render_template` function to render the child template. Templates allow us to separate the presentation logic from the business logic in our Flask application, making our code more modular and maintainable.
