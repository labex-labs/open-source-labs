# 파일에서 구성

코드에 구성 값을 하드코딩하는 것은, 특히 민감한 정보의 경우, 이상적이지 않습니다. Flask 는 별도의 파일에서 구성을 로드하는 방법을 제공합니다. `config.py`라는 새 파일을 생성하고 다음 코드를 추가합니다.

```python
DEBUG = False
SECRET_KEY = 'myothersecretkey'
```

`app.py` 파일에서 이전 구성 코드를 다음으로 바꿉니다.

```python
app.config.from_object('config')
```

`from_object` 메서드는 `config` 모듈에서 구성을 로드합니다. 이제 `DEBUG` 및 `SECRET_KEY` 값은 `config.py` 파일에서 로드됩니다.

Flask 애플리케이션을 다시 시작하고 `http://localhost:5000`을 방문하여 새로운 구성 값으로 업데이트된 메시지를 확인합니다.
