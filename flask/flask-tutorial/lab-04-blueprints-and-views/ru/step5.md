# Реализуйте представление выхода

Теперь давайте добавим представление выхода в `flaskr/auth.py`. Это представление будет обрабатывать функциональность выхода пользователя.

```python
# flaskr/auth.py

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```
