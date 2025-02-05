# 注册蓝图

创建蓝图后，我们需要将其注册到我们的应用程序中。这在`flaskr/__init__.py`中的应用程序工厂函数中完成。

```python
# flaskr/__init__.py

def create_app():
    app =...
    # 省略现有代码

    # 导入并注册蓝图
    from. import auth
    app.register_blueprint(auth.bp)

    return app
```
