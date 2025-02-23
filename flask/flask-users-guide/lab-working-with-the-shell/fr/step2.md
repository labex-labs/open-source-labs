# Création d'un contexte de requête

Pour créer un contexte de requête approprié dans le shell, utilisez la méthode `test_request_context()`, qui crée un objet `RequestContext`. Dans le shell, poussez et dépilez manuellement le contexte de requête à l'aide des méthodes `push()` et `pop()`.

```python
# Fichier : shell.py
# Exécution : python shell.py

from flask import Flask

app = Flask(__name__)

# Crée un contexte de requête
ctx = app.test_request_context()

# Pousse le contexte de requête
ctx.push()

# Travailler avec l'objet de requête

# Dépile le contexte de requête
ctx.pop()
```
