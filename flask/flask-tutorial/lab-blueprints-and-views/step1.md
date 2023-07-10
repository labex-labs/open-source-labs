# Create a Blueprint

Let's start by creating a blueprint for our application. This blueprint will be named 'auth' and will handle user authentication related views. We will define our blueprint in a separate module named `flaskr/auth.py`.

```python
# flaskr/auth.py

import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

# Create a Blueprint named 'auth'
bp = Blueprint('auth', __name__, url_prefix='/auth')
```
