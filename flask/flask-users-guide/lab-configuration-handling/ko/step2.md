# 기본 구성

이제 Flask 애플리케이션에 몇 가지 기본 구성을 추가해 보겠습니다. 동일한 `app.py` 파일에 다음 코드를 추가합니다.

```python
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mysecretkey'
```

`DEBUG` 구성은 개발 중에 유용한 오류 메시지를 제공하는 디버그 모드를 활성화합니다. `SECRET_KEY` 구성은 세션 쿠키 및 기타 보안 관련 요구 사항을 안전하게 서명하는 데 사용됩니다.

구성 값에 액세스하려면 `app.config` 딕셔너리를 사용할 수 있습니다. 예를 들어, `SECRET_KEY`의 값을 출력하려면 `hello` 라우트에 다음 코드를 추가합니다.

```python
@app.route('/')
def hello():
    secret_key = app.config['SECRET_KEY']
    return f'Hello, Flask! Secret Key: {secret_key}'
```

Flask 애플리케이션을 다시 시작하고 `http://localhost:5000`을 방문하여 비밀 키가 포함된 업데이트된 메시지를 확인합니다.
