# Implementar el decorador de inicio de sesión requerido

También necesitaremos un decorador para proteger nuestras vistas que requieren que el usuario esté autenticado. Este decorador se implementará en `flaskr/auth.py`.

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
