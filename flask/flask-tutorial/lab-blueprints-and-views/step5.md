# Implement User Authentication

To implement user authentication, we need to load the logged-in user's information at the beginning of each request. We can do this by using the `before_app_request` decorator provided by Flask.

```python
# flaskr/auth.py

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
```
