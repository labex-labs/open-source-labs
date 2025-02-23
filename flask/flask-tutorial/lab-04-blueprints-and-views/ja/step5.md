# ログアウトビューを実装する

次に、`flaskr/auth.py` にログアウトビューを追加しましょう。このビューはユーザーのログアウト機能を処理します。

```python
# flaskr/auth.py

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```
