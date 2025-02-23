# アプリケーションの構成

同じ `__init__.py` ファイルに、アプリケーションに必要な構成詳細を追加します。これには、シークレットキーの設定とデータベースファイルの場所の指定が含まれます。

```python
# flaskr/__init__.py

# 上にさらにコードがあります...

if test_config is None:
    # テストしていない場合、存在する場合はインスタンス構成を読み込む
    app.config.from_pyfile('config.py', silent=True)
else:
    # 渡された場合はテスト構成を読み込む
    app.config.from_mapping(test_config)

# インスタンスフォルダが存在することを確認する
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# 簡単なページで挨拶をする
@app.route('/')
def hello():
    return 'Hello, World!'
```
