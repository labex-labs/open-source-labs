# ブログのインデックスを作成する

さて、すべてのブログ投稿を表示するインデックスビューを作成しましょう。結果に `user` テーブルからの著者情報を含めるために、SQLの `JOIN` を使用します。

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
