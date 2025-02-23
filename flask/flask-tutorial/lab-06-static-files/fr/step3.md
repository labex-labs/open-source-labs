# Lier le fichier CSS dans le HTML

Maintenant, nous devons lier notre fichier CSS dans les modèles HTML. Flask ajoute automatiquement une vue `static` qui sert les fichiers statiques. Nous pouvons utiliser la fonction `url_for` dans le modèle `base.html` pour lier notre fichier CSS.

```html+jinja
<!-- base.html -->

{{ url_for('static', filename='style.css') }}
```
