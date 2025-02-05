# 为工厂函数编写测试

接下来，我们将为负责创建 Flask 应用的工厂函数编写测试。这些测试可确保应用根据传递给它的配置按预期运行。

以下是要添加到 `tests/test_factory.py` 中的代码：

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
