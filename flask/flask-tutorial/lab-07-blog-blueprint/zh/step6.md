# 文章删除

最后，我们将添加让作者删除自己文章的功能。

```python
# flaskr/blog.py

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id =?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))
```
