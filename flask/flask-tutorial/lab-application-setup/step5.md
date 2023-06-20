# Add a Route

Create a simple route that displays a "Hello, World!" message when accessed.

```python
# flaskr/__init__.py

# ...

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ...

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```
