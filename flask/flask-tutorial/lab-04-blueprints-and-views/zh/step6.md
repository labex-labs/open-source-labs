# 实现登录\_required装饰器

我们还需要一个装饰器来保护那些需要用户登录的视图。这个装饰器将在`flaskr/auth.py`中实现。

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
