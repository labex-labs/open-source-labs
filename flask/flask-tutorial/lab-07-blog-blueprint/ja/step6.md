# 投稿の削除

最後に、著者が自分の投稿を削除できる機能を追加します。

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
