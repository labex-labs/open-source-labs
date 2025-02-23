# Implémenter le décorateur de connexion requise

Nous aurons également besoin d'un décorateur pour protéger nos vues qui nécessitent qu'un utilisateur soit connecté. Ce décorateur sera implémenté dans `flaskr/auth.py`.

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
