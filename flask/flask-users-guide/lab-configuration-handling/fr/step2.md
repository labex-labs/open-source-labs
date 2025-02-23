# Configuration de base

Maintenant, ajoutons quelques configurations de base à notre application Flask. Dans le même fichier `app.py`, ajoutez le code suivant :

```python
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mysecretkey'
```

La configuration `DEBUG` active le mode de débogage, qui fournit des messages d'erreur utiles pendant le développement. La configuration `SECRET_KEY` est utilisée pour signer de manière sécurisée les cookies de session et d'autres besoins liés à la sécurité.

Pour accéder aux valeurs de configuration, vous pouvez utiliser le dictionnaire `app.config`. Par exemple, pour afficher la valeur de la `SECRET_KEY`, ajoutez le code suivant à la route `hello` :

```python
@app.route('/')
def hello():
    secret_key = app.config['SECRET_KEY']
    return f'Hello, Flask! Secret Key: {secret_key}'
```

Redémarrez l'application Flask et accédez à `http://localhost:5000` pour voir le message mis à jour avec la clé secrète.
