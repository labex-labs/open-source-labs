# Démarrage des fonctions avant/après une requête

En créant un contexte de requête, le code qui est normalement exécuté avant une requête n'est pas déclenché. Pour simuler la fonctionnalité avant une requête, appelez la méthode `preprocess_request()`. Cela garantit que les connexions à la base de données et autres ressources sont disponibles.

```python
# Fichier : shell.py
# Exécution : python shell.py

from flask import Flask

app = Flask(__name__)

# Crée un contexte de requête
ctx = app.test_request_context()
ctx.push()

# Simule la fonctionnalité avant une requête
app.preprocess_request()

# Travailler avec l'objet de requête

# Dépile le contexte de requête
ctx.pop()
```

Pour simuler la fonctionnalité après une requête, appelez la méthode `process_response()` avec un objet de réponse fictif avant de dépiler le contexte de requête.

```python
# Fichier : shell.py
# Exécution : python shell.py

from flask import Flask

app = Flask(__name__)

# Crée un contexte de requête
ctx = app.test_request_context()
ctx.push()

# Simule la fonctionnalité avant une requête
app.preprocess_request()

# Travailler avec l'objet de requête

# Simule la fonctionnalité après une requête
app.process_response(app.response_class())

# Dépile le contexte de requête
ctx.pop()
```
