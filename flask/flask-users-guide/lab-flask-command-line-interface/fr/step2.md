# Créer une application Flask

Créez un nouveau fichier Python nommé `app.py` et ajoutez le code suivant pour créer une application Flask de base :

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
```

Enregistrez le fichier et exécutez-le à l'aide de la commande suivante dans votre terminal :

```
python app.py
```
