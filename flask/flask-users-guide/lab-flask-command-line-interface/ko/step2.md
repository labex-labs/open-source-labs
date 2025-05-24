# Flask 애플리케이션 생성

`app.py`라는 새 Python 파일을 생성하고, 기본적인 Flask 애플리케이션을 생성하기 위해 다음 코드를 추가합니다:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
```

파일을 저장하고 터미널에서 다음 명령을 사용하여 실행합니다:

```
python app.py
```
