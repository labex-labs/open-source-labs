# Dossier d'instance

Flask fournit un dossier d'instance pour stocker les fichiers de configuration spécifiques à un déploiement particulier. Cela vous permet de séparer les configurations spécifiques au déploiement du reste de votre code. Par défaut, Flask utilise un dossier nommé `instance` dans le même répertoire que votre application.

Créez un nouveau dossier appelé `instance` dans le même répertoire que votre fichier `app.py`. Dans le dossier `instance`, créez un fichier appelé `config.cfg` et ajoutez le code suivant :

```
DEBUG = True
SECRET_KEY = 'instancekey'
```

Dans le fichier `app.py`, ajoutez le code suivant avant le code de configuration :

```python
app.instance_path = os.path.abspath(os.path.dirname(__file__))
app.config.from_pyfile('config.cfg')
```

La variable `instance_path` est définie sur le chemin absolu du dossier `instance`. La méthode `from_pyfile` charge la configuration à partir du fichier `config.cfg` dans le dossier d'instance.

Redémarrez l'application Flask et accédez à `http://localhost:5000` pour voir le message mis à jour avec les valeurs de configuration de l'instance.
