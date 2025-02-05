# Instance Folder

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
