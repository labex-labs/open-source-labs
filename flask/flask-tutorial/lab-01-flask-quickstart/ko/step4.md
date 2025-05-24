# HTML 템플릿 추가

Flask 는 Jinja2 템플릿을 사용하여 HTML 콘텐츠를 생성합니다. 템플릿 파일을 생성하고 라우트에서 렌더링해 보겠습니다.

1. 프로젝트에 `templates`라는 새 디렉토리를 생성합니다.

2. `templates` 디렉토리 안에 `index.html`이라는 새 파일을 생성합니다.

3. `index.html` 파일을 열고 다음 HTML 코드를 추가합니다:

   ```html
   <!doctype html>
   <html>
     <head>
       <title>Flask Quickstart</title>
     </head>
     <body>
       <h1>Hello, Flask!</h1>
     </body>
   </html>
   ```

4. `app.py` 파일을 수정하여 `index.html` 템플릿을 렌더링합니다:

   ```python
   from flask import render_template

   @app.route("/")
   def hello_world():
       return render_template("index.html")
   ```
