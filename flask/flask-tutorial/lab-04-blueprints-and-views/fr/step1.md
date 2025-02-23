# Créer un blueprint

Commencez par créer un blueprint pour notre application. Ce blueprint sera nommé 'auth' et gérera les vues liées à l'authentification des utilisateurs. Nous définirons notre blueprint dans un module séparé nommé `flaskr/auth.py`.

```python
# flaskr/auth.py

import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

# Créez un blueprint nommé 'auth'
bp = Blueprint('auth', __name__, url_prefix='/auth')
```
