# Implementieren der Logout-Ansicht

Fügen wir nun eine Logout-Ansicht in `flaskr/auth.py` hinzu. Diese Ansicht wird die Benutzerabmeldungsfunktion verarbeiten.

```python
# flaskr/auth.py

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```
