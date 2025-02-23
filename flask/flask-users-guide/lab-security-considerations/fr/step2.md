# Falsification de requêtes entre sites (Cross-Site Request Forgery - CSRF)

La falsification de requêtes entre sites (Cross-Site Request Forgery - CSRF) est une attaque qui trompe les utilisateurs pour qu'ils effectuent des actions involontaires sur un site web. Pour prévenir les attaques CSRF dans Flask, suivez ces directives :

- Utiliser des jetons uniques pour valider les requêtes qui modifient le contenu du serveur.
- Stockez le jeton dans le cookie et le transmettez avec les données du formulaire.
- Comparez le jeton reçu sur le serveur avec celui stocké dans le cookie.

Exemple de code :

```python
# app.py

from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/delete', methods=['POST'])
def delete_user():
    if request.method == 'POST':
        token = request.form.get('token')
        if token and token == session.get('csrf_token'):
            # Supprimer le profil de l'utilisateur
            return redirect(url_for('index'))
    return 'Requête invalide'

if __name__ == '__main__':
    app.run()
```

Pour exécuter le code, enregistrez-le dans un fichier appelé `app.py` et exécutez la commande `flask run`.
