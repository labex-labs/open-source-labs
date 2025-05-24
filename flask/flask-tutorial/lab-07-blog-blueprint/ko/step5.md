# 게시물 업데이트

이제 작성자가 자신의 게시물을 업데이트할 수 있는 기능을 추가합니다. 코드 중복을 피하기 위해, 게시물을 가져오고 현재 사용자가 작성자인지 확인하는 헬퍼 함수를 생성합니다.

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
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)
```
