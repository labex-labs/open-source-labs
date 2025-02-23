# Создание индекса блога

Теперь создадим представление для отображения всех записей блога. Мы будем использовать SQL `JOIN`, чтобы включить информацию об авторе из таблицы `user` в наши результаты.

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
