# 投稿の更新

著者が自分の投稿を更新できる機能を追加します。コードの重複を避けるため、投稿を取得して現在のユーザーが著者であるかどうかを確認するためのヘルパー関数を作成します。

```python
# flaskr/blog.py

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title =?, body =?'
                ' WHERE id =?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)
```
