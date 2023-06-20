# Require Authentication in Other Views

To require authentication for certain views, we can create a decorator that checks if a user is logged in. If the user is not logged in, they will be redirected to the login page.

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
