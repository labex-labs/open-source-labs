# Create a Blueprint

A Blueprint is a way to organize a group of related views and other code. To create a Blueprint, define a new Python module and import the necessary Flask functions and classes. Then, create an instance of the Blueprint class and define the necessary views and code within the module.

```python
# flaskr/auth.py

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
```
