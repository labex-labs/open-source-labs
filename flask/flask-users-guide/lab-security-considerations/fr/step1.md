# Injection de scripts croisés (Cross-Site Scripting - XSS)

L'injection de scripts croisés (Cross-Site Scripting - XSS) est une vulnérabilité qui permet aux attaquants d'injecter des scripts malveillants dans les pages web affichées aux utilisateurs. Pour prévenir les attaques XSS dans Flask, suivez ces directives :

- Toujours échapper le texte pour empêcher l'inclusion de balises HTML arbitraires.
- Être prudent lors de la génération de HTML sans l'aide de modèles Jinja2.
- Utiliser la classe `Markup` pour échapper les données soumises par l'utilisateur.
- Éviter d'envoyer des fichiers HTML ou de texte provenant de fichiers téléchargés.

Exemple de code :

```python
# app.py

from flask import Flask, render_template_string, Markup

app = Flask(__name__)

@app.route('/')
def index():
    value = '<script>alert("XSS Attack")</script>'
    safe_value = Markup.escape(value)
    return render_template_string('<input value="{{ value }}">', value=safe_value)
```

Pour exécuter le code, enregistrez-le dans un fichier appelé `app.py` et exécutez la commande `flask run`.
