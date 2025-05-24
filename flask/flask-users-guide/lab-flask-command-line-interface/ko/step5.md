# Flask 애플리케이션에 명령어 등록

Flask CLI 를 통해 사용자 정의 명령어를 사용할 수 있도록 하려면 Flask 애플리케이션에 등록해야 합니다. `app.py` 파일을 열고 다음과 같이 수정합니다:

```python
from flask import Flask
from commands import greet

app = Flask(__name__)
app.cli.add_command(greet)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
```

파일을 저장하고 `flask run` 명령을 사용하여 Flask 개발 서버를 다시 시작합니다. 이제 명령줄에서 사용자 정의 명령어 `greet`를 실행할 수 있습니다:

```
flask greet John
```

터미널에 "Hello, John!" 메시지가 출력되는 것을 확인할 수 있습니다.
