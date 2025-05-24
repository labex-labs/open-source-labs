# Factory (팩토리) 에 대한 테스트 작성

다음으로, Flask 애플리케이션을 생성하는 역할을 하는 factory (팩토리) 함수에 대한 테스트를 작성합니다. 이러한 테스트는 애플리케이션이 전달된 구성에 따라 예상대로 동작하는지 확인합니다.

`tests/test_factory.py`에 추가할 코드는 다음과 같습니다.

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
