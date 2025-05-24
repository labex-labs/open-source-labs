# 로그아웃 뷰 구현

이제 `flaskr/auth.py`에 로그아웃 뷰를 추가해 보겠습니다. 이 뷰는 사용자 로그아웃 기능을 처리합니다.

```python
# flaskr/auth.py

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```
