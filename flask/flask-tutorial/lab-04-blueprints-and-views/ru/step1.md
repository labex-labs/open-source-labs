# Создайте блюпринт

Давайте начнем с создания блюпринта для нашего приложения. Этот блюпринт будет называться 'auth' и будет обрабатывать представления, связанные с аутентификацией пользователей. Мы определим наш блюпринт в отдельном модуле с именем `flaskr/auth.py`.

```python
# flaskr/auth.py

import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

# Создайте блюпринт с именем 'auth'
bp = Blueprint('auth', __name__, url_prefix='/auth')
```
