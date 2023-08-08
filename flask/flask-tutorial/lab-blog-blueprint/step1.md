# Define Blueprint

Firstly, we'll define a blueprint for our blog. A blueprint is a way to organize a group of related views and other code.

```python
# flaskr/blog.py

from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

# The Blueprint is named 'blog'. It's defined in the same file.
# The blueprint needs to know where it's defined, so __name__ is passed as the second argument.
bp = Blueprint('blog', __name__)
```
