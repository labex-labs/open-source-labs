# ファクトリ関数のテストの作成

次に、Flask アプリケーションを作成する責任のあるファクトリ関数のテストを作成します。これらのテストは、渡された設定に基づいてアプリケーションが期待通りに動作することを確認します。

`tests/test_factory.py` に追加するコードは以下の通りです。

```python
# tests/test_factory.py

from flaskr import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
```
