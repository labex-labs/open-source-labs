# Configuration from Files

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


