# Definir el Blueprint

En primer lugar, definiremos un blueprint para nuestro blog. Un blueprint es una forma de organizar un grupo de vistas relacionadas y otros códigos.

```python
# flaskr/blog.py

from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

# El Blueprint se llama 'blog'. Está definido en el mismo archivo.
# El blueprint necesita saber dónde está definido, por lo que __name__ se pasa como segundo argumento.
bp = Blueprint('blog', __name__)
```
