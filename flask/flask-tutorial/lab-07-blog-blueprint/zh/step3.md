# 创建博客索引

现在，让我们创建一个索引视图来显示所有博客文章。我们将使用 SQL `JOIN` 来在结果中包含来自 `user` 表的作者信息。

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
