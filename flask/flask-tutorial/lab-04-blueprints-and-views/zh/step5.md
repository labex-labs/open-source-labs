# 实现登出视图

现在让我们在`flaskr/auth.py`中添加一个登出视图。此视图将处理用户登出功能。

```python
# flaskr/auth.py

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```
