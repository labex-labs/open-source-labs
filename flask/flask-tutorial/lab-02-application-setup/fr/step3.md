# Configuration de l'application

Dans le même fichier `__init__.py`, ajoutez les détails de configuration nécessaires pour votre application. Cela inclut la définition d'une clé secrète et la spécification de l'emplacement du fichier de base de données.

```python
# flaskr/__init__.py

# Plus de code ci-dessus...

if test_config is None:
    # charger la configuration de l'instance, s'il existe, lorsqu'on ne teste pas
    app.config.from_pyfile('config.py', silent=True)
else:
    # charger la configuration de test si elle est passée en paramètre
    app.config.from_mapping(test_config)

# s'assurer que le dossier d'instance existe
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# une page simple qui dit bonjour
@app.route('/')
def hello():
    return 'Hello, World!'
```
