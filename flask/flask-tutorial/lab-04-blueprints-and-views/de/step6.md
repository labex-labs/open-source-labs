# Implementieren des Login-Required-Dekorators

Wir werden auch einen Dekorator benötigen, um unsere Views zu schützen, die ein angemeldeten Benutzer erfordern. Dieser Dekorator wird in `flaskr/auth.py` implementiert.

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
