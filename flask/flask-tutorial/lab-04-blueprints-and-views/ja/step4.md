# ログインビューを実装する

次に、`flaskr/auth.py` にログインビューを実装します。このビューはユーザーのログイン機能を処理します。

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
            error = 'ユーザー名が間違っています。'
        elif not check_password_hash(user['password'], password):
            error = 'パスワードが間違っています。'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')
```
