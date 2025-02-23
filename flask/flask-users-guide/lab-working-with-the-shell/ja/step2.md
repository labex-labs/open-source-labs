# リクエストコンテキストの作成

シェル内で適切なリクエストコンテキストを作成するには、`RequestContext` オブジェクトを作成する `test_request_context()` メソッドを使用します。シェル内では、`push()` および `pop()` メソッドを使用して、リクエストコンテキストを手動でプッシュおよびポップします。

```python
# File: shell.py
# Execution: python shell.py

from flask import Flask

app = Flask(__name__)

# リクエストコンテキストを作成
ctx = app.test_request_context()

# リクエストコンテキストをプッシュ
ctx.push()

# リクエストオブジェクトを使用する

# リクエストコンテキストをポップ
ctx.pop()
```
