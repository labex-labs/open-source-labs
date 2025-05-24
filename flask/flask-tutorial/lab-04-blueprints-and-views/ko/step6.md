# 로그인 필요 데코레이터 구현

또한 사용자가 로그인해야 하는 뷰를 보호하기 위해 데코레이터가 필요합니다. 이 데코레이터는 `flaskr/auth.py`에서 구현됩니다.

```python
# flaskr/auth.py

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
```
