# 게시물 삭제

마지막으로, 작성자가 자신의 게시물을 삭제할 수 있는 기능을 추가합니다.

```python
# flaskr/blog.py

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))
```
