# Flask Quickstart Lab

## Introduction

This lab will guide you through the process of getting started with Flask, a lightweight web framework for Python. You will learn how to create a basic Flask application, run it locally, and understand the basic concepts of routing and rendering templates.

## Steps

### Step 1: Setting up Flask

To get started with Flask, you need to install it and set up a new project. Follow the instructions below:

1. Install Flask by running the following command in your terminal or command prompt:

   ```bash
   pip install flask
   ```

2. Create a new directory for your Flask project.

3. Open a new file and save it as `app.py`.

4. Import the Flask module and create an instance of the Flask class:

   ```python
   from flask import Flask

   app = Flask(__name__)
   ```

### Step 2: Creating a Basic Route

Routes in Flask define the URL patterns for your application. Let's create a basic route that displays a "Hello, World!" message.

1. Add the following code to your `app.py` file:

   ```python
   @app.route("/")
   def hello_world():
       return "Hello, World!"
   ```

2. Save the file.

### Step 3: Running the Application

Now that you have set up your Flask application and created a basic route, let's run the application and see it in action.

1. In your terminal or command prompt, navigate to the directory where your `app.py` file is located.

2. Run the following command to start the Flask development server:

   ```bash
   flask run
   ```

3. You should see some output indicating that the server is running. Open your web browser and visit `http://localhost:5000` to see the "Hello, World!" message.

### Step 4: Adding HTML Templates

Flask uses Jinja2 templates to generate HTML content. Let's create a template file and render it in our route.

1. Create a new directory in your project called `templates`.

2. Inside the `templates` directory, create a new file called `index.html`.

3. Open the `index.html` file and add the following HTML code:

   ```html
   <!DOCTYPE html>
   <html>
     <head>
       <title>Flask Quickstart</title>
     </head>
     <body>
       <h1>Hello, World!</h1>
     </body>
   </html>
   ```

4. Modify your `app.py` file to render the `index.html` template:

   ```python
   from flask import render_template

   @app.route("/")
   def hello_world():
       return render_template("index.html")
   ```

### Step 5: Running the Application Again

Now that we have added an HTML template, let's run the application again and see the rendered template.

1. Stop the Flask development server if it is still running (press Ctrl+C).

2. Run the following command to start the server again:

   ```bash
   flask run
   ```

3. Visit `http://localhost:5000` in your web browser. You should now see the "Hello, World!" message displayed in the HTML template.

### Step 6: Adding Dynamic Content

Flask allows us to pass dynamic content to our templates. Let's modify our route to pass a name parameter and display a personalized greeting.

1. Modify your `app.py` file to accept a name parameter in the route:

   ```python
   @app.route("/<name>")
   def hello(name):
       return render_template("index.html", name=name)
   ```

2. Open the `index.html` file and modify the `<h1>` tag to display the personalized greeting:

   ```html
   <h1>Hello, {{ name }}!</h1>
   ```

### Step 7: Running the Application Again

Let's run the application again and test the dynamic content feature.

1. Stop the Flask development server if it is still running (press Ctrl+C).

2. Run the following command to start the server again:

   ```bash
   flask run
   ```

3. Visit `http://localhost:5000/John` in your web browser. You should now see a personalized greeting that says "Hello, John!".

## Summary

In this lab, you learned how to get started with Flask by setting up a new project, creating routes, rendering templates, and passing dynamic content. Flask is a powerful tool for building web applications, and this lab provides a solid foundation for further exploration and development.
