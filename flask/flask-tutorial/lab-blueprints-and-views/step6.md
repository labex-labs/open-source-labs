# Create the Logout View

The logout view will handle requests to the `/auth/logout` URL. It will clear the user's session and redirect them to the homepage.

```python
# flaskr/auth.py

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```
