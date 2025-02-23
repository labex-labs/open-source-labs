# Crear un blueprint

Comencemos creando un blueprint para nuestra aplicación. Este blueprint se llamará 'auth' y manejará las vistas relacionadas con la autenticación de usuarios. Definiremos nuestro blueprint en un módulo separado llamado `flaskr/auth.py`.

```python
# flaskr/auth.py

import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

# Crea un blueprint llamado 'auth'
bp = Blueprint('auth', __name__, url_prefix='/auth')
```
