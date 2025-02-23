# Beitraglöschung

Schließlich werden wir den Autoren die Möglichkeit geben, ihre eigenen Beiträge zu löschen.

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
