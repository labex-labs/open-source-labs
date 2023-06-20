# Setting up the Application Factory

Next, create an `__init__.py` file in the `flaskr` directory. This file serves two purposes: it will contain the application factory, and it signals to Python that the `flaskr` directory should be treated as a package.

In your `__init__.py` file, import the necessary modules and define a function, `create_app()`, that will instantiate and configure your application.

```python
# flaskr/__init__.py

import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # More code to be added here...

    return app
```
