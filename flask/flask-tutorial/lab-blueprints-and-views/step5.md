# Implement Logout View

Let's now add a logout view in `flaskr/auth.py`. This view will handle user logout functionality.

```python
# flaskr/auth.py

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```
