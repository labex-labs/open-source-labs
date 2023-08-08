# Basic Configuration

Now let's add some basic configuration to our Flask application. In the same `app.py` file, add the following code:

```python
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mysecretkey'
```

The `DEBUG` configuration enables debug mode, which provides helpful error messages during development. The `SECRET_KEY` configuration is used for securely signing session cookies and other security-related needs.

To access the configuration values, you can use the `app.config` dictionary. For example, to print the value of the `SECRET_KEY`, add the following code to the `hello` route:

```python
@app.route('/')
def hello():
    secret_key = app.config['SECRET_KEY']
    return f'Hello, Flask! Secret Key: {secret_key}'
```

Restart the Flask application and visit `http://localhost:5000` to see the updated message with the secret key.
