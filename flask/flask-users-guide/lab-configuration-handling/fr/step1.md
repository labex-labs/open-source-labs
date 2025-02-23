# Créer une application Flask

Tout d'abord, créons une application Flask de base. Créez un fichier appelé `app.py` et ajoutez le code suivant :

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'
```

Pour exécuter l'application, exécutez la commande suivante dans votre terminal :

```shell
python app.py
```

Ouvrez votre navigateur web et accédez à `http://localhost:5000` pour voir le message "Hello, Flask!".
