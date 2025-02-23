# Configuration à partir de fichiers

Le codage direct des valeurs de configuration dans le code n'est pas idéal, en particulier pour les informations sensibles. Flask propose un moyen de charger la configuration à partir de fichiers séparés. Créez un nouveau fichier appelé `config.py` et ajoutez le code suivant :

```python
DEBUG = False
SECRET_KEY ='myothersecretkey'
```

Dans le fichier `app.py`, remplacez le code de configuration précédent par le suivant :

```python
app.config.from_object('config')
```

La méthode `from_object` charge la configuration à partir du module `config`. Maintenant, les valeurs de `DEBUG` et `SECRET_KEY` seront chargées à partir du fichier `config.py`.

Redémarrez l'application Flask et accédez à `http://localhost:5000` pour voir le message mis à jour avec les nouvelles valeurs de configuration.
