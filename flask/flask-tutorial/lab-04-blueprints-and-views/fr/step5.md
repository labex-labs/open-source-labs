# Implémenter la vue de déconnexion

Ajoutons maintenant une vue de déconnexion dans `flaskr/auth.py`. Cette vue gérera la fonctionnalité de déconnexion des utilisateurs.

```python
# flaskr/auth.py

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```
