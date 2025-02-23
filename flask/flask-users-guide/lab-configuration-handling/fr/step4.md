# Configuration basée sur l'environnement

Il est courant d'avoir des configurations différentes pour différents environnements, tels que le développement, la production et les tests. Flask vous permet de basculer entre les configurations en fonction des variables d'environnement. Créez un nouveau fichier appelé `config_dev.py` et ajoutez le code suivant :

```python
DEBUG = True
SECRET_KEY = 'devsecretkey'
```

Créez un autre fichier appelé `config_prod.py` avec le code suivant :

```python
DEBUG = False
SECRET_KEY = 'prodsecretkey'
```

Dans le fichier `app.py`, remplacez le code de configuration précédent par le suivant :

```python
import os

if os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object('config_prod')
else:
    app.config.from_object('config_dev')
```

La variable d'environnement `FLASK_ENV` est utilisée pour déterminer l'environnement. Si elle est définie sur `'production'`, la configuration de production sera chargée ; sinon, la configuration de développement sera chargée.

Définissez la variable d'environnement `FLASK_ENV` sur `'production'` et redémarrez l'application Flask. Accédez à `http://localhost:5000` pour voir le message mis à jour avec les valeurs de configuration de production.
