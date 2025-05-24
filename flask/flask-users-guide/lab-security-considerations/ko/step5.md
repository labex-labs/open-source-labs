# Set-Cookie 옵션

Flask 에서 쿠키를 설정할 때, 민감한 데이터를 보호하기 위해 보안 옵션을 고려하는 것이 중요합니다. 권장되는 몇 가지 옵션은 다음과 같습니다.

- Secure: 쿠키를 HTTPS 트래픽으로만 제한합니다.
- HttpOnly: JavaScript 를 사용하여 쿠키 내용을 읽는 것을 방지합니다.
- SameSite: 외부 사이트의 요청과 함께 쿠키가 전송되는 방식을 제한합니다.

예제 코드:

```python
# app.py

from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('Hello, world!')
    response.set_cookie('username', 'flask', secure=True, httponly=True, samesite='Lax')
    return response

if __name__ == '__main__':
    app.run()
```

코드를 실행하려면 `app.py`라는 파일에 저장하고 `flask run` 명령을 실행하십시오.
