# Adding Dynamic Content

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


