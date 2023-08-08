# Environment-based Configuration

It's common to have different configurations for different environments, such as development, production, and testing. Flask allows you to switch configurations based on environment variables. Create a new file called `config_dev.py` and add the following code:

```python
DEBUG = True
SECRET_KEY = 'devsecretkey'
```

Create another file called `config_prod.py` with the following code:

```python
DEBUG = False
SECRET_KEY = 'prodsecretkey'
```

In the `app.py` file, replace the previous configuration code with the following:

```python
import os

if os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object('config_prod')
else:
    app.config.from_object('config_dev')
```

The `FLASK_ENV` environment variable is used to determine the environment. If it is set to `'production'`, the production configuration will be loaded; otherwise, the development configuration will be loaded.

Set the `FLASK_ENV` environment variable to `'production'` and restart the Flask application. Visit `http://localhost:5000` to see the updated message with the production configuration values.
