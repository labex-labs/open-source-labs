# Implement Login Required Decorator

We will also need a decorator to protect our views that require a user to be logged in. This decorator will be implemented in `flaskr/auth.py`.

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
