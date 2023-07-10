# Creating a Basic Route

Routes in Flask define the URL patterns for your application. Let's create a basic route that displays a "Hello, World!" message.

1. Add the following code to your `app.py` file:

   ```python
   @app.route("/")
   def hello_world():
       return "Hello, World!"
   ```

2. Save the file.


