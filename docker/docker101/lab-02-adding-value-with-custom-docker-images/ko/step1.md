# `Python` 앱 생성 (Docker 미사용)

다음 명령을 실행하여 간단한 파이썬 프로그램이 포함된 `app.py`라는 파일을 생성합니다. (전체 코드 블록을 복사하여 붙여넣기)

```bash
cd ~/project
```

```bash
echo 'from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")' > app.py
```

이것은 flask 를 사용하여 포트 5000(5000 은 flask 의 기본 포트) 에서 http 웹 서버를 노출하는 간단한 파이썬 앱입니다. 파이썬이나 flask 에 익숙하지 않더라도 걱정하지 마십시오. 이러한 개념은 모든 언어로 작성된 애플리케이션에 적용될 수 있습니다.

**선택 사항:** 파이썬과 pip 가 설치되어 있다면 이 앱을 로컬에서 실행할 수 있습니다. 그렇지 않은 경우 다음 단계로 진행하십시오.

```bash
$ python3 --version
$ pip3 --version
$ pip3 install flask

$ python3 app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

`http://0.0.0.0:5000/`를 사용하여 새 브라우저 탭에서 앱을 엽니다.

![Flask app browser output](../assets/20230829-13-51-38-psaOqQ42.png)
