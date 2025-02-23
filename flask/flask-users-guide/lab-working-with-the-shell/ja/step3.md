# リクエスト前/後の関数の実行

リクエストコンテキストを作成することで、通常はリクエストの前に実行されるコードがトリガーされません。リクエスト前の機能をシミュレートするには、`preprocess_request()` メソッドを呼び出します。これにより、データベース接続やその他のリソースが利用可能になります。

```python
# File: shell.py
# Execution: python shell.py

from flask import Flask

app = Flask(__name__)

# リクエストコンテキストを作成
ctx = app.test_request_context()
ctx.push()

# リクエスト前の機能をシミュレート
app.preprocess_request()

# リクエストオブジェクトを使用する

# リクエストコンテキストをポップ
ctx.pop()
```

リクエスト後の機能をシミュレートするには、リクエストコンテキストをポップする前に、ダミーのレスポンスオブジェクトを使って `process_response()` メソッドを呼び出します。

```python
# File: shell.py
# Execution: python shell.py

from flask import Flask

app = Flask(__name__)

# リクエストコンテキストを作成
ctx = app.test_request_context()
ctx.push()

# リクエスト前の機能をシミュレート
app.preprocess_request()

# リクエストオブジェクトを使用する

# リクエスト後の機能をシミュレート
app.process_response(app.response_class())

# リクエストコンテキストをポップ
ctx.pop()
```
