# Cross-Site Request Forgery (CSRF)

Cross-Site Request Forgery (CSRF) 는 사용자가 웹사이트에서 의도하지 않은 작업을 수행하도록 속이는 공격입니다. Flask 에서 CSRF 공격을 방지하려면 다음 지침을 따르십시오.

- 서버 콘텐츠를 수정하는 요청을 검증하기 위해 일회성 토큰을 사용합니다.
- 쿠키에 토큰을 저장하고 폼 데이터와 함께 전송합니다.
- 서버에서 수신된 토큰과 쿠키에 저장된 토큰을 비교합니다.

예제 코드:

```python
# app.py

from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/delete', methods=['POST'])
def delete_user():
    if request.method == 'POST':
        token = request.form.get('token')
        if token and token == session.get('csrf_token'):
            # Delete user profile
            return redirect(url_for('index'))
    return 'Invalid request'

if __name__ == '__main__':
    app.run()
```

코드를 실행하려면 `app.py`라는 파일에 저장하고 `flask run` 명령을 실행하십시오.
