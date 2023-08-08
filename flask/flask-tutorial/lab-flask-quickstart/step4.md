# Adding HTML Templates

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


