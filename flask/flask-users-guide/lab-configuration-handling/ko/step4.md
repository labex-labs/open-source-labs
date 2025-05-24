# 환경 기반 구성

개발, 프로덕션, 테스트 등 다양한 환경에 대해 서로 다른 구성을 갖는 것은 일반적입니다. Flask 를 사용하면 환경 변수를 기반으로 구성을 전환할 수 있습니다. `config_dev.py`라는 새 파일을 생성하고 다음 코드를 추가합니다.

```python
DEBUG = True
SECRET_KEY = 'devsecretkey'
```

다음 코드를 사용하여 `config_prod.py`라는 다른 파일을 생성합니다.

```python
DEBUG = False
SECRET_KEY = 'prodsecretkey'
```

`app.py` 파일에서 이전 구성 코드를 다음으로 바꿉니다.

```python
import os

if os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object('config_prod')
else:
    app.config.from_object('config_dev')
```

`FLASK_ENV` 환경 변수는 환경을 결정하는 데 사용됩니다. 이 변수가 `'production'`으로 설정되면 프로덕션 구성이 로드되고, 그렇지 않으면 개발 구성이 로드됩니다.

`FLASK_ENV` 환경 변수를 `'production'`으로 설정하고 Flask 애플리케이션을 다시 시작합니다. `http://localhost:5000`을 방문하여 프로덕션 구성 값으로 업데이트된 메시지를 확인합니다.
