# Définir un Blueprint

Tout d'abord, nous allons définir un blueprint pour notre blog. Un blueprint est un moyen d'organiser un groupe de vues et d'autres codes liés.

```python
# flaskr/blog.py

from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

# Le Blueprint porte le nom de 'blog'. Il est défini dans le même fichier.
# Le blueprint doit savoir où il est défini, donc __name__ est passé en tant que deuxième argument.
bp = Blueprint('blog', __name__)
```
