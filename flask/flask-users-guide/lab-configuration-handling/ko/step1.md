# Flask 애플리케이션 생성

먼저, 기본적인 Flask 애플리케이션을 생성해 보겠습니다. `app.py`라는 파일을 생성하고 다음 코드를 추가합니다.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'
```

애플리케이션을 실행하려면 터미널에서 다음 명령을 실행합니다.

```shell
python app.py
```

웹 브라우저를 열고 `http://localhost:5000`을 방문하여 "Hello, Flask!" 메시지를 확인합니다.
