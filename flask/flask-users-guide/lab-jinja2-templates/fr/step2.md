# Créer une application Flask

Créez un nouveau fichier appelé `app.py` et importez les modules nécessaires :

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

Dans ce code, nous créons une nouvelle application Flask et définissons une route pour l'URL racine ("/"). Lorsqu'un utilisateur visite l'URL racine, la fonction `index()` sera appelée et elle affichera le modèle `index.html`.
