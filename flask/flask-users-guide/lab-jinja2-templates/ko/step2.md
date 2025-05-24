# Flask 애플리케이션 생성

`app.py`라는 새 파일을 생성하고 필요한 모듈을 가져옵니다.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

이 코드에서 새로운 Flask 애플리케이션을 생성하고 루트 URL ("/") 에 대한 라우트를 정의합니다. 사용자가 루트 URL 을 방문하면 `index()` 함수가 호출되고 `index.html` 템플릿이 렌더링됩니다.
