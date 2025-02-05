# 实现登录视图

接下来，我们将在`flaskr/auth.py`中实现登录视图。此视图将处理用户登录功能。

```python
# flaskr/auth.py

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username =?', (username,)
        ).fetchone()

        if user is None:
            error = '用户名错误。'
        elif not check_password_hash(user['password'], password):
            error = '密码错误。'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')
```
