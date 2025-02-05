# 实现注册视图

现在，让我们在`flaskr/auth.py`中实现注册视图。此视图将呈现一个注册表单并处理表单提交。

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
            error = '用户名是必填项。'
        elif not password:
            error = '密码是必填项。'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?,?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"用户 {username} 已注册。"
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')
```
