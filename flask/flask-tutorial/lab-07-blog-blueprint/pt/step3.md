# Criar Índice do Blog

Agora, vamos criar uma view de índice para exibir todas as postagens do blog. Usaremos um `JOIN` SQL para incluir informações do autor da tabela `user` em nossos resultados.

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
