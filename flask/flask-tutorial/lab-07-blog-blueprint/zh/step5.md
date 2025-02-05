# 文章更新

我们将添加让作者更新自己文章的功能。为避免重复代码，我们将创建一个辅助函数来获取一篇文章并检查当前用户是否为作者。

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
            error = '标题是必填项。'

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
