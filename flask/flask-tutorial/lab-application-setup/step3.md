# Configuring the Application

In the same `__init__.py` file, add the necessary configuration details for your application. This includes setting up a secret key and specifying the location of your database file.

```python
# flaskr/__init__.py

# More code above...

if test_config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'
```
