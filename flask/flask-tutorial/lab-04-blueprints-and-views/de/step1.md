# Erstellen eines Blueprints

Lassen Sie uns beginnen, indem wir ein Blueprint für unsere Anwendung erstellen. Dieses Blueprint wird 'auth' genannt und wird die mit der Benutzerauthentifizierung verbundenen Views verarbeiten. Wir werden unser Blueprint in einem separaten Modul namens `flaskr/auth.py` definieren.

```python
# flaskr/auth.py

import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

# Erstellen eines Blueprints namens 'auth'
bp = Blueprint('auth', __name__, url_prefix='/auth')
```
