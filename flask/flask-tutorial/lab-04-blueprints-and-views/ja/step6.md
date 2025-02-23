# ログインが必要なデコレータを実装する

ユーザーがログインしていることが必要なビューを保護するために、デコレータも必要になります。このデコレータは `flaskr/auth.py` に実装されます。

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
