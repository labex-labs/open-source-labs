# Options de définition des cookies

Lorsque vous définissez des cookies dans Flask, il est important de prendre en compte les options de sécurité pour protéger les données sensibles. Certaines options recommandées sont :

- Secure : Limite les cookies au trafic HTTPS uniquement.
- HttpOnly : Protège le contenu des cookies contre la lecture avec JavaScript.
- SameSite : Restreint la manière dont les cookies sont envoyés avec les requêtes provenant de sites externes.

Exemple de code :

```python
# app.py

from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('Hello, world!')
    response.set_cookie('username', 'flask', secure=True, httponly=True, samesite='Lax')
    return response

if __name__ == '__main__':
    app.run()
```

Pour exécuter le code, enregistrez-le dans un fichier appelé `app.py` et exécutez la commande `flask run`.
