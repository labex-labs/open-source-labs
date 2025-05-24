# 기본 라우트 생성

Flask 의 라우트는 애플리케이션의 URL 패턴을 정의합니다. "Hello, World!" 메시지를 표시하는 기본 라우트를 생성해 보겠습니다.

1. `app.py` 파일에 다음 코드를 추가합니다:

   ```python
   @app.route("/")
   def hello_world():
       return "Hello, World!"
   ```

2. 파일을 저장합니다.
