# Erstelle den Blog-Index

Lassen Sie uns jetzt eine Index-Ansicht erstellen, um alle Blogbeiträge anzuzeigen. Wir werden eine SQL `JOIN` verwenden, um die Autorinformationen aus der `user`-Tabelle in unseren Ergebnissen zu enthalten.

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
