# Реализуйте декоратор требующий аутентификации

Нам также понадобится декоратор для защиты наших представлений, которые требуют аутентификации пользователя. Этот декоратор будет реализован в `flaskr/auth.py`.

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
