# Criar um Blueprint (Planta)

Vamos começar criando um blueprint (planta) para nossa aplicação. Este blueprint (planta) será nomeado 'auth' e lidará com as views (visualizações) relacionadas à autenticação do usuário. Definiremos nosso blueprint (planta) em um módulo separado chamado `flaskr/auth.py`.

```python
# flaskr/auth.py

import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

# Create a Blueprint named 'auth'
bp = Blueprint('auth', __name__, url_prefix='/auth')
```
