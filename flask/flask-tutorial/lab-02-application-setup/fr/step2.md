# Configuration de la fabrique d'applications

Ensuite, créez un fichier `__init__.py` dans le répertoire `flaskr`. Ce fichier a deux fonctions : il contiendra la fabrique d'applications et il signalera à Python que le répertoire `flaskr` doit être traité comme un package.

Dans votre fichier `__init__.py`, importez les modules nécessaires et définissez une fonction, `create_app()`, qui instanciera et configurera votre application.

```python
# flaskr/__init__.py

import os
from flask import Flask

def create_app(test_config=None):
    # créer et configurer l'application
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # Plus de code à ajouter ici...

    return app
```
