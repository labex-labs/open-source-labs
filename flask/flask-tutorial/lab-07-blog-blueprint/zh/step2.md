# 注册蓝图

接下来，我们会将蓝图注册到我们的应用程序中。

```python
# flaskr/__init__.py

def create_app():
    app =...
    # 省略现有代码

    # 使用 app.register_blueprint() 从工厂函数中导入并注册蓝图
    from. import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
```
