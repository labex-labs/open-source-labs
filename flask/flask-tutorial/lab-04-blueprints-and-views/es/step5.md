# Implementar la vista de cierre de sesión

Ahora agreguemos una vista de cierre de sesión en `flaskr/auth.py`. Esta vista manejará la funcionalidad de cierre de sesión de usuario.

```python
# flaskr/auth.py

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```
