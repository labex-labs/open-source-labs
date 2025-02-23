# ブループリントを登録する

次に、アプリケーションにブループリントを登録します。

```python
# flaskr/__init__.py

def create_app():
    app =...
    # 既存のコードは省略
    # ファクトリーからブループリントをインポートし、app.register_blueprint() を使って登録
    from. import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
```
