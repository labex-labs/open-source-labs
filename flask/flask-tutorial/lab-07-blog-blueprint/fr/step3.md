# Créer l'index du blog

Maintenant, créons une vue d'index pour afficher tous les articles de blog. Nous utiliserons une jointure SQL (`JOIN`) pour inclure les informations sur l'auteur à partir de la table `user` dans nos résultats.

```python
# flaskr/blog.py

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)
```
