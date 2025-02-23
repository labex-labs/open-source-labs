# Enregistrer des commandes avec l'application Flask

Pour rendre vos commandes personnalisées disponibles via l'interface de ligne de commande (CLI) de Flask, vous devez les enregistrer avec votre application Flask. Ouvrez le fichier `app.py` et modifiez-le comme suit :

```python
from flask import Flask
from commands import greet

app = Flask(__name__)
app.cli.add_command(greet)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
```

Enregistrez le fichier et redémarrez le serveur de développement Flask à l'aide de la commande `flask run`. Maintenant, vous pouvez exécuter votre commande personnalisée `greet` à partir de la ligne de commande :

```
flask greet John
```

Vous devriez voir le message "Hello, John!" affiché dans le terminal.
