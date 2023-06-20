# Configure the Application

In the "create_app" function, configure the Flask application by setting the secret key and database path.

```python
# flaskr/__init__.py

# ...

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # ...
```
