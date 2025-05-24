# Flask 애플리케이션 설정

개발 서버를 실행하기 전에 Flask 애플리케이션을 설정해야 합니다. `app.py`라는 새 Python 파일을 생성하고 다음 코드를 추가합니다.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == "__main__":
    app.run(debug=True)
```

이 코드에서는 Flask 애플리케이션을 생성하고 간단한 "Hello, Flask!" 메시지를 반환하는 라우트 (route) 를 정의합니다. `if __name__ == "__main__":` 블록은 스크립트가 모듈로 가져올 때가 아니라 직접 실행될 때만 Flask 애플리케이션이 실행되도록 보장합니다.
