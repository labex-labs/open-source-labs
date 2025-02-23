# Configurez l'application Flask

Avant d'être en mesure d'exécuter le serveur de développement, nous devons configurer une application Flask. Créez un nouveau fichier Python appelé `app.py` et ajoutez le code suivant :

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == "__main__":
    app.run(debug=True)
```

Dans ce code, nous créons une application Flask et définissons une route qui renvoie un message simple "Hello, Flask!". Le bloc `if __name__ == "__main__":` assure que l'application Flask est exécutée uniquement lorsque le script est exécuté directement, et non lorsqu'il est importé en tant que module.
