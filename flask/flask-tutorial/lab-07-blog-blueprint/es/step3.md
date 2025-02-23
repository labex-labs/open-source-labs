# Crear el índice del blog

Ahora, creemos una vista de índice para mostrar todas las publicaciones del blog. Usaremos un `JOIN` SQL para incluir la información del autor de la tabla `user` en nuestros resultados.

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
