# 인스턴스 폴더

Flask 는 특정 배포에 특정한 구성 파일을 저장하기 위한 인스턴스 폴더를 제공합니다. 이를 통해 배포 관련 구성을 나머지 코드와 분리할 수 있습니다. 기본적으로 Flask 는 애플리케이션과 동일한 디렉토리에 `instance`라는 폴더를 사용합니다.

`app.py` 파일과 동일한 디렉토리에 `instance`라는 새 폴더를 생성합니다. `instance` 폴더 내에 `config.cfg`라는 파일을 생성하고 다음 코드를 추가합니다.

```
DEBUG = True
SECRET_KEY = 'instancekey'
```

`app.py` 파일에서 구성 코드 앞에 다음 코드를 추가합니다.

```python
app.instance_path = os.path.abspath(os.path.dirname(__file__))
app.config.from_pyfile('config.cfg')
```

`instance_path`는 `instance` 폴더의 절대 경로로 설정됩니다. `from_pyfile` 메서드는 인스턴스 폴더의 `config.cfg` 파일에서 구성을 로드합니다.

Flask 애플리케이션을 다시 시작하고 `http://localhost:5000`을 방문하여 인스턴스 구성 값으로 업데이트된 메시지를 확인합니다.
