# 블로그 인덱스 생성

이제 모든 블로그 게시물을 표시하는 인덱스 뷰를 생성해 보겠습니다. SQL `JOIN`을 사용하여 결과에 `user` 테이블의 작성자 정보를 포함시킵니다.

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
