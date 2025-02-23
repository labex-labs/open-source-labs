# ブループリントを登録する

ブループリントを作成した後、アプリケーションに登録する必要があります。これは、`flaskr/__init__.py` のアプリケーションファクトリ関数で行われます。

```python
# flaskr/__init__.py

def create_app():
    app =...
    # 既存のコードは省略
    # ブループリントをインポートして登録する
    from. import auth
    app.register_blueprint(auth.bp)

    return app
```
