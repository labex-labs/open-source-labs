# 登録ビューを実装する

次に、`flaskr/auth.py` に登録ビューを実装しましょう。このビューは登録フォームを表示し、フォームの送信を処理します。

```python
# flaskr/auth.py

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'ユーザー名は必須です。'
        elif not password:
            error = 'パスワードは必須です。'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?,?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"ユーザー {username} は既に登録されています。"
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')
```
